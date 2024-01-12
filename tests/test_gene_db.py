from genes import GeneDB


def test_that_gene_db():
    gene_db = GeneDB("../data/biogrid.txt")

    assert gene_db.to_official_symbol_interactor("6416") == "MAP2K4"
