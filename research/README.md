# Research Workspace

## Current research direction

**Working theme:** LLM-based text representations with classical and quantum/hybrid machine-learning classifiers.

The goal is to study whether quantum or hybrid approaches offer measurable benefits for a carefully defined text-classification task, rather than assuming an advantage in advance.

## Planned workflow

1. Select a suitable public text-classification dataset and record its licence.
2. Define labels, train/validation/test splits, and baseline metrics.
3. Clean and preprocess text consistently.
4. Generate text embeddings with a documented LLM or embedding model.
5. Analyze embedding dimensions and consider dimensionality reduction.
6. Train classical baseline classifiers.
7. Implement suitable quantum or hybrid classifiers at a feasible scale.
8. Evaluate using consistent splits and metrics.
9. Compare accuracy, F1, runtime, resource requirements, and limitations.
10. Document results so another researcher can reproduce the experiment.

## Research integrity

Keep the test set isolated from model and hyperparameter selection. Record random seeds, model versions, package versions, and hardware/simulator settings. Report unsuccessful runs and constraints. Do not claim quantum advantage unless supported by a fair and reproducible experiment.
