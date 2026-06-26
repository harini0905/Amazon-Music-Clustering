# 🎵 Amazon Music Song Clustering using Unsupervised Machine Learning

## 📌 Project Overview

This project applies **Unsupervised Machine Learning** techniques to cluster Amazon Music songs based on their audio characteristics. The objective is to automatically group similar songs based on their audio features, making it easier to build music recommendation systems, generate playlists, and improve music discovery.

The project includes:

- Data Exploration and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Scaling using StandardScaler
- K-Means Clustering
- Elbow Method for Optimal Cluster Selection
- Silhouette Score Evaluation
- PCA Visualization
- Cluster Interpretation
- Streamlit Dashboard
- Model Serialization using Pickle

---

## 🎯 Problem Statement

Music streaming platforms contain thousands of songs with varying audio characteristics. Manually organizing songs based on their musical properties is inefficient and time-consuming.

The objective of this project is to automatically group songs with similar audio characteristics using clustering techniques, enabling playlist generation, personalized recommendations, and music discovery.

---

## 📂 Dataset Information

**Dataset:** `single_genre_artists.csv`

### Features Used for Clustering

| Feature | Description |
|---------|-------------|
| danceability | Suitability of a track for dancing |
| energy | Intensity and activity level |
| loudness | Overall loudness of the song |
| speechiness | Presence of spoken words |
| acousticness | Acoustic nature of the track |
| instrumentalness | Probability of containing no vocals |
| liveness | Presence of audience/live recording |
| valence | Musical positivity |
| tempo | Beats per minute |
| duration_ms | Song duration in milliseconds |

### Reference Columns

- name_song
- name_artists
- genres

These columns are used only for displaying song information and interpreting clusters.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn
- Streamlit
- Pickle

---

# 📊 Project Workflow

### Step 1: Data Loading

- Load the dataset into Pandas DataFrame.
- Understand dataset dimensions.
- Check column names and data types.

### Step 2: Data Cleaning

- Check missing values.
- Check duplicate records.
- Remove unnecessary columns.
- Select relevant numerical features.

### Step 3: Exploratory Data Analysis (EDA)

- Summary statistics
- Distribution plots
- Correlation Heatmap

### Step 4: Feature Scaling

Apply **StandardScaler** to standardize feature values.

Reason:
- K-Means is distance-based.
- Features should have equal importance.

### Step 5: Determine Optimal Number of Clusters

Two evaluation techniques were used:

#### Elbow Method

- Calculates Inertia for different K values.
- Helps identify the optimal number of clusters.

#### Silhouette Score

- Measures cluster quality.
- Higher score indicates better clustering.

### Step 6: K-Means Clustering

- Train K-Means model.
- Assign cluster labels.
- Add cluster labels to the original dataset.

### Step 7: PCA Visualization

Reduce high-dimensional data into two principal components for visualization.

### Step 8: Cluster Interpretation

Analyze average feature values of each cluster to understand song characteristics.

### Step 9: Save Models

Using Pickle:

- scaler.pkl
- kmeans_model.pkl
- pca.pkl

### Step 10: Streamlit Dashboard

Interactive dashboard providing:

- Song Search
- Cluster Filtering
- PCA Visualization
- Cluster Distribution
- Cluster Statistics

---

# 📈 Evaluation Metrics

## Silhouette Score

Measures how similar a song is to its own cluster compared to other clusters.

Interpretation:

- Close to 1 → Excellent clustering
- Close to 0 → Overlapping clusters
- Less than 0 → Poor clustering

---

## Davies-Bouldin Index

Measures cluster compactness and separation.

Lower value indicates better clustering.

---

## Inertia

Measures cluster compactness.

Used to determine the optimal K using the Elbow Method.

---

# 📷 Streamlit Application Screenshots

## 🏠 Home Page

![Home Page](Screenshots/Home%20Page.png)

---

## 📊 PCA Visualization

![PCA Visualization](Screenshots/PCA%20Visualization.png)

---

## 🎯 Cluster Analysis

![Cluster Analysis](Screenshots/Cluster%20Analysis.png)

---

## 📋 Cluster Explorer

![Cluster Explorer](Screenshots/Cluster%20Explorer.png)
---


# 📁 Project Structure

```text
AMAZON MUSIC CLUSTERING PROJECT/
│
├── Report/
│   └── Amazon Music Song Clustering Report.pdf
│
├── Screenshots/
│   ├── Home Page.png
│   ├── PCA Visualization.png
│   ├── Cluster Analysis.png
│   └── Cluster Explorer.png
│
├── app.py
├── genre_artists analysis.ipynb
├── README.md
├── requirements.txt
├── scaler.pkl
├── kmeans_model.pkl
├── pca.pkl
├── songs_clustered.csv
└── single_genre_artists.csv
```

---
## 📂 Dataset

The songs_clustered.csv  dataset is not included in this repository due to its large size. 

---

# ▶️ Running the Project

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Open Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
genre_artists analysis.ipynb
```

---

## 4. Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 💼 Business Applications

- Music Recommendation Systems
- Playlist Generation
- Song Similarity Analysis
- Audio Feature Analysis
- User Preference Analysis
- Music Discovery
- Content Personalization

---

# 🚀 Future Enhancements

- Implement DBSCAN Clustering
- Hierarchical Clustering
- Personalized Recommendation Engine
- Cloud Deployment
- Real-Time Audio Analysis
- Deep Learning-Based Song Embeddings

---

# 📚 Key Learnings

- Unsupervised Machine Learning
- K-Means Clustering
- Principal Component Analysis (PCA)
- Feature Scaling using StandardScaler
- Cluster Evaluation Techniques
- Data Visualization
- Model Serialization using Pickle
- Streamlit Dashboard Development

---

