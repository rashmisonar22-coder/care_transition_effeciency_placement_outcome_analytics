import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Care Transition Analytics",
    page_icon="🏥",
    layout="wide"
)
st.title("Care Transition Efficiency and Placement Outcome Analytics")
st.write("A dashboard to analyse patient care transitions, discharge efficiency and placement outcomes.")
st.info("DEMO VERSION – Using six sample patient records.")
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
# Display dataset
st.subheader("Project Dataset")
st.dataframe(df, use_container_width=True)

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Patient Records", len(df))
col2.metric("Average Transition Days", f"{df['Transition Days'].mean():.1f}")
col3.metric("Readmissions", int((df["Readmission"] == "Yes").sum()))

# Pie chart
st.subheader("Distribution of Placement Outcomes")

outcome_counts = df["Placement Outcome"].value_counts()
fig = px.pie(
    names=outcome_counts.index,
    values=outcome_counts.values,
    title="Placement Outcome Distribution"
)

fig.update_traces(textinfo="label+percent")
st.plotly_chart(fig, use_container_width=True)

# Histogram
st.subheader("Distribution of Patient Transition Days")

fig2 = px.histogram(
    df,
    x="Transition Days",
    title="Patient Transition Duration",
    nbins=6
)

fig2.update_layout(
    xaxis_title="Transition Days",
    yaxis_title="Number of Patients"
)

st.plotly_chart(fig2, use_container_width=True)

# Readmission status
st.subheader("Readmission Status")

readmission_counts = df["Readmission"].value_counts()

st.dataframe(
    readmission_counts.rename_axis("Readmission").reset_index(
        name="Patient Count"
    ),
    use_container_width=True
)

st.success("Dashboard analysis completed.")






