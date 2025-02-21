# Users and Groups Management in Linux

## Introduction
Managing users and groups in Linux is essential for controlling access and permissions. This guide covers commands to add, modify, and delete users and groups.

## 1. **Adding a New User**
Create a new user with:
```bash
sudo adduser username
```

## 2. **Deleting a User**
Remove a user account:
```bash
sudo deluser username
```
To remove the user and their home directory:
```bash
sudo deluser --remove-home username
```

## 3. **Adding a User to a Group**
Assign a user to a group:
```bash
sudo usermod -aG groupname username
```

## 4. **Listing Users and Groups**
- List all users:
  ```bash
  cat /etc/passwd
  ```
- List all groups:
  ```bash
  cat /etc/group
  ```
- Check a user’s groups:
  ```bash
  groups username
  ```

## 5. **Creating and Deleting Groups**
- Create a new group:
  ```bash
  sudo addgroup groupname
  ```
- Delete a group:
  ```bash
  sudo delgroup groupname
  ```

## 6. **Changing User Passwords**
To update a user's password:
```bash
sudo passwd username
```

## 7. **Modifying User Information**
Change user details like home directory or shell:
```bash
sudo usermod -d /new/home/path username
sudo usermod -s /bin/bash username
```

## 8. **Switching Users**
To switch to another user account:
```bash
su - username
```

## 9. **Managing sudo Privileges**
To grant admin privileges, add the user to the `sudo` group:
```bash
sudo usermod -aG sudo username
```


Understanding user and group management in Linux is crucial for system security and access control. These commands help in efficiently managing user accounts and permissions.

