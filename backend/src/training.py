import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

DATASET_DF = pd.read_csv("datasets/spotify_data.csv").dropna(subset=["artist_name", "track_name"])
DATASET_DF["artist+song"] = DATASET_DF["artist_name"] + " - " + DATASET_DF["track_name"]

def preprocess_dataset(df: pd.DataFrame, numerical_features: list[str], categorical_features: list[str]):
    encoder = OneHotEncoder()
    encoded_cat_features = encoder.fit_transform(df[categorical_features])

    scaler = StandardScaler()
    scaled_num_features = scaler.fit_transform(df[numerical_features])

    features = np.hstack((encoded_cat_features.toarray(), scaled_num_features))

    sparse_matrix = csr_matrix(features)

    return sparse_matrix


def find_song(df: pd.DataFrame, name: str, artist: str) -> int:
    if name == "" and artist == "":
        return -1
    track_index = df.query("(track_name == @name) & (artist_name == @artist)")
    if not track_index.empty:
        return track_index.index[0]
    return -1


def get_similar_songs(track_name: str, artist_name: str, amount: int) -> pd.DataFrame | None:
    print(os.getcwd())
    print(f"Finding {amount} similar songs to '{track_name}' by '{artist_name}'")
    print("=> Loading dataset")
    df = DATASET_DF

    print("=> Searching for song in the dataset")
    chosen_track_index = find_song(df, track_name, artist_name)

    if chosen_track_index == -1:
        return None

    print("=> Preprocessing dataset")
    categorical_features = ["genre"]
    numerical_features = ["danceability", "energy", "speechiness",
                          "acousticness", "instrumentalness", "liveness",
                          "valence", "tempo"]
    processed_matrix = preprocess_dataset(df, numerical_features, categorical_features)

    print("=> Computing song similarities")
    cosine_sim = cosine_similarity(processed_matrix, processed_matrix[chosen_track_index])

    print("=> Generating result dataframe")
    similarity_scores_df = pd.DataFrame(cosine_sim, columns=["similarity_score"])
    similarity_scores_df = (
        similarity_scores_df.sort_values(by="similarity_score", ascending=False)
        .iloc[0:min(amount, len(similarity_scores_df))]
        .join(df, how="inner")
    )
    similarity_scores_df = similarity_scores_df[
        ["artist_name", "track_name", "track_id", "year", "genre", "duration_ms", "similarity_score"]
    ]

    return similarity_scores_df
