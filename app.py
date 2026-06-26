import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------
# PAGE CONFIG
# -------------------------------------

st.set_page_config(
    page_title="Amazon Music Song Clustering",
    layout="wide"
)

# -------------------------------------
# LOAD DATA
# -------------------------------------

df = pd.read_csv("songs_clustered.csv")

# -------------------------------------
# SIDEBAR
# -------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Cluster Visualization",
        "Cluster Analysis",
        "Cluster Explorer"
    ]
)

# =====================================
# HOME PAGE
# =====================================

if page == "Home":

    st.title("🎵 Amazon Music Song Clustering")

    st.markdown("""
    This project groups songs based on their audio characteristics
    using K-Means Clustering and PCA Visualization.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Songs",
            len(df)
        )

    with col2:
        st.metric(
            "Total Features",
            10
        )

    with col3:
        st.metric(
            "Total Clusters",
            df['Cluster'].nunique()
        )

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

# =====================================
# CLUSTER VISUALIZATION
# =====================================

elif page == "Cluster Visualization":

    st.title("📊 PCA Cluster Visualization")

    fig = px.scatter(
        df,
        x='PCA1',
        y='PCA2',
        color='Cluster',
        hover_data=[
            'name_song',
            'name_artists'
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# CLUSTER ANALYSIS
# =====================================

elif page == "Cluster Analysis":

    st.title("📈 Cluster Analysis")

    cluster_counts = (
        df['Cluster']
        .value_counts()
        .reset_index()
    )

    cluster_counts.columns = [
        'Cluster',
        'Count'
    ]

    st.subheader("Cluster Distribution")

    fig = px.bar(
        cluster_counts,
        x='Cluster',
        y='Count'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Cluster Statistics")

    st.dataframe(cluster_counts)

# =====================================
# CLUSTER EXPLORER
# =====================================

elif page == "Cluster Explorer":

    st.title("🔍 Cluster Explorer")

    cluster = st.selectbox(
        "Select Cluster",
        sorted(df['Cluster'].unique())
    )

    filtered_df = df[
        df['Cluster'] == cluster
    ]

    st.write(
        f"Songs in Cluster {cluster}:",
        len(filtered_df)
    )

    st.dataframe(
        filtered_df[
            [
                'name_song',
                'name_artists',
                'Cluster'
            ]
        ]
    )