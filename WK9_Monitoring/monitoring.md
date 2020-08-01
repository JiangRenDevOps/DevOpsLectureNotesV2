# Monitoring Basics

Often, in SRE interviews, the interviewer may ask you about how would you monitor the following system 
and trouble shoot a latency issue?

![Alt text](images/voting_system_example.png?raw=true)

If we break this question down, there are literally two questions:
* 1. how do you design the monitoring systems? What metrics are you going to look at?
   
* 2. are you able to troubleshooting the latency problem of this system?

Okay, before we answer the first question let us look at the monitoring from a top down approach

# What is monitoring?

Collecting, processing, aggregating, and displaying real-time quantitative data about a system, such as query counts 
and types, error counts and types, processing times, and server lifetimes.

# Monitoring Types

```
whitebox
blackbox
```

## White-box monitoring
Monitoring based on metrics exposed by the internals of the system, including logs, interfaces like the Java Virtual Machine Profiling Interface, or an HTTP handler that emits internal statistics.

Metrics: 
* Prometheus + Grafana
* Datadog (Commercial)
* SignalFx (Commercial)

Log Monitoring:
* Kibana  (Open Source/Commercial)
* Splunk  (Commercial)

## Black-box monitoring
Testing externally visible behavior as a user would see it.

Synthetic monitoring
* Selenium Webdriver
* Cypress
* New Relic (Commercial)

Load-testing
* Gatling
* Locust 

# Why monitor?
* Analyzing long-term trends
   * How big is my database and how fast is it growing? 
      * How quickly is my daily-active user count growing?
      * Are they caused by abusive, bug in the code or a real growth?
      
* Comparing over time or experiment groups
   * Are queries faster with Acme Bucket of Bytes 2.72 versus Ajax DB 3.14? 
   * How much better is my memcache hit rate with an extra node? 
   * Is my site slower than it was last week?
   
* Alerting
   * Something is broken, and somebody needs to fix it right now!
   * Or, something might break soon, so somebody should look soon.
   
* Building dashboards
   * Dashboards should answer basic questions about your service, 
     and normally include some form of the four golden signals
     
* Debugging
   * Our latency just shot up; what else happened around the same time?

## SRE - 4 Golden Signals

### 1. Latency

The time it takes to serve a request.

#### Visbility
Backend Latency: 
* The latency to serve an API (access log)
   - by web nodes
   - by log level
   - by method
   - by user agent
   - by environment (dev, stg, prod)
   - by region (prod-east, prod-west)
   - by customer* (be careful with cardinality)
   - by microservices (if there is any)

* DB time (application logging)
   - by logger
   - by log level

Frontend Latency:
* Page/Component loading time 
* TTI (Time to interaction)


#### Should we look at the max or the average?
For latency, we shall look at it statistically with percentile e.g. p50 (median), p75 (~average), p90 (the majority)

Sometimes, we need to now about 99 percentile to make sure we are not missing some outliers

For example, the 50th percentile is the value below which 50% of the observations may be found.
https://en.wikipedia.org/wiki/Percentile


#### Error latency is also important

It’s important to distinguish between the latency of successful requests and 
the latency of failed requests. For example, an HTTP 500 error triggered due to loss of connection to a database or 
other critical backend might be served very quickly; however, as an HTTP 500 error indicates a failed request, 
factoring 500s into your overall latency might result in misleading calculations. On the other hand, a slow error is 
even worse than a fast error! Therefore, it’s important to track error latency, as opposed to just filtering out errors.

#### Trouble shooting
If it takes too long: 
* Do we have network issue/connectivity issue? 
* Was this reported by a single customer?
    * cross-region issue
    * other connectivity issue (if our application does not show a high latency)
* Is our DNS or CDN having issue?
* Is there any function of our application not efficient?
* Is our DB under pressure?



### 2. Traffic

A measure of how much demand is being placed on your system.

* Network In (Load Balancer, Application, Microservices, Cache and DB)
* Network Out (Load Balancer, Application, Microservices, Cache and DB)
* HTTP Request Rate (by region, by status_code, etc...) 
* Transactions per second (Cache, Queue and DB)

For a web service, this measurement is usually HTTP requests per second, 
perhaps broken out by the nature of the requests (e.g. static versus dynamic content). 

For a key-value storage system, this measurement might be transactions and retrievals per second.

### 3. Errors

The rate of requests that fail, either explicitly (e.g., HTTP 500s), 
implicitly (for example, an HTTP 200 success response, but coupled with the wrong content), 
or by policy (for example, "If you committed to one-second response times, any request over one second is an error"). 

* Error rate = Error/(Error+Success) (Sidecar, Microservice, API, DB etc...)
   * 5xx Error Rate (Application Error)
   * 4xx Error Rate (User generated Error)

* The size of Dead Letter Queue (Failed messages that are dumped into message queue) 
   
