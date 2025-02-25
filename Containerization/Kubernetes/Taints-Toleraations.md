# Taints & Tolerations in Kubernetes  
 
Taints and tolerations in Kubernetes control pod placement by preventing or allowing pods to be scheduled on specific nodes.

- **Taints**: Applied to nodes to repel pods unless they have a matching toleration.
- **Tolerations**: Applied to pods, allowing them to be scheduled on tainted nodes.

## **Types of Taints**
1. **NoSchedule**: Prevents scheduling of new pods unless they tolerate the taint.
2. **PreferNoSchedule**: Soft preference; tries to avoid scheduling but doesn’t enforce it strictly.
3. **NoExecute**: Evicts running pods from the node unless they tolerate the taint.

## **Practical Implementation**

### **1. Add a Taint to a Node**
```bash
kubectl taint nodes <node-name> key=value:NoSchedule
```
This prevents any pod without a toleration for `role=database` from being scheduled on `node1`.

### **2. Remove a Taint from a Node**
```bash
kubectl taint nodes <node-name> key=value:NoSchedule-
```


### **3. Add a Toleration to a Pod**
Define tolerations in a Pod's YAML file:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tolerant-pod
spec:
  tolerations:
    - key: "role"
      operator: "Equal"
      value: "database"
      effect: "NoSchedule"
  containers:
    - name: nginx
      image: nginx
```
This allows the pod to be scheduled on a node with `role=database:NoSchedule`.

### **4. Verify Taints & Tolerations**
- List taints on a node:
  ```bash
  kubectl describe nodes <node-name>
  ```
- Check which pods tolerate a taint:
  ```bash
  kubectl get pods --all-namespaces -o json | jq '.items[].spec.tolerations'
  ```

Taints and tolerations are crucial for defining node-pod relationships, ensuring that workloads are placed on appropriate nodes based on resource needs and isolation requirements.
