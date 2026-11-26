# Verification

Run from the repository root with Python 3.12.

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The checks use exact rational probabilities for the proper marginals. They enumerate fair signs on the Grover plane to compare direct matrix updates with the signed rotation formulas. That comparison includes fixed offsets, both signs of the full parity coefficient and both candidate diffusion residues. The verifier tests the two-reference certificate against all possible marks and the no-mark case, and it checks that the charging schedule places the probes, verification calls and next trial in distinct hidden blocks.

Seeded complex matrices exercise the mean-unitary expansion, the positive residual after extracting its pure component, contraction and the progress bound. The incomplete-block check sums out unused signs before comparing the same mean unitary with the independent-omission product. The tests cover finite cases. The [scientific account](../science/README.md) gives the proofs of the uniform bounds.
