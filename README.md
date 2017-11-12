# Testcases for Telekube alerting system

### Check enabled Kapacitor's tasks

``` bash
kubectl --namespace=kube-system exec -ti $(kubectl --namespace=kube-system get po -l component=kapacitor -ojsonpath='{.items[0].metadata.name}') -c kapacitor -- kapacitor list tasks
```

### Turning off IPV4 forwarding

```bash
sysctl -w net.ipv4.ip_forward=0
```

```bash
kubectl --namespace=kube-system exec -ti $(kubectl --namespace=kube-system get po -l component=kapacitor -ojsonpath='{.items[0].metadata.name}') -c kapacitor -- kapacitor show networking_params
```

### Jumping into influxDB

```
kubectl --namespace=kube-system exec -ti $(kubectl --namespace=kube-system get po -l component=influxdb -ojsonpath='{.items[0].metadata.name}') -c influxdb -- /bin/sh -c "influx --username=grafana --password=grafana --database=k8s"
```


### Show Pod High CPU task

``` bash
kubectl --namespace=kube-system exec -ti $(kubectl --namespace=kube-system get po -l component=kapacitor -ojsonpath='{.items[0].metadata.name}') -c kapacitor -- kapacitor show pod-high-cpu
```
