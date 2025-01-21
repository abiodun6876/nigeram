import streamlit as st
import statsmodels.api as sm
import matplotlib.pyplot as plt  # Import matplotlib for plotting

def homoscedasticity(df):
    """
    Check homoscedasticity using residual plots.
    """
    st.subheader("Homoscedasticity Test")
    st.write("This test evaluates if residuals have constant variance.")

    x_column = st.selectbox("Select the predictor (X) column", df.columns)
    y_column = st.selectbox("Select the response (Y) column", df.columns)

    if st.button("Run Homoscedasticity Test"):
        X = df[x_column]
        y = df[y_column]

        X = sm.add_constant(X)  # Add constant for regression
        model = sm.OLS(y, X).fit()
        residuals = model.resid

        st.write("Residuals Plot")
        fig = sm.graphics.plot_partregress_grid(model)
        st.pyplot(fig)  # Pass the figure object to st.pyplot()
