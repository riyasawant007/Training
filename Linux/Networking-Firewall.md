# Networking & Firewall in Linux

## Introduction
Networking and firewall management are crucial for securing and maintaining connectivity in a Linux system. This guide covers essential commands for configuring network interfaces, checking connectivity, and managing firewall rules.

## 1. **Checking Network Configuration**
View network interfaces and IP addresses:
```bash
ip a
```

## 2. **Testing Network Connectivity**
- Ping a remote server:
  ```bash
  ping -c 4 google.com
  ```
- Check DNS resolution:
  ```bash
  nslookup google.com
  ```
- Trace the route packets take:
  ```bash
  traceroute google.com
  ```
  (Use `sudo apt install traceroute` if not installed.)

## 3. **Managing Network Interfaces**
Enable or disable a network interface:
```bash
sudo ip link set eth0 up   # Enable interface
sudo ip link set eth0 down # Disable interface
```

## 4. **Viewing Active Network Connections**
Check open ports and active connections:
```bash
netstat -tulnp  # Requires net-tools package
ss -tulnp       # Alternative to netstat
```

## 5. **Configuring Firewall with UFW**
UFW (Uncomplicated Firewall) is a simple tool for managing firewall rules.
- Enable UFW:
  ```bash
  sudo ufw enable
  ```
- Allow or deny specific ports:
  ```bash
  sudo ufw allow 22/tcp   # Allow SSH
  sudo ufw deny 80/tcp    # Deny HTTP
  ```
- Check firewall status:
  ```bash
  sudo ufw status
  ```
- Disable UFW:
  ```bash
  sudo ufw disable
  ```

## 6. **Configuring Firewall with iptables**
For advanced firewall configurations, use `iptables`.
- List existing rules:
  ```bash
  sudo iptables -L -v
  ```
- Allow incoming SSH traffic:
  ```bash
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
  ```
- Block an IP address:
  ```bash
  sudo iptables -A INPUT -s 192.168.1.100 -j DROP
  ```
- Save firewall rules:
  ```bash
  sudo iptables-save > /etc/iptables.rules
  ```


Understanding networking and firewall management in Linux is essential for securing and optimizing system performance. Commands like `ip`, `ping`, `ufw`, and `iptables` help in configuring and monitoring network security efficiently.

