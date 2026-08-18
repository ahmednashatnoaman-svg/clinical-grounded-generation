# Design Justification: Grounded Generation and Refusal Pipeline

## 1. Grounding System Prompt Engineering
The system prompt was engineered around four critical pillars to ensure clinical safety and strict JSON formatting:

- **Role & Boundary Definition:** The LLM is strictly positioned as a clinical assistant that can *only* answer questions using the provided context.
- **Strict Structure:** The prompt enforces a JSON output containing `recommendation`, `evidence`, `citations`, and `confidence`. This structured output allows the application layer to deterministically parse and validate the LLM's response.
- **The Escape Hatch (Refusal):** The prompt explicitly instructs the LLM to return `confidence="insufficient"` when the provided context does not contain the answer, or when the query is entirely off-topic.

## 2. JSON Schema Validation
We utilize `jsonschema` to enforce structural and logical constraints on the LLM's output. The schema employs `allOf` conditions to enforce cross-field logic:
- If `confidence` is "insufficient", then `evidence` must be empty and `citations` must be an empty array.
- If `confidence` is "high", "medium", or "low", then `evidence` must have a length of at least 1, and `citations` must contain at least 1 item.

This prevents the LLM from outputting high confidence while failing to provide evidence, effectively blocking subtle hallucinations.

## 3. Regression Testing for Refusals
The solution utilizes a regression suite (`Day3_Refusal_Test_Cases.csv`) that includes adversarial queries (e.g., ignoring instructions, asking about sports, or requesting unauthorized medical advice). Testing the pipeline against this suite ensures that the refusal mechanisms are robust and trigger correctly.
