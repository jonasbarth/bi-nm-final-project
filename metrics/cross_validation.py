from typing import Union, Iterable

import pandas as pd
from sklearn.model_selection import KFold


def cross_validate(algorithm, network: Union[str, pd.DataFrame], seed_genes: Union[str, pd.DataFrame],
                   num_genes_to_evaluate: Iterable[int], num_folds: int, **kwargs):
    """Cross validates a network algorithm of choice on the specified network and seed genes.

    Args:
        algorithm: the function of the algorithm, should have the signature f(network, seed_genes, num_genes_to_add, **kwargs)
        network: the network on which to run the algorithm.
        seed_genes: the seed genes on which to run the algorithm.
        num_genes_to_evaluate: the number of genes to evaluate the metrics for.
        num_folds: the number of folds in the K-Fold cross validation.
    Returns:

    """
    network = pd.read_csv(network, header=None, dtype=str)
    seed_genes = pd.read_csv(seed_genes, header=None, dtype=str)
    num_genes_to_predict = len(seed_genes)
    metrics = []

    k_fold = KFold(n_splits=num_folds, shuffle=True, random_state=42)

    for train_index, _ in k_fold.split(seed_genes):
        # We divide the set in train and test subsets
        train_seed_genes = seed_genes.iloc[train_index]

        result = algorithm(network, train_seed_genes, num_genes_to_predict, **kwargs)

        for num_genes in num_genes_to_evaluate:
            top_n = set(result.head(num_genes).gene)
            scores = calculate_metrics(top_n, set(seed_genes.iloc[:, 0]))
            metrics.append([num_genes, *scores])

    metrics = pd.DataFrame(metrics, columns=['num_genes', 'precision', 'recall', 'f1'])
    return metrics


def calculate_metrics(top_n_predicted_genes: set, seed_genes: set):
    """Calculate the Precision, Recall, and F1 scores for the predicted genes of an algorithm.

    Args:
        top_n_predicted_genes (set): the set of predicted genes.
        seed_genes (set): the set of seed genes.

    Returns:
        (float, float, float): The Precision, Recall, and F1 scores.
    """
    true_positives = len(top_n_predicted_genes.intersection(seed_genes))
    false_positives = len(top_n_predicted_genes.difference(seed_genes))
    false_negatives = len(seed_genes.difference(top_n_predicted_genes))

    if true_positives + false_positives > 0:
        precision = true_positives / (true_positives + false_positives)
    else:
        precision = 0.0

    if true_positives + false_negatives > 0:
        recall = true_positives / (true_positives + false_negatives)
    else:
        recall = 0.0

    if precision + recall > 0:
        f1 = 2 * precision * recall / (precision + recall)
    else:
        f1 = 0.0

    return precision, recall, f1
