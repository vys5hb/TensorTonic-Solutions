def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    res = []
    for i in items:
        R = i[0]
        v = i[1]
        WR = (v/(v+min_votes)) * R + ((min_votes / (v+min_votes)) * global_mean)
        res.append(WR)
    return res
        
            
        
    # Write code here