import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Dataset Creation
def load_data():
    movies = pd.DataFrame([
        [1, 'Inception', 'Sci-Fi Thriller', 'dream subconscious mind heist action'],
        [2, 'Interstellar', 'Sci-Fi Adventure', 'space science wormhole family survival'],
        [3, 'The Dark Knight', 'Action Crime', 'superhero crime joker gotham action'],
        [4, 'Avengers: Endgame', 'Action Sci-Fi', 'superhero marvel time travel action'],
        [5, 'The Matrix', 'Sci-Fi Action', 'virtual reality chosen one cyber action'],
        [6, 'Titanic', 'Romance Drama', 'ship love tragedy historical romance'],
        [7, 'La La Land', 'Romance Musical', 'music dreams love hollywood romance'],
        [8, 'Coco', 'Animation Family', 'music family afterlife culture animation'],
        [9, 'Toy Story', 'Animation Comedy', 'toys friendship adventure animation family'],
        [10, 'The Godfather', 'Crime Drama', 'mafia family crime power drama']
    ], columns=['movie_id', 'title', 'genre', 'tags'])

    ratings = pd.DataFrame([
        [1, 1, 5], [1, 2, 5], [1, 3, 4], [1, 5, 5], [1, 10, 3],
        [2, 1, 4], [2, 2, 5], [2, 4, 5], [2, 5, 4], [2, 8, 3],
        [3, 6, 5], [3, 7, 5], [3, 8, 4], [3, 9, 4], [3, 2, 3],
        [4, 3, 5], [4, 4, 5], [4, 5, 4], [4, 10, 4], [4, 1, 4],
        [5, 6, 4], [5, 7, 4], [5, 9, 5], [5, 8, 5], [5, 10, 2]
    ], columns=['user_id', 'movie_id', 'rating'])

    return movies, ratings


# 2. Content-Based Filtering
def build_content_similarity(movies):
    movie_profiles = movies['genre'] + ' ' + movies['tags']

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movie_profiles)

    similarity = cosine_similarity(tfidf_matrix)

    return pd.DataFrame(
        similarity,
        index=movies['movie_id'],
        columns=movies['movie_id']
    )


# 3. Collaborative Filtering
def build_collaborative_similarity(ratings):
    user_movie_matrix = ratings.pivot_table(
        index='user_id',
        columns='movie_id',
        values='rating'
    ).fillna(0)

    similarity = cosine_similarity(user_movie_matrix.T)

    return pd.DataFrame(
        similarity,
        index=user_movie_matrix.columns,
        columns=user_movie_matrix.columns
    )


# 4. Hybrid Recommendation
def hybrid_recommend(user_id, movies, ratings,
                     content_similarity_df,
                     item_similarity_df,
                     top_n=5,
                     content_weight=0.45,
                     collaborative_weight=0.55):

    user_ratings = ratings[ratings['user_id'] == user_id]
    watched_movies = user_ratings['movie_id'].tolist()

    candidate_movies = movies[
        ~movies['movie_id'].isin(watched_movies)
    ]['movie_id'].tolist()

    results = []

    for movie_id in candidate_movies:

        # Content Score
        content_score = content_similarity_df.loc[movie_id, watched_movies].mean()

        # Collaborative Score
        weighted_sum = 0
        similarity_sum = 0

        for _, row in user_ratings.iterrows():
            similarity = item_similarity_df.loc[movie_id, row['movie_id']]
            weighted_sum += similarity * row['rating']
            similarity_sum += abs(similarity)

        collaborative_score = (
            weighted_sum / similarity_sum if similarity_sum != 0 else 0
        )

        # Hybrid Score
        hybrid_score = (
            content_weight * content_score +
            collaborative_weight * (collaborative_score / 5)
        )

        results.append([
            movie_id,
            content_score,
            collaborative_score,
            hybrid_score
        ])

    recommendation_df = pd.DataFrame(
        results,
        columns=['movie_id', 'content_score', 'collaborative_score', 'hybrid_score']
    )

    recommendation_df = recommendation_df.merge(
        movies[['movie_id', 'title', 'genre']],
        on='movie_id'
    )

    recommendation_df = recommendation_df.sort_values(
        by='hybrid_score',
        ascending=False
    ).reset_index(drop=True)

    recommendation_df.insert(0, 'rank', np.arange(1, len(recommendation_df) + 1))

    return recommendation_df.head(top_n)


# 5. Visualization
def plot_results(recommendations, save_path="recommendations.png"):
    plt.figure(figsize=(10, 5.6), dpi=160)

    colors = ['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']

    plt.barh(
        recommendations['title'],
        recommendations['hybrid_score'],
        color=colors[:len(recommendations)]
    )

    plt.gca().invert_yaxis()
    plt.title('Hybrid Recommendation System Output', fontsize=16, fontweight='bold')
    plt.xlabel('Hybrid Score')
    plt.grid(axis='x', linestyle='--', alpha=0.35)

    plt.tight_layout()

    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()

    print(f"Plot saved as: {save_path}")
# 6. Main Execution
def main():
    movies, ratings = load_data()

    print("Movies:", movies.shape)
    print("Ratings:", ratings.shape)

    content_sim = build_content_similarity(movies)
    item_sim = build_collaborative_similarity(ratings)

    recommendations = hybrid_recommend(
        user_id=1,
        movies=movies,
        ratings=ratings,
        content_similarity_df=content_sim,
        item_similarity_df=item_sim
    )

    print("\nTop Recommendations:")
    print(recommendations)

    plot_results(recommendations)


if __name__ == "__main__":
    main()