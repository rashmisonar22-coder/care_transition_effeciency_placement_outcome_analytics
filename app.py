# Placement Outcome Distribution - Pie Chart

st.subheader("Distribution of Placement Outcomes")

outcome_counts = df["Placement Outcome"].value_counts()

fig = px.pie(
    names=outcome_counts.index,
    values=outcome_counts.values,
    title="Distribution of Placement Outcomes",
    hole=0
)

fig.update_traces(textinfo="label+percent")

st.plotly_chart(fig, use_container_width=True)
