## Prototype summary

- Implemented InfluxDB client 2.0 support in `db.backends.influx2`.
- Updated `__init__` and added the requirements needed for InfluxDB 2.0
- Added test cases.
- note: I have implemented it completely except the chart queries. (wrote around 5queries, others can also be written similarly)

## Purpose

This prototype shows how a new client can be added and used by the main codebase without changing existing functionality, keeping backward compatibility with InfluxDB 1.8
## docs for reference 
https://influxdb-client.readthedocs.io/en/latest/index.html
## installation
pip install influxdb-client==1.50.0