# Kubernetes Init Containers

## **What are Init Containers?**
Init Containers are specialized containers in a Kubernetes pod that run before the main application containers. They help set up necessary conditions, such as initializing databases, fetching secrets, or waiting for a service to become available before the primary container starts.

### **Key Features:**
- Run **before** the main application container.
- Execute in sequence; each must complete successfully before the next starts.
- Have their own image and environment separate from the main container.

---

## **Example Use Case**
Scenario: A web application needs a PostgreSQL database to be ready before it starts.

### **YAML Configuration: Init Container in a Pod**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-container-demo
spec:
  initContainers:
  - name: wait-for-db
    image: busybox
    command: ['sh', '-c', 'until nc -z db-service 5432; do echo waiting for db; sleep 2; done;']
  containers:
  - name: app-container
    image: nginx
    ports:
    - containerPort: 80
```


1. **`initContainers`**: Defines an Init Container (`wait-for-db`) that checks if `db-service` is available on port `5432`.
2. **`containers`**: The main `nginx` container starts only after the Init Container completes.

---

## **Deployment & Testing**

### **Step 1: Apply the YAML File**
```bash
kubectl apply -f init-container.yaml
```

### **Step 2: Check the Pod Status**
```bash
kubectl get pods
```
- Initially, the pod will show `Init:0/1`, indicating the Init Container is running.
- Once the Init Container completes successfully, the main container transitions to `Running`.

### **Step 3: Verify Logs**
```bash
kubectl logs init-container-demo -c wait-for-db
```
This displays logs from the Init Container, showing its progress in waiting for the database service.

---

## **Why Use Init Containers?**
✅ Ensures dependencies are met before the main container starts.

✅ Keeps the main application lightweight by moving setup tasks to separate containers.

✅ Improves container startup reliability and consistency.

---

