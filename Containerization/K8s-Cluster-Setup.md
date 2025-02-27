# Kubernetes Cluster Setup & Management

## 1. kubeadm - Bootstrapping a Kubernetes Cluster
### What is kubeadm?
`kubeadm` is a tool that simplifies Kubernetes cluster setup. It initializes the control plane and provides a way to add worker nodes.

### Steps to Set Up a Cluster with kubeadm
1. **Install Required Packages**
   ```bash
   sudo dnf install -y kubelet kubeadm kubectl
   sudo systemctl enable --now kubelet
   ```
2. **Disable Swap (Required for Kubernetes)**
   ```bash
   sudo swapoff -a
   sudo sed -i '/ swap / s/^/#/' /etc/fstab
   ```
3. **Initialize the Control Plane (Master Node)**
   ```bash
   sudo kubeadm init --pod-network-cidr=192.168.0.0/16
   ```
4. **Configure kubectl for Admin Access**
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```
5. **Deploy a CNI Plugin for Networking (Example: Calico)**
   ```bash
   kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
   ```
6. **Verify Cluster Status**
   ```bash
   kubectl get nodes
   kubectl get pods -A
   ```

## 2. kubelet - The Heart of Every Node
### What is kubelet?
`kubelet` is an agent running on each Kubernetes node that ensures Pods are running as expected.


- **Start kubelet:**
  ```bash
  sudo systemctl start kubelet
  ```
- **Enable kubelet on boot:**
  ```bash
  sudo systemctl enable kubelet
  ```
- **Check kubelet logs:**
  ```bash
  journalctl -u kubelet -f
  ```

## 3. CNI - Container Networking Interface
### What is CNI?
CNI (Container Networking Interface) allows Pods to communicate inside the cluster.

### Common CNI Plugins
- **Calico** → Network policies + routing
- **Flannel** → Simple overlay network
- **Cilium** → Security & observability

### Deploying Calico
```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

## 4. CSI - Container Storage Interface
### What is CSI?
CSI allows Kubernetes to use various storage providers like AWS EBS, Google Persistent Disks, or NFS.

### Example: Deploying an NFS-based CSI Driver
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/nfs-subdir-external-provisioner/master/deploy/rbac.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/nfs-subdir-external-provisioner/master/deploy/deployment.yaml
```

## 5. Nodes - Worker Machines in a Cluster
### Types of Nodes
- **Control Plane Node (Master)** → Runs API Server, Controller Manager, Scheduler
- **Worker Node** → Runs application workloads

### Check Node Status
```bash
kubectl get nodes
```

### Drain a Node (For Maintenance)
```bash
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
```

### Uncordon a Node (Make it Schedulable Again)
```bash
kubectl uncordon <node-name>
```

## 6. Joining & Removing Nodes
### Joining a Worker Node
On the worker node, run:
```bash
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

Generate a new join token if needed:
```bash
kubeadm token create --print-join-command
```

### Removing a Node
1. **Drain the Node**
   ```bash
   kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
   ```
2. **Remove from Cluster**
   ```bash
   kubectl delete node <node-name>
   ```
3. **Reset the Node (For Reuse)**
   ```bash
   sudo kubeadm reset
   ```
4. **Reboot the Node (Recommended)**
   ```bash
   sudo reboot
   ```

## Summary
| Concept  | Description |
|----------|------------|
| `kubeadm` | Bootstraps a Kubernetes cluster |
| `kubelet` | Runs on every node, manages Pods |
| `CNI` | Handles networking between Pods |
| `CSI` | Manages storage providers in Kubernetes |
| `Nodes` | Machines that form a cluster |
| **Joining Nodes** | Adds worker nodes using `kubeadm join` |
| **Removing Nodes** | Uses `kubectl drain` + `kubectl delete node` |

---



