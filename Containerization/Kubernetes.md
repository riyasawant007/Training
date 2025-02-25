# 1. Kubernetes Setup on Fedora

## Prerequisites
Before installing Kubernetes and Minikube, ensure your system has the required dependencies installed.

### Install Required Packages
```bash
sudo dnf -y install curl wget git
sudo dnf -y install conntrack
```

## Install Kubectl
Kubectl is the command-line tool used to interact with the Kubernetes cluster.

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

### Verify Installation
```bash
kubectl version --client
```

## Install Minikube
Minikube allows you to run a Kubernetes cluster locally.

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube
```

### Verify Installation
```bash
minikube version
```

## Start Minikube
Ensure Docker is installed and running before starting Minikube.

```bash
minikube start --driver=docker
```

### Check Minikube Status
```bash
minikube status
```

## Verify Kubernetes Cluster
```bash
kubectl cluster-info
kubectl get nodes
```

## Enable Kubectl Auto-Completion (Optional)
To enable bash completion for `kubectl`:

```bash
echo 'source <(kubectl completion bash)' >> ~/.bashrc
source ~/.bashrc
```

## Kubernetes Basic Commands
```bash
kubectl get pods -A  # List all pods in all namespaces
kubectl get nodes    # List all nodes in the cluster
kubectl get services # List all services
```

---
# 2.  Kubernetes Pods
A Pod is the smallest and simplest unit in the Kubernetes object model. It represents a single instance of a running process in a cluster.

### Creating a Pod
A basic example of a Pod definition in YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
```
To create this Pod:
```bash
kubectl apply -f my-pod.yaml
```

### Viewing Pods
List all Pods in the default namespace:
```bash
kubectl get pods
```

Describe a specific Pod:
```bash
kubectl describe pod my-pod
```

### Deleting a Pod
To delete a Pod:
```bash
kubectl delete pod my-pod
```



