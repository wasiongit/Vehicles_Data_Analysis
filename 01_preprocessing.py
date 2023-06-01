# to convert given format to datetime[ns]
import pandas as pd

df=pd.read_csv('Trip-info.csv')
print(df.dtypes)
df['date_time'] = pd.to_datetime(df['date_time'], format='%Y%m%d%H%M%S')

 
print(df.dtypes)
df.to_csv('trips.csv')


