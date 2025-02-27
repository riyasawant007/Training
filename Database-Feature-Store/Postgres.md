# PostgreSQL on Fedora

PostgreSQL is an open-source, powerful, and feature-rich relational database management system (RDBMS). It supports SQL for querying data and is widely used for enterprise applications due to its reliability, extensibility, and compliance with ACID principles.

## Installation

### Step 1: Update Fedora
```bash
sudo dnf update -y
```

### Step 2: Install PostgreSQL
```bash
sudo dnf install -y postgresql-server postgresql-contrib
```

### Step 3: Initialize the Database
```bash
sudo postgresql-setup --initdb
```

### Step 4: Enable and Start PostgreSQL Service
```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

### Step 5: Check PostgreSQL Status
```bash
sudo systemctl status postgresql
```

## Usage

### Accessing PostgreSQL CLI
```bash
sudo -u postgres psql
```
Once inside, check the PostgreSQL version:
```sql
SELECT version();
```
To exit:
```sql
\q
```

### Creating a New Database
```sql
CREATE DATABASE test_db;
```

### Creating a User
```sql
CREATE USER test_user WITH ENCRYPTED PASSWORD 'password123';
```

### Granting Permissions
```sql
GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;
```

## Changing PostgreSQL Data Directory
By default, PostgreSQL stores data in `/var/lib/pgsql/data/`. You can change it by following these steps:

### Step 1: Stop PostgreSQL
```bash
sudo systemctl stop postgresql
```

### Step 2: Copy Data to New Location (e.g., `/data/pgsql`)
```bash
sudo cp -r /var/lib/pgsql/data /data/pgsql
```

### Step 3: Update Configuration
Edit the `postgresql.service` file:
```bash
sudo nano /etc/systemd/system/postgresql.service
```
Modify the `ExecStart` line:
```
ExecStart=/usr/bin/postgres -D /data/pgsql
```

### Step 4: Restart PostgreSQL
```bash
sudo systemctl daemon-reload
sudo systemctl start postgresql
```

