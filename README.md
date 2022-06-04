# STORING AND VISUALIZING TIME SERIES WITH GRAFANA AND INFLUXDB
This is a project for time based data like measurmant from IOT devices or events been streamed to a database from machines, sensors which are visualized on a dashboard.
This is a project of timeseries data with InfluxDB and Grafana dashboards

# Data set used
a weather time-series data set(CSV) gotton from kaggle was used for this project.

# Tools used
Docker,
InfluxDB,
Grafana dashboard

# Goals
1. using a time series data set, creating a python injestion program to read data from the CSV file where it takes the whole file and writes it to influxDB using Docker. data is then queried from grafana dashboard where client can access the files.
2. Python injestion scriptS is used to query data from weather API where data is now sent to influxDB and grafana dashboard for clients to be able to view/access data.

# Conclusion
Time series data set was read from a python injestion and wrote to the influxDB. grafana UI was used to query data from influxDB, where client can query the data from the grafana dashboard.
python injestion was used to query data from the weather API and written into influxDB and focused more on grafana where two organizations was set up(editors and viewers) and given different permissions to see/query data.
