# 06 — Quantum Entanglement

Quantum entanglement is a property of a joint quantum state in which the state of a composite system cannot be expressed as a product of states belonging to its separate parts.

Entangled systems can exhibit correlations between measurement outcomes that are stronger than correlations allowed by local hidden-variable models.

## Product and entangled states

A two-qubit product state can be written as:

\[
|\psi\rangle_A \otimes |\phi\rangle_B.
\]

A Bell state that cannot be expressed in this product form is:

\[
|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle).
\]

## Measurement example

When \(|\Phi^+\rangle\) is measured in the computational basis:
- 00 occurs with probability 1/2.
- 11 occurs with probability 1/2.

Each individual qubit has a 50/50 marginal distribution, while the joint outcomes are perfectly correlated in this basis.

## Visual reference

![Illustration of two entangled particles](https://commons.wikimedia.org/wiki/Special:FilePath/Entangled_particles.svg)

*Sean Kelley / The Quantum Atlas, via Wikimedia Commons. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). [Source and attribution](https://commons.wikimedia.org/wiki/File:Entangled_particles.svg).*

## Topics in this module
- Joint quantum states
- Separable and entangled states
- Bell states
- Quantum correlations
- Einstein–Podolsky–Rosen (EPR) paradox
- Bell's theorem and Bell inequalities
- No-signalling
- Multipartite entanglement, including GHZ and W states

## Correlation is not faster-than-light messaging

Entanglement produces non-classical correlations, but it does not provide a way to transmit usable information faster than light. Comparing results requires a classical communication channel.

## Example

See [bell_state_sampling.py](../../examples/python/bell_state_sampling.py). It samples the ideal 00/11 probability distribution for \(|\Phi^+\rangle\). It is a toy sampler, not a physical quantum simulator.

## Current learning boundary

This concludes the current foundational quantum study. Quantum gates, circuits, algorithms, and hardware are reserved for a future stage.
