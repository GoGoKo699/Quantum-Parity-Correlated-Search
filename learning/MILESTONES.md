# Project understanding map

These 30 milestones connect clean Grover search to the query law for parity-correlated faults. The first 12 develop the oracle, geometry, probability and resource model. The remaining 18 follow the construction and converse through their separate arguments, then bring them together to explain when temporal correlations offer a speedup. The [Childs bridge](CHILDS_BRIDGE.md) gives the single educational anchor and the derivations connecting it to the scientific account.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01-addresses-and-the-null-case)–[M04](#m04-phase-kickback-and-ordinary-phase-access) | Addresses, counting and the available oracle operations |
| Background/preliminaries | [M05](#m05-the-two-dimensional-grover-plane)–[M08](#m08-the-empty-input-as-a-reference) | Clean Grover geometry and the distinguishability benchmark |
| Background/preliminaries | [M09](#m09-unflagged-omissions)–[M12](#m12-the-complete-fault-model) | Hidden fault signs, parity and the complete query model |
| Narrative/innovation | [M13](#m13-only-one-coefficient-is-left)–[M16](#m16-the-negative-parity-schedule) | Which correlation survives and how both signs yield a coherent update |
| Narrative/innovation | [M17](#m17-from-random-angles-to-success)–[M22](#m22-an-unannounced-fixed-block-offset) | Success, verification, physical budgets and boundary alignment |
| Narrative/innovation | [M23](#m23-the-mean-unitary-of-one-block)–[M28](#m28-from-distinguishability-to-total-cost) | Matching progress bounds for arbitrary query algorithms |
| Narrative/innovation | [M29](#m29-the-matched-classical-comparison)–[M30](#m30-the-whole-parity-search-result) | Classical cost and the scope of the result |

## Phase I — Background and preliminaries

### M01 Addresses and the null case

**Central question.** What does an oracle instance specify, and what counts as a correct reply?

**Understanding target.** Describe the $`N`$ possible nonempty instances and the empty instance. Distinguish finding the marked address from deciding whether the instance is empty, and see how a finder for this promise yields a decider.

**Prerequisites.** First milestone.

**Conceptual connection.** A performance guarantee on only the marked inputs cannot establish that the same algorithm rejects the empty input.

**Canonical sources.** [Childs §21.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Model](../science/model.md).

### M02 Physical queries and known controls

**Central question.** Which operations contribute to the query budget?

**Understanding target.** Count every submitted oracle call, including an omitted, padded or verification call. Identify state preparation, diffusion and measurement as known operations outside the oracle count.

**Prerequisites.** [M01](#m01-addresses-and-the-null-case).

**Conceptual connection.** A rotation can be a single effective step while costing a full block of physical calls.

**Canonical sources.** [Childs §§21.1–21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Model](../science/model.md).

### M03 Reversible bit access

**Central question.** How can an oracle answer on a superposition of addresses?

**Understanding target.** Explain why writing the answer by XOR into a response qubit implements an involution and extends linearly. Separate input-dependent action from operations on workspace.

**Prerequisites.** [M01](#m01-addresses-and-the-null-case), [M02](#m02-physical-queries-and-known-controls).

**Conceptual connection.** The lower bound permits an algorithm to use the entire response qubit and arbitrary ancillary registers.

**Canonical sources.** [Childs §21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Model](../science/model.md) · [Converse](../science/converse.md).

### M04 Phase kickback and ordinary phase access

**Central question.** When does a bit query act as a phase query?

**Understanding target.** Use the two eigenstates of a bit flip to distinguish an inert response from a response that flips the relative phase at the mark. Identify which restricted operation the constructive schedule uses.

**Prerequisites.** [M03](#m03-reversible-bit-access).

**Conceptual connection.** An ordinary phase oracle marks an amplitude by its sign. A later interference test can learn that sign by comparing two addresses.

**Canonical sources.** [Childs §21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Childs bridge](CHILDS_BRIDGE.md).

### M05 The two-dimensional Grover plane

**Central question.** Why does an $`N`$-address state admit an angle description?

**Understanding target.** Identify the directions of the marked basis vector and the uniform superposition of unmarked vectors, and read the initial marked amplitude $`1/\sqrt N`$ as the sine of the initial angle.

**Prerequisites.** [M01](#m01-addresses-and-the-null-case), [M04](#m04-phase-kickback-and-ordinary-phase-access).

**Conceptual connection.** Both controls preserve the plane, so coherent search can be studied through one real angle and its measurement probability.

**Canonical sources.** [Childs §19.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Childs bridge](CHILDS_BRIDGE.md) · [Construction](../science/construction.md).

### M06 Reflections and the clean iterate

**Central question.** What happens when the two Grover reflections are composed?

**Understanding target.** Track a sign flip at the mark, then reflection about the uniform state. Derive the clean increase $`2\theta`$ per iterate in the chosen angle convention.

**Prerequisites.** [M05](#m05-the-two-dimensional-grover-plane).

**Conceptual connection.** Clean search requires order $`\sqrt N`$ effective rotations because the initial angle is of order $`1/\sqrt N`$.

**Canonical sources.** [Childs §19.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Childs bridge](CHILDS_BRIDGE.md).

### M07 Angle and measured success

**Central question.** What does the final angle tell an algorithm when it measures the address?

**Understanding target.** Relate angle $`\phi`$ to probability $`\sin^2\phi`$ and distinguish a probable candidate from a certified answer.

**Prerequisites.** [M05](#m05-the-two-dimensional-grover-plane), [M06](#m06-reflections-and-the-clean-iterate).

**Conceptual connection.** The noisy analysis will average probabilities over fault branches. The sine squared of the average angle generally gives a different quantity.

**Canonical sources.** [Childs §19.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Childs bridge](CHILDS_BRIDGE.md) · [Construction](../science/construction.md).

### M08 The empty input as a reference

**Central question.** How can one prove a lower bound without prescribing a search algorithm?

**Understanding target.** Compare the empty-input output with each marked-input output and explain why bounded error requires distinguishability for all marks.

**Prerequisites.** [M01](#m01-addresses-and-the-null-case), [M03](#m03-reversible-bit-access), [M07](#m07-angle-and-measured-success).

**Conceptual connection.** The clean lower bound tracks progress for all possible marks. The noisy converse retains that comparison while changing the progress quantity.

**Canonical sources.** [Childs §§23.1 and 23.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Converse](../science/converse.md).

### M09 Unflagged omissions

**Central question.** What remains available when an attempted phase query silently does nothing?

**Understanding target.** Distinguish the physical call from its random action, and the hidden fault sign from any classical measurement result. Interpret each submission as active or identity on that branch.

**Prerequisites.** [M02](#m02-physical-queries-and-known-controls), [M04](#m04-phase-kickback-and-ordinary-phase-access).

**Conceptual connection.** Averaging a state over unknown fault trajectories represents loss of side information even though each realized branch is coherent.

**Canonical sources.** [Model](../science/model.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M10 Products of fault signs

**Central question.** How can several fair signs share one correlation?

**Understanding target.** Compute a product of signs and distinguish a marginal distribution from the full joint law. Explain how conditioning three fair signs on an even number of omissions preserves every pair marginal.

**Prerequisites.** [M09](#m09-unflagged-omissions).

**Conceptual connection.** Parity describes correlations in the environment independently of the marked-address input.

**Canonical sources.** [Model](../science/model.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M11 Clean classical and quantum benchmarks

**Central question.** Why is a linear scan the relevant fallback?

**Understanding target.** Compare ideal $`\Theta(N)`$ classical access with the clean Grover $`\Theta(\sqrt N)`$ bound. Explain the classical adversary that can hide a unique mark outside the inspected set.

**Prerequisites.** [M01](#m01-addresses-and-the-null-case), [M02](#m02-physical-queries-and-known-controls), [M06](#m06-reflections-and-the-clean-iterate), [M08](#m08-the-empty-input-as-a-reference).

**Conceptual connection.** The meaningful comparison for the result will reuse the same faulty physical interface and charge each attempt.

**Canonical sources.** [Childs §§19.1 and 23.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Model](../science/model.md).

### M12 The complete fault model

**Central question.** Which conditions define the task whose query law is proved?

**Understanding target.** Combine the zero-or-one promise, fixed worst-case query budget, independently sampled length-$`L`$ fault blocks, fair proper marginals, and lack of flags. Identify $`N`$, $`L`$ and signed parity bias $`\kappa`$ as distinct parameters.

**Prerequisites.** [M02](#m02-physical-queries-and-known-controls), [M08](#m08-the-empty-input-as-a-reference), [M09](#m09-unflagged-omissions), [M10](#m10-products-of-fault-signs), [M11](#m11-clean-classical-and-quantum-benchmarks).

**Conceptual connection.** Coherent information can depend on all $`L`$ slots of a block even when any strictly smaller selected set is distributed as fair independent omissions.

**Canonical sources.** [Model](../science/model.md) · [Scientific route](../science/README.md).

## Phase II — Narrative and innovation

### M13 Only one coefficient is left

**Central question.** Which joint laws can have every proper marginal fair and independent?

**Understanding target.** Expand the sign distribution in products of signs. Use its marginals to eliminate every nonconstant product coefficient except the product of all $`L`$ signs, and use positivity to bound its coefficient.

**Prerequisites.** [M10](#m10-products-of-fault-signs), [M12](#m12-the-complete-fault-model).

**Conceptual connection.** An independent draw of the preferred or wrong parity followed by a uniform draw within that parity class realizes every admissible law.

**Canonical sources.** [Model](../science/model.md).

### M14 What a partial block exposes

**Central question.** Which observations can distinguish the parity model from independent omissions?

**Understanding target.** Explain why retaining only fixed proper subsets of slots yields fair independent signs, and why this also describes a truncated final block of a fixed-budget experiment.

**Prerequisites.** [M09](#m09-unflagged-omissions), [M12](#m12-the-complete-fault-model), [M13](#m13-only-one-coefficient-is-left).

**Conceptual connection.** Whole-block control is what can exploit the surviving coefficient. The final tail contributes only independent-omission progress in the converse.

**Canonical sources.** [Model](../science/model.md) · [Converse](../science/converse.md).

### M15 Affine updates through a block

**Central question.** Where does the full parity enter the Grover dynamics?

**Understanding target.** Compose the updates $`\phi\mapsto 2\theta+s_j\phi`$ and identify full parity in the coefficient of the incoming angle. Identify the remaining random contributions as suffix products.

**Prerequisites.** [M06](#m06-reflections-and-the-clean-iterate), [M09](#m09-unflagged-omissions), [M13](#m13-only-one-coefficient-is-left).

**Conceptual connection.** For positive preferred parity, every preferred block preserves the entering orientation while adding a deterministic drift and random increments.

**Canonical sources.** [Childs bridge](CHILDS_BRIDGE.md) · [Construction](../science/construction.md).

### M16 The negative-parity schedule

**Central question.** How can a block with preferred negative parity preserve orientation?

**Understanding target.** Omit one known diffusion, track the replacement $`\phi\mapsto-s_j\phi`$, and identify how this changes the product of angle coefficients and removes one additive term.

**Prerequisites.** [M02](#m02-physical-queries-and-known-controls), [M15](#m15-affine-updates-through-a-block).

**Conceptual connection.** The sign of $`\kappa`$ changes the placement of known controls. Each block still consumes $`L`$ oracle submissions.

**Canonical sources.** [Construction](../science/construction.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M17 From random angles to success

**Central question.** How does a distribution of suffix signs change the mean marked probability?

**Understanding target.** Use the identity $`\sin^2\phi=(1-\cos 2\phi)/2`$. Recognize the independent fair suffix products under preferred parity and relate each to attenuation of the second harmonic.

**Prerequisites.** [M07](#m07-angle-and-measured-success), [M13](#m13-only-one-coefficient-is-left), [M15](#m15-affine-updates-through-a-block), [M16](#m16-the-negative-parity-schedule).

**Conceptual connection.** The calculation preserves the cumulative drift and averages the oscillatory term. It avoids replacing random angles by their mean.

**Canonical sources.** [Construction](../science/construction.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M18 The usable run length

**Central question.** How many full blocks should a coherent trial use?

**Understanding target.** Compare the clean rotation scale $`\sqrt N`$ with the scale $`1/\eta`$ of a wrong-parity event, for $`\eta=1-|\kappa|`$. Interpret the limiting case $`\eta=0`$ and the floor at one block.

**Prerequisites.** [M13](#m13-only-one-coefficient-is-left), [M17](#m17-from-random-angles-to-success).

**Conceptual connection.** A run of the chosen length has a constant probability of preferred parity throughout and a marked-candidate probability of order $`t^2/N`$ after averaging.

**Canonical sources.** [Construction](../science/construction.md).

### M19 Two-reference candidate verification

**Central question.** How can phase queries certify one address with no false positives?

**Understanding target.** Explain how two distinct reference addresses expose a minus phase relative to the candidate. Show why a wrong or empty candidate cannot pass both tests, and why a true candidate passes with constant probability.

**Prerequisites.** [M04](#m04-phase-kickback-and-ordinary-phase-access), [M07](#m07-angle-and-measured-success), [M14](#m14-what-a-partial-block-exposes), [M18](#m18-the-usable-run-length).

**Conceptual connection.** Verification makes independent short runs useful. A clean mark oracle or a fault flag is unnecessary.

**Canonical sources.** [Construction](../science/construction.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M20 A charged direct scan

**Central question.** How do both access models obtain a linear fallback?

**Understanding target.** Trace a repeated bit-query scan and its phase-query analogue. Check why the calls relevant to the true address form proper subsets within each fault block and how the null answer is certified.

**Prerequisites.** [M11](#m11-clean-classical-and-quantum-benchmarks), [M14](#m14-what-a-partial-block-exposes), [M19](#m19-two-reference-candidate-verification).

**Conceptual connection.** The capped query law reflects a real algorithm with the same cost accounting, including phase verification.

**Canonical sources.** [Construction](../science/construction.md) · [Model](../science/model.md).

### M21 From trials to a query budget

**Central question.** How does moderate trial success yield the claimed upper bound?

**Understanding target.** Convert $`\Omega(t^2/N)`$ candidate probability and constant verification probability into a fixed number of independent trials. Charge $`O(Lt)`$ calls per trial and take the better route between trials and scanning.

**Prerequisites.** [M02](#m02-physical-queries-and-known-controls), [M18](#m18-the-usable-run-length), [M19](#m19-two-reference-candidate-verification), [M20](#m20-a-charged-direct-scan).

**Conceptual connection.** The $`L`$ multiplier, the small-parity-error regime and the linear cap follow from one calculation.

**Canonical sources.** [Construction](../science/construction.md) · [Model](../science/model.md).

### M22 An unannounced fixed block offset

**Central question.** What changes when the first true block boundary is unknown?

**Understanding target.** Separate complete blocks, initial and final proper fragments, and fully charged gaps between trials. Explain how a random choice of periodic control schedule addresses fixed phase ambiguity and why charged gaps separate the relevant fault blocks.

**Prerequisites.** [M14](#m14-what-a-partial-block-exposes), [M16](#m16-the-negative-parity-schedule), [M19](#m19-two-reference-candidate-verification), [M21](#m21-from-trials-to-a-query-budget).

**Conceptual connection.** A fixed hidden offset attains the same query order. Controlling endpoint contributions is what permits a guarantee uniform over offsets.

**Canonical sources.** [Hidden boundaries](../science/hidden-boundaries.md) · [Construction](../science/construction.md).

### M23 The mean unitary of one block

**Central question.** Which two operator products survive averaging a full fault block?

**Understanding target.** Use a fixed control frame and write the fair slot mean as a projection $`P_j`$ and the sign-weighted slot mean as $`-Q_j`$. Read their two ordered products directly from the fault law.

**Prerequisites.** [M03](#m03-reversible-bit-access), [M08](#m08-the-empty-input-as-a-reference), [M13](#m13-only-one-coefficient-is-left).

**Conceptual connection.** The ordinary independent-omission part and the parity correction remain separate for arbitrary interleaved controls, without a Grover-plane ansatz.

**Canonical sources.** [Converse](../science/converse.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M24 A retained substate and its norm

**Central question.** How can a mean amplitude be used inside a mixed noisy state?

**Understanding target.** Explain the completely positive remainder after subtracting the mean-amplitude term, and use the orthogonal final ranges of the two products to read off a norm-loss estimate.

**Prerequisites.** [M09](#m09-unflagged-omissions), [M23](#m23-the-mean-unitary-of-one-block).

**Conceptual connection.** The estimate tracks amplitude removed by projections and the first-slot amplitude partly returned by the parity term.

**Canonical sources.** [Converse](../science/converse.md) · [Childs bridge](CHILDS_BRIDGE.md).

### M25 Progress summed over marks

**Central question.** Why does the proof track all possible marked inputs together?

**Understanding target.** Define a squared distance from the empty reference to the retained substate for each mark. Explain how orthogonality across candidate marks at one slot bounds the sum of squared projections.

**Prerequisites.** [M08](#m08-the-empty-input-as-a-reference), [M23](#m23-the-mean-unitary-of-one-block), [M24](#m24-a-retained-substate-and-its-norm).

**Conceptual connection.** A fixed slot has a bounded amount of reference amplitude to allocate across addresses, even when its control used an adaptive record.

**Canonical sources.** [Childs §§23.1 and 23.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) · [Converse](../science/converse.md).

### M26 Two estimates for the parity term

**Central question.** Why are two progress estimates needed in the same converse?

**Understanding target.** Distinguish the $`\sqrt N`$ bound from summing overlaps over marks and the $`1/\eta`$ bound from completing a square against first-slot norm loss. Identify which one is useful near perfect parity.

**Prerequisites.** [M24](#m24-a-retained-substate-and-its-norm), [M25](#m25-progress-summed-over-marks).

**Conceptual connection.** The ordinary slot contributions cost order $`L`$ per block. The cheaper parity estimate gives the extra scale without breaking the proof at $`|\kappa|=1`$.

**Canonical sources.** [Converse](../science/converse.md).

### M27 Adaptive controls and unfinished blocks

**Central question.** How does the block analysis cover algorithms that measure midway or stop partway through a block?

**Understanding target.** Explain purification of controls, the use of a fixed budget, and inert padding in the stronger bit-query model. Relate a terminal proper fragment to the independent-omission progress bound.

**Prerequisites.** [M03](#m03-reversible-bit-access), [M14](#m14-what-a-partial-block-exposes), [M23](#m23-the-mean-unitary-of-one-block), [M26](#m26-two-estimates-for-the-parity-term).

**Conceptual connection.** These reductions keep the converse applicable to arbitrary adaptive strategies while the construction retains ordinary phase access.

**Canonical sources.** [Converse](../science/converse.md).

### M28 From distinguishability to total cost

**Central question.** How do the block progress estimates force the same query scale as the construction?

**Understanding target.** Use the bounded-error separation of final outputs to obtain positive progress per mark, sum over marks, and compare the required order $`N`$ with the progress of complete blocks and the partial tail.

**Prerequisites.** [M08](#m08-the-empty-input-as-a-reference), [M21](#m21-from-trials-to-a-query-budget), [M25](#m25-progress-summed-over-marks), [M26](#m26-two-estimates-for-the-parity-term), [M27](#m27-adaptive-controls-and-unfinished-blocks).

**Conceptual connection.** The lower-bound denominator $`L+\min\{\sqrt N,1/\eta\}`$ yields the same clipped query law as the two constructive routes.

**Canonical sources.** [Converse](../science/converse.md) · [Model](../science/model.md).

### M29 The matched classical comparison

**Central question.** What does the classical baseline control for?

**Understanding target.** Simulate the faulty bit-query record with a clean classical oracle and sampled signs. Explain why the simulated algorithm cannot beat the clean linear lower bound, and use the charged scan for the matching upper bound.

**Prerequisites.** [M11](#m11-clean-classical-and-quantum-benchmarks), [M20](#m20-a-charged-direct-scan), [M21](#m21-from-trials-to-a-query-budget), [M28](#m28-from-distinguishability-to-total-cost).

**Conceptual connection.** Both competitors face the same fault law and physical call count. The constructive difference is coherent use of all the slots in a block.

**Canonical sources.** [Construction](../science/construction.md) · [Model](../science/model.md) · [Converse](../science/converse.md).

### M30 The whole parity-search result

**Central question.** When does an invisible full-block correlation change query complexity?

**Understanding target.** State the fault model, preferred-parity construction and matching converse in one account. Explain the dependence on block length, wrong parity and alignment, and separate finite checks on the mechanism from the asymptotic theorem. See [finite verification](../verification/README.md).

**Prerequisites.** [M12](#m12-the-complete-fault-model), [M21](#m21-from-trials-to-a-query-budget), [M22](#m22-an-unannounced-fixed-block-offset), [M28](#m28-from-distinguishability-to-total-cost), [M29](#m29-the-matched-classical-comparison).

**Conceptual connection.** An algorithm can benefit from a temporal correlation that no proper marginal sees. The speedup depends jointly on parity quality and the charged cost of accessing it.

**Canonical sources.** [Scientific route](../science/README.md) · [Model](../science/model.md) · [Construction](../science/construction.md) · [Converse](../science/converse.md) · [Hidden boundaries](../science/hidden-boundaries.md).

[Childs bridge](CHILDS_BRIDGE.md) · [Scientific route](../science/README.md)
