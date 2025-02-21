# Package Management: yum & dnf

## Introduction
Package management in Linux is crucial for installing, updating, and removing software. The **yum** (Yellowdog Updater, Modified) and **dnf** (Dandified Yum) package managers are used primarily in **RHEL-based** distributions such as CentOS, Fedora, and Rocky Linux.

## yum vs. dnf
- **yum** is the traditional package manager for RHEL-based distributions.
- **dnf** is the modern replacement for yum, offering better performance and dependency resolution.

## Basic Commands

### 1. **Checking for Updates**
```bash
yum check-update  # Using yum
dnf check-update  # Using dnf
```

### 2. **Installing Packages**
```bash
yum install package-name  # Using yum
dnf install package-name  # Using dnf
```

### 3. **Removing Packages**
```bash
yum remove package-name  # Using yum
dnf remove package-name  # Using dnf
```

### 4. **Updating Packages**
```bash
yum update  # Update all packages using yum
dnf update  # Update all packages using dnf
```

### 5. **Listing Installed Packages**
```bash
yum list installed  # Using yum
dnf list installed  # Using dnf
```

### 6. **Searching for a Package**
```bash
yum search package-name  # Using yum
dnf search package-name  # Using dnf
```

### 7. **Getting Package Info**
```bash
yum info package-name  # Using yum
dnf info package-name  # Using dnf
```

### 8. **Clearing Cache**
```bash
yum clean all  # Using yum
dnf clean all  # Using dnf
```

### 9. **Managing Repositories**
- List enabled repositories:
  ```bash
  yum repolist
  dnf repolist
  ```
- Enable/disable a repository:
  ```bash
  yum-config-manager --enable repo-name  # Enable repo in yum
  dnf config-manager --set-enabled repo-name  # Enable repo in dnf
  ```


Using **yum** and **dnf**, you can efficiently manage packages in RHEL-based Linux distributions. While **yum** is still in use, **dnf** is the recommended package manager due to its improvements in speed and dependency handling.