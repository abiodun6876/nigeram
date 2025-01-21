import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

# Import components for statistical tests
from components.regression_analysis import regression_analysis
from components.multicollinearity_test import multicollinearity_test
from components.normality_test import normality_test
from components.pearson_correlation import pearson_correlation
from components.homoscedasticity import homoscedasticity
from components.p_p_plot import p_p_plot
from components.scatter_plots import scatter_plots
from components.histogram_curve import histogram_curve

# Function to load data
def load_data():
    """Load datasets for public, private, and online universities."""
    try:
        public_df = pd.read_csv('public.csv')
        private_df = pd.read_csv('private.csv')
        online_df = pd.read_csv('online.csv')
        return public_df, private_df, online_df
    except FileNotFoundError as e:
        st.error(f"Error loading data: {e}")
        return None, None, None
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV files: {e}")
        return None, None, None


# Function to display detailed statistics
def display_statistics(df, selected_column=None):
    """Display detailed statistics for all columns or a specific column."""
    if df is None or df.empty:
        st.warning("The DataFrame is empty or not loaded correctly.")
        return

    # If a specific column is provided, process it; otherwise, process all columns
    columns_to_process = [selected_column] if selected_column else df.columns

    for column in columns_to_process:
        st.write(f"### Detailed Statistics for `{column}`")

        # Check if the column exists in the DataFrame
        if column not in df.columns:
            st.warning(f"Column `{column}` does not exist in the DataFrame.")
            continue

        # Check if the column is numeric
        if pd.api.types.is_numeric_dtype(df[column]):
            # Drop NaN and compute statistics
            numeric_column = df[column].dropna()
            if not numeric_column.empty:
                stats_data = {
                    "Statistic": ["Min", "Max", "Mean (M)", "Std Dev (SD)", "Median", "IQR"],
                    "Value": [
                        numeric_column.min(),
                        numeric_column.max(),
                        numeric_column.mean(),
                        numeric_column.std(),
                        numeric_column.median(),
                        numeric_column.quantile(0.75) - numeric_column.quantile(0.25),
                    ],
                }
                stats_df = pd.DataFrame(stats_data)
                st.table(stats_df)
            else:
                st.warning(f"Column `{column}` contains no valid numeric data.")
        else:
            # Handle non-numeric (categorical) columns
            st.write("**Unique Values Count:**")
            value_counts = df[column].value_counts(dropna=False)
            st.dataframe(value_counts)


public_df, private_df, online_df = load_data()

