# Kubernetes Error: ErrImageNeverPulled

## Overview
`ErrImageNeverPulled` is an error status reported by Kubernetes when a container image was never successfully pulled from its registry and the pod's container cannot be started as a result. This error indicates that Kubernetes attempted to pull an image but the operation did not complete successfully.

## Why Does This Error Occur?

This error typically occurs due to one of the following reasons:

1. **Image Does Not Exist**: The specified image name or tag doesn't exist in the container registry.
2. **Registry Authentication Failure**: Kubernetes does not have proper credentials to access a private registry.
3. **Network Issues**: Network connectivity problems between the Kubernetes node and the container registry.
4. **Registry Rate Limiting**: The container registry has imposed rate limits that have been exceeded.
5. **Node Resource Constraints**: The node doesn't have enough resources to complete the image pull operation.
6. **Image Pull Policy Configuration**: Improper image pull policy settings.

## How This Error Is Produced

### Kubernetes Events

When this error occurs, you'll typically see it in the pod's events:

```bash
kubectl describe pod <pod-name>
```

Output might include:

```
Events:
  Type     Reason             Age                From               Message
  ----     ------             ----               ----               -------
  Normal   Scheduled          10s                default-scheduler  Successfully assigned default/myapp-pod to node1
  Warning  Failed             8s (x2 over 9s)    kubelet            Error: ErrImageNeverPulled
  Warning  FailedCreatePodSandBox  8s           kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to get sandbox image "registry.k8s.io/pause:3.8": failed to pull image "registry.k8s.io/pause:3.8": failed to pull and unpack image "registry.k8s.io/pause:3.8": failed to resolve reference "registry.k8s.io/pause:3.8": failed to do request: Head "https://registry.k8s.io/v2/pause/manifests/3.8": dial tcp: lookup registry.k8s.io: no such host
```

### Code Example That Can Produce This Error

Here's a Pod manifest that might produce this error:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: erroneous-pod
spec:
  containers:
  - name: mycontainer
    # Incorrect image name or non-existent tag
    image: non-existent-registry.io/myimage:v1.0
    # Or a typo in the image name
    # image: dockerhub.io/myapp:lateest  # Incorrect spelling of "latest"
```

## How to Fix This Error

### 1. Verify Image Name and Tag

Ensure the image and tag exist in the registry:

```bash
# Docker Hub
docker pull <image>:<tag>

# For other registries
docker pull <registry>/<image>:<tag>
```

Fix the Pod manifest with the correct image reference:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: corrected-pod
spec:
  containers:
  - name: mycontainer
    image: docker.io/myimage:v1.0  # Corrected image reference
```

### 2. Configure Registry Authentication

For private registries, create a Kubernetes Secret:

```bash
kubectl create secret docker-registry regcred \
  --docker-server=<your-registry-server> \
  --docker-username=<your-username> \
  --docker-password=<your-password> \
  --docker-email=<your-email>
```

Then reference the secret in your Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-reg-pod
spec:
  containers:
  - name: private-reg-container
    image: <your-private-registry>/<image>:<tag>
  imagePullSecrets:
  - name: regcred
```

### 3. Check Network Connectivity

Ensure the Kubernetes nodes can access the registry:

```bash
# From node (if possible)
curl -v https://<registry-url>/v2/ 

# Or using a debug pod
kubectl run debug-pod --rm -i --tty --image=alpine -- sh -c "ping <registry-url> && wget -q -O- https://<registry-url>/v2/"
```

### 4. Resolve Registry Rate Limiting

For public registries with rate limits:

- Use a pull secret even for public registries to increase rate limits
- Implement a container registry mirror or proxy
- Use a private registry to store copies of your images

```yaml
# Example for Docker Hub rate limiting
apiVersion: v1
kind: Secret
metadata:
  name: dockerhub-secret
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: <base64-encoded-docker-config>
---
apiVersion: v1
kind: Pod
metadata:
  name: rate-limited-fix-pod
spec:
  containers:
  - name: mycontainer
    image: docker.io/myapp:v1.0
  imagePullSecrets:
  - name: dockerhub-secret
```

### 5. Adjust Image Pull Policy

Modify the image pull policy if appropriate:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pull-policy-pod
spec:
  containers:
  - name: mycontainer
    image: myregistry.io/myapp:v1.0
    imagePullPolicy: IfNotPresent  # Only pulls if not present locally
    # Other options: Always, Never
```

### 6. Check Node Resources

Verify node has sufficient resources:

```bash
kubectl describe node <node-name>
```

Look for resource pressure indicators in the output.

### 7. Use a Local Image (for Development/Testing)

For local development with minikube:

```bash
# Load image into minikube
minikube image load myimage:tag

# Then use it in your pod with imagePullPolicy: Never
apiVersion: v1
kind: Pod
metadata:
  name: local-image-pod
spec:
  containers:
  - name: mycontainer
    image: myimage:tag
    imagePullPolicy: Never  # Don't try to pull from remote registry
```

## Troubleshooting Steps

1. **Check Pod Status**:
   ```bash
   kubectl get pods
   kubectl describe pod <pod-name>
   ```

2. **Check Node Logs**:
   ```bash
   kubectl logs <pod-name>
   # Or kubelet logs on the node
   journalctl -u kubelet
   ```

3. **Test Registry Access**:
   ```bash
   # Create a debug pod
   kubectl run -it --rm debug --image=alpine -- sh
   # Then inside the pod
   apk add --no-cache curl
   curl -v https://<registry-url>/v2/
   ```

4. **Verify Image Exists**:
   ```bash
   # For Docker Hub
   curl -s https://registry.hub.docker.com/v2/repositories/<username>/<image>/tags | grep "name"
   ```

By methodically checking each of these potential causes, you should be able to diagnose and resolve the `ErrImageNeverPulled` error in your Kubernetes environment.
