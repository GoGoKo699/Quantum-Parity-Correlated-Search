# Quantum Parity-Correlated Search

**Can Grover search stay fast when every partial view of the oracle's faults looks independent?** Yes. In this model each oracle call is omitted with probability one half. Every proper subset of calls in a block has exactly the independent fault law. The parity of the complete block is the only statistic that can differ.

For zero or one marked address among $`N\ge3`$, let $`L\ge3`$ be the length of each independent fault block. The parameter $`\eta`$ is the probability of drawing a block from the independent half-omission process. Otherwise the block has a supplied preferred parity. At fixed bounded error the optimal quantum query budget is

```math
Q_*(N,L,\eta)=\Theta\left(\min\left\{N,\ L\left(\sqrt N+\eta N\right)\right\}\right).
```

The constants are uniform in $`N`$, $`L`$ and $`\eta`$. The same order holds when the physical block offset is fixed and hidden. The matched classical bit-query budget is $`\Theta(N)`$. Ordinary phase queries suffice for the quantum construction, including candidate verification.

The algorithm interleaves the faulty calls with known reflections. A block with the preferred parity rotates the Grover state in a consistent direction on average. The lower bound uses the same full-block parity to factor the average block operator and bound the progress of arbitrary adaptive algorithms. All physical calls count, including the calls used to verify an answer and the calls used to cross a block boundary.

| Regime | Optimal quantum calls |
|---|---:|
| Perfect preferred parity and fixed $`L`$ | $`\Theta(\sqrt N)`$ |
| Perfect preferred parity and growing $`L`$ | $`\Theta(\min\{N,L\sqrt N\})`$ |
| Independent omissions | $`\Theta(N)`$ |

## Read the science

Start with the [model and theorem](science/model.md), then follow the [search and certification algorithm](science/construction.md), [adaptive lower bound](science/converse.md), and [hidden block boundaries](science/hidden-boundaries.md). The [interpretation](science/interpretation.md) explains which statistics control the advantage and which costs the result charges. [Related work](references/RELATED_WORK.md) traces the inherited reflection algebra, the independent-fault lower bound, and the paired model.

## Learn the project

The educational anchor is Andrew M. Childs's *Lecture Notes on Quantum Algorithms* (17 April 2025). The [Childs bridge](learning/CHILDS_BRIDGE.md) leads from basic query access and clean Grover rotations to the fault-block proof. The [30-milestone map](learning/MILESTONES.md) gives a route through the complete argument.

## Reproduce the finite checks

See the [verification guide](verification/README.md) for commands, tested cases, and the analytical claims each check illustrates. The [LLM reading guide](llms.txt) maps questions to the corresponding source files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
