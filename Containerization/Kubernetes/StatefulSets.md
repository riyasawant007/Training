# StatefulSets in Kubernetes

A **StatefulSet** is a Kubernetes workload API object used to manage **stateful applications**. It ensures stable identities, persistent storage, and ordered pod management, making it ideal for databases and distributed applications.

---

## Key Features
- **Stable Pod Names**: Pods are assigned predictable names (`podname-0`, `podname-1`, etc.).
- **Ordered Deployment & Scaling**: Pods are created and deleted in a defined sequence.
- **Stable Network Identity**: Each pod retains a unique DNS name.
- **Persistent Storage**: Each pod gets its own **PersistentVolumeClaim (PVC)**.

---

## Headless Service (Required for StatefulSet)
Before creating a StatefulSet, define a **headless service** to ensure stable networking:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  clusterIP: None
  selector:
    app: mysql
  ports:
    - port: 3306
      targetPort: 3306
```

---

## Creating a StatefulSet

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: "mysql"
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:latest
          ports:
            - containerPort: 3306
          env:
            - name: MYSQL_ROOT_PASSWORD
              value: "rootpassword"
          volumeMounts:
            - name: mysql-storage
              mountPath: /var/lib/mysql
  volumeClaimTemplates:
    - metadata:
        name: mysql-storage
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

---

## Deployment and Verification
Apply the StatefulSet and verify its status:

```sh
kubectl apply -f mysql-statefulset.yaml
kubectl get pods -l app=mysql
kubectl get pvc
kubectl get statefulset mysql
```

---

## Scaling a StatefulSet
To scale the StatefulSet up or down:

```sh
kubectl scale statefulset mysql --replicas=5
```

---

## Deleting a StatefulSet
Deleting a StatefulSet does **not** delete associated volumes:

```sh
kubectl delete statefulset mysql --cascade=orphan
kubectl delete pvc -l app=mysql
```

---

## Use Cases
✅ Databases (PostgreSQL, MySQL, Cassandra)  
✅ Applications needing **stable identities and persistent storage**

---

StatefulSets provide a robust way to manage stateful workloads in Kubernetes by ensuring stable identities, persistent storage, and ordered pod deployment. They are essential for database management and other applications requiring data persistence.

---

