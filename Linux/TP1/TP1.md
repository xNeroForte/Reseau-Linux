# TP1 : (re)Familiaration avec un système GNU/Linux (WIP)

🌞 **Setup de deux machines Rocky Linux configurées de façon basique.**

- **un accès internet (via la carte NAT)**
  ![ping internet](.Images/l1-1.png)

- **un accès à un réseau local** (les deux machines peuvent se `ping`) (via la carte Host-Only)
  ![fichier config](.Images/l1-2.png)

- La deuxième machine aura pour adresse `10.101.1.12`
  ![ping réseau local](./Images/l1-3.png)

- **vous n'utilisez QUE `ssh` pour administrer les machines**
  ![ssh](./Images/l1-4.png)

- **les machines doivent avoir un nom**
- Après avoir effectué les commandes suivantes:
  `node hostname <nom machine>` (changement provisoire)
  puis `echo 'vm1.tp1.b3' | sudo tee /etc/hostname` (changement permanent, effectif après redémarrage)
  ![hostname](./Images/l1-5.png)
- La seconde machine aura pour nom `10.101.1.12`

- **utiliser `1.1.1.1` comme serveur DNS**
  ![dns](.Images/l1-6.png)

- **les machines doivent pouvoir se joindre par leurs noms respectifs**
  ![ping](./Images/l1-7.png)

- **le pare-feu est configuré pour bloquer toutes les connexions exceptées celles qui sont nécessaires**
  ![ping](./Images/l1-8.png)

## I. Utilisateurs

### 1. Création et configuration

🌞 **Ajouter un utilisateur à la machine**, qui sera dédié à son administration
![nouvel utilisateur](./Images/l1-9.png)

🌞 **Créer un nouveau groupe `admins`**

- `sudo groupadd admins`
- on modifie `/etc/sudoers`

🌞 **Ajouter votre utilisateur à ce groupe `admins`**

- `sudo usermod -aG admins admin`

Puis on vérifie:
![nouveau groupe](./Images/l1-10.png)

### 2. SSH

🌞 **Assurez vous que la connexion SSH est fonctionnelle**
(voir premier screen)

## II. Partitionnement

### 1. Préparation de la VM

⚠️ **Uniquement sur `node1.tp1.b2`.**

Ajout de deux disques durs à la machine virtuelle, de 3Go chacun.

### 2. Partitionnement

![partition](.Images/l1-11)

## III. Gestion de services

## 1. Interaction avec un service existant

⚠️ **Uniquement sur `node1.tp1.b2`.**

🌞 **Assurez-vous que l'unité est démarrée et activée**
![start service](./Images/l1-12.png)

## 2. Création de service

![Création de service systemd](./pics/create_service.png)

### A. Unité simpliste

⚠️ **Uniquement sur `node1.tp1.b2`.**

![unit](./Images/l1-13.png)

### B. Modification de l'unité

🌞 **Préparez l'environnement pour exécuter le mini serveur web Python**

- créer un utilisateur `web`
- créer un dossier `/var/www/meow/`
- créer un fichier dans le dossier `/var/www/meow/` (peu importe son nom ou son contenu, c'est pour tester)
- montrez à l'aide d'une commande les permissions positionnées sur le dossier et son contenu

> Pour que tout fonctionne correctement, il faudra veiller à ce que le dossier et le fichier appartiennent à l'utilisateur `web` et qu'il ait des droits suffisants dessus.

🌞 **Modifiez l'unité de service `web.service` créée précédemment en ajoutant les clauses**

- `User=` afin de lancer le serveur avec l'utilisateur `web` dédié
- `WorkingDirectory=` afin de lancer le serveur depuis le dossier créé au dessus : `/var/www/meow/`
- ces deux clauses sont à positionner dans la section `[Service]` de votre unité

🌞 **Vérifiez le bon fonctionnement avec une commande `curl`**
