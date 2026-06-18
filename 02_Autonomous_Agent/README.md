# Autonomous AI Data Analyst Agent (ReAct Framework)

An enterprise-ready AI orchestration pipeline built in n8n that leverages Large Language Models to dynamically reason, select, and chain custom data tools to solve complex reporting requests.

## System Architecture Overview
The workflow bridges an interactive customer chat interface to a reasoning model (`gemini-2.5-flash-lite`), a conversation state buffer, and specialized tool runtimes.

![n8n System Architecture](images/workflow_blueprint.png)

## Execution Trace & Dynamic Tool Routing
This log captures the agent's internal monologue resolving a complex multi-step prompt. Notice how the agent breaks down the request, executes the custom JavaScript Code Tool to pull database strings, extracts the numerical values, and passes them to the Calculator node.

![n8n Internal Monologue Execution](images/execution_log.png)

## The Result: Autonomous Execution
This final view demonstrates the seamless end-user experience. While the ReAct loop handles the complex logic of selecting tools, pulling mock database records, and executing mathematical formulas in the background, the user is presented with a clean, conversational, and highly accurate response.

![n8n Final Chat Output](images/chat_response.png)
