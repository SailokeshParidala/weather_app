import json
import requests
import pandas as pd
city=input()
date=input()
resp=requests.get('https://api.oikolab.com/weather',
                 params={'param': ['temperature'],
                         'start': date,
                         'end': date,
                         'location':city,
                         'api-key': 'ef7152b74aeb4cb09913066f5394a7b0',
                         'freq':'D'}
                  
                 )
weather_data = json.loads(resp.json()['data'])
df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],
                                       unit='s'),
                  data=weather_data['data'],
                  columns=weather_data['columns'])
temp=int(df.iloc[0,4])
print(f'Temperature for {city} on {date} = {temp}C')







import json
import requests
import pandas as pd
import datetime
def city_variance(city,start,end):
     resp=requests.get('https://api.oikolab.com/weather',
                 params={'param': ['temperature'],
                         'start':start,
                         'end': end,
                         'location':city,
                         'api-key': 'ef7152b74aeb4cb09913066f5394a7b0',
                         'freq':'D'}
                  
                 )
     weather_data = json.loads(resp.json()['data'])
     df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],
                                       unit='s'),
                  data=weather_data['data'],
                  columns=weather_data['columns'])
     variance=df['temperature (degC)'].var()
     return variance

city1=input()
city2=input()
start_date=input()
start_date=start_date.split('-')
obj1=datetime.datetime(int(start_date[0]),int(start_date[1]),int(start_date[2]))
obj2=obj1 + datetime.timedelta(days=7)
s=str(obj1)
e=str(obj2)
start_date=s[:10]
end_date=e[:10]
var1=city_variance(city1,start_date,end_date)
var2=city_variance(city2,start_date,end_date)
if var1<var2:
    print(f"We choose {city1} because of less temperature variance")
else:
    print(f"We choose {city2} because of less temperature variance")



