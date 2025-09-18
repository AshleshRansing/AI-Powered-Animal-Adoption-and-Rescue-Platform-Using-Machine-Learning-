import os
import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors

BASE_DIR = os.path.dirname(__file__)

_transformer = None
_orig_df = None
_input_cols = None
_model = None

def load_artifacts(base_path=BASE_DIR):
    global _transformer, _orig_df, _input_cols, _model

    _transformer = joblib.load(os.path.join(base_path, "transformer.joblib"))
    _input_cols = joblib.load(os.path.join(base_path, "input_cols.joblib"))
    _orig_df = pd.read_csv(os.path.join(base_path, "pets_clean.csv"))

    # Fit Nearest Neighbors model
    X = _transformer.transform(_orig_df[_input_cols])
    _model = NearestNeighbors(n_neighbors=5, metric="cosine")
    _model.fit(X)

def recommend(profile: dict, top_n=5):
    global _transformer, _orig_df, _input_cols, _model

    if _transformer is None or _orig_df is None or _model is None:
        raise RuntimeError("Artifacts not loaded. Call load_artifacts() first.")

    # Create a dataframe from user profile
    profile_df = pd.DataFrame([profile], columns=_input_cols)

    # Transform input
    profile_vec = _transformer.transform(profile_df)

    # Find nearest neighbors
    distances, indices = _model.kneighbors(profile_vec, n_neighbors=top_n)

    # Get recommended pets
    results = _orig_df.iloc[indices[0]].copy()
    results["similarity"] = 1 - distances[0]
    return results
