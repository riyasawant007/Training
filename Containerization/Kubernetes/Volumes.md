# Volumes - Managing Persistent Data
Kubernetes **Volumes** provide a way to persist data beyond the lifetime of a pod.

### Creating a Pod with a Volume
Create a YAML file named `volumes.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-volume-pod
spec:
  volumes:
    - name: my-storage
      emptyDir: {}
  containers:
    - name: my-container
      image: nginx:latest
      volumeMounts:
        - mountPath: /usr/share/nginx/html
          name: my-storage
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: "/mnt/data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
---
apiVersion: v1
kind: Pod
metadata:
  name: my-pvc-pod
spec:
  volumes:
    - name: my-persistent-storage
      persistentVolumeClaim:
        claimName: my-pvc
  containers:
    - name: my-container
      image: nginx:latest
      volumeMounts:
        - mountPath: /usr/share/nginx/html
          name: my-persistent-storage
```

Apply the configuration:
```sh
kubectl apply -f volumes.yaml
```

Verify the Pods, PV, and PVC:
```sh
kubectl get pods
kubectl get pv
kubectl get pvc
kubectl describe pod my-volume-pod
kubectl describe pod my-pvc-pod
```

This single YAML file defines both a temporary volume (`emptyDir`) and a persistent volume with a claim (`PV` and `PVC`). Next, we will proceed with Init Containers and Multi-Container Pods.

