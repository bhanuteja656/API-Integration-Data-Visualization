import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

city = 'Vijayawada'
api_key = 'f2251d4bace6ab4017229b5bd7b8905f'
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()
forecast_list = data['list']

dates = []
temperatures = []

for item in forecast_list:
    dates.append(item['dt_txt'])
    temperatures.append(item['main']['temp'])

df = pd.DataFrame({
    'DateTime': dates,
    'Temperature (°C)': temperatures
})

df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = df['DateTime'].dt.date
daily_avg = df.groupby('Date')['Temperature (°C)'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_avg, x='Date', y='Temperature (°C)', marker='o', color='blue')
plt.title(f'Daily Average Temperature Forecast for {city}')
plt.xlabel('Date')
plt.ylabel('Avg Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
