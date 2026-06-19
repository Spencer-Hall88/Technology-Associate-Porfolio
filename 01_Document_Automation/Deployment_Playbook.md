# Incident Report Generator

## Overview
This project is an automated pipeline that transforms raw, unstructured troubleshooting transcripts into formal, compliance-ready Incident Reports. By replicating the backend logic of M365 Copilot, this project demonstrates proficiency in AI orchestration, local LLM deployment, and enterprise document automation.

## Visual Architecture
![Incident Pipeline](assets/incident_report.png)

---

## Standard Operating Procedure: AI-Automated Incident Report Generator

## Document Purpose

This runbook details the deployment steps and architectural configuration for the AI-Automated Incident Report Generator. It provides the necessary specifications for an engineer to replicate the local LLM orchestration, data ingestion pipeline, and automated document generation logic required to transform unstructured troubleshooting data into standardized corporate reports.

## Phase 1: Local Inference & Data Environment

*This phase configures the local compute environment, establishing the LLM inference server (architectural equivalent to the Azure OpenAI Service layer).*

**1. Inference Server Setup**

* Install and launch **LM Studio**.
* Navigate to the "Local Server" tab and configure the API server port to `1234`.
* Load a high-performance instruction-tuned model (e.g., Llama-3-8B-Instruct or Mistral-7B).
* Start the server to expose the OpenAI-compatible API endpoint.

**2. Data Source Initialization**

* Provision the project workspace directory and the `data/` subdirectory.
* Create the `chat_transcript.txt` file within the data directory.
* **Schema Requirement:** The source file must contain raw, timestamped conversational text logs (unstructured data) to be ingested as the context payload.

## Phase 2: Pipeline Orchestration Logic

*This phase constructs the transformation logic, bridging the raw unstructured data to the structured document model (architectural equivalent to Microsoft 365 Copilot Semantic Indexing and Orchestration).*

**1. Environment & Dependency Configuration**

* Initialize a Python virtual environment: `python -m venv venv`.
* Install the necessary bridging and formatting libraries: `pip install openai python-docx`.

**2. Contextual Assembly & Prompt Engineering**

* Execute the `generate_report.py` pipeline.
* **Orchestration Logic:** The script performs a four-part framing process:
    * **Goal:** Assigns the summary task.
    * **Context:** Defines the "Incident Report" business outcome.
    * **Source:** Implements strict grounding to the `chat_transcript.txt` data.
    * **Expectation:** Enforces three-section structural constraints (`### Issue`, `### Troubleshooting Steps`, `### Resolution`).
* **Strategic Benefit:** Utilizing a low temperature ($\tau = 0.2$) during the inference call ensures deterministic factual extraction, minimizing hallucinations during the incident summary process.

## Phase 3: Automated Documentation Rendering

*This phase configures the presentation layer and document persistence (architectural equivalent to Microsoft Word’s automation and compliance export).*

**1. Document Object Model (DOM) Construction**

* The script initializes a blank document object via `python-docx`.
* Define structural parameters:
    * **Margins:** 1.0" top/bottom/left/right.
    * **Styling:** Applied globally using the Arial font family (standard corporate baseline).

**2. Parsing and Styling Injection**

* Iterate through the LLM’s structured response strings.
* Map LLM section headers to Word-native Heading objects to ensure accessibility and document navigation.
* Clean raw markdown characters (e.g., `**`, `###`) during ingestion to prevent formatting artifacts from appearing in the final production document.

**3. Persistence and State Management**

* The script saves the finalized object to the `outputs/` directory.
* **Strategic Benefit:** By automating the structural layout via the OpenXML standard, this pipeline eliminates human variability in documentation formatting, ensuring 100% compliance with corporate reporting standards for every incident generated.
