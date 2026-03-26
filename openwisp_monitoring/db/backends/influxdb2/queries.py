"""
InfluxDB 2.x Flux queries for monitoring charts.
These queries follow the Flux query language syntax.
"""

chart_query = {
    "uptime": {
        "influxdb2": (
            'from(bucket: "{bucket}")'
            ' |> range(start: {time_start})'
            ' |> filter(fn: (r) => r._measurement == "{key}")'
            ' |> filter(fn: (r) => r.content_type == "{content_type}")'
            ' |> filter(fn: (r) => r.object_id == "{object_id}")'
            ' |> filter(fn: (r) => r._field == "{field_name}")'
            ' |> aggregateWindow(every: 1d, fn: mean)'
            ' |> map(fn: (r) => ({{r with _value: r._value * 100}}))'
        )
    },
    "packet_loss": {
        "influxdb2": (
            'from(bucket: "{bucket}")'
            ' |> range(start: {time_start})'
            ' |> filter(fn: (r) => r._measurement == "{key}")'
            ' |> filter(fn: (r) => r.content_type == "{content_type}")'
            ' |> filter(fn: (r) => r.object_id == "{object_id}")'
            ' |> filter(fn: (r) => r._field == "loss")'
            ' |> aggregateWindow(every: 1d, fn: mean)'
        )
    },
    "rtt": {
        "influxdb2": (
            'from(bucket: "{bucket}")'
            ' |> range(start: {time_start})'
            ' |> filter(fn: (r) => r._measurement == "{key}")'
            ' |> filter(fn: (r) => r.content_type == "{content_type}")'
            ' |> filter(fn: (r) => r.object_id == "{object_id}")'
            ' |> filter(fn: (r) => r._field =~ /^rtt_(avg|max|min)$/)'
            ' |> aggregateWindow(every: 1d, fn: mean)'
        )
    },
    "wifi_clients": {
        "influxdb2": (
            'from(bucket: "{bucket}")'
            ' |> range(start: {time_start})'
            ' |> filter(fn: (r) => r._measurement == "{key}")'
            ' |> filter(fn: (r) => r.content_type == "{content_type}")'
            ' |> filter(fn: (r) => r.object_id == "{object_id}")'
            ' |> filter(fn: (r) => r.ifname == "{ifname}")'
            ' |> filter(fn: (r) => r._field == "{field_name}")'
            ' |> aggregateWindow(every: 1d, fn: count)'
        )
    },
    "traffic": {
        "influxdb2": (
            'from(bucket: "{bucket}")'
            ' |> range(start: {time_start})'
            ' |> filter(fn: (r) => r._measurement == "{key}")'
            ' |> filter(fn: (r) => r.content_type == "{content_type}")'
            ' |> filter(fn: (r) => r.object_id == "{object_id}")'
            ' |> filter(fn: (r) => r.ifname == "{ifname}")'
            ' |> filter(fn: (r) => r._field =~ /^(tx_bytes|rx_bytes)$/)'
            ' |> aggregateWindow(every: 1d, fn: sum)'
        )
    },
}

# Mapping of metric field names to Flux query expressions
field_mappings = {
    "uptime": "uptime",
    "packet_loss": "loss",
    "rtt": "rtt_avg",
    "traffic": ["tx_bytes", "rx_bytes"],
    "wifi_clients": "num_clients",
}