#### Tips
Where protocol response codes are insufficient to express all failure conditions, secondary (internal) protocols may
be necessary to track partial failure modes. Monitoring these cases can be drastically different: catching HTTP 500s
at your load balancer can do a decent job of catching all completely failed requests, while only end-to-end system
tests can detect that you’re serving the wrong content.


### 4. Saturation

How "full" your service is.
 
A measure of your system fraction, emphasizing the resources that are most constrained (e.g., in a memory-constrained 
system, show memory; in an I/O-constrained system, show I/O). Note that many systems degrade in performance before they
achieve 100% utilization (typically 60%-80%), so having a utilization target is essential.

In complex systems, saturation can be supplemented with higher-level load measurement: 
can your service properly handle double the traffic, handle only 10% more traffic, 
or handle even less traffic than it currently receives? For very simple services that have no parameters that alter 
the complexity of the request (e.g., "Give me a nonce" or "I need a globally unique monotonic integer") that rarely
change configuration, a static value from a load test might be adequate. As discussed in the previous paragraph, 
however, most services need to use indirect signals like CPU utilization or network bandwidth that have a known 
upper bound. Latency increases are often a leading indicator of saturation. Measuring your 99th percentile response
time over some small window (e.g., one minute) can give a very early signal of saturation.

Finally, saturation is also concerned with predictions of impending saturation, such as "It looks like your database
will fill its hard drive in 4 hours."

System Level
* CPU Utilisation
* Memory Utilisation
* Disk Utilisation
* I/O Utilisation

Application Level
* Thread Pool Saturation
* Message Queue Saturation

The key here: try to understand the system constrain first by running some load testing or fundamental analysis.

# Symptoms Versus Causes

#### Your monitoring system should address two questions: what’s broken, and why?

The "what’s broken" indicates the symptom; the "why" indicates a (possibly intermediate) cause.
```
Symptom	                               |    Cause                         
I’m serving HTTP 500s or 404s          |    Database servers are refusing connections
                                       |
My responses are slow                  |    CPUs are overloaded by a bogosort, or an Ethernet cable is crimped under a
                                       |    rack, visible as partial packet loss

Users in Antarctica aren’t 
receiving animated cat GIFs            |    Your Content Distribution Network hates scientists and felines, 
                                       |    and thus blacklisted some client IPs

Private content is world-readable      |    A new software push caused ACLs to be forgotten and allowed all requests
```

However, In read world, it can be more complicated than the above example.
e.g. 
* multiple metrics could be just the symptoms
   *  e.g. tomcat thread saturated, multiple nodes become unhealthy, but the main cause can happens at the garbage 
      collection.
      
* entangled dependencies
   *  e.g. when the alert of my application gets triggered, it could be a micro-service's problem or AWS may have
    an ongoing problem.      

Recap:
* Black-box monitoring is symptom-oriented and represents active—not predicted—problems: "The system isn’t working 
correctly, right now." 

* White-box monitoring depends on the ability to inspect the innards of the system, such as logs or HTTP endpoints, 
with instrumentation. White-box monitoring therefore allows detection of imminent problems, failures masked by retries,
and so forth.

There are three approaches that you could use:

### Problem Statement Approach
1. What makes you think there is a performance problem?
2. Has this system ever performed well?
3. What has changed recently? (Software? Hardware?
Load?)
4. Can the performance degradation be expressed in
terms of latency or run time?
5. Does the problem affect other people or applications (or
is it just you)?
6. What is the environment? Software, hardware,
instance types? Versions? Configuration?

### Workload Characterization Approach	
1. Who is causing the load? PID, UID, IP addr, ...
2. Why is the load called? code path, stack trace
3. What is the load? IOPS, tput, type, r/w
4. How is the load changing over time? 

### The USE Approach
1. Utilization: busy time
2. Saturation: queue length or queued time 
3. Error: error logs


## Other Tips

* Choosing an Appropriate Resolution for Measurements

    Different aspects of a system should be measured with different levels of granularity. For example:

    * Observing CPU load over the time span of a minute won’t reveal even quite long-lived spikes that drive high tail latencies.
    * On the other hand, for a web service targeting no more than 9 hours aggregate downtime per year (99.9% annual uptime), probing for a 200 (success) status more than once or twice a minute is probably unnecessarily frequent.
    * Similarly, checking hard drive fullness for a service targeting 99.9% availability more than once every 1–2 minutes is probably unnecessary.

* Most of the alerts are caused by changes in the system; double check them.
  * Code release
  * Database upgrade
  * Configuration changes
  * Performance tuning
  * Hardware (AWS) maintenance
  * Traffic increase

* Logs are your best friend, but logs may not always help.
  * Use metrics as the indicator and use logs to locate the true problem.
  * Sometimes you may need to use performance profiler such as CodeGuru to get the heapdump, threaddump or flamechart
  
