# VM & Disk Snapshots

Snapshots capture the state of a virtual machine (VM) or disk at a specific point in time. They are useful for backups, disaster recovery, and cloning instances.

## Features of Snapshots
- **Incremental Snapshots** – Only saves changed data, reducing storage costs.
- **Automated Scheduling** – Cloud providers support scheduled snapshots for data protection.
- **Cross-Region Replication** – Some services allow snapshots to be replicated to different regions for redundancy.

## Snapshots in Cloud Providers

| Cloud Provider | VM Snapshots | Disk Snapshots |
|---------------|-------------|---------------|
| **AWS** | EC2 Snapshots | EBS Snapshots |
| **Azure** | VM Snapshots | Managed Disk Snapshots |
| **GCP** | Compute Engine Snapshots | Persistent Disk Snapshots |

## Use Cases
- **Backup & Disaster Recovery** – Restore systems in case of failure.
- **Testing & Development** – Quickly create test environments from existing VM states.
- **Migration** – Move instances or disks between regions or cloud providers.

## Best Practices
- **Schedule regular snapshots** to ensure data protection.
- **Retain only necessary snapshots** to optimize storage costs.
- **Encrypt snapshots** for security and compliance.
- **Test snapshot restoration** periodically to verify recoverability.

