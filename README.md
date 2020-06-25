CheckYerFlags
===

A bot notifying when a user reach a certain flag count

Redunda: https://redunda.sobotics.org/bots/26/bot_instances  

## Dependencies
Python 3.6 or newer (default on Ubuntu 18.04 systems)

Run `pip install setuptools --upgrade` if your version is not >= 30  
Run `pip install -r requirements.txt`

## Thanks to the bug hunters
- @K-Davis1
- @geisterfurz007



### List of commands ###
```
del[ete], poof                - Deletes the message replied to, if possible. Requires privileges.
amiprivileged                 - Checks if you're allowed to run privileged commands.
a[live]                       - Replies with a message if the bot is running.
v[ersion]                     - Returns current version.
loc[ation]                    - Returns current location where the bot is running.
say <message>                 - Sends [message] as a chat message.
welcome <username>            - Post a chat room introduction message (only in SOBotics). If the username is specified, the user will also get pinged.
quota                         - Returns the amount of remaining Stack Exchange API quota.
kill, stop                    - Stops the bot. Requires privileges.
standby, sb                   - Tells the bot to go to standby mode. That means it leaves the chat room and a bot maintainer needs to issue a restart manually. Requires privileges.
restart, reboot               - Restarts the bot. Requires privileges.
commands, help                - This command. Lists all available commands.
s[tatus] m[ine]               - Gets your own flag rank and status to the next rank.
s[tatus] <user id>            - Gets flag rank and status to the next rank for the specified <user id>.
goal <flag count> [message]   - Set your custom goal to <flag count> flags. Displays an optional message once you reach your custom rank.
goal del[ete]                 - Deletes our custom goal
ranks, ranks next, r n        - Gets your next flag rank and how much flags you need to get to it. Returns your custom goal if it's closer than the next rank.
uptime                        - Returns how long the bot is running
update                        - Updates the bot to the latest git commit and restarts it. Requires owner privileges.
system                        - Returns uptime, location and api quota.
why                           - Gives the answer to everything.
```
