# Autoscaling in Kubernetes
This is the handson to show you use kubectl tools to autoscale the application.

## Kind and Kubectl
kind is a tool for running local Kubernetes clusters using Docker container “nodes”.
https://kind.sigs.k8s.io/

# Prerequisite 

Please install kind, kubectl, and go if you haven't

* https://kind.sigs.k8s.io/docs/user/quick-start/
* https://kubernetes.io/docs/tasks/tools/install-kubectl/
* https://golang.org/doc/install

## create the cluster
```
kind create cluster
```
## verify the cluster

```
kind get clusters
```

```
kubectl cluster-info
```

You should be able to see

![Alt text](../images/kind-kubectl.png?raw=true)

![Alt text](../images/kube_history.png?raw=true)
![Alt text](../images/cluster.png?raw=true)
![Alt text](../images/node.png?raw=true)
![Alt text](../images/pods.png?raw=true)


# Autoscaling
```
git clone https://github.com/dockersamples/example-voting-app
```
Go to the clone folder and create namespace
```
kubectl create namespace vote                                                           
```
You should see
```
namespace/vote created
```

Now let us create the cluster
```
kubectl create -f k8s-specifications/                                                   
```
It should return
```
deployment.apps/db created
service/db created
deployment.apps/redis created
service/redis created
deployment.apps/result created
service/result created
deployment.apps/vote created
service/vote created
deployment.apps/worker created
```

Check the status
```
kubectl get pods --namespace=vote --output=wide
kubectl get services --namespace=vote
```
You will probably see an error for postgres `CrashLoopBackOff`

Let us check the error
```
kubectl logs <NAME> --namespace=vote
```
This was because a recent upgrade of postgres and we have to pass in the postgres password, even it is the default one.
Let us specify the password by adding the following in the `db-deployment.yml`
```
        env:
        - name: POSTGRES_PASSWORD
          value: password
```
You should also see some errors here:
```
kubectl describe pods --namespace=vote
```

Let us stop everything
``` 
kubectl delete deployments --all --namespace=vote
kubectl delete services --all --namespace=vote
```
and restart them:
```
kubectl create -f k8s-specifications/
```

Since we are not on google cloud and don't have a loadbalancer setup, we can port forward to access our app:
```
kubectl port-forward svc/vote --namespace=vote 5000:5000
```

You should be able to visit http://localhost:5000, which is the vote service.

![Alt text](../images/app-localhost.png?raw=true)


```
kubectl port-forward svc/result --namespace=vote 5001:5001
```

You should be able to visit http://localhost:5001, which is the result service.

![Alt text](../images/app-result.png?raw=true)

Also, try to understand what does these mean:
```
kubectl get pods --namespace=vote --output=wide
kubectl get svc --namespace=vote
kubectl get deployments --namespace=vote

```

Note: pod (po), service (svc), replicationcontroller (rc), deployment (deploy), replicaset (rs) 
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get

Try to delete a pod and see if it gets deleted:
```
What command should we use?
```

You can also try to see the log, which is useful if something is wrong, e.g.
```
kubectl logs svc/vote -n vote
```

## Manual Scaling
You can set the replicas to higher number and it should generate more nodes for each deployment.
You can also scale the nodes manually. Are you able to find the command?

check the current replicas
```bash
kubectl get rs -n vote
```
manually scale the replica for vote deployment
```bash
kubectl scale --replicas=3 deployment/vote -n vote
```
check the replica for the deployment and also check the vote detail
```
kubectl get deploy -n vote
```
```
kubectl describe deploy/vote -n vote
```
so what is the big deal of setting replica?

## Auto Scaling
Let us set the Auto Scaling Policy for our nodes
```
kubectl autoscale deployment vote --namespace=vote --cpu-percent=50 --min=1 --max=10
```
check the settings:
```
kubectl get hpa --namespace=vote
```

Let us check what is wrong?
Did you see `<unknown>/50%`?
```
kubectl describe hpa --namespace=vote
```
We will see the error and warning message as below.

![Alt text](../images/horizonal-pod-autoscaler-error.png?raw=true)

To fix it, we need to spin up metric server. It is a app to be added into the app
1. Clone metrics-server with `git clone https://github.com/kubernetes-sigs/metrics-server`
2. Edit `manifests/base/deployment.yaml` and add these:
```
containers:
- name: metrics-server
    image: k8s.gcr.io/metrics-server-amd64:v0.3.1
    command:
      - /metrics-server
      - --kubelet-insecure-tls
      - --kubelet-preferred-address-types=InternalIP
``` 
![Alt text](../images/edit-yaml-metricserver.png?raw=true)

