import streamlit as st
import pandas as pd
import plotly.express as px
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
