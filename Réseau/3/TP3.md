# TP3 : On va router des trucs

## I. ARP

### 1. Echange ARP

🌞**Générer des requêtes ARP**

- On fait un `ping` entre les deux machines:

```bash
[admin@john ~]$ ping -c 1 10.3.1.12
PING 10.3.1.12 (10.3.1.12) 56(84) bytes of data.
64 bytes from 10.3.1.12: icmp_seq=1 ttl=64 time=1.79 ms

--- 10.3.1.12 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.793/1.793/1.793/0.000 ms
[admin@john ~]$
```

- On observe les tables ARP des deux machines avec `ip a`:

```bash
MAC de John: 08:00:27:8d:65:07
MAC de Marcel: 08:00:27:03:57:6e

[admin@marcel ~]$ ip neigh show dev enp0s8
10.3.1.0 lladdr 0a:00:27:00:00:05 REACHABLE
10.3.1.11 lladdr 08:00:27:03:57:6e REACHABLE
```

- prouvez que l'info est correcte (que l'adresse MAC que vous voyez dans la table est bien celle de la machine correspondante)
  - une commande pour voir la MAC de `marcel` dans la table ARP de `john`

```bash
[admin@marcel ~]$ ip neigh show 10.3.1.11
10.3.1.11 dev enp0s8 lladdr 08:00:27:03:57:6e REACHABLE
```

- et une commande pour afficher la MAC de `marcel`, depuis `marcel`

```bash
ip a
```

### 2. Analyse de trames

🌞**Analyse de trames**

- utiliser la commande `tcpdump` pour réaliser une capture de trame:

```bash
# On vide les tables ARP, sur les deux machines, puis effectuez un `ping`
[admin@john ~]$ sudo ip -s -s neigh flush all

[admin@marcel ~]$ ping 10.3.1.11
PING 10.3.1.11 (10.3.1.11) 56(84) bytes of data.
64 bytes from 10.3.1.11: icmp_seq=1 ttl=64 time=0.960 ms
64 bytes from 10.3.1.11: icmp_seq=2 ttl=64 time=0.589 ms
64 bytes from 10.3.1.11: icmp_seq=3 ttl=64 time=0.838 ms
64 bytes from 10.3.1.11: icmp_seq=4 ttl=64 time=1.55 ms
64 bytes from 10.3.1.11: icmp_seq=5 ttl=64 time=0.686 ms
^C
--- 10.3.1.11 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 3996ms
rtt min/avg/max/mdev = 0.589/0.924/1.550/0.337 ms

```

🦈 **Capture réseau `tp2_arp.pcapng`** qui contient un ARP request et un ARP reply
[Trame ARP](./Pics/tp2_arp.pcap)

## II. Routage

| Machine  | `10.3.1.0/24` | `10.3.2.0/24` |
| -------- | ------------- | ------------- |
| `router` | `10.3.1.254`  | `10.3.2.254`  |
| `john`   | `10.3.1.11`   | no            |
| `marcel` | no            | `10.3.2.12`   |

`

### 1. Mise en place du routage

🌞**Activer le routage sur le noeud `router`**

```bash
[admin@router ~]$ cat /etc/sysctl.d/router.conf
net.ipv4.ip_forward=1
[admin@router ~]$ cat /proc/sys/net/ipv4/ip_forward
1
```

🌞**Ajouter les routes statiques nécessaires pour que `john` et `marcel` puissent se `ping`**

- il faut ajouter une seule route des deux côtés

```bash
#De manière temporaire
[admin@john ~]$ sudo ip route add 10.3.1.0/24 via 10.3.1.254 dev enp0s8
#Définitivement
[admin@john ~]$ cat /etc/sysconfig/network-scripts/route-enp0s8
10.3.2.0/24 via 10.3.1.254 dev enp0s8
#On vérifie que la route soit en place
[admin@john ~]$ ip route show
default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 metric 100
10.3.2.0/24 via 10.3.1.254 dev enp0s8
```

- une fois les routes en place, vérifiez avec un `ping` que les deux machines peuvent se joindre

```bash
[admin@marcel ~]$ ping -c 5 10.3.1.11
PING 10.3.1.11 (10.3.1.11) 56(84) bytes of data.
64 bytes from 10.3.1.11: icmp_seq=1 ttl=63 time=2.82 ms
64 bytes from 10.3.1.11: icmp_seq=2 ttl=63 time=1.99 ms
64 bytes from 10.3.1.11: icmp_seq=3 ttl=63 time=1.90 ms
64 bytes from 10.3.1.11: icmp_seq=4 ttl=63 time=1.97 ms
64 bytes from 10.3.1.11: icmp_seq=5 ttl=63 time=1.66 ms

--- 10.3.1.11 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4042ms
rtt min/avg/max/mdev = 1.662/2.068/2.821/0.394 ms
```

### 2. Analyse de trames

🌞**Analyse des échanges ARP**

- On vide les tables ARP des trois noeuds avec `sudo ip neigh flush all`
- effectuez un `ping` de `john` vers `marcel`

```
[admin@john ~]$ ping -c1 10.3.2.12
PING 10.3.2.12 (10.3.2.12) 56(84) bytes of data.
64 bytes from 10.3.2.12: icmp_seq=1 ttl=63 time=3.91 ms

--- 10.3.2.12 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 3.908/3.908/3.908/0.000 ms
```

- On enregistre la trame sur `marcel`

| ordre | type trame  | IP source            | MAC source                   | IP destination       | MAC destination              |
| ----- | ----------- | -------------------- | ---------------------------- | -------------------- | ---------------------------- |
| 1     | Requête ARP | x                    | `john` `08:00:27:03:57:6e`   | x                    | Broadcast `FF:FF:FF:FF:FF`   |
| 2     | Réponse ARP | `marcel` `10.3.2.12` | `marcel` `08:00:27:8d:65:07` | x                    | `john` `AA:BB:CC:DD:EE`      |
| 3     | Ping        | `john` `10.3.1.11`   | `john` `08:00:27:03:57:6e`   | `marcel` `10.3.2.12` | `marcel` `08:00:27:8d:65:07` |
| 4     | Pong        | `marcel` `10.3.2.12` | `marcel` `08:00:27:8d:65:07` | `john` `10.3.1.11`   | `marcel` `08:00:27:8d:65:07` |
| 5     | Requête ARP | `marcel` `10.3.2.12` | `marcel` `08:00:27:8d:65:07` | `john` `10.3.1.11`   | `john` `08:00:27:03:57:6e`   |
| 6     | Réponse ARP | `john` `10.3.1.11`   | `john` `08:00:27:03:57:6e`   | `marcel` `10.3.2.12` | `marcel` `08:00:27:8d:65:07` |

🦈 **Capture réseau `tp2_routage_marcel.pcapng`**
![Capture réseau](./Pics/tp2_routage_marcel.pcapng)
