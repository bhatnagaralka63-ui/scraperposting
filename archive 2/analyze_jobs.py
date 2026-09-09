import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_jobs.csv')

print("=" * 50)
print("JOB POSTINGS ANALYSIS")
print("=" * 50)

# Top 10 most common job titles
print("\n--- Top 10 Job Titles ---")
print(df['clean_title'].value_counts().head(10))

# Top 10 cities with most job postings
print("\n--- Top 10 Cities Hiring ---")
print(df['city'].value_counts().head(10))

# Work type breakdown (remote/onsite/hybrid)
print("\n--- Work Type Breakdown ---")
print(df['work_type'].value_counts())

# Top 10 companies posting the most jobs
print("\n--- Top 10 Companies ---")
print(df['company_name'].value_counts().head(10))

# Average number of applicants per listing
print("\n--- Application Competitiveness ---")
print(f"Average applicants per job: {df['no_of_application'].mean():.0f}")
print(f"Most competitive job (most applicants):")
most_competitive = df.loc[df['no_of_application'].idxmax()]
print(f"  {most_competitive['clean_title']} at {most_competitive['company_name']} — {most_competitive['no_of_application']:.0f} applicants")

# What % of listings mention a salary
salary_pct = (df['salary_mentioned'].sum() / len(df)) * 100
print(f"\n--- Salary Transparency ---")
print(f"{salary_pct:.1f}% of listings mention salary in the title")