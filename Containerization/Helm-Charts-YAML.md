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
### 🔹 Install an Nginx Helm Chart
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx
```

## 📌 Key Takeaways
✅ **Helm** simplifies Kubernetes deployments.  
✅ **Helm Charts** provide reusable templates.  
✅ **YAML** is used for Kubernetes configurations.  
