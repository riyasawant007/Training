# Feast Feature Store

## Introduction
Feast (Feature Store) is an **open-source feature store** that manages and serves machine learning (ML) features in production. It acts as a **bridge between data engineering and ML models**, ensuring that features used during training are consistent with those used in real-time inference.

## Why Use a Feature Store?
When building ML models, feature consistency is crucial. Without a feature store:
- Different data pipelines may be used for training and inference, leading to **training-serving skew**.
- Feature engineering logic might be inconsistent across teams.
- Tracking, versioning, and sharing features becomes complex.

Feast addresses these issues by:
- Providing a **centralized feature repository**.
- Ensuring **feature consistency** between training and inference.
- Enabling **low-latency retrieval** of features.
- Supporting both **batch and real-time feature ingestion**.

## Architecture Overview
Feast consists of the following key components:

1. **Feature Repository** - Stores metadata about feature definitions, usually version-controlled.
2. **Data Sources** - Raw data sources such as PostgreSQL, BigQuery, Snowflake, Kafka, or S3.
3. **Offline Store** - Stores historical features for model training. Common backends include BigQuery, Redshift, Snowflake, and PostgreSQL.
4. **Online Store** - Stores real-time features for fast inference, using Redis, DynamoDB, or PostgreSQL.
5. **Feature Registry** - A metadata store that tracks feature definitions and versions.
6. **Feast SDK (Python/CLI)** - Used to define, retrieve, and manage features.
7. **Feast Serving Layer** - Provides an API to retrieve features with low latency.

## Installation & Setup

### 1. Install Feast
Feast can be installed using pip:
```sh
pip install feast
```

### 2. Initialize a Feature Repository
Create a new Feast repository:
```sh
feast init my_feature_repo
cd my_feature_repo
```
This generates a project structure with:
- `feature_store.yaml` → Configuration file
- `example.py` → Sample script
- `data/` → Example feature data
- `feature_repo/` → Directory for feature definitions

## Defining Features
### 1. Define a Feature View
A **Feature View** represents a group of related features. Below is an example of defining user transaction features stored in **PostgreSQL**.

```python
from feast import Entity, Feature, FeatureView, Field
from feast.types import Float32, Int64
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource

# Define data source
user_transactions = PostgreSQLSource(
    name="user_transactions",
    query="SELECT user_id, transaction_count, avg_spend FROM transactions",
    timestamp_field="event_timestamp"
)

# Define an Entity (primary key)
user = Entity(name="user_id", join_keys=["user_id"])

# Define Feature View
user_transactions_view = FeatureView(
    name="user_transactions",
    entities=[user],
    schema=[
        Field(name="transaction_count", dtype=Int64),
        Field(name="avg_spend", dtype=Float32),
    ],
    source=user_transactions
)
```

### 2. Register Features
Run the following command to **apply the feature definitions** to the feature store:
```sh
feast apply
```

### 3. Load Historical Features for Training
Retrieve features for training ML models:
```python
from feast import FeatureStore

store = FeatureStore(repo_path=".")
training_df = store.get_historical_features(
    entity_df="SELECT user_id, event_timestamp FROM training_data",
    features=["user_transactions:transaction_count", "user_transactions:avg_spend"]
).to_df()

print(training_df.head())
```

### 4. Load Real-time Features for Inference
Retrieve real-time features using an API:
```python
feature_vector = store.get_online_features(
    features=["user_transactions:transaction_count", "user_transactions:avg_spend"],
    entity_rows=[{"user_id": 123}]
).to_dict()

print(feature_vector)
```

## Online & Offline Feature Stores

| **Feature Store** | **Usage** | **Example Backend** |
|------------------|----------|--------------------|
| Offline Store | Stores historical features for training | PostgreSQL, BigQuery, Snowflake |
| Online Store | Stores real-time features for low-latency inference | Redis, DynamoDB, PostgreSQL |

## Use Cases
- **Fraud Detection:** Real-time transaction monitoring.
- **Recommendation Systems:** Personalized product recommendations.
- **Customer Segmentation:** Predict customer behavior.
- **Predictive Maintenance:** Real-time sensor data ingestion.


Feast simplifies ML feature management by ensuring consistency between training and inference. It integrates with multiple data sources and provides low-latency feature serving. Whether you need batch processing or real-time feature retrieval, Feast is a powerful tool for your ML pipeline.


