import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Earthquakes_database.csv')


df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
df['Date'] = df['DateTime'].dt.date
df['Time'] = df['DateTime'].dt.time


df.drop('Depth Seismic Stations', axis=1, inplace=True)


df['Depth'].fillna(df['Depth'].median(), inplace=True)
df['Magnitude Error'].fillna(df['Magnitude Error'].mean(), inplace=True)


magnitude_categories = ['Low', 'Medium', 'High']
df['Magnitude_Category'] = pd.cut(df['Magnitude'], bins=[0, 5.5, 6.5, 10], labels=magnitude_categories)


df_melted = pd.melt(df, id_vars=['Date', 'Time', 'Latitude', 'Longitude'], value_vars=['Depth', 'Magnitude'])


df_pivot = df.pivot_table(index='Date', columns='Magnitude_Category', values='Magnitude', aggfunc='mean')


plt.figure(figsize=(10, 5))
plt.plot(pd.to_datetime(df['Date']), df['Magnitude'])
plt.title('Magnitude Over Time')
plt.xlabel('Date')
plt.ylabel('Magnitude')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
df['Magnitude_Category'].value_counts().plot(kind='bar') 
plt.title('Frequency of Magnitude Categories')
plt.xlabel('Magnitude Category')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df['Latitude'], df['Longitude'])
plt.title('Earthquake Coordinates')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()

plt.figure(figsize=(7, 5))
df['Type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Earthquake Types')
plt.ylabel('')
plt.show()

df['Year'] = pd.DatetimeIndex(df['Date']).year
df['Month'] = pd.DatetimeIndex(df['Date']).month

yearly_earthquakes = df.set_index('DateTime').resample('Y').size()

df.to_csv('cleaned_earthquake_data.csv', index=False)
