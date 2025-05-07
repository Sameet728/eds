import numpy as np

import pandas as pd

# Load dataset

df = pd.read_csv('Movie Review And Rating.csv')

# Q1

print("Q1. Mean of Rating:", np.mean(df['Rating']))

# Q2

print("Q2. Median of Rating:", np.median(df['Rating']))

# Q3

print("Q3. Maximum Rating:", np.max(df['Rating']))

# Q4

print("Q4. Minimum Rating:", np.min(df['Rating']))

# Q5

print("Q5. Standard Deviation of Rating:", np.std(df['Rating']))

# Q6

print("Q6. Movies released after 2010:", np.sum(df['Year'] > 2010))

#Q7

print("Q7. Percentage of movies with Rating > 8:", (np.sum(df['Rating'] 

> 8) / len(df)) * 100)

# Q8

print("Q8. Average length of Movie names:", 

np.mean(df['Movie'].apply(len)))

# Q9

print("Q9. 75th percentile of Rating:", np.percentile(df['Rating'], 75))

# Q10

print("Q10. Movies with exactly 10 Rating:", np.sum(df['Rating'] == 

10))

# Q11

print("Q11. Number of unique Genres:", df['Genres'].nunique())

# Q12

print("Q12. Movies released in the earliest year:", df[df['Year'] 

== df['Year'].min()].shape[0])

# Q13

print("Q13. Top 5 frequent Genres:\n", 

df['Genres'].value_counts().head(5))

# Q14

print("Q14. Number of missing Reviews:", 

df['Review'].isnull().sum())

# Q15

df['Review'].fillna('No Review Provided', inplace=True)

print("Q15. Missing Reviews replaced with 'No Review 

Provided'.")

# Q16

print("Q16. Number of unique Movies:", df['Movie'].nunique())

# Q17

print("Q17. Top 3 most common words in Reviews:\n", 

pd.Series(''.join(df['Review'].dropna()).lower().split()).value_counts().head

(3))

# Q18

print("Q18. Number of reviews mentioning 'excellent' or 

'amazing':", df['Review'].str.contains('excellent|amazing', 

case=False, na=False).sum())

# Q19

print("Q19. Average Rating for each Genre:\n", 

df.groupby('Genres')['Rating'].mean())

# Q20

print("Q20. Total number of movies released each year:\n", 

df['Year'].value_counts())
