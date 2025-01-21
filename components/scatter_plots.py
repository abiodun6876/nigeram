import streamlit as st
import plotly.express as px

def scatter_plots(df):
    """
    Generate scatter plots for visualizing relationships between variables.
    """
    st.subheader("Scatter Plots")
    st.write("Scatter plots help visualize the relationship between two variables.")

    x_column = st.selectbox("Select the X-axis column", df.columns)
    y_column = st.selectbox("Select the Y-axis column", df.columns)

    if st.button("Generate Scatter Plot"):
        scatter_plot = px.scatter(df, x=x_column, y=y_column, title=f"Scatter Plot: {y_column} vs {x_column}")
        st.plotly_chart(scatter_plot, use_container_width=True)
