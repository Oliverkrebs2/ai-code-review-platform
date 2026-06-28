# API Documentation

## GET /health

Returns service health status.

## POST /reviews/analyze

Runs a mock pull request analysis and returns a score, summary, and issues.

## Example Response

```json
{
  "score": 82,
  "summary": "The pull request is mostly safe but includes a potential N+1 query and missing input validation.",
  "issues": []
}
