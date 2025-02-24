# File System Operations in Linux

## 1. Checking the File System Type
To check the file system of a partition:
```bash
lsblk -f
blkid
df -T
mount | column -t
```

## 2. Formatting a Partition with a File System
To format a disk with a specific file system:

- **ext4** (most common for Linux):
  ```bash
  sudo mkfs.ext4 /dev/sdX1
  ```
- **XFS**:
  ```bash
  sudo mkfs.xfs /dev/sdX1
  ```
- **Btrfs**:
  ```bash
  sudo mkfs.btrfs /dev/sdX1
  ```

## 3. Mounting a File System
To mount a partition:
```bash
sudo mount /dev/sdX1 /mnt/mydrive
```
To make it permanent, add an entry to `/etc/fstab`:
```bash
/dev/sdX1  /mnt/mydrive  ext4  defaults  0  2
```
Apply the changes:
```bash
sudo mount -a
```

## 4. Converting File Systems
- **Convert ext2 to ext3:**
  ```bash
  sudo tune2fs -j /dev/sdX1
  ```
- **Convert ext3 to ext4:**
  ```bash
  sudo tune2fs -O extents,uninit_bg,dir_index /dev/sdX1
  sudo fsck -pf /dev/sdX1
  
