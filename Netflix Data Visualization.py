import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Preparation
df = pd.read_csv("netflix_data.csv")
df.name = "Netflix_shows_movies"

# Data Cleaning
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df.dropna(subset=['date_added', 'rating'], inplace=True)

# Data Exploration
print(df.describe())
print(df['type'].value_counts())
print(df['rating'].value_counts())
print(df['listed_in'].str.split(', ').explode().value_counts().head(10))


# Data Visualization
plt.figure(figsize=(10,6))
genre_counts = df['listed_in'].str.split(', ').explode().value_counts().head(10)
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
plt.title('Top 10 Most Watched Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette="magma")
plt.title('Ratings Distribution on Netflix')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()
