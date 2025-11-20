from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
#pip install uvicorn

app = FastAPI()
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

class QARequest(BaseModel):
  question: str
  context: str

@app.post("/ask/")
def ask_question(request: QARequest):
  result = qa_pipeline(question=request.question, context=request.context)
  return {"answer": result["answer"], "score": result["score"]}

  #run in terminal: python -m uvicorn nlp-api:app --reload