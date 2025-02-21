# Monitoring System Resources in Linux

## Introduction
Monitoring system resources is crucial for performance tuning and troubleshooting. Linux provides several built-in commands to check CPU usage, memory usage, disk usage, and system uptime.

## 1. **top** - Real-time System Monitoring
The `top` command displays a dynamic real-time view of system processes and resource usage.
```bash
top
```
### Key Shortcuts in `top`:
- `q` → Quit
- `h` → Help
- `M` → Sort by memory usage
- `P` → Sort by CPU usage

## 2. **htop** - Interactive Process Monitoring
A more user-friendly alternative to `top` with color-coded output and easier navigation.
```bash
htop
```
**Installation (if not installed):**
```bash
sudo apt update && sudo apt install htop -y
```

## 3. **ps** - Process Status
Lists active processes.
```bash
ps aux  # Show all running processes
ps -ef  # Detailed process information
```

## 4. **free** - Memory Usage
Displays information about system memory usage.
```bash
free -h  # Show memory in human-readable format
```

## 5. **df** - Disk Usage
Displays disk space usage for mounted filesystems.
```bash
df -h  # Human-readable disk usage
```

## 6. **du** - Directory Size
Checks the size of a specific directory.
```bash
du -sh /path/to/directory
```

## 7. **uptime** - System Uptime
Shows how long the system has been running.
```bash
uptime
```

## 8. **last reboot** - System Reboot History
Displays the history of system reboots.
```bash
last reboot
```

## Conclusion
Using these commands, you can effectively monitor CPU, memory, disk usage, and system uptime, helping to maintain system health and diagnose performance issues.

