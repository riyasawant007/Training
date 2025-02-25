# Kubernetes ConfigMaps


A **ConfigMap** in Kubernetes is used to store non-sensitive configuration data separately from application code. It allows you to decouple configuration details from containerized applications, making your deployments more flexible and reusable.

## **Why Use a ConfigMap?**  
- Centralized management of configuration data.
- Avoid hardcoding environment variables inside container images.
- Can be used across multiple pods.
- Supports key-value pairs, JSON, or entire configuration files.

---

## **Creating a ConfigMap**  

### **1. Creating a ConfigMap from a YAML File**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  database_url: "postgres://user:password@db-host:5432/dbname"
  log_level: "debug"
```
Apply this ConfigMap:
```sh
kubectl apply -f configmap.yaml
```

### **2. Creating a ConfigMap from the Command Line**
```sh
kubectl create configmap my-config \
  --from-literal=database_url="postgres://user:password@db-host:5432/dbname" \
  --from-literal=log_level="debug"
```
Verify:
```sh
kubectl get configmap my-config -o yaml
```

---

## **Using ConfigMaps in Pods**

### **Using ConfigMap as Environment Variables**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-app:latest
    env:
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: database_url
    - name: LOG_LEVEL
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: log_level
```
Apply and check logs:
```sh
kubectl apply -f pod-with-configmap.yaml
kubectl logs my-pod
```

---

### **Using ConfigMap as a Volume**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-volume-pod
spec:
  volumes:
  - name: config-volume
    configMap:
      name: my-config
  containers:
  - name: my-container
    image: busybox
    command: ["sleep", "3600"]
    volumeMounts:
    - name: config-volume
      mountPath: "/etc/config"
```
This will mount the ConfigMap keys as files inside `/etc/config/`.

---

## **Deleting a ConfigMap**
```sh
kubectl delete configmap my-config
```

