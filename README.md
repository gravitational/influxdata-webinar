# Installing of all components
### InfluxDB

```bash
helm install --name=influxdb --values=influxdb-values.yaml stable/influxdb
```

### Telegraf
```bash
helm install --name=telegraf --values=telegraf-values.yaml stable/telegraf
```

### Kapacitor
```bash
helm install --name=kapacitor --values=kapacitor-values.yaml stable/kapacitor
```

### Chronograf
```bash
helm install --values=chronograf-values.yaml stable/chronograf
```

### Check all components
#### InfluxDB: Check that we have new measurements in telegraf database
```bash
kubectl exec -ti $(kubectl get po -l app=influxdb-influxdb -o jsonpath='{.items[0].metadata.name}') influx -- -database telegraf -execute "show measurements"
```

#### Kapacitor: received points should have non-zero value for each measurement
```bash
kubectl exec -ti $(kubectl get pods --namespace default -l app=kapacitor-kapacitor -o jsonpath='{ .items[0].metadata.name }') -- kapacitor stats ingress | ( read -r head; printf '%s\n' "$head"; grep telegraf )
```

#### Chronograf: configure sources and check data
```bash
kubectl port-forward --namespace default $(kubectl get pods --namespace default -l app=chronograf-chronograf -o jsonpath='{ .items[0].metadata.name }') 8888
```
Go to `http://locahost:8888` and configure
| Name | Value |
| ---- | ----- |
| Connection string | http://chronograf-chronograf.default.svc:8086 |
| Username | admin |
| Password | passw0rd |
| Telegraf database | telegraf |

And there in Host List you can show autogenerated graphs for all collected metrics.