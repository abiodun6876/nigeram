import streamlit as st
import matplotlib.pyplot as plt

def display_line_chart(df, x_col, y_col, title):
    """Display a line chart."""
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

def display_bar_chart(df, x_col, y_col, title):
    """Display a bar chart."""
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

def display_pie_chart(df, col, title):
    """Display a pie chart."""
    pie_data = df[col].value_counts()
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)
    st.pyplot(fig)
