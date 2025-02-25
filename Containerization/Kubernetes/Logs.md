# Kubernetes Logging Guide

Logs are crucial for debugging and monitoring applications running in Kubernetes. Kubernetes provides various ways to retrieve logs from Pods, Containers, and system components.

## 1. Viewing Logs for a Pod
To check logs of a specific Pod:
```sh
kubectl logs <pod-name>
```
For multi-container Pods, specify the container name:
```sh
kubectl logs <pod-name> -c <container-name>
```
To follow real-time logs:
```sh
kubectl logs -f <pod-name>
```

## 2. Retrieving Previous Logs (For Restarted Containers)
```sh
kubectl logs --previous <pod-name>
```

## 3. Viewing System Logs (Kubelet & Cluster Components)
For nodes using systemd:
```sh
journalctl -u kubelet -f
```
For API Server, Controller Manager, and Scheduler logs:
```sh
kubectl get pods -n kube-system
kubectl logs <pod-name> -n kube-system
```

## 4. Aggregating Logs with Logging Solutions
Since Kubernetes does not store logs permanently, centralized logging solutions include:
- **Fluentd** (Log collector)
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Loki & Grafana**
- **Stackdriver (for GKE)**

---

Understanding and managing logs is vital for maintaining a healthy Kubernetes cluster. Integrating a logging solution ensures efficient monitoring and debugging.

---

