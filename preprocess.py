import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

BASE_DIR = os.path.dirname(__file__)

def main():
    # Load dataset
    df = pd.read_csv(os.path.join(BASE_DIR, "pets.csv"))

    # Identify categorical and numerical columns
    categorical_cols = ["type", "breed"]
    numerical_cols = ["age", "energy_level"]

    # Save column names
    joblib.dump(categorical_cols + numerical_cols, os.path.join(BASE_DIR, "input_cols.joblib"))

    # Build preprocessing pipeline
    transformer = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numerical_cols)
        ]
    )

    pipeline = Pipeline(steps=[("preprocessor", transformer)])
    pipeline.fit(df[categorical_cols + numerical_cols])

    # Save artifacts
    joblib.dump(pipeline, os.path.join(BASE_DIR, "transformer.joblib"))
    df.to_csv(os.path.join(BASE_DIR, "pets_clean.csv"), index=False)

if __name__ == "__main__":
    main()
