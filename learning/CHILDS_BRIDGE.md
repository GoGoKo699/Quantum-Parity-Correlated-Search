# From clean Grover search to parity-correlated search

Suppose an oracle marks one address by flipping its phase. Half of the
submitted calls are misses on average, and even two calls at different
times reveal no correlation. The algorithm still has a way to make several
calls work together. A full block can carry a parity bias that no proper
subset of its calls reveals.

The educational anchor is **Andrew M. Childs, *Lecture Notes on Quantum
Algorithms*, 17 April 2025**. The [author's page](https://www.cs.umd.edu/~amchilds/qa/)
and [author-hosted notes](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) identify
the version used here. The page numbers below are the notes' printed pages.
The [30 milestones](MILESTONES.md) follow the connections from the clean
problem to the correlated one. The [scientific model](../science/model.md)
states the promises and results.

## Targeted reading

| Sections in Childs | Milestones | What to bring to this project |
|---|---|---|
| §21.1, p. 97 | M01, M02 | Oracle access, bounded error, and counting calls independently of the interleaved controls. |
| §21.2, p. 98 | M03, M04, M09 | The reversible bit oracle, phase kickback, and query algorithms with arbitrary workspace. Read the phase oracle with both response eigenspaces before specializing to an ordinary address phase query. |
| §19.1, p. 87 | M05–M07, M11 | The marked subspace, the uniform state, the two reflections in clean Grover search, and the clean classical and quantum benchmarks. |
| §23.1, pp. 109–110, and §23.3, pp. 113–114 | M08, M25, M28 | Tracking query-by-query progress toward distinguishing the empty oracle from each single-mark oracle. §23.3 applies the idea to the same zero-or-one promise. |

Childs uses input parity as a different query problem in §21.5. Here
the input is a zero-or-one marked set, and parity is a statistic of the
environment's fault signs. The notes establish the clean search foundations.
The parity model, both sign-dependent schedules, and the noisy converse are
developed in the project.

## From bit access to an angle update

A clean bit query sends $`|i,b\rangle`$ to $`|i,b\oplus f(i)\rangle`$.
Using the response eigenstate $`|-\rangle=(|0\rangle-|1\rangle)/\sqrt{2}`$
makes one such query act on the address by $`(-1)^{f(i)}`$. On a unique
mark $`x`$, write that ordinary phase oracle as
$`O_x=I-2|x\rangle\langle x|`$. Its sign differs from the reflection about
the marked subspace in Childs §19.1 by a global phase, so the clean
measurement probabilities agree. In the fault model the two possible
address operations are explicitly $`O_x`$ and $`I`$. The converse works
with arbitrary reversible bit-query access and arbitrary response states.
A submitted call costs one in either model, including a call whose
response is set to an oracle-insensitive eigenstate.

Set $`|u\rangle`$ to the uniform superposition of the unmarked addresses and
write a real state in the invariant plane as
$`\sin\phi\,|x\rangle+\cos\phi\,|u\rangle`$. For the uniform initial state
$`|S\rangle`$, the initial angle satisfies $`\sin\theta=1/\sqrt N`$.
The reflection $`D=2|S\rangle\langle S|-I`$ sends an angle $`\alpha`$
to $`2\theta-\alpha`$. An active call $`O_x`$ negates $`\phi`$, so the
usual clean iterate adds $`2\theta`$. An omitted call leaves $`\phi`$
alone, so diffusion now reverses the angle about $`\theta`$.
With $`s=+1`$ for active and $`s=-1`$ for omitted, the two steps together
give

```math
\phi\ \longmapsto\ 2\theta+s\phi.
```

This affine form exposes what successive calls can preserve. Their angle
coefficient multiplies, while the added angles depend on suffix products.

## A complete length-three example

Take $`L=3`$, positive fixed parity $`\kappa=1`$, and one marked address.
Each of the four rows below occurs with probability $`1/4`$. There is
diffusion after every call. The middle column comes from composing three
copies of the update above, and the final angle uses input $`\phi=\theta`$.

| Fault signs | Block update | Final angle |
|---|---|---|
| $`(+,+,+)`$ | $`\phi+6\theta`$ | $`7\theta`$ |
| $`(+,-,-)`$ | $`\phi+2\theta`$ | $`3\theta`$ |
| $`(-,+,-)`$ | $`\phi-2\theta`$ | $`-\theta`$ |
| $`(-,-,+)`$ | $`\phi+2\theta`$ | $`3\theta`$ |

Every pair of signs has the four equally likely outcomes. The whole
sequence nevertheless preserves orientation on every row. The random angle
increment has mean $`2\theta`$. One submitted block costs three queries.
For example, the probability to sample the mark after this block from
$`|S\rangle`$ is
$`[\sin^2(7\theta)+2\sin^2(3\theta)+\sin^2(\theta)]/4`$.
The coherent effect concerns the conditional angle distribution, so taking
the sine squared of its mean would give a different calculation.

For negative preferred parity, omitting the **first diffusion** changes its
update to $`\phi\mapsto-s_1\phi`$. Every block still uses three oracle calls.
The extra minus sign makes the orientation positive on the preferred
parity, and leaving out the first constant addition changes the list of
random suffix terms. The [construction](../science/construction.md)
counts those terms and computes the success probability for any block size.

## From a rotated state to a verified answer

If $`\eta=1-|\kappa|`$, a block has preferred orientation with probability
$`1-\eta/2`$ under the corresponding schedule. An independent run of
$`t`$ blocks sees a constant probability of all preferred events up to
$`t`$ of order $`1/\eta`$. At $`t`$ of order $`\sqrt N`$, even clean Grover
rotation is on the scale of a constant angle. Choose the shorter scale.
The exact second-harmonic calculation gives a candidate probability
$`\Omega(t^2/N)`$ on that run scale. The failure to observe any fault flags
is compatible with this use of conditioning. The calculation proves a
bound on the actual unconditioned trials.

A sampled address is a candidate. For each of two distinct reference
addresses, put that address and the candidate in an equal superposition,
submit an ordinary phase query, and check whether the resulting relative
sign is minus. A wrong candidate can pass at most one test because there
is at most one mark. A true candidate passes both when both calls are
active, an event of probability $`1/4`$ for these two slots. Empty
instances can then lead to a null answer. Repeated fresh trials with
padding and verification cost $`O(LN/t)`$, and a charged direct scan
also supplies an $`O(N)`$ route. The [algorithm proof](../science/construction.md)
gives the parameter choice, finite budgets and success guarantee.

## Progress for a whole noisy block

Childs compares clean algorithms on different input oracles. For noisy
queries, first move all known controls into a common frame. In this
frame the marked action in one slot is a reflection $`I-2Q_j`$, while
the empty input stays in a fixed pure reference state. Put
$`P_j=I-Q_j`$. For one fixed mark the full-block average unitary is

```math
K=P_L\cdots P_1+(-1)^L\kappa Q_L\cdots Q_1.
```

At each slot the fair mean is $`P_j`$, and the sign-weighted fair mean
is $`-Q_j`$. The block law has a constant Walsh component and one full
parity component. Their ordered products give exactly the two terms in
$`K`$. The true averaged output is a density operator, with the mean
amplitude giving one retained substate. Indeed, for branch unitaries
$`U_s`$, the difference between the average channel and
$`\rho\mapsto K\rho K^\dagger`$ is the completely positive map
$`\rho\mapsto\mathbb E_s[(U_s-K)\rho(U_s-K)^\dagger]`$.

The first term of $`K`$ ends in the range of $`P_L`$ and the second
ends in the orthogonal range of $`Q_L`$. Their squared norms therefore
add. Telescoping the first product uses the amount of amplitude each
projection discards. The parity term can spare some first-slot
amplitude, so the converse uses two bounds on this exception: one from
summing over all possible marks, and one from the scale
$`1-\kappa^2`$ of the remaining norm loss. The
[converse](../science/converse.md) shows why the cheaper estimate
governs and why the final incomplete block has only an independent-fault
contribution. Comparing the substate to the empty-input state closes the
lower bound for adaptive bit-query algorithms.

## What the comparison establishes

For the promised model, the optimal physical query count is

```math
\Theta\!\left(\min\!\left\{N,\ L\bigl(\sqrt N+\eta N\bigr)\right\}\right).
```

The $`L`$ multiplier charges all submissions used to expose full parity.
The $`\sqrt N`$ and $`\eta N`$ terms describe the useful-run length and
the penalty from wrong-parity blocks. Changing the sign of $`\kappa`$
changes the diffusion placement, while reflecting its magnitude about
zero leaves the complexity scale the same. When independent half
omissions are recovered at $`\kappa=0`$, or the block overhead dominates,
the charged direct scan has the optimal scale. The classical comparison
uses the same physical fault process with bit-query access and costs
$`\Theta(N)`$.

The same budget order holds for an unannounced fixed offset. Periodic
control, proper endpoint fragments and charged trial gaps give uniform
success over the possible offsets. The analysis requires a stable phase
of the length-$`L`$ block clock and independently generated blocks. See
the [hidden-boundary proof](../science/hidden-boundaries.md).

[Scientific route](../science/README.md) · [30 milestones](MILESTONES.md)
