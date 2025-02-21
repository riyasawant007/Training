# File System Navigation in Linux

## Introduction
Navigating the file system is essential for working efficiently in Linux. This guide covers basic Linux commands for navigating, managing, and manipulating files and directories.

## Basic Commands

### 1. **pwd** (Print Working Directory)
Displays the absolute path of the current working directory.
```bash
pwd
```

### 2. **ls** (List Directory Contents)
Lists files and directories in the current location.
```bash
ls
```
**Common Options:**
- `ls -l` → Long listing format
- `ls -a` → Show hidden files
- `ls -lh` → Human-readable file sizes

### 3. **cd** (Change Directory)
Navigates to a different directory.
```bash
cd /path/to/directory
```
- `cd ..` → Move up one directory
- `cd ~` → Go to the home directory
- `cd -` → Switch to the previous directory

### 4. **mkdir** (Make Directory)
Creates a new directory.
```bash
mkdir new_directory
```
- `mkdir -p parent/child` → Create nested directories

### 5. **rmdir** (Remove Directory)
Deletes an empty directory.
```bash
rmdir empty_directory
```
- Use `rm -r directory_name` to remove non-empty directories

### 6. **mv** (Move/Rename Files)
Moves or renames files and directories.
```bash
mv old_name new_name
mv file.txt /new/location/
```

### 7. **cp** (Copy Files & Directories)
Copies files or directories.
```bash
cp file.txt destination/
cp -r directory/ destination/
```

### 8. **rm** (Remove Files & Directories)
Deletes files or directories permanently.
```bash
rm file.txt
rm -r directory/
```
**WARNING:** Be careful while using `rm -r`, as it deletes files irreversibly.

### 9. **find** (Search for Files & Directories)
Searches for files and directories based on conditions.
```bash
find /path -name "filename"
```
- `find /home -type d` → Find directories
- `find . -size +100M` → Find files larger than 100MB

### 10. **cat** (Concatenate & View Files)
Displays file content in the terminal.
```bash
cat file.txt
```
- `cat file1.txt file2.txt > merged.txt` → Merge files

### 11. **less** & **more** (View Large Files)
Used for paginated viewing of large files.
```bash
less largefile.txt
more largefile.txt
```

### 12. **touch** (Create Empty Files)
Creates an empty file or updates its timestamp.
```bash
touch newfile.txt
```

### 13. **head & tail** (View First/Last Lines)
```bash
head -n 10 file.txt   # Show first 10 lines
tail -n 10 file.txt   # Show last 10 lines
```


