# AI-Powered-Animal-Adoption-and-Rescue-Platform-Using-Machine-Learning


---

# 🐶 Animal Adoption Recommender

This project is an **AI-powered recommendation system** that helps match adopters with the most suitable pets based on their preferences and lifestyle.

## 📌 Features

* Interactive **Streamlit web app**
* Recommends pets based on adopter inputs like:

  * Type (Dog, Cat, etc.)
  * Breed
  * Age
  * Energy level
  * Size
  * Compatibility with kids/other pets
  * Special needs
  * Location
* Uses **Machine Learning (Nearest Neighbors)** to suggest the top matching pets.

## 🧠 Tech & ML Concepts

* **Data Preprocessing**:

  * OneHotEncoder → converts categorical data (like breed, type) into numbers.
  * StandardScaler → normalizes numeric features (like age, weight/size).
* **Model**:

  * K-Nearest Neighbors (KNN) → finds pets most similar to adopter preferences.
* **Interface**:

  * Built using **Streamlit** for easy user interaction.

## ⚙️ Installation & Setup

1. Clone this repository:

   ```bash
   git clone <repo_link>
   cd animal_adoption
   ```

2. Create a virtual environment & activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Preprocess the dataset:

   ```bash
   python preprocess.py
   ```

5. Run the app:

   ```bash
   streamlit run app_streamlit.py
   ```

## 📊 Example Output

* User selects preferences (e.g., Dog, small size, good with kids).
* The recommender suggests **Top 5 pets** with similarity scores.
* A chart shows how closely each pet matches.

## 📂 Project Structure

```
├── app_streamlit.py   # Streamlit UI
├── recommender.py     # Recommendation logic
├── preprocess.py      # Data preprocessing
├── pets.csv           # Sample dataset
├── requirements.txt   # Dependencies
└── README.md          # Project overview
```

## 🚀 Future Improvements

* Add more datasets (real adoption centers).
* Include images of pets.
* Improve model accuracy with advanced ML (e.g., Random Forest, Neural Nets).

---