3 . Create the resource
```
kubectl create -f manifests/base/deployment.yaml
```

4 . Check Metric Server status

```
kubectl get pods -n kube-system
kubectl logs <pod> -n kube-system 
```
You should be able to see metric server running

5 . Go to example-voting-app repo and Delete the old hpa:

```
kubectl delete hpa --all --namespace=vote
```

6 . Stop the current app:
```
kubectl delete -f k8s-specifications/
``` 
7 . Add the following to `vote-deployment.yaml` under container
```
        resources:
          limits:
            cpu: 20m
          requests:
            cpu: 10m
```

See more https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/

8 . Recreate everything:
```
kubectl create -f k8s-specifications/
``` 
9 . Recreate asg rule:
```
kubectl autoscale deployment vote --namespace=vote --cpu-percent=50 --min=1 --max=10
```
In the beginning, you will still see the metric error, but after a couple of mins, then you should see
```
kubectl get hpa --namespace=vote                                                        
NAME   REFERENCE         TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
vote   Deployment/vote   xxx%/50%     1         10        1          38s
```

- Q: Do you know why it is like that?

10 . Test scale

We can give a low cpu-percent so it will scale up. Or more interestingly, we can increase the load
in the real world, so we will see how the autoscaler reacts to the increased load.

We will send an infinite loop of queries to localhost:5000.

run it in a different terminal:
```
./generate-load.sh
```

After a minute or so, you can stop the load script, and check the hpa again.

Note: If the load is lower, then it can also scale down.
```
kubectl describe hpa --namespace=vote
```
You will find it automatically scale up and down

![Alt text](../images/scale-up-down.png?raw=true)

```
kubectl get po -n vote
```
You will find more pods for vote

![Alt text](../images/auto-scaling-pod2.png?raw=true)

It is required to balance the auto-scaling policy with the resource limit.

See more https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

## Something about Resource limit.

- Q: What if you specify a CPU request that is too big for your Nodes,

Try to edit
```
    resources:
      limits:
        cpu: "100"
      requests:
        cpu: "100"
```
Stop/restart again

```
kubectl get pods -n vote
NAME                      READY   STATUS             RESTARTS   AGE
db-6789fcc76c-bb8hc       1/1     Running            0          21s
redis-554668f9bf-qzv58    1/1     Running            0          21s
result-79bf6bc748-cxwf4   1/1     Running            0          21s
vote-bfb5bbc9d-m4kfr      0/1     Pending            0          21s
worker-dd46d7584-gcbbk    0/1     CrashLoopBackOff   1          21s
```
The output shows that the Pod status for vote is Pending. That is, the Pod has not been scheduled to run on any Node, and it will remain in the Pending state indefinitely

```
kubectl describe pod vote-bfb5bbc9d-m4kfr -n vote
```

then you will see error as below
```
Events:
  Type     Reason            Age                  From               Message
  ----     ------            ----                 ----               -------
  Warning  FailedScheduling  14s (x5 over 3m17s)  default-scheduler  0/1 nodes are available: 1 Insufficient cpu.
```

- Q: What if you do not specify a CPU limit?
If you do not specify a CPU limit for a Container, then one of these situations applies:

1. The Container has no upper bound on the CPU resources it can use. The Container could use all of the CPU resources available on the Node where it is running.

2. The Container is running in a namespace that has a default CPU limit, and the Container is automatically assigned the default limit. Cluster administrators can use a LimitRange to specify a default value for the CPU limit.

- Motivation for CPU requests and limits 
By configuring the CPU requests and limits of the Containers that run in your cluster, you can make efficient use of the CPU resources available on your cluster Nodes. By keeping a Pod CPU request low, you give the Pod a good chance of being scheduled. By having a CPU limit that is greater than the CPU request, you accomplish two things:

The Pod can have bursts of activity where it makes use of CPU resources that happen to be available.
The amount of CPU resources a Pod can use during a burst is limited to some reasonable amount.

## Other commands and some references

```
kubectl get deployments
kubectl get deployments --namespace=vote
```
We need to delete the deployments before delete all the pods
```
kubectl delete deployment hello-world
kubectl delete service hello-world
kubectl delete --all pods
```
https://itnext.io/starting-local-kubernetes-using-kind-and-docker-c6089acfc1c0

