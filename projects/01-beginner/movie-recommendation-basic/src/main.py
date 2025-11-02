import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def build_user_item_matrix(ratings_df):
    return ratings_df.pivot_table(index="user_id", columns="item_id", values="rating").fillna(0.0)


def recommend_for_user(user_id, uim, top_k=5):
    sims = cosine_similarity(uim)
    user_idx = uim.index.get_loc(user_id)
    scores = sims[user_idx]
    similar_users = np.argsort(scores)[::-1]

    # Simple score: weighted sum of neighbor ratings
    weighted = scores @ uim.values
    # Exclude already rated
    already = uim.loc[user_id] > 0
    weighted = np.where(already.values, -np.inf, weighted)

    top_items = np.argsort(weighted)[::-1][:top_k]
    return list(uim.columns[top_items])


def main():
    # Toy ratings
    ratings = pd.DataFrame({
        "user_id": [1,1,2,2,3,3,4,4,5,5],
        "item_id": [10,11,10,12,11,13,12,13,10,13],
        "rating":  [5, 4, 4, 5, 5, 3, 4, 4, 3, 5],
    })
    uim = build_user_item_matrix(ratings)
    recs = recommend_for_user(1, uim)
    print("Recommendations for user 1:", recs)


if __name__ == "__main__":
    main()
