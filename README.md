<div align="center">
  <img src="https://img.icons8.com/color/96/000000/brain.png" alt="Brain Icon" width="80" />
  <h1>Clinical Grounded Generation Pipeline</h1>
  <p><em>Robust, Schema-Validated RAG Pipeline with Built-in Refusal Mechanisms</em></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python" />
    <img src="https://img.shields.io/badge/LangChain-Enabled-green.svg" alt="LangChain" />
    <img src="https://img.shields.io/badge/JSON-Schema_Validation-orange.svg" alt="Schema" />
    <img src="https://img.shields.io/badge/Status-Production_Ready-success.svg" alt="Status" />
  </p>
</div>

## 📌 Overview

The **Clinical Grounded Generation Pipeline** is an advanced RAG (Retrieval-Augmented Generation) component designed to guarantee that Large Language Models (LLMs) only generate answers grounded in verified context. It employs strict JSON schema validation, rigorous prompt engineering, and deterministic refusal mechanisms to prevent hallucinations and handle off-topic queries gracefully.

This repository demonstrates how to bind LLM outputs to a strict schema and reject unverified responses, making it highly suitable for clinical and enterprise environments.

## 🏗️ Architecture

```mermaid
flowchart TD
    %% Define Styles
    classDef user fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b;
    classDef system fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px,color:#4a148c;
    classDef db fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#1b5e20;
    classDef error fill:#ffebee,stroke:#d32f2f,stroke-width:2px,color:#b71c1c;

    %% Nodes
    A([User Query]):::user
    B[Vector Store Retrieval]:::db
    C{Context Found?}:::system
    D[LLM Generation<br>with Grounding Prompt]:::system
    E[JSON Output]:::system
    F{JSON Schema<br>Validation}:::system
    G([Return Grounded Response]):::user
    H([Trigger Refusal / Fallback]):::error

    %% Connections
    A --> B
    B --> C
    C -- Yes --> D
    C -- No --> H
    D --> E
    E --> F
    F -- Valid JSON + Confidence --> G
    F -- Invalid / Insufficient Confidence --> H
```

## ✨ Key Features

- **Strict Grounding Prompt:** A carefully crafted system prompt that positions the LLM as a highly constrained clinical assistant.
- **Deterministic Refusal:** Off-topic or unanswerable queries trigger a structured refusal with `confidence: "insufficient"`.
- **JSON Schema Enforcement:** Output is strictly bound to a `jsonschema` definition, forcing the LLM to provide evidence and citations for any confident claim.
- **Simulation Mode:** Run the pipeline without API keys to verify logic and schema handling against mock LLM responses.
- **Regression Testing:** Built-in validation against adversarial and off-topic test cases (`Day3_Refusal_Test_Cases.csv`).

## 🛠️ Requirements

- `python 3.10+`
- `langchain`
- `jsonschema`
- `pypdf`
- `fastembed`
- `chromadb`

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ahmednashatnoaman-svg/clinical-grounded-generation.git
   cd clinical-grounded-generation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Explore the Notebook:**
   Open `Task3_Grounded_Generation.ipynb` to see the end-to-end pipeline in action, including the simulated LLM generation and schema validation processes.

## 📖 Design Justification
For a detailed explanation of the prompt engineering and JSON schema decisions, please refer to the [JUSTIFICATION.md](JUSTIFICATION.md) file.
