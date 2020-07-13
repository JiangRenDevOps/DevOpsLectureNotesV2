# What is system test?

System Testing means testing the system as a whole. All the modules/components are integrated in order to verify if the system works as expected or not.

System Testing is done after Integration Testing. This plays an important role in delivering a high-quality product.


# Focus area
* External interfaces
* Multiprogram and complex functionalities
* Security
* Recovery
* Performance
* Operator and user’s smooth interaction with the system
* Installability
* Documentation
* Usability
* Load/Stress

# More to read
* It is not as simple. 
* It may involve multiple months of iterations
* From plan, implementation, test, report to action taken

More to read:
https://www.softwaretestinghelp.com/system-testing/

# Hands-On - Load Test/Perf Test with Locust

I) Install locust

```
pip3 install locust
```

II) Enter the right folder

```
cd hands_on/load_test_demo
```

III) Open another terminal and spin up EasyCRM

IV) Run locust

```
locust -f load_test_easy_crm.py
```

V) Open a browser `localhost:8090` and fill in the following values
![Alt text](../../images/locust_setup.png?raw=true)

VI) Start swarming and you should see the following

![Alt text](../../images/locust_demo.png?raw=true)

You can also check the success rate and latency
![Alt text](../../images/locust_stats.png?raw=true)

### Open Questions

Could you fill in different values to figure out the limitation of these endpoints?

What can you do to uplift the limitation?

What else can you figure out with this test?


# Other load test tool comparison

Gatling vs Loader.io vs Locust

https://stackshare.io/stackups/gatling-vs-loader-io-vs-locust
