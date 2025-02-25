# Kubernetes Pods

A Pod is the smallest and simplest unit in the Kubernetes object model. It represents a single instance of a running process in a cluster.

### Creating a Pod
A basic example of a Pod definition in YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
```
To create this Pod:
```bash
kubectl apply -f my-pod.yaml
```

### Viewing Pods
List all Pods in the default namespace:
```bash
kubectl get pods
```

Describe a specific Pod:
```bash
kubectl describe pod my-pod
```

### Deleting a Pod
To delete a Pod:
```bash
kubectl delete pod my-pod
```
