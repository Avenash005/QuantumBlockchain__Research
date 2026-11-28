# 03 — Qubits

A qubit is a two-level quantum system used as a unit of quantum information. A pure qubit state in the computational basis is:

\[
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle,
\qquad |\alpha|^2 + |\beta|^2 = 1.
\]

Here, \(\alpha\) and \(\beta\) are complex probability amplitudes. The normalization condition means the total probability of the computational-basis outcomes is one.

## Measurement preview
- Outcome 0 occurs with probability \(|\alpha|^2\).
- Outcome 1 occurs with probability \(|\beta|^2\).

A measurement gives a definite outcome. The state determines the probability distribution; it does not mean a measurement reads both values at once.

## Classical bit and qubit

| Classical bit | Qubit |
|---|---|
| Logical value 0 or 1 | Quantum state vector |
| Classical uncertainty can be represented by probabilities | Amplitudes can produce interference |
| Classical data can be copied | An unknown quantum state cannot be perfectly cloned in general |

## State overview

```mermaid
flowchart TD
  A[Qubit state] --> B[Amplitude for |0>]
  A --> C[Amplitude for |1>]
  B --> D[Normalization]
  C --> D
  D --> E[Measurement probabilities]
```

## Questions
- What is a basis?
- Why are amplitudes complex?
- How does the measurement basis affect probabilities?
