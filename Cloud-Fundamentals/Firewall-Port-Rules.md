# Firewall Port Rules

Firewall port rules are security configurations that control network traffic to and from a system based on predefined policies. These rules specify which ports are open or blocked to allow or restrict traffic.

## Key Concepts:
- **Ingress Rules**: Control incoming traffic to a system.
- **Egress Rules**: Control outgoing traffic from a system.
- **Port Ranges**: Define specific port numbers or a range of ports for communication.
- **Protocol Types**:
  - **TCP (Transmission Control Protocol)**: Ensures reliable communication.
  - **UDP (User Datagram Protocol)**: Used for faster, connectionless communication.
  - **ICMP (Internet Control Message Protocol)**: Used for network diagnostics (e.g., ping requests).

## Commonly Used Firewall Ports:
| Port Number | Protocol | Description |
|-------------|---------|-------------|
| 22 | TCP | SSH (Secure Shell) |
| 80 | TCP | HTTP (Web Traffic) |
| 443 | TCP | HTTPS (Secure Web Traffic) |
| 3306 | TCP | MySQL Database |
| 5432 | TCP | PostgreSQL Database |
| 3389 | TCP | Remote Desktop Protocol (RDP) |

## Firewall Rules in Cloud Providers:
### AWS:
- Managed through **Security Groups** and **Network ACLs**.
- Rules apply to inbound and outbound traffic.

### Azure:
- Managed through **Network Security Groups (NSGs)**.
- Allows filtering of traffic by port, source, destination, and protocol.

### GCP:
- Managed using **VPC Firewall Rules**.
- Can allow or deny specific traffic based on IP ranges and protocols.

## Best Practices:
- Follow the **principle of least privilege** – only open necessary ports.
- Use **logging and monitoring** to track unauthorized access attempts.
- Restrict administrative access using **IP whitelisting**.
- Apply **layered security** with additional measures like VPNs and intrusion detection systems.