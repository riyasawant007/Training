# Apache (httpd) Configuration on Fedora

## Table of Contents
1. [Installation of Apache](#installation-of-apache)
2. [Configuring Apache as a Reverse Proxy](#configuring-apache-as-a-reverse-proxy)
3. [Enabling SSL (HTTPS) with Apache](#enabling-ssl-https-with-apache)
4. [Configuring DNS in Apache](#configuring-dns-in-apache)
5. [Serving a Frontend (HTML Page)](#serving-a-frontend-html-page)
6. [Hiding or Changing Apache Server Name](#hiding-or-changing-apache-server-name)

---

## **1. Installation of Apache**

### **Install Apache on Fedora**
```bash
sudo dnf install httpd -y
```

### **Start and Enable Apache**
```bash
sudo systemctl start httpd
sudo systemctl enable httpd
```

### **Verify Installation**
```bash
sudo systemctl status httpd
```

Apache should now be running on `http://localhost/`.

---

## **2. Configuring Apache as a Reverse Proxy**

### **Enable Required Modules**
```bash
sudo dnf install mod_ssl -y
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart httpd
```

### **Edit Apache Configuration**
```bash
sudo nano /etc/httpd/conf/httpd.conf
```
Add the following configuration:
```apache
<VirtualHost *:80>
    ServerName myproxy.local
    ProxyPass "/app" "http://backend-server-ip:5000/"
    ProxyPassReverse "/app" "http://backend-server-ip:5000/"

    ErrorLog /var/log/httpd/reverse_proxy_error.log
    CustomLog /var/log/httpd/reverse_proxy_access.log combined
</VirtualHost>
```

### **Restart Apache**
```bash
sudo systemctl restart httpd
```

### **Update Hosts File for Local Testing**
```bash
sudo nano /etc/hosts
```
```
127.0.0.1 myproxy.local
```

Test via `http://myproxy.local/app`.

---

## **3. Enabling SSL (HTTPS) with Apache**

### **Install mod_ssl and OpenSSL**
```bash
sudo dnf install mod_ssl openssl -y
```

### **Generate a Self-Signed SSL Certificate**
```bash
sudo openssl req -new -x509 -days 365 -nodes -out /etc/pki/tls/certs/apache-selfsigned.crt -keyout /etc/pki/tls/private/apache-selfsigned.key
```

### **Configure Apache for SSL**
```bash
sudo nano /etc/httpd/conf.d/ssl.conf
```
Modify the following lines:
```apache
<VirtualHost *:443>
    ServerName mysecure.local
    SSLEngine on
    SSLCertificateFile /etc/pki/tls/certs/apache-selfsigned.crt
    SSLCertificateKeyFile /etc/pki/tls/private/apache-selfsigned.key
</VirtualHost>
```

### **Restart Apache and Open HTTPS Port**
```bash
sudo systemctl restart httpd
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --reload
```

Test via `https://mysecure.local`.

---

## **4. Configuring DNS in Apache**

### **Local DNS (For Testing)**
Update the `/etc/hosts` file:
```bash
sudo nano /etc/hosts
```
```
127.0.0.1 mywebsite.local
```

### **Configure Apache Virtual Host**
```bash
sudo nano /etc/httpd/conf.d/mywebsite.conf
```
```apache
<VirtualHost *:80>
    ServerName mywebsite.local
    DocumentRoot "/var/www/mywebsite"
</VirtualHost>
```

Restart Apache:
```bash
sudo systemctl restart httpd
```
Test via `http://mywebsite.local`.

---

## **5. Serving a Frontend (HTML Page)**

### **Create Web Directory and Index Page**
```bash
sudo mkdir -p /var/www/myfrontend
echo "<h1>Welcome to My Apache Frontend</h1>" | sudo tee /var/www/myfrontend/index.html
```

### **Configure Apache Virtual Host**
```bash
sudo nano /etc/httpd/conf.d/myfrontend.conf
```
```apache
<VirtualHost *:80>
    ServerName myfrontend.local
    DocumentRoot "/var/www/myfrontend"
</VirtualHost>
```

### **Set Permissions and Restart Apache**
```bash
sudo chown -R apache:apache /var/www/myfrontend
sudo chmod -R 755 /var/www/myfrontend
sudo systemctl restart httpd
```

Update `/etc/hosts`:
```
127.0.0.1 myfrontend.local
```

Test via `http://myfrontend.local`.

---

## **6. Hiding or Changing Apache Server Name**

### **Hide Apache Version Information**
Edit `httpd.conf`:
```bash
sudo nano /etc/httpd/conf/httpd.conf
```
Add:
```apache
ServerTokens Prod
ServerSignature Off
```
Restart Apache:
```bash
sudo systemctl restart httpd
```
Test:
```bash
curl -I http://localhost
```
Expected output:
```
Server: Apache
```

### **Modify Apache Server Header**
Enable `mod_headers`:
```bash
sudo dnf install mod_headers -y
```
Modify `httpd.conf`:
```apache
<IfModule mod_headers.c>
    Header set Server "MyCustomServer"
</IfModule>
```
Restart Apache:
```bash
sudo systemctl restart httpd
```
Test:
```bash
curl -I http://localhost
```
Expected output:
```
Server: MyCustomServer
```

---



