## Metrics and metric types

For our purposes, a __metric__ is an observed value of a certain quantity at a given point in time. The total of number hits on a blog post, the total number of people attending a talk, the number of times the data was not found in the caching system, the number of logged-in users on your website—all are examples of metrics.

They broadly fall into three categories:

### Counters

A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase
or be reset to zero on restart. For example, you can use a counter to represent the number of requests served, tasks
completed, or errors.

Consider your personal blog. You just published a post and want to keep an eye on how many hits it gets over time, 
a number that can only increase. This is an example of a counter metric. Its value starts at 0 and increases during
 the lifetime of your blog post. Graphically, a counter looks like this:
![Alt text](./images/counter-graph.png?raw=true)

### Gauges
A gauge is a metric that represents a single numerical value that can arbitrarily go up and down.

Gauges are typically used for measured values like temperatures or current memory usage, but also "counts" that can go
 up and down, like the number of concurrent requests.
 
![Alt text](./images/gauge-graph.png?raw=true)
![Alt text](./images/gauge.png?raw=true)
A gauge's value usually has a ceiling and a floor in a certain time window.

### Histograms and timers
A histogram (as Prometheus calls it) or a timer (as StatsD calls it) is a metric to track sampled observations. 
A histogram samples observations (usually things like request durations or response sizes) and counts them in 
configurable buckets. It also provides a sum of all observed values.
![Alt text](./images/histogram-graph.png?raw=true)

```
http_request_duration_seconds_bucket{le="0.5"} 0
http_request_duration_seconds_bucket{le="1"} 1
http_request_duration_seconds_bucket{le="2"} 2
http_request_duration_seconds_bucket{le="3"} 3
http_request_duration_seconds_bucket{le="5"} 3
http_request_duration_seconds_bucket{le="+Inf"} 3
http_request_duration_seconds_sum 6
http_request_duration_seconds_count 3
```


