import pandas as pd

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\electricity.csv")


df.head()  # Preview first rows
df.info()  # Data types & missing values
df.describe()  # Summary statistics
df.shape  # Rows & columns

# df.isnull().sum()
# df.dropna()                     # Drop rows with any NA
# df.dropna(subset=['column'])    # Drop based on specific column
# df.fillna(0)                               # Replace with 0
# df['age'].fillna(df['age'].mean())         # Replace with mean
# df.fillna(method='ffill')                  # Forward fill
# df['date'] = pd.to_datetime(df['date'])
# df['price'] = df['price'].astype(float)
# df['category'] = df['category'].astype('category')
# Q1 = df['salary'].quantile(0.25)
# Q3 = df['salary'].quantile(0.75)
# IQR = Q3 - Q1

# df = df[(df['salary'] >= Q1 - 1.5*IQR) &
#         (df['salary'] <= Q3 + 1.5*IQR)]
# df['name'] = df['name'].str.strip()
# df['name'] = df['name'].str.lower()
# df['email'] = df['email'].str.replace(r'\s+', '', regex=True)
