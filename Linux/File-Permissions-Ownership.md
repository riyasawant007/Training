# File Permissions and Ownership in Linux

## Introduction
Managing file permissions and ownership is essential for system security and proper access control in Linux. This guide covers essential commands like `chmod`, `chown`, and `chgrp` for handling file and directory permissions.

## Understanding File Permissions
Each file and directory in Linux has three types of permissions:
- **Read (r)** → Allows viewing the file contents
- **Write (w)** → Allows modifying the file
- **Execute (x)** → Allows running the file as a program

Permissions are assigned to three categories:
- **Owner (u)** → The user who owns the file
- **Group (g)** → A group of users
- **Others (o)** → Everyone else

To view permissions, use:
```bash
ls -l filename
```
Example output:
```
-rwxr-xr-- 1 user group 1234 Feb 21 12:34 file.txt
```

## Changing Permissions with chmod
### 1. **Using Symbolic Mode**
```bash
chmod u+x file.txt  # Add execute permission for owner
chmod g-w file.txt  # Remove write permission for group
chmod o+r file.txt  # Add read permission for others
```

### 2. **Using Numeric Mode**
Permissions can also be represented numerically:
- **r = 4**, **w = 2**, **x = 1**
- Combine values to set permissions:
  ```bash
  chmod 755 file.txt  # Owner: rwx (7), Group: r-x (5), Others: r-x (5)
  chmod 644 file.txt  # Owner: rw-, Group: r--, Others: r--
  ```

## Changing Ownership with chown
### 1. **Change File Owner**
```bash
chown newuser file.txt
```
### 2. **Change Group Ownership**
```bash
chown :newgroup file.txt
```
### 3. **Change Both Owner and Group**
```bash
chown newuser:newgroup file.txt
```
### 4. **Recursively Change Ownership**
```bash
chown -R newuser:newgroup directory/
```

## Changing Group Ownership with chgrp
Change the group ownership of a file or directory:
```bash
chgrp newgroup file.txt
```

## Special Permissions
### 1. **Setuid (4xxx) - Execute as File Owner**
```bash
chmod 4755 script.sh  # Allows execution with owner’s privileges
```
### 2. **Setgid (2xxx) - Execute as Group**
```bash
chmod 2755 directory/  # Files created inside inherit group
```
### 3. **Sticky Bit (1xxx) - Restrict Deletion**
```bash
chmod 1755 directory/  # Only owners can delete their files
```

## Conclusion
Understanding file permissions and ownership is critical for Linux security and access control. By using `chmod`, `chown`, and `chgrp`, users can effectively manage permissions to protect files and directories.

