from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from transformers import pipeline

app = FastAPI()

# Load a more powerful roberta QA model
qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2"
)

class QARequest(BaseModel): #this is where the client enters a paragraph
    context: str = Field(..., description="The paragraph / context in which to answer questions")
    questions: List[str] = Field(..., description="One or more questions about the context")

class QAResponseItem(BaseModel): #this shows the model answers a qstn. contains the qstn, ansr, conf, start and end.
    question: str
    answer: str
    score: float
    start: Optional[int] = None
    end: Optional[int] = None

class QAResponse(BaseModel): #returns a list of all answer items
    results: List[QAResponseItem]

@app.post("/ask/", response_model=QAResponse)
def ask_questions(request: QARequest):
    # We pass lists for question and context. Because context is the same for all, we replicate it.
    context = request.context
    questions = request.questions

    qa_inputs = { #hugging face pipelines can accept lists as an input
        "question": questions,
        "context": [context] * len(questions)
    }
    results = qa_pipeline(**qa_inputs)

    # results is a list of dicts (one per question)
    response_items = []
    for q, res in zip(questions, results):
        response_items.append(QAResponseItem(
            question=q,
            answer=res.get("answer"),
            score=res.get("score"),
            start=res.get("start"),
            end=res.get("end"),
        )) #iterates through each question and corresponding model output, creates a QAResponseItem for each and collects them in a list

    return QAResponse(results=response_items)


'''
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline

app = FastAPI()

# Load QA pipeline once (this is relatively expensive, so do it at startup)
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

class QARequest(BaseModel):
    context: str
    questions: List[str]

class QAAnswer(BaseModel):
    answer: str
    score: float

@app.post("/ask/", response_model=List[QAAnswer])
def ask(request: QARequest):
    # The pipeline supports batching: you can pass a list of questions
    results = qa(question=request.questions, context=[request.context] * len(request.questions))
    # results will be a list of dicts
    return [{"answer": res["answer"], "score": res["score"]} for res in results]'''