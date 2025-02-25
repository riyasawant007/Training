# Services (svc) - Exposing Applications
A **Service** exposes a set of Pods to network traffic, providing stable networking.

### Creating a Service
Create a YAML file named `service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: NodePort
```

Apply the Service:
```sh
kubectl apply -f service.yaml
```

Check the Service:
```sh
kubectl get services
```

Get the NodePort to access the service:
```sh
kubectl describe service my-service
```


