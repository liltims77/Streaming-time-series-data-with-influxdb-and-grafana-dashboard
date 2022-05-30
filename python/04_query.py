import pandas as pd
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import influxdb_client.client.influxdb_client


client = influxdb_client.InfluxDBClient(
   url='http://localhost:8086',
   token='upCYN7MuF1Wpn6XxsmdGm_7C8I0K6jVo3bj7ZwLDMMyknAE4SWK6Mt5sRvWC1cGIXtcDOxx7LVHyp2-oPAuDjA==',
   org='my-org'
)

queryAPI = client.query_api()

#create flux query
myquery_location = 'from(bucket: "air-quality") |> range(start: 2013-03-25T00:00:00Z, stop: 2013-05-01T00:00:00Z)' \
            '|> filter(fn: (r) => r["_measurement"] == "location-tag-only")' \
            '|> filter(fn: (r) => r["_field"] == "TEMP")' 

location_df = queryAPI.query_data_frame( query= myquery_location)

print(location_df.info())
print(location_df)


myquery_everything = 'from(bucket: "air-quality") |> range(start: 2013-03-25T00:00:00Z, stop: 2013-05-01T00:00:00Z)' \
            '|> filter(fn: (r) => r["_measurement"] == "full-tags")' \
            '|> filter(fn: (r) => r["_field"] == "TEMP")' 


everything_df = queryAPI.query_data_frame( query= myquery_everything)

print(everything_df)


# '|> filter(fn: (r) => r["_measurement"] == "with-tags")' \
#    '|> filter(fn: (r) => r["_field"] == "CO")' \
#    '|> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)' \
#    '|> yield(name: "mean")'