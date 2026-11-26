# What the parity changes

A classical controller can generate the block distribution with a counter and one bit that tracks accumulated parity. It draws $`L-1`$ fair independent signs. It then selects the last sign by drawing the total parity with the supplied bias and dividing by the parity already accumulated. Starting a new block resets this record. This implementation needs no access to the marked address and does not reveal any fault flag to the search algorithm.

## Marginals and algorithms

An experiment that acts on only a proper subset of each block, inserting identity operations at the other fault slots, gets exactly the corresponding independent-fault process. This holds for any quantum interleaving supported on the chosen slots. It also holds for classical causal selection of slots when every execution path leaves at least one slot in each block unused: the probability of each transcript path depends on the joint marginal of the path's selected signs. A coherent superposition of schedules is a different access condition because its interfering branches can jointly use all slots.

The full block can carry a nonzero parity correlation even when any fixed list of fewer than $`L`$ calls is independent. At perfect preferred parity and $`L=o(\sqrt N)`$, [the query law](model.md) gives a sublinear quantum search cost. Taking $`L`$ to be a fixed large integer restores the square-root scaling while making all marginals up to that order minus one completely uninformative about the speedup. In contrast, an independent half-omission process has the same marginals at those orders and linear query complexity.

## The cost of accessing the correlation

The algorithm pays $`L`$ calls to use a block even when it performs only a few distinct types of known control. In the clean-parity regime, this factor comes on top of the square-root search scale. When $`\eta\sqrt N`$ grows beyond a constant, the preferred parity can persist for only order $`1/\eta`$ blocks before restarts become useful. The second term $`L\eta N`$ accounts for that loss. A full scan caps the query cost at order $`N`$ in either case.

The [lower bound](converse.md) makes these observations constraints on the task. Each full block can contribute only order $`L+\min\{\sqrt N,1/\eta\}`$ to aggregate progress against the no-mark reference. A partial block gives only order one progress per call. The two pieces match the quantum search plus the linear scan, including when the growing block length makes exploiting parity costlier than scanning.

The resource is the number of submitted oracle calls. Known control and state preparation have separate gate costs. In binary address representation the diffuser is a reflection about an explicitly prepared uniform superposition on the known addresses. The two-address checks likewise use only known candidate and reference indices. The model assumes ideal known controls and independent blocks with a fixed length. [A hidden fixed offset](hidden-boundaries.md) leaves the call complexity unchanged. A drifting boundary, correlated departures from the block law, or extra noise in the known operations changes the model.
