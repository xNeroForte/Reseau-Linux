# TP4 : Conteneurs

# I. Docker

🖥️ Machine **docker1.tp4.linux**

## 1. Install

🌞 **Installer Docker sur la machine**

- On insstalle Docker avec les commandes suivantes:

```bash
[user@localhost ~]$ sudo dnf install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
Complete!
```

- On démarre Docker:

```bash
[user@localhost ~]$ sudo systemctl start docker
```

- On s'ajoute au groupe `docker`:

```bash
[user@localhost ~]$ sudo usermod -aG docker user
#On vérifie
[user@localhost ~]$ groups user
user : user wheel docker
```

## 2. Vérifier l'install

```bash
[user@docker1 ~]$ docker info
Client:
 Context:    default
 Debug Mode: false
 Plugins:
  app: Docker App (Docker Inc., v0.9.1-beta3)
  buildx: Docker Buildx (Docker Inc., v0.9.1-docker)
  compose: Docker Compose (Docker Inc., v2.12.2)
  scan: Docker Scan (Docker Inc., v0.21.0)
...

[user@docker1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[user@docker1 ~]$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
975a2b3de672   hello-world   "/hello"   19 minutes ago   Exited (0) 19 minutes ago             interesting_colden
[user@docker1 ~]$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    feb5d9fea6a5   14 months ago   13.3kB

[user@docker1 ~]$ docker run debian
Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
a8ca11554fce: Pull complete
Digest: sha256:3066ef83131c678999ce82e8473e8d017345a30f5573ad3e44f62e5c9c46442b
Status: Downloaded newer image for debian:latest

[user@docker1 ~]$ docker run -d debian sleep 99999
05f3a9de4d60b720428ada4696f23cbbeb8ca2b49ac1605aebce4867c61e8b31
[user@docker1 ~]$ docker run -it debian bash
root@8635b292494e:/#

[user@docker1 ~]$ sudo docker exec competent_morse ls
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
[user@docker1 ~]$ sudo docker exec -t competent_morse bash
root@97c17e7cc5d4:/#

```

## 3. Lancement de conteneurs

🌞 **Utiliser la commande `docker run`**

```bash
#on crée le fichier index.html et .conf dans lesquels on pose une config:
#Puis on fait la commande
[user@docker1 ~]$ docker run -d --memory="512m" --cpus="1.0" --name web -v $(pwd)/index.html:/usr/share/nginx/html/index.html -v $(pwd)/nginx.conf:/etc/nginx/conf.d/nginx.conf nginx
69ca1ca6f8610ff029e89430573c05aad0c2e4fff15061f032d8a949b2366c12
[user@docker1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS     NAMES
69ca1ca6f861   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    web

```

# II. Images

## 1. Construisez votre propre Dockerfile

🌞 **Construire votre propre image**
📁 **`Dockerfile`**

```bash
FROM debian

RUN apt update -y

RUN apt upgrade -y

RUN apt install apache2 -y

ADD . /etc/apache2/logs/

COPY ./index.html /var/www/html/index.html

COPY ./apache2.conf	/etc/apache2/apache2.conf

CMD ["apache2", "-D", "FOREGROUND"]

```

# III. `docker-compose`

(WIP)
