from metrics import cross_validate
from diamond import diamond

def test_cross_validation():
    num_genes_to_evaluate = [1, 2, 3]
    num_folds = 2
    result = cross_validate(diamond, "../ppi_lcc.txt", "../seed_genes.txt", num_genes_to_evaluate, num_folds)

    assert len(result) == len(num_genes_to_evaluate) * num_folds
