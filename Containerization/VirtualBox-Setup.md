# VirtualBox Setup Guide

## **1. System Update and Kernel Modules Setup**
```bash
sudo nano /etc/dnf/dnf.conf
sudo dnf upgrade --refresh
sudo reboot now
sudo dnf search kernel-devel-*
sudo dnf install kernel-devel-matched.x86_64
sudo reboot now
```

- Updated Fedora system packages.
- Installed kernel development packages required for VirtualBox Guest Additions.

---

## **2. VirtualBox Guest Additions Installation**
```bash
ls
chmod +x VBoxLinuxAdditions.run
ls
sudo ./VBoxLinuxAdditions.run
sudo reboot now
```

- Made the VirtualBox Guest Additions script executable and ran it.
- Rebooted the system for changes to take effect.

---