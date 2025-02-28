# Public & Private IP Addresses

IP (Internet Protocol) addresses are unique identifiers assigned to devices in a network. They can be categorized as **public** or **private**, each serving distinct purposes.

## Public IP Address
A **public IP** is a globally unique IP address assigned to a device, allowing it to be reachable over the internet.

### Characteristics:
- Assigned by **Internet Service Providers (ISPs)**.
- Used for **internet-facing servers, websites, and cloud resources**.
- Routable across the **public internet**.
- Can be **static** (fixed) or **dynamic** (changes periodically).

### Examples:
- Web servers
- Cloud-hosted applications (AWS EC2, Azure VMs, GCP Compute Engine)
- VPN gateways

## Private IP Address
A **private IP** is used within a local network and is not accessible from the internet.

### Characteristics:
- Assigned by **routers** and used within LAN (Local Area Networks).
- Not routable over the public internet.
- Helps in **reducing the need for public IPs**.
- Commonly used for internal communication between servers.

### Private IP Ranges:
| Address Class | Private IP Range |
|--------------|-----------------|
| Class A | 10.0.0.0 – 10.255.255.255 |
| Class B | 172.16.0.0 – 172.31.255.255 |
| Class C | 192.168.0.0 – 192.168.255.255 |

## Differences Between Public and Private IPs
| Feature | Public IP | Private IP |
|---------|----------|-----------|
| Accessibility | Accessible over the internet | Only within private networks |
| Assignment | Assigned by ISP | Assigned by routers/DHCP |
| Cost | Usually incurs cost | Free to use |
| Security | More vulnerable to attacks | Safer as it's not exposed |

## NAT (Network Address Translation)
Since private IPs cannot directly communicate with the internet, **NAT** is used to map private IPs to a public IP when making external requests.

### Cloud Providers & IP Allocation:
- **AWS**: Elastic IPs (Static Public IPs), Private IPs within VPCs.
- **Azure**: Public IPs for VM instances, Private IPs within VNets.
- **GCP**: External IPs for internet access, Internal IPs for private communication.

## Best Practices:
- Use **private IPs** for internal communication to enhance security.
- Restrict **public IP exposure** using firewalls and security groups.
- Leverage **NAT gateways** for controlled internet access.
- Implement **VPNs** for secure communication between networks.

