# AI Code Review Platform

AI-powered code review platform that analyzes pull requests for bugs, security risks, performance issues, and maintainability problems.

## What It Does

- Reviews pull request diffs
- Detects risky code changes
- Flags security vulnerabilities
- Finds performance issues
- Scores maintainability
- Generates actionable review comments

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- OpenAI API
- Docker
- GitHub Actions

## Architecture

GitHub Pull Request → FastAPI API → Diff Parser → AI Review Engine → Risk Scoring → PostgreSQL / Redis → Review Dashboard

## Example Output

```json
{
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
