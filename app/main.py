from fastapi import FastAPI

app = FastAPI(title="AI Code Review Platform")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ai-code-review-platform"}


@app.post("/reviews/analyze")
def analyze_review():
    return {
        "score": 82,
        "summary": "The pull request is mostly safe but includes a potential N+1 query and missing input validation.",
        "issues": [
            {
                "severity": "medium",
                "category": "performance",
                "file": "services/users.py",
                "line": 88,
                "message": "Potential N+1 query pattern detected.",
                "suggestion": "Batch database calls or use eager loading."
            }
        ]
    }
