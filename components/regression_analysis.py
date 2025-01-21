import streamlit as st
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

def regression_analysis(df):
    """
    Perform regression analysis and display results.
    """
    st.subheader("Regression Analysis")
    st.write("Fit a regression model and display the summary.")

    x_column = st.selectbox("Select the predictor (X) column", df.columns)
    y_column = st.selectbox("Select the response (Y) column", df.columns)

    if st.button("Run Regression Analysis"):
        X = df[[x_column]]
        y = df[y_column]

        X = sm.add_constant(X)  # Add constant for the intercept
        model = sm.OLS(y, X).fit()

        st.write("Regression Summary")
        st.text(model.summary())

        st.write("Fitted vs. Residuals Plot")
        fig, ax = plt.subplots()
        ax.scatter(model.fittedvalues, model.resid)
        ax.axhline(0, color='red', linestyle='--')
        ax.set_xlabel("Fitted Values")
        ax.set_ylabel("Residuals")
        st.pyplot(fig)
