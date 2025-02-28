# PostgreSQL 14 Setup on Fedora with Custom Data Directory

## Overview
This document details the step-by-step process for installing and configuring **PostgreSQL 14** on **Fedora**, including changing the **data directory** to a custom location.

---

## **1. Installation of PostgreSQL 14**

### **Step 1: Install PostgreSQL 14 Server**
```bash
sudo dnf install postgresql14-server
```

### **Step 2: Initialize PostgreSQL Database**
```bash
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb
```

### **Step 3: Verify the Default Data Directory**
```bash
sudo ls /var/lib/pgsql/14/data
```

This confirms that PostgreSQL has been initialized properly.

---

## **2. Starting PostgreSQL Service**

### **Step 1: Start the PostgreSQL Service**
```bash
sudo systemctl start postgresql-14
```

### **Step 2: Verify Service Status**
```bash
sudo systemctl status postgresql-14
```

If the service is running, you should see an **active (running)** status.

### **Step 3: Access PostgreSQL CLI**
```bash
sudo -u postgres psql
```

Exit PostgreSQL using:
```sql
\q
```

---

## **3. Changing the PostgreSQL Data Directory**

### **Step 1: Stop the PostgreSQL Service**
```bash
sudo systemctl stop postgresql-14
```

### **Step 2: Create a New Directory for PostgreSQL Data**
```bash
sudo mkdir /pg
sudo chmod 777 /pg
cd /pg/
sudo mkdir pgdata
sudo chown postgres:postgres pgdata
sudo chmod 700 pgdata
```

### **Step 3: Move PostgreSQL Data to the New Directory**
```bash
sudo rsync -av /var/lib/pgsql/14/data /pg/pgdata/
```

Verify the files:
```bash
sudo ls pgdata/data
```

### **Step 4: Update PostgreSQL Configuration**
Modify **postgresql.conf** to point to the new data directory:
```bash
sudo vi /pg/pgdata/data/postgresql.conf
```
Update:
```
data_directory = '/pg/pgdata/data'
```
Modify **pg_hba.conf** to allow remote connections:
```bash
sudo vi /pg/pgdata/data/pg_hba.conf
```
Update:
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
host    all             all             0.0.0.0/32              md5
```

### **Step 5: Update PostgreSQL Service File**
Modify the systemd service file:
```bash
sudo vi /usr/lib/systemd/system/postgresql-14.service
```
Update the **PGDATA** environment variable:
```
Environment=PGDATA=/pg/pgdata/data
```

### **Step 6: Enable and Restart PostgreSQL Service**
```bash
sudo systemctl enable postgresql-14
sudo systemctl start postgresql-14
```

### **Step 7: Verify Service Status**
```bash
sudo systemctl status postgresql-14
```

### **Step 8: Confirm PostgreSQL is Using the New Data Directory**
```bash
sudo -u postgres psql -c "SHOW data_directory;"
```
Expected output:
```
      data_directory
------------------------------
 /pg/pgdata/data
(1 row)
```

---

## **4. Testing PostgreSQL Connection**

Try connecting to PostgreSQL:
```bash
sudo -u postgres psql
```
If successful, exit with:
```sql
\q
```

---

## **5. Cleanup (Optional)**
Once you have verified everything is working, you can delete the old PostgreSQL data directory:
```bash
sudo rm -rf /var/lib/pgsql/14/data.bak
```

---

## **6. Final Verification**
### **Restart System and Verify PostgreSQL**
```bash
sudo reboot
```
After reboot, verify the PostgreSQL service is running:
```bash
sudo systemctl status postgresql-14
```
And confirm the correct data directory:
```bash
sudo -u postgres psql -c "SHOW data_directory;"
```

---

You have successfully installed **PostgreSQL 14** on **Fedora**, moved its data directory to a custom location (`/pg/pgdata/data`), updated the configuration, and ensured everything is working properly.

Your PostgreSQL setup is now optimized and can persist data safely even after reboots! 🚀

