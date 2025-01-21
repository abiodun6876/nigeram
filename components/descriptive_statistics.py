import streamlit as st
import pandas as pd

def display_descriptive_statistics(df, label, description=None):
    # Displaying the general descriptive statistics for the given data
    if df is not None and not df.empty:
        st.subheader(f'Descriptive Statistics for {label}')
        
        # If description is provided (e.g., research-specific details)
        if description:
            st.write(description)
        
        # Display the DataFrame's descriptive statistics
        st.write(df.describe())
        
    else:
        st.warning(f"No data available for {label}.")
        
# Example of research-specific descriptive statistics (Replace with your data as needed)

# Example 1: Descriptive Statistics for Gender of Respondents
gender_description = """
**Table 2: Descriptive Statistics for Gender of Respondents**

This table summarizes the gender distribution of the survey respondents across different categories of respondents (Public Universities, Private Universities, and Online Universities). The data includes the number and percentage of male and female lecturers who responded to the survey.
"""

# Example DataFrame (Replace with actual data)
data_gender = {
    'Sample': ['Total Participants', 'Public Universities - Male', 'Public Universities - Female', 'Private Universities - Male', 'Private Universities - Female'],
    'f': [500, 200, 300, 150, 350],
    '%': [100, 40, 60, 30, 70]
}

df_gender = pd.DataFrame(data_gender)
display_descriptive_statistics(df_gender, 'Gender of Respondents', description=gender_description)

# Example 2: Descriptive Statistics for Responses to Transformational Leadership
leadership_description = """
**Table 3: Descriptive Statistics for Responses to Scale Items on Transformational Leadership**

This table presents descriptive statistics for responses to items measuring Transformational Leadership dimensions (Attributional Idealized Influence, Behavioral Idealized Influence, Inspirational Motivation, Intellectual Stimulation, and Individual Consideration).
"""

# Example DataFrame (Replace with actual data)
data_leadership = {
    'Transformational Leadership Dimension': [
        'Attributional Idealized Influence - Item 1', 'Attributional Idealized Influence - Item 2', 
        'Behavioral Idealized Influence - Item 1', 'Behavioral Idealized Influence - Item 2',
        'Inspirational Motivation - Item 1', 'Inspirational Motivation - Item 2'
    ],
    'Min': [1, 3, 1, 2, 2, 2],
    'Max': [4, 4, 4, 4, 4, 4],
    'M': [3.26, 3.59, 2.85, 3.71, 3.76, 3.76],
    'SD': [0.751, 0.5, 0.857, 0.629, 0.554, 0.554]
}

df_leadership = pd.DataFrame(data_leadership)
display_descriptive_statistics(df_leadership, 'Transformational Leadership Responses', description=leadership_description)
