# Kubernetes Secrets

Kubernetes Secrets are used to store sensitive data such as passwords, OAuth tokens, and SSH keys securely. Unlike ConfigMaps, Secrets are specifically designed to handle confidential information.

## Types of Secrets
1. **Opaque (Default Type)**: Stores arbitrary user-defined data.
2. **docker-registry**: Stores Docker registry credentials.
3. **tls**: Stores TLS certificates and keys.

## Creating a Secret

### 1. Creating a Secret Manually
You can create a Secret manually using the `kubectl create secret` command:

```sh
kubectl create secret generic my-secret --from-literal=username=admin --from-literal=password=supersecret
```

### 2. Creating a Secret from a File
If you have credentials stored in a file, you can create a Secret from it:

```sh
echo -n "admin" > username.txt
echo -n "supersecret" > password.txt

kubectl create secret generic my-secret --from-file=username.txt --from-file=password.txt
```

### 3. Creating a Secret Using YAML
You can define a Secret in a YAML file:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=    # base64 encoded "admin"
  password: c3VwZXJzZWNyZXQ=  # base64 encoded "supersecret"
```

> **Note**: The values must be base64 encoded. You can encode values using:
> ```sh
> echo -n "your-value" | base64
> ```

Apply the Secret:
```sh
kubectl apply -f secret.yaml
```

## Using Secrets in Pods

### 1. Mounting a Secret as an Environment Variable
Modify the Pod definition to use the Secret:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
    - name: my-container
      image: nginx
      env:
        - name: USERNAME
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: username
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: password
```

### 2. Mounting a Secret as a Volume
Secrets can also be mounted as files inside a container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-volume-pod
spec:
  volumes:
    - name: secret-volume
      secret:
        secretName: my-secret
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - name: secret-volume
          mountPath: "/etc/secret"
          readOnly: true
```

This will mount the Secret as files inside `/etc/secret/`.

## Viewing and Deleting Secrets

To list all Secrets:
```sh
kubectl get secrets
```

To view a specific Secret:
```sh
kubectl get secret my-secret -o yaml
```

To delete a Secret:
```sh
kubectl delete secret my-secret
```

---


