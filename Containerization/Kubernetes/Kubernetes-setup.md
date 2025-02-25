# Kubernetes Setup on Fedora


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
