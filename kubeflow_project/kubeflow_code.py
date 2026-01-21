from kfp.dsl import component, pipeline, Output, Metric


#load Data
@component(base_image="python:3.12")
def load_data() -> str:
    import pandas as pd

    #load the Iris dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )
    path = "/tmp/iris.csv"
    df.to_csv(path, index=False)
    return path


#Train Model
@component(base_image="python:3.12")
def train_model(data_path: str) -> str:
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    import joblib

    df = pd.read_csv(data_path)
    X = df.drop("species", axis=1)
    y = df["species"]

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    model_path = "/tmp/iris_model.joblib"
    joblib.dump(model, model_path)
    return model_path


#Evaluate Model
@component(
    base_image="python:3.12",
    output_component_file="evaluate_model_component.yaml"
)
def evaluate_model(
    model_path: str,
    data_path: str,
    accuracy: Output[Metric],
) -> None:
    import pandas as pd
    import joblib
    from sklearn.metrics import accuracy_score

    df = pd.read_csv(data_path)
    X = df.drop("species", axis=1)
    y = df["species"]

    model = joblib.load(model_path)
    predictions = model.predict(X)
    
    # Calculate & write metric
    acc = accuracy_score(y, predictions)
    accuracy.log(acc)


# Pipeline Definition
@pipeline(
    name="Automated ML Training Pipeline",
    description="Kubeflow pipeline that trains and evaluates an ML model on Iris data",
)
def automl_pipeline():
    #Load Data
    data_task = load_data()

    #Train Model
    train_task = train_model(data_path=data_task.output)

    #Evaluate Model
    eval_task = evaluate_model(
        model_path=train_task.output,
        data_path=data_task.output,
    )


if __name__ == "__main__":
    from kfp import compiler

    compiler.Compiler().compile(
        pipeline_func=automl_pipeline,
        package_path="automl_pipeline.yaml",
    )
    print("Pipeline compiled: automl_pipeline.yaml")