# Kubernetes Jobs

A **Job** in Kubernetes ensures that a task runs to completion. Unlike Deployments, Jobs are designed for short-lived workloads and batch processing.

## Types of Jobs
1. **One-Time Job**: Runs a single Pod until completion.
2. **Parallel Jobs**: Runs multiple Pods simultaneously.
3. **CronJobs**: Scheduled Jobs that execute at defined time intervals.

---

## 1. One-Time Job
A Job that runs once and completes successfully.

### YAML Definition:
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: one-time-job
spec:
  template:
    spec:
      containers:
        - name: job-container
          image: busybox
          command: ["echo", "Hello, Kubernetes Job!"]
      restartPolicy: Never
```

- **Apply the Job:**
  ```sh
  kubectl apply -f job.yaml
  ```
- **Check Job Status:**
  ```sh
  kubectl get jobs
  kubectl describe job one-time-job
  ```
- **View Logs:**
  ```sh
  kubectl logs -l job-name=one-time-job
  ```

---

## 2. Parallel Jobs
Useful when tasks need to run multiple times in parallel.

### YAML Definition:
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel-job
spec:
  completions: 5  # Total 5 Pods will run
  parallelism: 2  # 2 Pods run concurrently
  template:
    spec:
      containers:
        - name: parallel-container
          image: busybox
          command: ["echo", "Parallel Job execution"]
      restartPolicy: Never
```

- **Apply the Parallel Job:**
  ```sh
  kubectl apply -f parallel-job.yaml
  ```
- **Check Parallel Jobs:**
  ```sh
  kubectl get jobs
  ```

---

## 3. CronJobs
A **CronJob** allows running Jobs on a schedule, similar to Linux cron jobs.

### YAML Definition:
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: scheduled-job
spec:
  schedule: "*/2 * * * *"  # Runs every 2 minutes
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: cron-container
              image: busybox
              command: ["echo", "Scheduled Job executed"]
          restartPolicy: Never
```

- **Apply the CronJob:**
  ```sh
  kubectl apply -f cronjob.yaml
  ```
- **Check CronJobs:**
  ```sh
  kubectl get cronjobs
  kubectl get jobs
  ```
- **Manually Trigger a CronJob:**
  ```sh
  kubectl create job --from=cronjob/scheduled-job manual-run-job
  ```
- **Delete a CronJob:**
  ```sh
  kubectl delete cronjob scheduled-job
  ```

---

## Summary
- **Jobs** ensure task execution and completion.
- **Parallel Jobs** enable running multiple instances.
- **CronJobs** execute tasks on a schedule.

These Kubernetes Jobs help in automating workflows and batch processing effectively.

---


