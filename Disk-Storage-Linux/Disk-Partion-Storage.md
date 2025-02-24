# Disk Partitioning and Mounting in Linux

## 1. Checking Disk Partitions
Use the following commands to check existing partitions:

```bash
lsblk    # Shows disk partitions in a tree format
fdisk -l # Lists partition details (for MBR disks)
parted -l # Lists partitions (for both MBR & GPT)
```

## 2. Creating and Managing Partitions
To create a new partition, use `fdisk` (for MBR) or `parted` (for GPT):

### Using `fdisk` (MBR)
1. Open the disk for partitioning:
   ```bash
   sudo fdisk /dev/sdX  # Replace X with your disk letter (e.g., sda)
   ```
2. Inside `fdisk`:
   - Press **'n'** to create a new partition.
   - Press **'p'** for primary or **'e'** for extended.
   - Specify the partition size.
   - Press **'w'** to write changes.

### Using `parted` (GPT)
1. Open `parted`:
   ```bash
   sudo parted /dev/sdX
   ```
2. Inside `parted`, create a partition:
   ```bash
   mklabel gpt
   mkpart primary ext4 1MiB 50GiB
   ```

## 3. Mounting and Unmounting Partitions
After creating a partition, you must mount it to use it.

### Create a Filesystem (e.g., ext4):
```bash
sudo mkfs.ext4 /dev/sdX1
```

### Create a Mount Point:
```bash
sudo mkdir /mnt/mydisk
```

### Mount the Partition:
```bash
sudo mount /dev/sdX1 /mnt/mydisk
```

### Verify the Mount:
```bash
df -h
```

### Unmounting:
```bash
sudo umount /mnt/mydisk
```

## 4. Permanent Mounting (fstab)
To make the mount persistent after a reboot, add an entry to `/etc/fstab`:

```bash
/dev/sdX1  /mnt/mydisk  ext4  defaults  0  2
```

Then reload `fstab`:
```bash
sudo mount -a
