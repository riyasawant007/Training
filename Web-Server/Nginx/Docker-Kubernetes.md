# 🚀 Deploying Nginx with Docker & Kubernetes

---

## 🐳 **Deploying Nginx with Docker**

### **1️⃣ Build and Run Nginx in Docker**
#### **Create a Dockerfile**
```dockerfile
# Use the official Nginx image
FROM nginx:latest

# Copy custom HTML file
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
```

#### **Build & Run the Container**
```sh
docker build -t custom-nginx .
docker run -d -p 8080:80 --name my-nginx custom-nginx
```

#### **Verify Deployment**
```sh
docker ps
```
Visit `http://localhost:8080` ✅

### **2️⃣ Run Nginx with Custom Configuration**
#### **Create `nginx.conf`**
```nginx
server {
    listen 80;
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```

#### **Run Docker with Volume Mapping**
```sh
docker run -d -p 8080:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf --name my-nginx custom-nginx
```

✅ **Nginx is now running inside Docker!**

---

## ☸️ **Deploying Nginx in Kubernetes**

### **1️⃣ Create an Nginx Deployment**
#### **Create `nginx-deployment.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

#### **Apply the Deployment**
```sh
kubectl apply -f nginx-deployment.yaml
kubectl get pods
```

### **2️⃣ Expose Nginx as a Kubernetes Service**
#### **Create `nginx-service.yaml`**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

#### **Apply the Service**
```sh
kubectl apply -f nginx-service.yaml
kubectl get svc nginx-service
```

### **3️⃣ Access Nginx in Kubernetes**
- **Minikube:**
  ```sh
  minikube service nginx-service
  ```
- **Cloud Provider:** Use the **EXTERNAL-IP** from `kubectl get svc`.

✅ **Nginx is now running in Kubernetes!**

---

## 🎯 **Summary**
| **Command** | **Description** |
|------------|----------------|
| `docker build -t custom-nginx .` | Build custom Nginx image |
| `docker run -d -p 8080:80 --name my-nginx custom-nginx` | Run Nginx container |
| `kubectl apply -f nginx-deployment.yaml` | Deploy Nginx in Kubernetes |
| `kubectl apply -f nginx-service.yaml` | Expose Nginx via a Service |
| `kubectl get svc nginx-service` | Get service details |

---