# Function to display total counts
def display_total_cards(public_df, private_df, online_df):
    """Display total counts in rounded box format for each dataset."""
    if public_df is not None and private_df is not None and online_df is not None:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div style="background-color:#4CAF50; color:white; padding:15px; border-radius:10px; text-align:center;">
                    <h4>Total Public Universities</h4>
                    <h2>{len(public_df)}</h2>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div style="background-color:#2196F3; color:white; padding:15px; border-radius:10px; text-align:center;">
                    <h4>Total Private Universities</h4>
                    <h2>{len(private_df)}</h2>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div style="background-color:#FF5722; color:white; padding:15px; border-radius:10px; text-align:center;">
                    <h4>Total Online Universities</h4>
                    <h2>{len(online_df)}</h2>
                </div>
            """, unsafe_allow_html=True)


# Function to display dataset preview
def display_data_preview(df, label):
    """Display a preview of the first few rows of the dataset."""
    if df is not None:
        st.subheader(f'{label} University Data Preview')
        st.dataframe(df)


# Function to plot graphs
def plot_graphs(df, label):
    """Allow users to plot multiple graphs."""
    st.subheader(f"{label} University Data Visualizations")
    if df is not None:
        columns = list(df.columns)
        selected_columns = st.multiselect("Select columns to visualize", columns, key=f"multi_{label}")
        if selected_columns:
            col1, col2, col3 = st.columns(3)
            for i, column in enumerate(selected_columns):
                with [col1, col2, col3][i % 3]:
                    # Pie chart
                    if not pd.api.types.is_numeric_dtype(df[column]) and df[column].nunique() <= 20:
                        pie_chart = px.pie(df, names=column, title=f"Pie Chart: {column}")
                        st.plotly_chart(pie_chart, use_container_width=True)
                    # Histogram
                    elif pd.api.types.is_numeric_dtype(df[column]):
                        histogram = px.histogram(df, x=column, title=f"Histogram: {column}")
                        st.plotly_chart(histogram, use_container_width=True)
                    else:
                        st.write(f"Column `{column}` cannot be visualized.")


def multiple_regression_analysis(df):
    st.subheader("Multiple Regression Analysis")
    if df is not None:
        st.write("Select dependent and independent variables for regression analysis.")

        dependent_var = st.selectbox("Select Dependent Variable (Y)", df.columns)
        independent_vars = st.multiselect(
            "Select Independent Variables (X)", df.columns, default=[]
        )

        if st.button("Run Regression Analysis"):
            if not independent_vars or dependent_var in independent_vars:
                st.warning("Please select valid independent variables.")
            else:
                # Check and preprocess data
                df = df[[dependent_var] + independent_vars].dropna()
                df = df.apply(pd.to_numeric, errors='coerce')
                df = df.dropna()  # Remove rows with invalid data

                if df.empty:
                    st.error("No valid data available after cleaning. Please check your dataset.")
                    return

                X = df[independent_vars]
                y = df[dependent_var]

                # Add constant and fit the model
                X = sm.add_constant(X)
                try:
                    model = sm.OLS(y, X).fit()

                    # Display results
                    st.text("Regression Model Summary")
                    st.text(model.summary())

                    # Visualization: Residuals vs Fitted values
                    st.write("Residuals vs Fitted Values")
                    residuals_fig = px.scatter(
                        x=model.fittedvalues,
                        y=model.resid,
                        labels={'x': "Fitted Values", 'y': "Residuals"},
                        title="Residuals vs Fitted"
                    )
                    residuals_fig.add_hline(y=0, line_dash="dash", line_color="red")
                    st.plotly_chart(residuals_fig)

                    # Visualization: Predicted vs Actual
                    st.write("Predicted vs Actual Values")
                    actual_predicted_fig = px.scatter(
                        x=y,
                        y=model.fittedvalues,
                        labels={'x': "Actual Values", 'y': "Predicted Values"},
                        title="Actual vs Predicted"
                    )
                    st.plotly_chart(actual_predicted_fig)

                except Exception as e:
                    st.error(f"Regression analysis failed: {e}")



# Main application
def main():
    st.title('University Data Analysis and Visualization')
    st.markdown("""
        Analyze and visualize datasets for public, private, and online universities.
    """)

    public_df, private_df, online_df = load_data()
    if public_df is not None and private_df is not None and online_df is not None:
        # Display total counts
        st.header('University Dataset Summary')
        display_total_cards(public_df, private_df, online_df)

        # Sidebar options
        dataset_option = st.sidebar.selectbox("Choose dataset", ["Public", "Private", "Online"])
        df = public_df if dataset_option == "Public" else private_df if dataset_option == "Private" else online_df

        selected_analysis = st.sidebar.radio(
            "Choose an analysis type",
            ["Data Preview", "Statistics", "Visualizations", "Multiple Regression Analysis"]
        )

        if selected_analysis == "Data Preview":
            display_data_preview(df, dataset_option)
        elif selected_analysis == "Statistics":
            selected_column = st.sidebar.selectbox("Select a column", df.columns)
            display_statistics(df, selected_column)
        elif selected_analysis == "Visualizations":
            plot_graphs(df, dataset_option)
        elif selected_analysis == "Multiple Regression Analysis":
            multiple_regression_analysis(df)


if __name__ == "__main__":
    main()
