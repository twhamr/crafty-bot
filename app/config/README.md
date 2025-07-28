# Configuration

CraftyBot and API configuration settings are found in the main.ini file that generates after running setup_craftybot.sh  
Initialization of main.ini follows a template (as to avoid pushing my own credentials), so it's required for you to fill out the variables with your own information.  

## Settings

There are several configuration settings  

### General

| type   | setting   | default_value    | description                                          |
| :----: | :-------: | :--------------: | :--------------------------------------------------: |
| (str)  | app_name  | "CraftyBot"      | name for application, no need to change              |
| (str)  | version   | current_version  | current version of the CraftyBot, no need to change  |

### API

| type   | setting  | default_value        | description                                                                   |
| :----: | :------: | :------------------: | :---------------------------------------------------------------------------: |
| (str)  | api_url  | YOUR_CRAFTY_API_URL  | the API url_path for Crafty Controller \["https://192.168.1.158:8443/api/v2]  |
| (str)  | api_key  | YOUR_CRAFTY_API_KEY  | the API key for Crafty Controller                                             |

### Discord

| type   | setting    | default_value      | description                                        |
| :----: | :--------: | :----------------: | :------------------------------------------------: |
| (int)  | owner_id   | YOUR_USER_ID       | your Discord User ID                               |
| (int)  | guild_id   | YOUR_SERVER_ID     | your Discord Server ID, for initializing commands  |
| (str)  | bot_token  | DISCORD_BOT_TOKEN  | the bot token for your Discord Bot                 |

### Logging

| type   | setting    | default_value                      | description                                              |
| :----: | :--------: | :--------------------------------: | :------------------------------------------------------: |
| (bool) | enabled    | true                               | logging on/off                                           |
| (str)  | root_path  | ./app/logs                         | directory path to save all log files                     |
| (str)  | timezone   | America/Indiana/Indianapolis       | override timezone for timestamp, use pytz timezones      |