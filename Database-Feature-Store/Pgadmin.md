# **pgVector: Vector Search in PostgreSQL**

pgVector is a PostgreSQL extension designed to store and search high-dimensional vectors efficiently. It enables similarity searches using techniques like **Euclidean distance, cosine similarity, and inner product**, making it useful for applications in **machine learning, NLP, recommendation systems, and image retrieval**.

---

## **🔹 Theoretical Concepts**

### **1️⃣ What is a Vector Database?**
A **vector database** stores and queries numerical representations (vectors) instead of traditional structured data. These vectors represent real-world data like **text, images, and user interactions**, enabling similarity-based search rather than exact matches.

### **2️⃣ Similarity Search Methods in pgVector**
pgVector supports three main methods for vector similarity searches:

- **Euclidean Distance (`L2 Norm`)**: Measures the straight-line distance between two vectors.
- **Cosine Similarity**: Measures the angle between two vectors, useful for text embeddings.
- **Inner Product**: Measures vector similarity through dot product calculations.

### **3️⃣ Indexing for Performance**
Since searching through millions of vectors can be slow, pgVector provides **indexing techniques**:

- **HNSW (Hierarchical Navigable Small World)**: Best for approximate nearest neighbor searches.
- **IVFFlat (Inverted File Index)**: Groups vectors into clusters for faster searching.

---

## ** Installation and Setup**

### **🔹 Installing PostgreSQL and pgVector on Fedora**
```sh
# Install PostgreSQL (if not already installed)
sudo dnf install postgresql14-server

# Start PostgreSQL service
sudo systemctl enable --now postgresql-14

# Install pgVector extension
sudo -u postgres psql -c "CREATE EXTENSION vector;"
```

### **🔹 Verifying Installation**
Run the following command inside `psql`:
```sql
SELECT * FROM pg_extension WHERE extname = 'vector';
```

If `vector` appears in the results, the extension is successfully installed.

---

## ** Practical Usage: Creating and Querying Vectors**

### **1️⃣ Creating a Table with Vector Columns**
```sql
CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    data_vector vector(3) -- 3D vector example
);
```

### **2️⃣ Inserting Vectors**
```sql
INSERT INTO embeddings (data_vector) VALUES ('[0.1, 0.2, 0.3]');
INSERT INTO embeddings (data_vector) VALUES ('[0.4, 0.5, 0.6]');
```

### **3️⃣ Querying with Similarity Search**
```sql
-- Find the nearest vector using Euclidean Distance
SELECT id, data_vector <-> '[0.2, 0.3, 0.4]' AS distance
FROM embeddings ORDER BY distance LIMIT 1;
```

### **4️⃣ Creating an Index for Faster Search**
```sql
-- Using IVFFlat index (must analyze data first)
CREATE INDEX vector_index ON embeddings USING ivfflat (data_vector);
```

### **5️⃣ Searching with Cosine Similarity**
```sql
SELECT id, data_vector <=> '[0.2, 0.3, 0.4]' AS similarity_score
FROM embeddings ORDER BY similarity_score DESC LIMIT 5;
```

---

## ** Use Cases**
1. **NLP (Natural Language Processing)**: Storing and searching text embeddings for semantic similarity.
2. **Image Search**: Storing CNN-based embeddings to find similar images.
3. **Recommendation Systems**: Finding similar user interactions for better recommendations.
4. **Fraud Detection**: Identifying suspicious transaction patterns.

---


pgVector extends PostgreSQL with powerful similarity search capabilities, making it a great choice for AI-powered applications that require **fast, scalable, and efficient** vector retrieval. By leveraging PostgreSQL’s reliability and indexing capabilities, pgVector provides a robust alternative to dedicated vector databases.

---