* Monitoring for the Long Term
  * (Homework) try to understand what are SLI, SLO and SLAs? 
  * What are the trends/relations between e.g. CPU increase and MAU increase?   
  
Now, would you be able to answer the first question?



## Linux system stats breakdown
### 1. vmstat
vmstat reports describe the current state of a Linux system. Information regarding the running state of a system is useful when diagnosing performance related issues.
```
vmstat [interval] [count]
```

```
vagrant@linux:/home/vagrant$ vmstat 1 20
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0   1804 296112 132244 1207392    0    0    21   119   53  130  0  0 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   98  217  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0  106  243  0  1 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   70  220  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   66  215  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   66  221  0  1 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   62  230  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   73  235  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   65  244  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   73  241  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   80  243  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0  109  231  0  0 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   84  225  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   94  285  1  0 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   66  234  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   76  257  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   65  237  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   65  247  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   75  250  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0  114  327  0  0 100  0  0
```
more readable: convert the number to Megabytes e.g. 1M=1000KB=1000000B
```
vagrant@linux:/home/vagrant$ vmstat -S m 1 10
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      1    303    135   1236    0    0    21   118   53  130  0  0 99  0  0
 0  0      1    303    135   1236    0    0     0     0  103  248  0  1 100  0  0
 0  0      1    303    135   1236    0    0     0     0   97  239  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   91  249  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0  106  272  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0  113  252  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   91  233  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   92  246  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   86  234  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   96  266  0  0 100  0  0
```
for 1M=1024KB, use `-S M` instead.


####Procs
Permalink
The procs data reports the number of processing jobs waiting to run and allows you to determine if there are processes “blocking” your system from running smoothly.
    
The `r` column displays the total number of processes waiting for access to the processor. 

The `b` column displays the total number of processes in a “sleep” state.
    
These values are often 0.

####MemoryPermalink
The information displayed in the memory section provides the same data about memory usage as the command `free -m`.

The `swpd` or “swapped” column reports how much memory has been swapped out to a swap file or disk. 

The `free` column reports the amount of unallocated memory. 

The `buff` or “buffers” column reports the amount of allocated memory in use. 

The `cache` column reports the amount of allocated memory that could be swapped to disk or unallocated if the resources are needed for another task.

####SwapPermalink
The swap section reports the rate that memory is sent to or retrieved from the swap system. By reporting “swapping” separately from total disk activity, vmstat allows you to determine how much disk activity is related to the swap system.

What is swap? see swap.md


The `si` column reports the amount of memory that is moved from swap to “real” memory per second. 

The `so` column reports the amount of memory that is moved to swap from “real” memory per second.

####I/OPermalink
The `io` section reports the amount of input and output activity per second in terms of blocks read and blocks written.

The `bi` column reports the number of blocks received, or “blocks in”, from a disk per second. The bo column reports the number of blocks sent, or “blocks out”, to a disk per second.

#### SystemPermalink
The system section reports data that reflects the number of system operations per second.

The `in` column reports the number of system interrupts per second, including interrupts from system clock. 

The `cs` column reports the number of context switches that the system makes in order to process all tasks.

CPUPermalink
The `cpu` section reports on the use of the system’s CPU resources. The columns in this section always add to 100 and reflect “percentage of available time”.


The `us` column reports the amount of time that the processor spends on userland tasks, or all non-kernel processes. 

The `sy` column reports the amount of time that the processor spends on kernel related tasks. 

The `id` column reports the amount of time that the processor spends idle. 

The `wa` column reports the amount of time that the processor spends waiting for IO operations to complete before being able to continue processing tasks.

### 2.uptime
```
vagrant@linux:/home/vagrant$ uptime
 15:22:38 up  5:26,  2 users,  load average: 0.00, 0.04, 0.06
```
uptime gives a one line display of the following information. The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes.

Load > # of CPUs, may mean CPU saturation.

### 3.top (htop)
System and per-process interval summary: 
```
Tasks: 142 total,   1 running, 106 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.2 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2041120 total,   295024 free,   406084 used,  1340012 buff/cache
KiB Swap:  2097148 total,  2095344 free,     1804 used.  1453912 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
17229 root      20   0  907880  44200  25148 S   0.7  2.2   0:18.58 containerd
19715 vagrant   20   0   41804   3696   3072 R   0.3  0.2   0:00.01 top
    1 root      20   0  159956   9080   6504 S   0.0  0.4   0:04.49 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq
    7 root      20   0       0      0      0 S   0.0  0.0   0:00.28 ksoftirqd/0
    8 root      20   0       0      0      0 I   0.0  0.0   0:00.58 rcu_sched
    ...
```
• %CPU is summed across all CPUs
• Can miss short-lived processes (atop won’t)
• Can consume noticeable CPU to read /proc

