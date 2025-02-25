# Kubernetes Deployments
A Deployment provides declarative updates for Pods and ReplicaSets. It ensures that a specified number of Pod replicas are running at all times.

### Creating a Deployment
A basic Deployment definition:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: nginx
        ports:
        - containerPort: 80
```
To apply this Deployment:
```bash
kubectl apply -f my-deployment.yaml
```

### Viewing Deployments
```bash
kubectl get deployments
```

### Scaling a Deployment
```bash
kubectl scale deployment my-deployment --replicas=3
```

### Deleting a Deployment
```bash
kubectl delete deployment my-deployment
```