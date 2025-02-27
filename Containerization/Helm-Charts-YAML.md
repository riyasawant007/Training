# Helm and Helm Charts

Helm is a package manager for Kubernetes that simplifies the deployment and management of applications. Helm uses **Helm Charts**, which are reusable, configurable templates for Kubernetes manifests.

## 📌 What is Helm?
Helm is used to:
- **Automate Kubernetes Deployments**
- **Manage Dependencies**
- **Easily Upgrade and Rollback Applications**
- **Parameterize Configurations**

### 🔹 Basic Helm Commands
| Command | Description |
|---------|------------|
| `helm install <release-name> <chart>` | Deploy an application using a Helm chart |
| `helm upgrade <release-name> <chart>` | Upgrade an existing release |
| `helm rollback <release-name> <revision>` | Rollback to a previous version |
| `helm list` | Show all deployed releases |
| `helm delete <release-name>` | Uninstall a Helm release |

## 📌 What are Helm Charts?
A **Helm Chart** is a structured directory that defines Kubernetes resources using templates. It includes:
- **Kubernetes manifests** (Deployments, Services, ConfigMaps, etc.)
- **Parameterization** using `values.yaml`
- **Dependencies** management

### 🔹 Helm Chart Directory Structure
```
my-helm-chart/
│── charts/                 # Dependencies (other Helm charts)
│── templates/              # Kubernetes resource templates
│   ├── deployment.yaml     # Defines Deployments
│   ├── service.yaml        # Defines Services
│   ├── configmap.yaml      # Defines ConfigMaps
│   ├── _helpers.tpl        # Stores helper functions
│── values.yaml             # Default configuration values
│── Chart.yaml              # Metadata about the chart
│── README.md               # Documentation
```

## 📌 YAML in Kubernetes
YAML (Yet Another Markup Language) is used to define Kubernetes configurations.

### 🔹 YAML Example (Kubernetes Deployment)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: nginx:latest
        ports:
        - containerPort: 80
```

## 📌 Using Helm with Kubernetes

## 1. Install Helm on Fedora

```bash
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Verify installation:

```bash
helm version
```

## 2. Add Helm Repositories
Helm uses repositories to store charts. Add the official Helm chart repository:

```bash
helm repo add stable https://charts.helm.sh/stable
helm repo update
```

List available repositories:

```bash
helm repo list
```

## 3. Install an Example Helm Chart
Install the **Nginx** chart from the Bitnami repository:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx
```

Check the status of the deployed release:

```bash
helm list
```

View installed pods:

```bash
kubectl get pods
```

## 4. Helm Chart Structure
A Helm chart consists of:

```
mychart/
  ├── charts/            # Dependency charts
  ├── templates/         # Kubernetes manifests (YAML files)
  ├── values.yaml        # Default values
  ├── Chart.yaml         # Chart metadata
  ├── README.md          # Documentation
```

## 5. Create a Custom Helm Chart
Create a new Helm chart:

```bash
helm create mychart
```

Modify `values.yaml`:

```yaml
replicaCount: 2
image:
  repository: nginx
  tag: latest
service:
  type: LoadBalancer
  port: 80
```

Install the custom chart:

```bash
helm install myapp ./mychart
```

Check deployment:

```bash
kubectl get all
```

## 6. Upgrade & Rollback
To upgrade:

```bash
helm upgrade myapp ./mychart
```

To rollback:

```bash
helm rollback myapp 1
```

## 7. Uninstall Helm Release

```bash
helm uninstall myapp
```

---


## 📌 Key Takeaways
✅ **Helm** simplifies Kubernetes deployments.  
✅ **Helm Charts** provide reusable templates.  
✅ **YAML** is used for Kubernetes configurations.  

