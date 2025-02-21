# Log Management in Ubuntu

## Introduction
Log management is crucial for monitoring system activity, troubleshooting issues, and ensuring security. Ubuntu stores logs in various locations, primarily under `/var/log/`.

## 1. **Viewing System Logs**
Ubuntu uses `journalctl` and log files in `/var/log/` for system logs.

- View the system journal:
  ```bash
  journalctl -xe
  ```
- View logs from the current boot:
  ```bash
  journalctl -b
  ```
- View logs for a specific service:
  ```bash
  journalctl -u service_name
  ```

## 2. **Important Log Files in Ubuntu**
- `/var/log/syslog` – General system logs
  ```bash
  sudo tail -f /var/log/syslog
  ```
- `/var/log/auth.log` – Authentication logs
  ```bash
  sudo tail -f /var/log/auth.log
  ```
- `/var/log/dmesg` – Kernel ring buffer logs
  ```bash
  dmesg | less
  ```
- `/var/log/kern.log` – Kernel logs
- `/var/log/apache2/access.log` – Web server access logs
- `/var/log/mysql/error.log` – Database error logs

## 3. **Rotating Logs with logrotate**
Ubuntu uses `logrotate` to manage log file sizes and archiving.

- Check `logrotate` configuration:
  ```bash
  cat /etc/logrotate.conf
  ```
- Rotate logs manually:
  ```bash
  sudo logrotate -f /etc/logrotate.conf
  ```

## 4. **Clearing and Managing Logs**
- Clear a specific log file:
  ```bash
  sudo truncate -s 0 /var/log/syslog
  ```
- Delete old journal logs:
  ```bash
  sudo journalctl --vacuum-time=7d  # Keep logs for the last 7 days
  ```
  ```bash
  sudo journalctl --vacuum-size=500M  # Limit log size to 500MB
  ```


Proper log management in Ubuntu helps in maintaining system health and troubleshooting errors efficiently. Utilizing `journalctl`, monitoring `/var/log/`, and managing logs with `logrotate` ensures optimal system performance.

