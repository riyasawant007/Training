# Private & Public Keys for SSH

Secure Shell (SSH) uses cryptographic key pairs (private and public keys) for secure authentication and communication between systems. These keys enhance security by eliminating the need for password-based logins.

## Understanding SSH Key Pairs
- **Public Key**: Shared with remote systems to grant access.
- **Private Key**: Kept secret and used for authentication.

## Generating SSH Key Pairs
To generate an SSH key pair on a Linux/macOS system:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- `-t rsa`: Specifies RSA algorithm.
- `-b 4096`: Sets key length to 4096 bits for enhanced security.
- `-C`: Adds a comment (e.g., email) for identification.

## Storing and Using SSH Keys
- Public key (`id_rsa.pub`) should be copied to the remote server.
- Private key (`id_rsa`) remains on the local machine.
- Add public key to the remote server using:
  ```bash
  ssh-copy-id user@remote_host
  ```

## SSH Key-Based Authentication
Once keys are set up, connect to the server:
```bash
ssh -i ~/.ssh/id_rsa user@remote_host
```

## Best Practices for SSH Keys
- **Use a strong passphrase** for additional security.
- **Restrict file permissions** (`chmod 600 ~/.ssh/id_rsa`).
- **Rotate SSH keys periodically** to mitigate risks.
- **Disable password authentication** in SSH configuration (`/etc/ssh/sshd_config`).

By implementing these practices, SSH key authentication ensures secure and efficient remote access to servers.

