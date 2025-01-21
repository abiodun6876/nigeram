import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def pearson_correlation(df):
    """
    Compute and display Pearson correlation matrix.
    """
    st.subheader("Pearson Correlation")
    st.write("Calculate and visualize correlation coefficients.")

    columns = st.multiselect("Select columns for correlation", df.columns)

    if st.button("Compute Correlation"):
        if len(columns) < 2:
            st.warning("Select at least two columns to compute correlation.")
        else:
            correlation_matrix = df[columns].corr()
            st.write("Correlation Matrix:")
            st.dataframe(correlation_matrix)

            st.write("Heatmap of Correlation Matrix")
            fig, ax = plt.subplots()
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
