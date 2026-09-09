import streamlit as st
import pandas as pd

st.set_page_config(page_title="Indian Job Market Dashboard", layout="wide")

# Load data
df = pd.read_csv('cleaned_jobs.csv')

st.title("📊 Indian Job Market Dashboard")
st.markdown("Analysis of job postings scraped from LinkedIn, focused on the Indian market.")

# Top-level stats
col1, col2, col3 = st.columns(3)
col1.metric("Total Job Listings", len(df))
col2.metric("Avg. Applicants per Job", f"{df['no_of_application'].mean():.0f}")
col3.metric("Salary Transparency", f"{(df['salary_mentioned'].sum() / len(df)) * 100:.1f}%")

st.divider()

# Two columns of charts
left, right = st.columns(2)

with left:
    st.subheader("Top 10 Job Titles")
    st.bar_chart(df['clean_title'].value_counts().head(10))

    st.subheader("Work Type Breakdown")
    st.bar_chart(df['work_type'].value_counts())

with right:
    st.subheader("Top 10 Cities Hiring")
    st.bar_chart(df['city'].value_counts().head(10))

    st.subheader("Top 10 Companies Posting Jobs")
    st.bar_chart(df['company_name'].value_counts().head(10))

st.divider()

# Filterable table
st.subheader("Browse Listings")
city_filter = st.selectbox("Filter by city", ["All"] + sorted(df['city'].dropna().unique().tolist()))
if city_filter != "All":
    filtered = df[df['city'] == city_filter]
else:
    filtered = df

st.dataframe(filtered[['clean_title', 'company_name', 'city', 'work_type', 'no_of_application']])