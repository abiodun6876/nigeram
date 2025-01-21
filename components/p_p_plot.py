import streamlit as st
import matplotlib.pyplot as plt
import statsmodels.api as sm

def p_p_plot(df):
    """
    Generate a P-P plot to check normality.
    """
    st.subheader("P-P Plot")
    st.write("This plot helps check the normality of the dataset.")

    column = st.selectbox("Select the column to test", df.columns)

    if st.button("Generate P-P Plot"):
        data = df[column].dropna()  # Drop missing values
        sm.qqplot(data, line='45')
        plt.title("P-P Plot")
        st.pyplot(plt)
