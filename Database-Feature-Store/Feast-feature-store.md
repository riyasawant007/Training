# **Feast Feature Store - Setup with Database Integration on Fedora**

## **Introduction**
Feast (Feature Store) is an open-source feature store for machine learning that manages and serves ML features. It bridges the gap between data engineering pipelines and ML models, providing a **centralized repository** for feature storage and retrieval.

## **Key Components**
- **Feature Registry**: Stores metadata about features.
- **Offline Store**: Stores historical features for training (PostgreSQL).
- **Online Store**: Stores real-time features for inference (Redis).
- **Feature Serving API**: Serves features to ML models.

---

## **1. Install Dependencies on Fedora**

### **1.1 Install Python and Pip (if not installed)**
```bash
sudo dnf install python3 python3-pip -y
```

### **1.2 Install PostgreSQL (Offline Store)**
```bash
sudo dnf install postgresql-server postgresql-contrib -y
```
Initialize and start PostgreSQL:
```bash
sudo postgresql-setup --initdb
sudo systemctl enable postgresql
sudo systemctl start postgresql
```
Create a PostgreSQL user and database:
```bash
sudo -u postgres psql
```
Inside the PostgreSQL shell, run:
```sql
CREATE DATABASE feast;
CREATE USER feast_user WITH PASSWORD 'feast_pass';
ALTER ROLE feast_user SET client_encoding TO 'utf8';
ALTER ROLE feast_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE feast_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE feast TO feast_user;
\q
```

### **1.3 Install Redis (Online Store)**
```bash
sudo dnf install redis -y
sudo systemctl enable redis
sudo systemctl start redis
```

### **1.4 Install Feast**
```bash
sudo dnf install gcc gcc-c++ python3-devel
pip install feast
```

### **1.5 Verify Feast Installation**
```bash
feast --version
```

---

## **2. Configure Feast to Use PostgreSQL and Redis**

### **2.1 Initialize a New Feast Repository**
```bash
mkdir feast_project && cd feast_project
feast init
```
Navigate into the project:
```bash
cd my_feature_repo
```

### **2.2 Edit `feature_store.yaml`**
Modify `feature_store.yaml` to integrate PostgreSQL and Redis:

```yaml
project: my_feature_repo
registry: data/registry.db
provider: local

offline_store:
  type: postgres
  host: localhost
  port: 5432
  database: feast
  user: feast_user
  password: feast_pass

online_store:
  type: redis
  connection_string: localhost:6379
```

---

## **3. Define Features with Database Integration**

Edit `feature_repo/feature_views.py` to use PostgreSQL:

```python
from feast import Entity, Feature, FeatureView, FileSource
from datetime import timedelta

# Define entity (primary key)
customer = Entity(name="customer_id", join_keys=["customer_id"])

# Define source (PostgreSQL)
customer_source = FileSource(
    query="SELECT * FROM customer_features",
    database="feast",
    user="feast_user",
    password="feast_pass",
    host="localhost",
    port=5432
)

# Define feature view
customer_fv = FeatureView(
    name="customer_features",
    entities=[customer],
    ttl=timedelta(days=1),
    source=customer_source,
)
```

---

## **4. Apply Configuration and Populate Database**

### **4.1 Apply Feast Configuration**
```bash
feast apply
```

### **4.2 Materialize Data into Redis**
```bash
feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")
```

---

## **5. Query Features from PostgreSQL and Redis**

### **5.1 Query Features in Python**
```python
from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Retrieve features
features = store.get_online_features(
    feature_refs=["customer_features:feature1", "customer_features:feature2"],
    entity_rows=[{"customer_id": 1}]
).to_dict()

print(features)
```

---

## **Conclusion**
This setup integrates PostgreSQL as an **offline store** and Redis as an **online store** for Feast. It enables efficient feature retrieval for ML models in production.

