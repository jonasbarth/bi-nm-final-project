"""Module for mapping genes."""
from typing import Union, Iterable, List

import numpy as np
import pandas as pd


class GeneDB:
    """Class interacting with genes."""

    def __init__(self, genes: Union[str, pd.DataFrame]):
        if isinstance(genes, str):
            self.genes = pd.read_csv(genes, sep="\t", low_memory=False)
        elif isinstance(genes, pd.DataFrame):
            self.genes = genes
        else:
            raise TypeError(f"Genes must either be a string or pandas DataFrame, found: {type(genes)}")

        interactor_a = self.genes[["Entrez Gene Interactor A", "Official Symbol Interactor A"]].drop_duplicates()
        interactor_b = self.genes[["Entrez Gene Interactor B", "Official Symbol Interactor B"]].drop_duplicates()

        entrez_genes = np.hstack((interactor_a["Entrez Gene Interactor A"],
                                       interactor_b["Entrez Gene Interactor B"]))

        official_symbols = np.hstack((interactor_a["Official Symbol Interactor A"],
                                      interactor_b["Official Symbol Interactor B"]))

        self.entrez_genes = {str(entrez_id): str(official_symbol) for entrez_id, official_symbol in zip(entrez_genes, official_symbols)}

    def to_official_symbol_interactor(self, entrez_id: Union[str, Iterable[str]]) -> List[str]:
        """Converts Entrez IDs to official symbol interactors.

        Args:
            entrez_id (Union[str, Iterable[str]]): Entrez IDs as strings to convert.

        Returns:
            List[str]: List of official symbol interactors that match the Entrez IDs. Order is preserved.
        """
        if isinstance(entrez_id, str):
            return self.entrez_genes[entrez_id]
        elif isinstance(entrez_id, Iterable):
            return [self.entrez_genes[id] for id in entrez_id]
        else:
            raise TypeError(f"Entrez gene ID should be a string or sequence, found: {type(entrez_id)}.")
