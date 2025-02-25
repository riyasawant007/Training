# Kubernetes Affinity

Affinity in Kubernetes allows users to control pod scheduling by specifying rules that determine on which nodes a pod should or should not run. It helps optimize resource allocation and improve system performance.

## Types of Affinity

### 1. Node Affinity
Node affinity is a mechanism that ensures pods are scheduled on nodes based on labels. It has two types:
- **Required (Hard) Node Affinity**: The pod will only be scheduled on nodes that match the specified conditions.
- **Preferred (Soft) Node Affinity**: The pod prefers specific nodes but can still be scheduled elsewhere if no matching nodes are available.

#### Example: Required (Hard) Node Affinity
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: disktype
                operator: In
                values:
                  - ssd
  containers:
    - name: nginx
      image: nginx
```

#### Example: Preferred (Soft) Node Affinity
```yaml
affinity:
  nodeAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
            - key: disktype
              operator: In
              values:
                - ssd
```

### 2. Pod Affinity
Pod affinity ensures that certain pods are scheduled close to each other to optimize performance for applications that require low latency.

#### Example: Pod Affinity
```yaml
affinity:
  podAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
            - key: app
              operator: In
              values:
                - backend
        topologyKey: "kubernetes.io/hostname"
```

### 3. Pod Anti-Affinity
Pod anti-affinity ensures that specific pods are scheduled apart from each other to enhance reliability and fault tolerance.

#### Example: Pod Anti-Affinity
```yaml
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
            - key: app
              operator: In
              values:
                - backend
        topologyKey: "kubernetes.io/hostname"
```

## Practical Steps
1. Apply a node label:
   ```sh
   kubectl label nodes <node-name> disktype=ssd
   ```
2. Deploy the pod with node affinity:
   ```sh
   kubectl apply -f node-affinity.yaml
   ```
3. Verify pod placement:
   ```sh
   kubectl get pods -o wide
   ```


Affinity rules provide fine-grained control over pod scheduling, ensuring that workloads are efficiently distributed and meet application-specific requirements. Kubernetes users can leverage node affinity, pod affinity, and pod anti-affinity to optimize performance and reliability.

