![Alt text](./images/prometheus_architecture.png?raw=true)


# Prometheus

## Concepts

Prometheus fundamentally stores all data as time series: streams of timestamped values belonging to the same metric and
the same set of labeled dimensions. Besides stored time series, Prometheus may generate temporary derived time series
as the result of queries.
 

### Metric names and labels

Every time series is uniquely identified by its metric name and optional key-value pairs called labels.

The metric name specifies the general feature of a system that is measured (e.g. http_requests_total - the total number
of HTTP requests received). It may contain ASCII letters and digits, as well as underscores and colons. It must match 
the regex [a-zA-Z_:][a-zA-Z0-9_:]*.

### Samples
Samples form the actual time series data. Each sample consists of:

* a float64 value
* a millisecond-precision timestamp

### Notation:
Given a metric name and a set of labels, time series are frequently identified using this notation:
```
<metric name>{<label name>=<label value>, ...}
```

For example, a time series with the metric name api_http_requests_total and the labels method="POST" 
and handler="/messages" could be written like this:
```
api_http_requests_total{method="POST", handler="/messages"}
```

Under the hood, the data is stored to http://opentsdb.net/overview.html


# Hands-on

## Demo
### Download
https://prometheus.io/download/

```
tar xvfz prometheus-*.tar.gz
cd prometheus-*

./prometheus --help
usage: prometheus [<flags>]

The Prometheus monitoring server
...
```

### Configuring Prometheus
```
global:
  scrape_interval:     15s
  evaluation_interval: 15s

rule_files:
  # - "first.rules"
  # - "second.rules"

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']
```
There are three blocks of configuration in the example configuration file: `global`, `rule_files`, and `scrape_configs`.

The `global` block controls the Prometheus server's global configuration. We have two options present. 
* The first, `scrape_interval`, controls how often Prometheus will scrape targets. You can override this for individual targets. In this case the global setting is to scrape every 15 seconds. 
* The `evaluation_interval` option controls how often Prometheus will evaluate rules. Prometheus uses rules to create new time series and to generate alerts.

The `rule_files` block specifies the location of any rules we want the Prometheus server to load. For now we've got no rules.

The last block, `scrape_configs`, controls what resources Prometheus monitors. Since Prometheus also exposes data about itself as an HTTP endpoint it can scrape and monitor its own health. In the default configuration there is a single job, called prometheus, which scrapes the time series data exposed by the Prometheus server. The job contains a single, statically configured, target, the localhost on port 9090. Prometheus expects metrics to be available on targets on a path of /metrics. So this default job is scraping via the URL: http://localhost:9090/metrics.

### Run Prometheus
```
./prometheus --config.file=prometheus.yml
```


### Logging and monitoring
Let us access

```
http://localhost:9090/metrics.
```
and you can see all the logs. Let us try something cooler

```
http://localhost:9090/graph
```

You can query
```
promhttp_metric_handler_requests_total
promhttp_metric_handler_requests_total{code="200"}
count(promhttp_metric_handler_requests_total)
rate(promhttp_metric_handler_requests_total{code="200"}[1m])
```

There are many other exporters to help you monitor a variety range of target 
https://prometheus.io/docs/guides/node-exporter



## Scape the app

The Prometheus monitoring system differs from most other similar software in at least one way. Instead of the 
application pushing metrics to the monitoring system, Prometheus scrapes the application via HTTP usually on 
the `/metrics/` endpoint.


### Optional Step. remove old docker images
Let us firstly stop and delete all the existing containers and images
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -aq)
docker rmi -f $(docker images -a -q)
```
and the volumes
```
docker volume prune
```
If you have run docker-compose up and would like to update the volume, please run
```
docker-compose down -v
```

### Step 1. Build and run a flask app
Now, we build all new image 
```
cd WK9_Monitoring
docker build -t jr/flask_app .
```
Let us run it and verify it works

```
docker run  -ti -p 5000:5000 -v `pwd`/src:/application jr/flask_app
```
Try to access `localhost:5000/test`, you should see `rest`

### Step 2. Spin up the infrastructure

Now, let us spin up the app with our infrastructure set up: prometheus and grafana

```
docker-compose -f docker-compose.yml -f docker-compose-infra.yml up
```
#### Check Prometheus

Hit some endpoints at `locahost:5000` and try the following query `localhost:9090/graph`
```
request_count
```
Let us return the 5-minute rate of the http_requests_total metric for the past 30 minutes, with a resolution of 1 minute.
```
rate(request_count[5m])
```
What do you need to change to make it shows the correct metrics?

Let us check out 
```
request_count{http_status="500"}
``` 
You may wonder why the request count ever go back to zero?

Because, we are running uwsgi with 5 different processes. And there is no aggregator for it and remember we scrape the 
`/metrics`, which made the distinguish of processes harder. Let us checkout `Statsd` to see a better solution.


Could you figure out how to report the request duration per 5m or p70 latency for different endpoints?

Hints:
```
rate(request_latency_seconds_sum{app_name="webapp",endpoint="/test/"}[1m])
```
and 
```
histogram_quantile(0.95, sum(rate(request_latency_seconds_bucket[5m])) by (le))
```





