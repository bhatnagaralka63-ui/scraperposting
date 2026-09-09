import pandas as pd
import re

# Load the raw data
df = pd.read_csv('linkdin_Job_data.csv')

print(f"Loaded {len(df)} raw job listings")

# Drop rows with no job title or location
df = df.dropna(subset=['job', 'location'])

# Extract clean job title (before the first comma)
df['clean_title'] = df['job'].apply(lambda x: str(x).split(',')[0].strip())

# Extract salary if mentioned in the title (e.g. "$60,000/year")
df['salary_mentioned'] = df['job'].str.contains(r'\$[\d,]+', regex=True, na=False)

# Clean location - just keep city name (before first comma)
df['city'] = df['location'].apply(lambda x: str(x).split(',')[0].strip())

# Convert applicant count to numeric
df['no_of_application'] = pd.to_numeric(df['no_of_application'], errors='coerce')

# Keep only the useful columns for analysis
clean_df = df[['job_ID', 'clean_title', 'city', 'company_name', 'work_type',
               'no_of_employ', 'no_of_application', 'posted_day_ago',
               'salary_mentioned', 'job_details']].copy()

# Remove exact duplicate listings
clean_df = clean_df.drop_duplicates(subset=['clean_title', 'company_name', 'city'])

print(f"Cleaned down to {len(clean_df)} unique listings")

# Save cleaned version
clean_df.to_csv('cleaned_jobs.csv', index=False)
print("Saved cleaned_jobs.csv")