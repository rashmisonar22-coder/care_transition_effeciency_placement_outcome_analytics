
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

# Sample dataset
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

# CSV file upload
uploaded_file = st.file_uploader(
    "Upload Your Project Dataset",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.subheader("Project Dataset")
st.dataframe(df, use_container_width=True)

# Key performance indicators
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Patient Records", len(df))

with col2:
    if "Transition Days" in df.columns:
        avg_days = df["Transition Days"].mean()
        st.metric("Average Transition Days", round(avg_days, 2))

# Pie chart
if "Placement Outcome" in df.columns:
    st.subheader("Distribution of Placement Outcomes")

    outcome_counts = df["Placement Outcome"].value_counts()

    fig = px.pie(
        names=outcome_counts.index,
        values=outcome_counts.values,
        title="Placement Outcome Distribution",
        color_discrete_sequence=["#26965B", "#E9A23B"]
    )

    fig.update_traces(textinfo="label+percent")

    st.plotly_chart(fig, use_container_width=True)

# Histogram
if "Transition Days" in df.columns:
    st.subheader("Distribution of Transition Days")

    hist = px.histogram(
        df,
        x="Transition Days",
        title="Patient Transition Duration in Days"
    )

    st.plotly_chart(hist, use_container_width=True)

st.success("Dashboard analysis completed.")
