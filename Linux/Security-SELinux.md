# Security & SELinux (for RHEL)

## Introduction
Security-Enhanced Linux (SELinux) is a security module for Linux that provides a mechanism for enforcing access control policies. It is primarily used in Red Hat Enterprise Linux (RHEL) and related distributions to enhance system security.

## 1. **Checking SELinux Status**
To check if SELinux is enabled and its current mode:
```bash
sestatus
```
Alternatively:
```bash
getenforce
```

## 2. **SELinux Modes**
SELinux operates in three modes:
- **Enforcing**: Policies are enforced, denying unauthorized access.
- **Permissive**: Logs policy violations but does not enforce them.
- **Disabled**: SELinux is turned off.

To temporarily switch SELinux mode:
```bash
sudo setenforce 0  # Permissive mode
sudo setenforce 1  # Enforcing mode
```

## 3. **Managing SELinux Policies**
### Listing SELinux Booleans
SELinux Booleans allow toggling specific policy features:
```bash
semanage boolean -l
```
To change a boolean setting:
```bash
sudo setsebool -P httpd_can_network_connect on
```

### Managing SELinux File Contexts
- Check file context:
  ```bash
  ls -Z /path/to/file
  ```
- Restore default SELinux context:
  ```bash
  sudo restorecon -Rv /path/to/file
  ```
- Manually change file context:
  ```bash
  sudo chcon -t httpd_sys_content_t /var/www/html/index.html
  ```

## 4. **SELinux Logs and Troubleshooting**
SELinux violations are logged in `/var/log/audit/audit.log`. Use `ausearch` to analyze logs:
```bash
sudo ausearch -m AVC -ts recent
```
For suggestions on resolving issues:
```bash
sudo sealert -a /var/log/audit/audit.log
```

## 5. **Disabling SELinux (Not Recommended)**
To permanently disable SELinux, edit the `/etc/selinux/config` file:
```bash
SELINUX=disabled
```
Then, reboot the system:
```bash
sudo reboot
```

SELinux provides an additional layer of security for RHEL systems by enforcing access control policies. Understanding how to manage SELinux policies, troubleshoot issues, and properly configure security settings is essential for system administrators.

