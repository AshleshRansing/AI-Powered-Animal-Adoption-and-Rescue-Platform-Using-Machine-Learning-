import streamlit as st
import pandas as pd
from recommender import recommend, load_artifacts

# Load original dataset
_orig_df = pd.read_csv("pets.csv")

# Load recommender artifacts
load_artifacts(".")

st.title("🐶 Animal Adoption Recommender")

# Collect user preferences
pet_type = st.selectbox("Pet Type", options=_orig_df["type"].unique())
breed = st.selectbox("Breed", options=_orig_df["breed"].unique())
age = st.slider("Age", int(_orig_df["age"].min()), int(_orig_df["age"].max()), int(_orig_df["age"].median()))
energy_level = st.selectbox("Energy Level", options=_orig_df["energy_level"].unique())
size = st.selectbox("Size", options=_orig_df["size"].unique())
good_with_kids = st.selectbox("Good with Kids?", options=_orig_df["good_with_kids"].unique())
health_condition = st.selectbox("Health Condition", options=_orig_df["health_condition"].unique())
other_pets = st.selectbox("Other Pets Compatibility", options=_orig_df["other_pets_compatibility"].unique())
environment = st.selectbox("Environment Suitability", options=_orig_df["environment_suitability"].unique())
special_needs = st.selectbox("Special Needs", options=_orig_df["special_needs"].unique())
location = st.selectbox("Preferred Location", options=_orig_df["location"].unique())

# Build user profile dictionary
profile = {
    "type": pet_type,
    "breed": breed,
    "age": age,
    "energy_level": energy_level,
    "size": size,
    "good_with_kids": good_with_kids,
    "health_condition": health_condition,
    "other_pets_compatibility": other_pets,
    "environment_suitability": environment,
    "special_needs": special_needs,
    "location": location
}

# Show recommendations
if st.button("🔍 Find Matching Pets"):
    results = recommend(profile, top_n=5)
    st.subheader("✨ Recommended Pets for You")
    st.dataframe(results)
