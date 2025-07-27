# Logging

All logs will be saved into this directory by default

## Formatting

Logs will follow the following format:  
* "[timestamp] [category] message"

## Filenames

Files are created and saved per day, and each category has it's own file.  
* "2025-07-22-api.log"
* "2025-07-23-bot.log"

## Configuration

Logging has configuration options within ./config/main.ini  
| type   | setting    | default_value | description                          |
| :----: | :--------: | :-----------: | :----------------------------------: |
| (bool) | enabled    | true          | logging on/off                       |
| (str)  | root_path  | "./logs"      | directory path to save all log files |
| (str)  | timezone   | system        | override timezone for timestamp      |