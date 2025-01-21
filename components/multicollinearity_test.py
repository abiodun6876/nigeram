import streamlit as st
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

def multicollinearity_test(df):
    """
    Check for multicollinearity using Variance Inflation Factor (VIF).
    """
    st.subheader("Multicollinearity Test")
    st.write("Calculate Variance Inflation Factor (VIF) for predictor variables.")

    predictors = st.multiselect("Select predictor columns", df.columns)

    if st.button("Run Multicollinearity Test"):
        if len(predictors) < 2:
            st.warning("Select at least two predictor columns to calculate VIF.")
        else:
            X = df[predictors]
            X = X.assign(Intercept=1)  # Add constant for regression
            vif_data = pd.DataFrame({
                "Variable": X.columns,
                "VIF": [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
            })
            st.write("Variance Inflation Factor (VIF):")
            st.dataframe(vif_data[vif_data["Variable"] != "Intercept"])
