# Architecture

## System Flow

1. GitHub sends pull request metadata.
2. The API receives changed files and diff content.
3. The diff parser extracts relevant code blocks.
4. The AI review engine analyzes the changes.
5. The scoring layer assigns severity and confidence.
6. Results are stored and displayed in the dashboard.

## Core Components

- API Gateway
- GitHub Integration Service
- Diff Parser
- AI Review Engine
- Risk Scoring Service
- Review History Store
