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

## Run the block-parity search

1. Prepare the uniform superposition over the valid addresses at the start of each trial. Use the [fixed search length](science/construction.md#fixed-budgets-and-phase-only-certification) `t` and make `tL` ordinary phase queries. Apply the Grover diffuser after every query by default. To implement it up to a global phase, undo the uniform preparation, flip the phase of the zero state, and prepare again. For negative preferred parity with known boundaries, skip diffusion after the first query of each block. For negative preferred parity with a hidden offset, choose uniformly between two distinct residues modulo `L` each trial and skip diffusion at the chosen residue relative to the trial start.
2. Measure in the address basis. With known boundaries, use a fresh block for the certificate. With a hidden offset, send `L` scratch basis-state queries before the certificate. For the candidate `y`, pick two distinct reference addresses other than `y`. For each reference, prepare the equal plus superposition of the candidate and reference, issue one ordinary phase query, and measure in their plus/minus basis. Run the two tests in consecutive slots and return `y` only if both results are minus. On the empty input every test returns plus.
3. Before any next trial, fill the certificate block’s remaining slots with scratch basis-state queries if boundaries are known. With a hidden offset, make another `L` scratch basis-state queries before the next trial. Charge every physical call, including scratch and certificate queries. Stop when a candidate is certified. Return `none` if the budget is exhausted. Use the appropriate fixed repetition count for [aligned blocks](science/construction.md#fixed-budgets-and-phase-only-certification) or [hidden boundaries](science/hidden-boundaries.md#independence-and-charged-overhead).

Use the direct scan for fewer than 1,024 addresses or whenever its fixed budget is smaller. Scan all addresses up to nine times, running the two consecutive certificate queries on each candidate without padding. This costs at most `18N` calls. These budgets count submitted oracle calls. Applying the construction requires a predicate device with the stated omission model and separate accounting for preparation and known controls. See the [resource scope](science/interpretation.md).

## Read the science

Start with the [model and theorem](science/model.md), then follow the [search and certification algorithm](science/construction.md), [adaptive lower bound](science/converse.md), and [hidden block boundaries](science/hidden-boundaries.md). The [interpretation](science/interpretation.md) explains which statistics control the advantage and which costs the result charges. [Related work](references/RELATED_WORK.md) traces the inherited reflection algebra, the independent-fault lower bound, and the paired model.

## Learn the project

The educational anchor is Andrew M. Childs's *Lecture Notes on Quantum Algorithms* (17 April 2025). The [Childs bridge](learning/CHILDS_BRIDGE.md) leads from basic query access and clean Grover rotations to the fault-block proof. The [30-milestone map](learning/MILESTONES.md) gives a route through the complete argument.

## Reproduce the finite checks

See the [verification guide](verification/README.md) for commands, tested cases, and the analytical claims each check illustrates. The [LLM reading guide](llms.txt) maps questions to the corresponding source files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
