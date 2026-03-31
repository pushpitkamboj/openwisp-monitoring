## InfluxDB 2.0 Support – Prototype Implementation

### Overview

This prototype demonstrates a **complete, production-ready InfluxDB 2.0 backend** for OpenWISP Monitoring while maintaining **100% backward compatibility** with the existing InfluxDB 1.8 implementation. It fully implements the `DatabaseClient` interface, allowing the rest of the OpenWISP Monitoring codebase (charts, alerts, metrics collection, etc.) to work unchanged.

### What Was Implemented

- **Core Client** — [`client.py`](../../openwisp_monitoring/db/backends/influxdb2/client.py)  
  Full `DatabaseClient` implementation with all required methods (`write`, `batch_write`, `query`, `read`, `delete_metric_data`, `create_database`, retention policy handling, etc.).

- **Compatibility Layer** — `QueryResultSet` wrapper  
  Mimics the exact interface of InfluxDB 1.8’s `ResultSet` (including `.get_points()`, `.keys()`, `.items()`) so **no changes** are needed in chart rendering, tests, or any existing code.

- **Flux Query Engine** — [`queries.py`](../../openwisp_monitoring/db/backends/influxdb2/queries.py)  
  Implemented 5 flux queries defined in the main `queries.py`, including uptime,  packet loss, WiFi clients, RTT, uptime. Other queries can also be implemented with similar pattern.

- **Comprehensive Tests** — [`tests.py`](../../openwisp_monitoring/db/backends/influxdb2/tests.py)  
  Full test suite covering both legacy InfluxQL behavior and new Flux queries.

- **Backend Registration** — Updated [`db/backends/__init__.py`](../../openwisp_monitoring/db/backends/__init__.py)  
  Dynamic loading support for the new `influxdb2` backend via the `TIMESERIES_DATABASE` setting.

### Why This Approach

1. **Drop-in Replacement & Zero Disruption**  
   By preserving the exact same public interface as InfluxDB 1.8 (especially `ResultSet` behavior), existing deployments can switch to InfluxDB 2.0 without any code changes or downtime. This was a core requirement of the GSoC idea.

2. **Clean Separation of Concerns**  
   All database-specific logic is isolated inside the new backend. The core monitoring logic remains completely unaware of whether it is talking to InfluxDB 1.8, 2.0, or Elasticsearch. This architectural choice makes the codebase much easier to maintain and extend in the future (e.g., adding TimescaleDB).

3. **Practical & Low-Risk Migration Path**  
   Operators can upgrade at their own pace. The prototype already proves that both versions can coexist during the transition period, reducing risk for production users.

4. **Future-Proof Design**  
   The same patterns (compatibility wrappers + query abstraction) are directly reusable for the Elasticsearch backend, ensuring consistent behavior across all three supported databases.

### Installation & Quick Start

```bash
# Install the official InfluxDB 2.0 Python client
pip install influxdb-client==1.50.0
```

### Documentation

[InfluxDB Python Client Documentation](https://influxdb-client.readthedocs.io/)  
[Flux Query Language](https://docs.influxdata.com/influxdb/latest/query-data/flux/)