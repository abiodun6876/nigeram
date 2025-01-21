import streamlit as st

def display_total_card(value, title="Total", icon="💰"):
    """
    Display a card showing the total value.
    """
    col1, col2 = st.columns([1, 4])  # Adjust the column width if necessary
    with col1:
        st.metric(label=title, value=value, delta=None)
    with col2:
        st.write(f"**{icon}**")  # You can change this to any icon you want to use for visualization
import streamlit as st

def display_table(df, title="Data Table"):
    """
    Display a dataframe in a table format with some basic options for interaction.
    """
    if df is not None and not df.empty:
        st.subheader(title)
        st.dataframe(df)  # Display table with interactive features (sortable, filterable)
    else:
        st.warning(f"No data available for {title}.")
