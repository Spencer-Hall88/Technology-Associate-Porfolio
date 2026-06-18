# Autonomous AI Data Analyst Agent (ReAct Framework)

An enterprise-ready AI orchestration pipeline built in n8n that leverages Large Language Models to dynamically reason, select, and chain custom data tools to solve complex reporting requests.

## System Architecture Overview
The workflow bridges an interactive customer chat interface to a reasoning model (`gemini-2.5-flash-lite`), a conversation state buffer, and specialized tool runtimes.

![n8n System Architecture](images/workflow_blueprint.png)

## Execution Trace & Dynamic Tool Routing
This log captures the agent's internal monologue resolving a complex multi-step prompt. Notice how the agent breaks down the request, executes the custom JavaScript Code Tool to pull database strings, extracts the numerical values, and passes them to the Calculator node.

![n8n Internal Monologue Execution](images/execution_log.png)

## Key Learning: Mitigating Model Hallucinations
During production testing with compact models, the agent experienced tool-calling drift (hallucinating estimated numbers rather than parsing strict tool outputs). This repository documents the prompt engineering guardrails and strict data-serialization methods applied to achieve deterministic outputs.
