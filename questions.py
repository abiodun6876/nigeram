import pandas as pd
import streamlit as st

def descriptive_statistics(df, category):
    if df is not None:
        st.subheader(f"Descriptive Statistics for {category} Data")
        
        # Gender breakdown (Categorical)
        if 'Your gender' in df.columns:
            gender_stats = df['Your gender'].value_counts(normalize=True) * 100
            st.write(f"Gender Distribution in {category}:")
            st.write(gender_stats)
            st.write("Scale: 0 = Male, 1 = Female, 2 = Other")
        
        # Religion breakdown (Categorical)
        if 'What is your religion?' in df.columns:
            religion_stats = df['What is your religion?'].value_counts(normalize=True) * 100
            st.write("Religion Distribution:")
            st.write(religion_stats)
            st.write("Scale: 0 = Christian, 1 = Muslim, 2 = Traditional, 3 = Other")
        
        # Education Level Breakdown (Ordinal Scale)
        if 'What is your current level of education?' in df.columns:
            education_stats = df['What is your current level of education?'].value_counts(normalize=True) * 100
            st.write("Education Level Distribution:")
            st.write(education_stats)
            st.write("Scale: 0 = High School, 1 = Undergraduate, 2 = Graduate, 3 = Doctorate, 4 = Masters")
        
        # Age Range Breakdown (Ordinal Scale)
        if 'What is your age range?' in df.columns:
            age_stats = df['What is your age range?'].value_counts(normalize=True) * 100
            st.write("Age Range Distribution:")
            st.write(age_stats)
            st.write("Scale: 0 = 18-24, 1 = 25-34, 2 = 35-44, 3 = 45-54, 4 = 55+")
        
        # Disability Status Breakdown (Categorical)
        if 'What is your current self-assessed disability status?' in df.columns:
            disability_status_stats = df['What is your current self-assessed disability status?'].value_counts(normalize=True) * 100
            st.write("Disability Status Distribution:")
            st.write(disability_status_stats)
            st.write("Scale: 0 = None, 1 = Mobility Impairment, 2 = Visual Impairment, 3 = Hearing Impairment, 4 = Other")
        
        # Geopolitical Zone Breakdown (Categorical)
        if 'What is your current geopolitical zone of origin in Nigeria?' in df.columns:
            geo_zone_stats = df['What is your current geopolitical zone of origin in Nigeria?'].value_counts(normalize=True) * 100
            st.write("Geopolitical Zone Distribution:")
            st.write(geo_zone_stats)
            st.write("Scale: 0 = North-East, 1 = North-West, 2 = North-Central, 3 = South-East, 4 = South-West, 5 = South-South")
        
        # Marital Status Breakdown (Categorical)
        if 'What is your current marital status?' in df.columns:
            marital_status_stats = df['What is your current marital status?'].value_counts(normalize=True) * 100
            st.write("Marital Status Distribution:")
            st.write(marital_status_stats)
            st.write("Scale: 0 = Single, 1 = Married, 2 = Divorced, 3 = Widowed")
        
        # Income Breakdown (Ordinal Scale)
        if 'What is your current total family income range per month?' in df.columns:
            income_stats = df['What is your current total family income range per month?'].value_counts(normalize=True) * 100
            st.write("Income Range Distribution:")
            st.write(income_stats)
            st.write("Scale: 0 = Less than ₦50,000, 1 = ₦50,000-₦100,000, 2 = ₦100,000-₦200,000, 3 = ₦200,000+")
        
        # Social Interaction Level Breakdown (Likert Scale)
        if 'What is your current level of social interaction within your local community?' in df.columns:
            social_interaction_stats = df['What is your current level of social interaction within your local community?'].value_counts(normalize=True) * 100
            st.write("Social Interaction Level Distribution:")
            st.write(social_interaction_stats)
            st.write("Scale: 0 = Never, 1 = Rarely, 2 = Sometimes, 3 = Often, 4 = Always")
        
        # Leadership-related questions (Likert Scale)
        leadership_columns = [
            "I instill pride in others for being associated with me",
            "I go beyond self-interest for the good of the group",
            "I act in ways that build others’ respect for me",
            "I display a sense of power and confidence",
            "I talk about my most important values and beliefs",
            "I specify the importance of having a strong sense of purpose",
            "I consider the moral and ethical consequences of decisions",
            "I emphasize the importance of having a collective sense of mission",
            "I talk optimistically about the future",
            "I talk enthusiastically about what needs to be accomplished",
            "I articulate a compelling vision of the future",
            "I express confidence that goals will be achieved",
            "I re-examine critical assumptions to question whether they are appropriate",
            "I seek differing perspectives when solving problems",
            "I get others to look at problems from many different angles",
            "I suggest new ways of looking at how to complete assignments",
            "I spend time teaching and coaching",
            "I treat others as individuals rather than just as a member of a group",
            "I consider an individual as having different needs, abilities, and aspirations from others",
            "I help others to develop their strengths"
        ]
        
        for column in leadership_columns:
            if column in df.columns:
                stats = df[column].value_counts(normalize=True) * 100
                st.write(f"{column} Distribution:")
                st.write(stats)
                st.write("Scale: 0 = Strongly Disagree, 1 = Disagree, 2 = Neutral, 3 = Agree, 4 = Strongly Agree")
        
        # Job-related questions (Likert Scale)
        job_columns = [
            "I feel I am being paid a fair amount for the work I do",
            "There is really too little chance for promotion on my job",
            "My supervisor is quite competent in doing his/her job",
            "I am not satisfied with the benefits I receive",
            "When I do a good job, I receive the recognition for it that I should receive",
            "Many of our rules and procedures make doing a good job difficult",
            "I like the people I work with",
            "I sometimes feel my job is meaningless",
            "Communications seem good within this organization",
            "Raises are too few and far between",
            "Those who do well on the job stand a fair chance of being promoted",
            "My supervisor is unfair to me",
            "The benefits we receive are as good as most other organizations offer",
            "I do not feel that the work I do is appreciated",
            "My efforts to do a good job are seldom blocked by red tape",
            "I find I have to work harder at my job because of the incompetence of people I work with",
            "I like doing the things I do at work",
            "The goals of this organization are not clear to me",
            "I often seriously consider leaving my current job",
            "I intend to quit my current job",
            "I have started to look for other jobs"
        ]
        
        for column in job_columns:
            if column in df.columns:
                stats = df[column].value_counts(normalize=True) * 100
                st.write(f"{column} Distribution:")
                st.write(stats)
                st.write("Scale: 0 = Strongly Disagree, 1 = Disagree, 2 = Neutral, 3 = Agree, 4 = Strongly Agree")

        # Additional Migration-related Questions (Likert Scale)
        migration_columns = [
            "I think about migrating to another country temporarily",
            "I think about migrating to another country permanently",
            "I seek information about opportunities available for me outside this country",
            "I apply for opportunities outside this country",
            "I express my desire to others about wanting to pursue opportunities outside this country",
            "I am approached about potential opportunities outside this country",
            "If you migrated to another country, how likely do you believe you would have better career development and fulfillment prospects?",
            "If you migrated to another country, how likely do you believe that you would have better income and financial wellness prospects?",
            "If you migrated to another country, how likely do you believe you would have better family life prospects?",
            "If you migrated to another country, how likely do you believe you would have better social life prospects?",
            "How likely do you believe your current university education and/or any upcoming degree will enable you to migrate to another country successfully?"
        ]

        for column in migration_columns:
            if column in df.columns:
                stats = df[column].value_counts(normalize=True) * 100
                st.write(f"{column} Distribution:")
                st.write(stats)
                st.write("Scale: 0 = Not Likely, 1 = Somewhat Likely, 2 = Likely, 3 = Very Likely")

        # Additional Information on Migration Plans and Support (Likert Scale)
        support_columns = [
            "Obtaining relevant information about migrant arrival, onboarding and welfare at the destination country",
            "Securing academic opportunities at destination country",
            "Securing job opportunities at destination country",
            "Obtaining an international passport",
            "Obtaining a destination travel visa",
            "Obtaining a destination work permit",
            "Securing savings and funding for travel to, and stay at intended destination",
            "Informing significant others (e.g., spouse, children, family, etc.) of plans",
            "Starting a potential migration process"
        ]
        
        for column in support_columns:
            if column in df.columns:
                stats = df[column].value_counts(normalize=True) * 100
                st.write(f"{column} Distribution:")
                st.write(stats)
                st.write("Scale: 0 = Not Important, 1 = Somewhat Important, 2 = Important, 3 = Very Important")
    else:
        st.write("No data available")
