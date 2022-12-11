#Monitoring avec Netdata

- On procède à une installation locale en suivant [ce lien](https://wiki.crowncloud.net/?How_to_Install_Netdata_on_Rocky_Linux_9).

- On vérifie que la surveillance a bien été mise en place en entrant dans le navigateur:

```bash
http://localhost:19999
```

ou

```bash
http://10.105.1.11:19999
```

## Rattacher Netdata à Discord

**Depuis Dicord:**

- Paramètres du serveur > _Applications_ > _Intégration_
- On génère un nouveau Webhook, qu'on copie-colle dans le fichier de configuration de Netdata.

**Sur notre serveur**

- On modifie le fichier de config de Netdata qui se trouve dans `/etc/netdata/health_alarm_notify`

```bash
[admin@web ~]$ cat /etc/netdata/health_alarm_notify.conf
###############################################################################
# sending discord notifications

# note: multiple recipients can be given like this:
#                  "CHANNEL1 CHANNEL2 ..."

# enable/disable sending discord notifications
SEND_DISCORD="YES"

# Create a webhook by following the official documentation -
# https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/954385479095173140/TJLsBmFZ5gEh-B2rySIliERaxU1M4tJIVbp22762SwJjubYtd3pvwnBq_Ww9ZGnqCvMa"

# if a role's recipients are not configured, a notification will be send to
# this discord channel (empty = do not send a notification for unconfigured
# roles):
DEFAULT_RECIPIENT_DISCORD="alarms"

role_recipients_discord[sysadmin]="test"
role_recipients_discord[dba]="test"
role_recipients_discord[webmaster]="test"

```
