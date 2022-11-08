I. Setup IP
🌞 Mettre en place une configuration réseau fonctionnelle entre les deux machines:

Afin de contenir au moins 38 adresses reseau, on choisira un masque /26:

**Avec la commande `nmcli con mod "Wired connection 1" ipv4.addresses <x.x.x.x/y>`**
PC 1 aura donc cette adresse: `10.33.0.4/26`
et PC 2 aura l'adresse suivante : `10.33.0.5/26`

L'adresse réseau est `10.33.0.0`
**nmcli con mod "Wired connection 1" ipv4.gateway "10.30.0.1"**
L'adresse broadcast : `10.33.0.1`

La connexion ne fonctionnant pas entre les deux machines pour des raisons qui m'échappent encore, nous passeront directement au III.

III. DHCP you too my brooo
🌞 **Wireshark it**
![trame DORA](Images/dhcp.pcapng)

IV. Avant-goût TCP et UDP
![yt](Images/tcpudp.pcapng)
