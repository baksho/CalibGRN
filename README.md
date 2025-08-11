# CalibGRN

**CalibGRN** is a research framework for **Gene Regulatory Network (GRN) inference** using **Calibrated Transformer models**.  
It supports both supervised and unsupervised workflows, integrates baseline methods, and adds novel calibration and attention regularization techniques for more reliable biological network predictions.



## Features
- Synthetic & real GRN datasets (DREAM4, DREAM5, etc.)
- Baseline methods: ARACNE, Pearson, TIGRESS, GENIE3, GRNBoost2
- Transformer-based GRN inference
- Calibration methods:
  - Temperature Scaling
  - Edge-level Dirichlet Calibration
- Attention regularization with biological priors
- Unified evaluation: AUROC, AUPR, ECE, reliability diagrams
- Open-source Python package for reproducibility



## Installation
```bash
git clone https://github.com/yourusername/calibgrn.git
cd calibgrn
pip install -e .
```

## Project Structure
```
calibgrn/         # Main package source
notebooks/        # Experiment notebooks
tests/            # Unit tests
setup_env.py      # Environment setup helper
requirements.txt  # Dependencies
setup.py          # Install script
```

**Goal**

Develop a unified and reproducible framework for GRN inference that combines:
- Baseline algorithms for benchmarking
- Transformer architectures for improved sequence/context modeling
- Novel calibration techniques for trustworthy probability outputs
- Biological prior regularization for interpretability

**Milestones**
- [x] Milestone 1: Baseline implementations (ARACNE, Pearson, TIGRESS, GENIE3, GRNBoost2)
- [ ] Milestone 2: Prototype Transformer model for GRN inference
- [ ] Milestone 3: Calibration methods (Temperature Scaling, Edge-level Dirichlet Calibration)
- [ ] Milestone 4: Attention regularization with biological priors
- [ ] Milestone 5: Ablation studies on synthetic data
- [ ] Milestone 6: Transfer to real-world datasets (DREAM4, DREAM5)
- [ ] Milestone 7: Final evaluation and comparison against baselines

**Novel Contributions**
1. **Calibration-aware training loss**: Combines BCE with a differentiable calibration penalty (e.g., soft ECE surrogate) to improve both accuracy and calibration.
2. **Attention regularization with biological priors**: Loss term nudging attention weights toward known TF→target likelihoods (e.g., motif presence).
3. **Edge-level Dirichlet calibration**: Models dependencies among outgoing edges from the same regulator, beyond independent scaling.

## LICENSE
This project is licensed under the MIT License.
