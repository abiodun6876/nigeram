import streamlit as st

def filter_and_search(df, column):
    if column in df.columns:
        st.subheader(f"Search and Filter by {column}")

        # Dropdown for filtering values
        unique_values = df[column].dropna().unique()
        selected_value = st.selectbox(f"Select a {column} to filter", unique_values)

        filtered_df = df[df[column] == selected_value]
        st.write(f"Showing data for {column}: {selected_value}")
        st.write(filtered_df)
    else:
        st.warning(f"Column '{column}' not found in the dataset.")
