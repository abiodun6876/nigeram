import streamlit as st
from scipy.stats import shapiro, normaltest
import matplotlib.pyplot as plt
import seaborn as sns

def normality_test(df):
    """
    Test for normality using Shapiro-Wilk and D’Agostino K-squared tests.
    """
    st.subheader("Normality Test")
    st.write("Evaluate if the data follows a normal distribution.")

    column = st.selectbox("Select a column to test", df.columns)

    if st.button("Run Normality Test"):
        data = df[column].dropna()

        st.write("Shapiro-Wilk Test")
        shapiro_stat, shapiro_p = shapiro(data)
        st.write(f"Statistic: {shapiro_stat:.4f}, p-value: {shapiro_p:.4f}")

        st.write("D’Agostino K-squared Test")
        dagostino_stat, dagostino_p = normaltest(data)
        st.write(f"Statistic: {dagostino_stat:.4f}, p-value: {dagostino_p:.4f}")

        st.write("Histogram and Density Plot")
        fig, ax = plt.subplots()
        sns.histplot(data, kde=True, ax=ax)
        ax.set_title("Histogram and KDE")
        st.pyplot(fig)
