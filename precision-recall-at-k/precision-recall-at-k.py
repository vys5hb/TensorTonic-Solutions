def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    cnt = 0
    for i in recommended[:k]:
        if i in relevant:
            cnt += 1
    recall =  cnt / len(relevant)
    cnt = 0
    for i in recommended[:k]:
        if i in relevant:
            cnt += 1
    precision = cnt / k
    return [precision, recall]