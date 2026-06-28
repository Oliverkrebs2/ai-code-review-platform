def analyze_pull_request():
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
                "suggestion": "Batch database calls or use eager loading.",
            },
            {
                "severity": "low",
                "category": "maintainability",
                "file": "controllers/auth.py",
                "line": 41,
                "message": "Function is handling validation, authentication, and response formatting.",
                "suggestion": "Split this into smaller service-layer functions.",
            },
        ],
    }
