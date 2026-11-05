
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Care Transition Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("Care Transition Efficiency and Placement Outcome Analytics")

st.write(
    "A dashboard to analyse patient care transitions, "
    "discharge efficiency and placement outcomes."
)

st.info("DEMO VERSION – Replace sample data with actual project data.")

# Sample project data
data = {
    "Patient ID": [101, 102, 103, 104, 105, 106],
    "Transition Days": [3, 5, 2, 7, 4, 3],
    "Placement Outcome": [
        "Successful", "Successful", "Delayed",
        "Successful", "Delayed", "Successful"
    ],
    "Readmission": ["No", "No", "Yes", "No", "No", "No"]
}

df = pd.DataFrame(data)

st.subheader("Upload Your Project Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset uploaded successfully!")

st.subheader("Project Dataset")
st.dataframe(df, use_container_width=True)

if "Transition Days" in df.columns:
    avg_days = pd.to_numeric(
        df["Transition Days"], errors="coerce"
    ).mean()

    st.subheader("Key Performance Indicators")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Records",
            len(df)
        )

    with col2:
        st.metric(
            "Average Transition Days",
            f"{avg_days:.2f}" if pd.notna(avg_days) else "N/A"
        )

if "Placement Outcome" in df.columns:
    st.subheader("Placement Outcome Analysis")

    outcome_data = df["Placement Outcome"].value_counts()

    fig = px.pie(
        values=outcome_data.values,
        names=outcome_data.index,
        title="Placement Outcome Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

if "Transition Days" in df.columns:
    st.subheader("Care Transition Efficiency")

    fig2 = px.histogram(
        df,
        x="Transition Days",
        title="Distribution of Transition Days"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.success("Demo analytics dashboard loaded successfully!")
