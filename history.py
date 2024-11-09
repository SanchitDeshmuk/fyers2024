from fyers_apiv3 import fyersModel
import pandas as pd

client_id = 'GCEG4OMS1B-100'
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MzEwODQ5NjQsImV4cCI6MTczMTExMjIwNCwibmJmIjoxNzMxMDg0OTY0LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbkxrS2tLSWpDbDlCZmE2ZkhFemdCVGM4RzB3bndBczVVNnpSRkd2dWprc2puZUswX0NCSUg3YW9oT1Vwa1dwLWFtYlN0SXAzM3pfTVpvNFptYjJ6bG5DQnJpSFhJZ1BZOXB4STAtY1M5bENJaGZWaz0iLCJkaXNwbGF5X25hbWUiOiJTQU5DSElUIERFU0hNVUtIIiwib21zIjoiSzEiLCJoc21fa2V5IjoiMDEyNDMxNDY5OGRjZDY5YzMyZDQ3M2EzOTEyZDg2ZDhjYmJjYWIwZTFiZDNjZDNkNWZkY2ZmMTciLCJmeV9pZCI6IlhTMDg0MTUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.lFYsDNW4UydgLLoaIfyPT7P68MkaS9Nz5Z5MdvMmMTs"

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol":"NSE:SBIN-EQ",
    "resolution":"1",
    "date_format":"1",
    "range_from":"2024-11-05",
    "range_to":"2024-11-06",
    "cont_flag":"1"
}

response = fyers.history(data=data)
data = response['candles']
df = pd.DataFrame(data)

# converting date to yyyy-mm-dd from epoch value
df.columns = ['date','open','high','low','close','volume']
df['date'] = pd.to_datetime(df['date'] , unit = 's')

# converting timezone to ist
df.date = (df.date.dt.tz_localize('UTC').dt.tz_convert('Asia/kolkata'))
df['date'] = df['date'].dt.tz_localize(None)
df = df.set_index('date')

print(df)

# saving data in csv format
# df.to_csv('data.csv')