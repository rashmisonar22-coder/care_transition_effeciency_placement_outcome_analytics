import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("Distribution of Patient Transition Days")
st.plotly_chart(fig2, use_container_width=True)
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

