# Nginx Web Server, Reverse Proxy, SSL, DNS, and Serving Frontend

## 📌 Overview
Nginx is a powerful web server that can serve static content, act as a reverse proxy, handle SSL encryption, and serve frontend applications efficiently. This document covers:
- Installing and configuring Nginx as a web server
- Setting up Nginx as a reverse proxy
- Enabling SSL using Let's Encrypt
- Configuring DNS for domain resolution
- Serving frontend applications like React, Vue, or Angular

---

## 🛠 Installation & Setup
### Install Nginx (Fedora)
```sh
sudo dnf install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```
### Check Status
```sh
sudo systemctl status nginx
```

### Configure Firewall (if needed)
```sh
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --reload
```

---

## 🌍 Configuring Nginx as a Web Server
### Serving Static Files
1. Navigate to the default web directory:
    ```sh
    cd /usr/share/nginx/html/
    ```
2. Create an `index.html` file:
    ```sh
    echo "<h1>Welcome to My Nginx Web Server</h1>" | sudo tee index.html
    ```
3. Restart Nginx:
    ```sh
    sudo systemctl restart nginx
    ```
4. Open a browser and visit `http://localhost`.

---

## 🔄 Configuring Nginx as a Reverse Proxy
### Example: Proxy Requests to a Flask Backend
1. Edit the Nginx configuration:
    ```sh
    sudo nano /etc/nginx/nginx.conf
    ```
2. Add the following inside the `server` block:
    ```nginx
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ```
3. Restart Nginx:
    ```sh
    sudo systemctl restart nginx
    ```
4. Ensure your backend (e.g., Flask) is running on port `5000`.

---

## 🔐 Enabling SSL with Let's Encrypt
### Install Certbot
```sh
sudo dnf install certbot python3-certbot-nginx -y
```
### Obtain SSL Certificate
```sh
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```
### Auto-Renew SSL Certificate
```sh
sudo crontab -e
```
Add:
```sh
0 0 * * * certbot renew --quiet
```

---

## 🌐 Configuring DNS for Domain Resolution
- Register a domain (e.g., from Cloudflare, GoDaddy).
- Set `A` record to point to your server's IP.
- Verify DNS using:
  ```sh
  nslookup yourdomain.com
  ```

---

## 🚀 Serving Frontend Applications
### Deploying a React App
1. Build the React project:
    ```sh
    npm run build
    ```
2. Copy build files to Nginx web directory:
    ```sh
    sudo cp -r build/* /usr/share/nginx/html/
    ```
3. Configure Nginx:
    ```sh
    sudo nano /etc/nginx/nginx.conf
    ```
4. Modify the `server` block:
    ```nginx
    server {
        listen 80;
        server_name yourdomain.com;
        root /usr/share/nginx/html;
        index index.html;
        location / {
            try_files $uri /index.html;
        }
    }
    ```
5. Restart Nginx:
    ```sh
    sudo systemctl restart nginx
    ```

---

## 🎯 Summary
| Feature | Description |
|---------|-------------|
| **Web Server** | Serves static files like HTML, CSS, JS |
| **Reverse Proxy** | Routes requests to backend services |
| **SSL** | Secures communication with HTTPS |
| **DNS** | Maps domain names to IP addresses |
| **Frontend Hosting** | Serves React, Vue, Angular applications |

---


