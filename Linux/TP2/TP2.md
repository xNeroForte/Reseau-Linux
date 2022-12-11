# TP2 : Gestion de service

# I. Un premier serveur web

## 1. Installation

🌞 **Installer le serveur Apache**
`sudo dnf install httpd -y`
`sudo vim /etc/httpd/conf/httpd.conf`

🌞 **Démarrer le service Apache**
`sudo systemctl start httpd sudo systemctl enable httpd`

🌞 **TEST**

- le service est démarré:
  `superadmin@10.102.1.11's password: Last login: Thu Nov 17 17:29:35 2022 [superadmin@web ~]$ systemctl status httpd ● httpd.service - The Apache HTTP Server Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled) Active: active (running) since Thu 2022-11-17 17:29:16 CET; 1min 22s ago Docs: man:httpd.service(8) Main PID: 680 (httpd) Status: "Total requests: 0; Idle/Busy workers 100/0;Requests/sec: 0; Bytes served/sec: 0 B/sec" Tasks: 213 (limit: 5905) Memory: 32.1M CPU: 169ms CGroup: /system.slice/httpd.service ├─680 /usr/sbin/httpd -DFOREGROUND ├─702 /usr/sbin/httpd -DFOREGROUND ├─704 /usr/sbin/httpd -DFOREGROUND ├─705 /usr/sbin/httpd -DFOREGROUND └─706 /usr/sbin/httpd -DFOREGROUND`

- vérifier qu'on peut joindre le serveur web localement:
``<!doctype html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>HTTP Server Test Page powered by: Rocky Linux</title>
    ...
  </head>
  <body>
    ...
  </body>
</html>
``
- Sur notre PC:
  ``
  <!doctype html>
  <html>
    <head>
      <meta charset='utf-8'>
      <meta name='viewport' content='width=device-width, initial-scale=1'>
      <title>HTTP Server Test Page powered by: Rocky Linux</title>
      <style type="text/css">
        ...
    </style>
    </head>
    <body>
      <h1>HTTP Server <strong>Test Page</strong></h1>
  ... 
    </body>

``

## 2. Avancer vers la maîtrise du service

🌞 **Le service Apache...**

!(screen user)[Images/screenuser.png]

🌞 **Déterminer sous quel utilisateur tourne le processus Apache**

🌞 **Changer l'utilisateur utilisé par Apache**

🌞 **Faites en sorte que Apache tourne sur un autre port**

- modifiez la configuration d'Apache pour lui demander d'écouter sur un autre port de votre choix
- ouvrez ce nouveau port dans le firewall, et fermez l'ancien
- redémarrez Apache
- prouvez avec une commande `ss` que Apache tourne bien sur le nouveau port choisi
- vérifiez avec `curl` en local que vous pouvez joindre Apache sur le nouveau port
- vérifiez avec votre navigateur que vous pouvez joindre le serveur sur le nouveau port

📁 **Fichier `/etc/httpd/conf/httpd.conf`**

```
ServerRoot "/etc/httpd"

Listen 443

Include conf.modules.d/*.conf

User toto
Group toto


ServerAdmin root@localhost


<Directory />
    AllowOverride none
    Require all denied
</Directory>


DocumentRoot "/var/www/html"

<Directory "/var/www">
    AllowOverride None
    Require all granted
</Directory>

<Directory "/var/www/html">
    Options Indexes FollowSymLinks

    AllowOverride None

    Require all granted
</Directory>

<IfModule dir_module>
    DirectoryIndex index.html
</IfModule>

<Files ".ht*">
    Require all denied
</Files>

ErrorLog "logs/error_log"

LogLevel warn

<IfModule log_config_module>
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common
```

# II. Une stack web plus avancée

## 2. Setup

### A. Base de données

🌞 **Install de MariaDB sur `db.tp2.linux`**

- `dnf install mariadb-server`
- `systemctl enable mariadb`
- `systemctl start mariadb`
- `sudo mysql_secure_installation`

- on ouvre le port 80/tcp

🌞 **Préparation de la base pour NextCloud**

🌞 **Exploration de la base de données**

![exploration db](./Images/l2-2-0.png)

🌞 **Trouver une commande SQL qui permet de lister tous les utilisateurs de la base de données**

- Depuis le serveur : `SELECT Host, User FROM mysql.user`
  ![liste users](./Images/l2-2-1.png)

### B. Serveur Web et NextCloud

🌞 **Install de PHP**

```
[superadmin@web ~]$ sudo dnf config-manager --set-enabled crb
[superadmin@web ~]$ sudo dnf install dnf-utils http://rpms.remirepo.net/enterprise/remi-release-9.rpm -y
...
Complete!
[superadmin@web ~]$ dnf module list php
Remi's Modular repository for Enterprise Linux 9 - x86_64
Name              Stream                Profiles                               Summary
php               remi-7.4              common [d], devel, minimal             PHP scripting language
php               remi-8.0              common [d], devel, minimal             PHP scripting language
php               remi-8.1              common [d], devel, minimal             PHP scripting language
php               remi-8.2              common [d], devel, minimal             PHP scripting language
Complete!
[superadmin@web ~]$ sudo dnf install -y php81-php
Complete!

```

🌞 **Install de tous les modules PHP nécessaires pour NextCloud**

```bash
[superadmin@web ~]$ sudo dnf install -y libxml2 openssl php81-php php81-php-ctype php81-php-curl php81-php-gd php81-php-iconv php81-php-json php81-php-libxml php81-php-mbstring php81-php-openssl php81-php-posix php81-php-session php81-php-xml php81-php-zip php81-php-zlib php81-php-pdo php81-php-mysqlnd php81-php-intl php81-php-bcmath php81-php-gmp
Complete!
```

🌞 **Récupérer NextCloud**

```
[superadmin@web ~]$ mv nextcloud/* /var/www/tp2_nextcloud/
[superadmin@web home]$ ls -l /var/www/
drwxr-xr-x. 14 superadmin superadmin 4096 Nov 18 17:35 tp2_nextcloud
```

- après voir modifié les droits de `/var/www/tp2_nextcloud` avec la cmd `sudo chown -R apache:apache ./tp2_nextcloud/`

```
[superadmin@web ~]$ ls -l /var/www/tp2_nextcloud/
total 128
drwxr-xr-x. 47 apache apache  4096 Oct  6 14:47 3rdparty
```

🌞 **Adapter la configuration d'Apache**

```
[superadmin@web tp2_nextcloud]$ sudo nano /etc/httpd/conf/httpd.conf
[superadmin@web tp2_nextcloud]$ sudo nano /etc/httpd/conf.d/nextcloud.conf
```

🌞 **Redémarrer le service Apache** pour qu'il prenne en compte le nouveau fichier de conf

```
[superadmin@web ~]$ curl localhost
<!DOCTYPE html>
<html>
<head>
	<script> window.location.href="index.php"; </script>
	<meta http-equiv="refresh" content="0; URL=index.php">
</head>
</html>

```

### C. Finaliser l'installation de NextCloud

🌞 **Exploration de la base de données**

```
MariaDB [(none)]> use nextcloud
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [nextcloud]> show tables;
+-----------------------------+
| Tables_in_nextcloud         |
+-----------------------------+
| oc_accounts                 |
| oc_accounts_data            |
| ...                         |
+-----------------------------+
95 rows in set (0.002 sec)

```

```
MariaDB [nextcloud]> select count(*) from information_schema.tables where table_schema='nextcloud';
+----------+
| count(*) |
+----------+
|       95 |
+----------+
1 row in set (0.003 sec)
```
