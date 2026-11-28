# Artificial Intelligence & Large Language Models

This section covers AI foundations and the language technologies relevant to the research direction.

## Planned modules
- AI fundamentals and problem formulation
- Neural networks and deep learning
- Natural language processing (NLP)
- Tokenization and text preprocessing
- Transformer architecture and attention
- Large language models: training, inference, capabilities, and limitations
- Text embeddings and semantic representations
- Embedding evaluation and dimensionality reduction
- Responsible evaluation and reproducibility

## Connection to the research project

The planned text-classification workflow uses an LLM to generate text embeddings from public datasets. Those embeddings may then be preprocessed and passed to classical, quantum, or hybrid classifiers. The LLM embedding stage and classifier stage should be evaluated and documented separately.

## Example workflow

```mermaid
flowchart LR
  A[Raw text] --> B[Preprocessing]
  B --> C[LLM encoder]
  C --> D[Embedding vectors]
  D --> E[Classifier]
  E --> F[Predicted class]
```

Document model name/version, pooling strategy, embedding dimension, token limits, preprocessing, and whether the embedding model is frozen.
