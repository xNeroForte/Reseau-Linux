# TP5 : Hébergement d'une solution libre et opensource

Le but de ce TP est de remettre en oeuvre les compétences acquises au fil de l'année.

On va donc s'exercer autour de l'hébergement d'une solution que vous aurez choisi.

Seule contrainte pour le choix de la solution : elle doit être libre et opensource.

Votre tâche consiste à :

- choisir une solution libre et opensource
- mettre en place la solution
  - installation, configuration, lancement
  - accéder à la solution : tester qu'elle fonctionne
- amélioration de la solution
  - sécurité & robustesse
  - respect des bonnes pratiques

> Ce TP s'apparente donc beaucoup aux TP2 et TP3 que nous avons réalisé ensemble (install de NextCloud + amélioration de la solution).

Le TP s'effectue à 2 ou seul.

## Sommaire

- [TP5 : Hébergement d'une solution libre et opensource](#tp5--hébergement-dune-solution-libre-et-opensource)
  - [Sommaire](#sommaire)
  - [Déroulement](#déroulement)
    - [Choix de la solution](#choix-de-la-solution)
    - [Mise en place de la solution](#mise-en-place-de-la-solution)
    - [Maîtrise de la solution](#maîtrise-de-la-solution)
    - [Amélioration de la solution](#amélioration-de-la-solution)
  - [Rendu attendu](#rendu-attendu)

## Déroulement

### Choix de la solution

Nous allons configurer Jellyfin, une plateforme d'hébergement muu=ltimédia, de façon à pouvoir streamer de la musique à distance.

### Mise en place de la solution

- Installation de Docker en suivant la [documentation officielle](https://docs.docker.com/engine/install/centos/).
- Mise en place d'un container Jellyfin en suivant la [documentation](https://jellyfin.org/docs/general/administration/installing#docker)

### Maîtrise de la solution

Une fois en place, posez-vous les questions pour comprendre ce qui a été mis en place, plus en détail. Réfléchissez avec les outils et concepts qu'on a vus en cours :

- y a-t-il un fichier de conf ?
- combien de programmes y a-t-il ?
  - et donc quels processus ?
  - sous quelle identité, quel user, tournent chacun de ces processus ?
- où sont stockées les données de l'application ?
  - dans quel dossier ?
  - y a-t-il une base de données ?
- sur quel(s) port(s) écoute la solution ?
- comment on gère le sycle de vie de l'app ?
  - c'est un service ? un conteneur ? autre chose ?
  - où sont les logs ?
- l'architecture et/ou la conf de la solution respectent-elles les bonnes pratiques élémentaires ?
  - un service par machine (ou un service par conteneur)
  - base de données sur une machine dédiée
  - gestion correcte des utilisateurs et des permissions

### Amélioration de la solution

Cette partie dépendra beaucoup de la solution que vous avez retenu. Pensez comme au TP3.

Chaque brique peut-être améliorée, d'un point de vue sécurité, performances, ou facilité la maintenabilité.

Quelques exemples :

- redondance
  - réplication de base de données
  - répartition de charges entre deux serveurs applicatifs
    - par ex, deux serveurs web pour accueillir 2x plus de clients sur un site web
- sécurité d'accès
  - mise en place d'un HTTPS pour un site web
- performances
  - ne pas utiliser les serveurs web des langages, mais préférer un serveur web dédié
  - préférez un php-fpm qu'un php géré par la machine
- autres, dépendant de la solution choisie

On pensera aussi, en plus de l'amélioration de chaque brique, au maintien en conditions opérationelles, notamment :

- monitoring + alerting
- sauvegarde + test de restauration
- documentation (ça, c'est votre compte-rendu)

## Rendu attendu

Vous livrerez dans un dossier dédié, dans le dépôt git de rendu habituel :

- une documentation d'installation
  - format Markdown
  - c'est l'ensemble des opérations à réaliser pour mettre en place votre solution
    - la suite des commandes donc
    - mais pas que, suivant vos sujets
  - vous livrerez aussi les fichiers nécessaires à la mise en place
    - fichiers de conf
    - `docker-compose.yml`
    - etc.
