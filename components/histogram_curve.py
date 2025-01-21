import streamlit as st
import plotly.express as px

def histogram_curve(df):
    """
    Generate histogram curves for a specific column.
    """
    st.subheader("Histogram Curve")
    st.write("This plot displays the distribution of a variable.")

    column = st.selectbox("Select the column for the histogram", df.columns)

    if st.button("Generate Histogram"):
        histogram = px.histogram(df, x=column, title=f"Histogram for {column}", nbins=20)
        st.plotly_chart(histogram, use_container_width=True)
