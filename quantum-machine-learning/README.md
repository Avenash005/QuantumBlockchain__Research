# Quantum Machine Learning (QML)

Quantum machine learning studies the integration of quantum computing with machine-learning methods. This folder will cover quantum-enhanced classical methods, native quantum learning models, and hybrid quantum-classical workflows.

## Learning roadmap
1. QML overview and mathematical prerequisites
2. Classical data encoding and quantum feature maps
3. Quantum kernels and state fidelity
4. Quantum Support Vector Machines (QSVM)
5. Quantum K-Nearest Neighbors (QKNN)
6. Quantum Neural Networks (QNNs)
7. Hybrid quantum-classical training
8. Noise, resource requirements, scalability, and evaluation

## Approaches to distinguish

- **Quantum-enhanced classical ML:** use quantum routines as components of classical models, for example a quantum kernel with an SVM.
- **Native QML:** formulate a learning model using quantum states and operations.
- **Hybrid QML:** combine classical preprocessing or optimization with quantum computation.

## Important evaluation cautions

Quantum methods are not automatically faster or more accurate. Account for data encoding, circuit depth, number of measurements/shots, hardware or simulator noise, classical optimization, and end-to-end runtime. Compare against credible classical baselines.

## Initial review paper

Devadas, R. M., & T, S. (2025). *Quantum machine learning: A comprehensive review of integrating AI with quantum computing for computational advancements*. MethodsX, 14, 103318. [https://doi.org/10.1016/j.mex.2025.103318](https://doi.org/10.1016/j.mex.2025.103318)

The review surveys SVM, KNN, QNN, feature mapping, distance metrics, and hybrid architectures. It also highlights noise sensitivity, hardware constraints, scalability, and training cost. See `references/research-papers.md` for the citation record.
