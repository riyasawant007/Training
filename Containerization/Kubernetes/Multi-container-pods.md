# **Multi-Container Pods**
Multi-container pods allow multiple containers to run within the same Kubernetes Pod, sharing the same storage and network. These containers can communicate with each other using inter-process communication (IPC) or shared volumes.

### **Use Cases:**
- **Sidecar Pattern**: Logging, monitoring, or proxy sidecar containers.
- **Adapter Pattern**: Transforming data before passing it to the main container.
- **Ambassador Pattern**: Handling network communication on behalf of the main container.

### **YAML Configuration: Multi-Container Pod**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-demo
spec:
  containers:
  - name: app-container
    image: nginx
    ports:
    - containerPort: 80
  - name: sidecar-container
    image: busybox
    command: ['sh', '-c', 'while true; do echo sidecar running; sleep 10; done']
```


1. **`app-container`**: Runs an Nginx web server.
2. **`sidecar-container`**: Runs a background process that continuously logs a message.

### **Deploy & Test Multi-Container Pod**
```bash
kubectl apply -f multi-container-pod.yaml
kubectl get pods
kubectl logs multi-container-demo -c sidecar-container
```

---

Multi-Container Pods are essential for building scalable and efficient Kubernetes applications. 
