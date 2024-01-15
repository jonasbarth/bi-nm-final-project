# Purpose
The purpose of this package is to provide code for running a cross validation of gene disease identification algorithms.

## Usage
```python
from metrics import cross_validate
from diamond import diamond

cross_validate(algorithm=diamond, network=network, seed_genes=seed_genes, num_genes_to_evaluate=100, num_folds=5)
```