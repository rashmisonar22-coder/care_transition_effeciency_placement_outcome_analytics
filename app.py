
# Histogram - Distribution of Transition Days

st.subheader("Distribution of Patient Transition Days")

fig2 = px.histogram(
    df,
    x="Transition Days",
    title="Patient Transition Duration",
    labels={"Transition Days": "Transition Days"},
    nbins=6,
    color_discrete_sequence=["#26965B"]
)

fig2.update_layout(
    xaxis_title="Transition Days",
    yaxis_title="Number of Patients"
)

st.plotly_chart(fig2, use_container_width=True)
