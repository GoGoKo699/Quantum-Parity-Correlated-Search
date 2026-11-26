# Lower bound for adaptive search

Allow the algorithm to use controlled queries, arbitrary memory, and adaptive operations. It suffices to lower bound a purified fixed-query circuit. Deferred measurement keeps the classical records in ancillas. Early stopping can retain its result and pad to the fixed horizon, using the query control to make padding act trivially on that branch. For the bit interface a Hadamard on its answer bit gives the controlled phase reflection.

Write $`\psi`$ for the unit state on the empty input at the beginning of an interval and $`\rho_x`$ for the state for mark $`x`$. Start with $`\rho_x=|\psi\rangle\langle\psi|`$. We track a vector $`\phi_x`$ such that $`\rho_x\succeq|\phi_x\rangle\langle\phi_x|`$. If a new independent interval has query-circuit unitaries $`V_s`$ conditional on its signs, updating $`\phi_x`$ by $`\mathbb E_s V_s`$ preserves this positive-semidefinite domination. This follows from the positive semidefiniteness of the covariance of $`V_s\phi_x`$; the remaining density-operator contribution is also positive under the channel.

Use the interaction frame of the empty-input circuit within each interval. The state $`\psi`$ is then unchanged across it. Let $`Q_j`$ denote the marked reflection projector for the $`j`$th call in that frame, and put $`P_j=I-Q_j`$. The projector depends on $`x`$; for each fixed $`j`$, the family satisfies $`\sum_x Q_j\preceq I`$. An active call applies $`I-2Q_j`$. For a fair sign, the unsigned mean of the slot operator is $`P_j`$ and its sign-weighted mean is $`-Q_j`$.

## One block

Averaging the ordered product with the block law gives the exact mean operator

```math
K=P_L\cdots P_1+\mu Q_L\cdots Q_1,\qquad \mu=(-1)^L\kappa.
```

The two terms have orthogonal ranges at the final slot. Suppress the mark subscript temporarily, set $`H=\|\psi-\phi\|^2`$, and write $`\Delta=\|\phi\|^2-\|K\phi\|^2`$. Define $`f_j=Q_jP_{j-1}\cdots P_1\phi`$ with $`f_1=Q_1\phi`$. Telescoping the squared losses along the product of orthogonal projections gives

```math
\Delta
=\sum_{j=1}^{L}\|f_j\|^2-\mu^2\|Q_L\cdots Q_1\phi\|^2
\ge\sum_{j=2}^{L}\|f_j\|^2+(1-\kappa^2)\|Q_1\phi\|^2.
```

The potential gain is

```math
H^+-H=2\operatorname{Re}\langle\psi,(I-K)\phi\rangle-\Delta .
```

Using $`(I-P_L\cdots P_1)\phi=\sum_j f_j`$, complete the square for every $`j\ge2`$. Its combined contribution is at most $`\|Q_j\psi\|^2`$. The magnitude of the remaining overlap is bounded by $`A_x\|Q_1\phi_x\|`$, where $`A_x=\|Q_1\psi\|+\|Q_L\psi\|`$. This uses the range of each end projection and contractivity of their product. We have $`\sum_x A_x^2\le4`$ and $`\sum_x\|Q_j\psi\|^2\le1`$.

For the aggregate $`S=\sum_x H_x`$, use $`\|Q_1\phi_x\|\le\|Q_1\psi\|+\sqrt{H_x}`$ and Cauchy–Schwarz. One bound is

```math
S^+-S\le (L-1)+4(1+\sqrt S).
```

Alternatively complete the square for the remaining overlap against the $`(1-\kappa^2)\|Q_1\phi_x\|^2`$ loss. If $`|\kappa|<1`$, this gives

```math
S^+-S\le (L-1)+\frac{4}{1-\kappa^2}.
```

## Partial blocks and terminal progress

A proper segment of a new block has fair independent signs. If the circuit uses $`r<L`$ slots of that block, its average interaction-frame operator is just $`P_r\cdots P_1`$. The same telescoping argument bounds its aggregate gain by $`r`$, since each loss $`\|f_j\|^2`$ pays for its overlap. This applies to a final incomplete block and any first partial block. Such intervals are independent of the other blocks. If all calls fall in a single partial block there is just one interval.

Let $`T`$ be the number of calls and $`B\le T/L`$ the number of complete blocks. Starting from $`S=0`$, let $`M`$ be the largest potential at any processed interval endpoint. Summing the first gain bound up to an endpoint attaining $`M`$ gives $`M\le C(T+B\sqrt M)`$ for an absolute constant $`C`$. Moving half of $`M`$ to the left by the elementary quadratic inequality for $`B\sqrt M`$ yields $`M=O(T+B^2)`$. The second gain bound also gives $`S=O(T+B/\eta)`$ when $`\eta=1-|\kappa|>0`$, using $`1-\kappa^2\ge\eta`$.

At the end, the probability of the event `none` differs by at least $`4/5`$ between the empty input and every mark. The trace-distance bound against a pure state gives $`\langle\psi|\rho_x|\psi\rangle\le9/25`$. Since $`\rho_x\succeq|\phi_x\rangle\langle\phi_x|`$, Cauchy–Schwarz gives $`H_x\ge(1-|\langle\psi,\phi_x\rangle|)^2\ge4/25`$. Therefore $`S\ge4N/25`$.

Combining the progress and terminal bounds gives

```math
T=\Omega(\min\{N,L\sqrt N\}),\qquad
T=\Omega(\min\{N,LN\eta\})
```

where the second statement is automatic at $`\eta=0`$. Taking their maximum proves $`T=\Omega(\min\{N,L[\sqrt N+N\eta]\})`$. The proof charges each query in an incomplete block directly. It holds at every fixed initial offset even if the circuit is told the offset.
