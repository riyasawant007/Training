# Kubernetes Resource Requests & Limits


Resource Requests & Limits in Kubernetes allow you to control the CPU and memory allocation for your pods. This ensures that pods get the resources they need while preventing any single pod from monopolizing the cluster’s resources.

---

## 1. Resource Requests
- Define the minimum amount of CPU and memory a container requires.
- The Kubernetes scheduler uses these values to determine which node to place the pod on.

### Example: Resource Requests
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-requests-pod
spec:
  containers:
  - name: my-container
    image: nginx
    resources:
      requests:
        memory: "128Mi"
        cpu: "250m"
```

Here:
- The container **requests** 128MB of memory.
- The container **requests** 250m (0.25) CPU.

---

## 2. Resource Limits
- Define the maximum amount of CPU and memory a container can use.
- If a container exceeds its CPU limit, it will be throttled.
- If it exceeds its memory limit, it will be **terminated**.

### Example: Resource Limits
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-limits-pod
spec:
  containers:
  - name: my-container
    image: nginx
    resources:
      limits:
        memory: "256Mi"
        cpu: "500m"
```

Here:
- The container **cannot exceed** 256MB of memory.
- The container **cannot exceed** 500m (0.5) CPU.

---

## 3. Combining Requests & Limits
Best practice is to define both **requests** and **limits** to balance cluster resource allocation.

### Example: Combining Requests & Limits
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-managed-pod
spec:
  containers:
  - name: my-container
    image: nginx
    resources:
      requests:
        memory: "128Mi"
        cpu: "250m"
      limits:
        memory: "512Mi"
        cpu: "1"
```

Here:
- The container requests **128Mi** memory and **250m** CPU.
- It **cannot exceed** **512Mi** memory and **1 CPU**.

---

## 4. Resource Requests & Limits in Deployments
For real-world applications, resource limits should be defined at the **Deployment** level.

### Example: Deployment with Resource Limits
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource-managed-deployment
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
        resources:
          requests:
            memory: "200Mi"
            cpu: "300m"
          limits:
            memory: "1Gi"
            cpu: "1"
```

---

## 5. Checking Resource Usage
You can monitor pod resource usage using:
```sh
kubectl describe pod <pod-name>
kubectl top pod
kubectl top node
```

---

- **Requests** ensure a pod gets the minimum required resources.
- **Limits** prevent a pod from over-consuming CPU and memory.
- Setting both **requests & limits** optimizes resource allocation.

