from fastapi import FastAPI

from app.review_engine import analyze_pull_request

app = FastAPI(title="AI Code Review Platform")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ai-code-review-platform"}


@app.post("/reviews/analyze")
def analyze_review():
    return analyze_pull_request()
