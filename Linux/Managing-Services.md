# Managing Services with systemd in Linux

## Introduction
`systemd` is the default service manager for most modern Linux distributions. It is used to manage system services, control startup behavior, and monitor service states.

## 1. **Checking Service Status**
To check the status of a service, use:
```bash
systemctl status service_name
```

## 2. **Starting and Stopping Services**
- Start a service:
  ```bash
  sudo systemctl start service_name
  ```
- Stop a service:
  ```bash
  sudo systemctl stop service_name
  ```
- Restart a service:
  ```bash
  sudo systemctl restart service_name
  ```
- Reload service configuration without restarting:
  ```bash
  sudo systemctl reload service_name
  ```

## 3. **Enabling and Disabling Services**
- Enable a service to start at boot:
  ```bash
  sudo systemctl enable service_name
  ```
- Disable a service from starting at boot:
  ```bash
  sudo systemctl disable service_name
  ```

## 4. **Listing Services**
- List all running services:
  ```bash
  systemctl list-units --type=service --state=running
  ```
- List all services (active/inactive):
  ```bash
  systemctl list-units --type=service
  ```

## 5. **Creating a Systemd Service**
To create a custom service, follow these steps:
1. Create a service file:
   ```bash
   sudo nano /etc/systemd/system/my_service.service
   ```
2. Add the following configuration:
   ```ini
   [Unit]
   Description=My Custom Service
   After=network.target
   
   [Service]
   ExecStart=/usr/bin/python3 /path/to/script.py
   Restart=always
   User=username
   
   [Install]
   WantedBy=multi-user.target
   ```
3. Reload `systemd` to apply changes:
   ```bash
   sudo systemctl daemon-reload
   ```
4. Start and enable the service:
   ```bash
   sudo systemctl start my_service
   sudo systemctl enable my_service
   ```

`systemd` provides a robust way to manage services in Linux. Whether starting, stopping, enabling, or creating custom services, these commands help control system behavior efficiently.

