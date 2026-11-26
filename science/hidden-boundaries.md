# Search without knowing the block boundaries

The search phase of a trial takes $`tL`$ consecutive calls, with $`t`$ chosen as in the [aligned construction](construction.md#fixed-budgets-and-phase-only-certification). If it starts at a block boundary there are $`t`$ full blocks. Otherwise there are $`k=t-1`$ full blocks bracketed by two nonempty partial blocks. The offset may be arbitrary and is fixed throughout the algorithm.

For $`\kappa\ge0`$, apply diffusion after every search query. For $`\kappa \lt 0`$, choose uniformly from two distinct residues modulo $`L`$ at the beginning of the trial. Omit diffusion after the calls at the selected residue relative to the beginning of search. Every full block contains exactly one omission of diffusion. For each initial offset, at most one of the two choices omits the diffuser at the last slot of a full block. The other choice gives the favorable-block rotation law from the [aligned construction](construction.md#an-aligned-block-becomes-a-rotation). That law uses the number of omitted diffusers and the fact that the last diffuser is present. The position of the omission before the last slot is immaterial to the independent suffix products. Call a trial's schedule valid when it leaves the last diffuser in place for full blocks. This event has probability at least $`1/2`$.

## The two partial blocks

In a proper segment of length $`r`$, the activation signs are independent and fair. Let $`d_j`$ indicate that the diffuser is applied, and set $`a_j=s_j`$ when $`d_j=1`$ and $`a_j=-s_j`$ otherwise. For the affine update

```math
c\longmapsto Ac+B,\qquad
A=\prod_{j=1}^r a_j,\qquad
B=d_r+\sum_{j=1}^{r-1}d_j\prod_{\ell=j+1}^r a_\ell,
```

the total product and the $`r-1`$ suffix products appearing in $`B`$ are independent fair signs. The map from effective signs to all these products is a bijection. The partial block's input is independent of its own signs, even after conditioning on full blocks being favorable. For the angular characteristic function $`z=\mathbb E e^{i4\theta c}`$, the partial segment therefore produces

```math
z\longmapsto e^{i4\theta d_r}
(\cos 4\theta)^{\sum_{j=1}^{r-1} d_j}
\mathrm{Re}z .
```

A favorable full block with a valid schedule produces $`z\mapsto e^{i4\theta}(\cos4\theta)^m z`$, with $`m=L-1`$ or $`L-2`$ as in the aligned construction.

Starting with $`z=e^{i2\theta}`$, compose the first partial map, the $`k`$ full-block maps, and the last partial map. With a valid schedule and all full blocks favorable, the real part of the final characteristic function is

```math
a\cos\!\bigl(4\theta(k+d_{\rm first})\bigr)
\cos(4\theta d_{\rm last}),
\qquad 0\le a\le1 .
```

Here $`d_{\rm first}`$ and $`d_{\rm last}`$ indicate diffusion at the last call of the first and last partial segments, respectively. The real nonnegative attenuation $`a`$ includes $`\cos2\theta`$ and the powers of $`\cos4\theta`$ from the three types of maps. For $`N\ge1024`$, the chosen $`t`$ makes all these angles lie in $`[0,\pi/2)`$. It follows by monotonicity of cosine that the conditional search success probability is at least $`\sin^2(2\theta k)\ge 4t^2/(\pi^2N)`$, since $`k=t-1\ge t/2`$. For the aligned case the same bound follows from the exact full-block formula. The probability of all the full blocks being favorable is at least $`1/4`$, since there are at most $`t`$ of them.

## Independence and charged overhead

After search, send $`L`$ scratch basis-state queries before the two certificate calls. This ensures that no block contains both a search call and a certificate call. Take the two tests consecutively. Their signs are independent fair signs, including if they straddle a block boundary. Add another $`L`$ scratch calls before any subsequent trial to separate the relevant blocks of distinct trials. The scratch calls are discarded and reveal no signs.

Each trial uses at most $`tL+2L+2`$ calls. Its probability of certifying the mark is at least $`t^2/(8\pi^2N)`$, uniformly in the fixed offset. Trials use independent blocks and fresh schedule coins given the offset. Use $`\lceil 8\pi^2\log(10)\,N/t^2\rceil`$ trials, or use the $`18N`$-call fallback whenever it has a smaller fixed budget. The search then achieves the same asymptotic cost as when the boundaries are known. The [converse](converse.md#partial-blocks-and-terminal-progress) already charges both partial blocks at any fixed offset.

If the fixed offset is sampled uniformly once and kept hidden, the resulting stationary process has the same query order even when success is required only on average over the offset. The upper bound is uniform. For the lower bound, use the potential bound at each offset. For each mark, let the difference in the probability of `none` between the empty and marked inputs be a function of the offset. Its average is at least $`4/5`$, and the difference is bounded above by $`1`$. It is at least $`3/5`$ on at least half the offsets. At those offsets the terminal argument gives $`H_x\ge(1-4/5)^2`$. Averaging the terminal potential over offsets still gives $`\Omega(N)`$, which yields the same lower bound.
