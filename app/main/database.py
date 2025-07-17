# tywahamr - Created: 07/13/2025
# This script will initialize database (DB) and create the following tables:
#   - <database>.<table>
#   - crafty.users

# This script will initialize Crafty data stored locally and store them in the following tables:
#   - <local_file> -> <database>.<table>
#   - crafty-users.json -> crafty.users

# Only needs to be ran when initializing DB tables

# ------ Libraries ------
from typing import Any
import pymysql.cursors
import pymysql
import json

from app.handlers.log_handler import LogHandler


# Load DB credentials stored locally
def load_json(filepath: str) -> dict[str, str]:
    # Open file at the given filepath
    with open(filepath, "r") as file:
        # Read JSON file
        data = json.load(file)

    # Return data within JSON file
    return data


class Database:
    def __init__(self) -> None:
        db_creds = load_json("./JSON/credentials/db-creds.json")

        self.emojis = {
            "success": "✅",
            "error": "🚫",
            "alert": "🚨"
        }
        self.logger = LogHandler()

        try:
            # Initialize connection to DB.crafty
            self.conn = pymysql.connect(
                host=db_creds['host'],
                user=db_creds['user'],
                password=db_creds['password'],
                database=db_creds['db'],
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            self.logger.create_log(location="database",
                                   message=f"ERROR: {e} {self.emojis['error']}")


    # ------ Database: Setup ------

    # Create a given table in the DB
    def create_table(self, table: dict[str, Any]) -> None:
        try:
            # Open the given connection and initialize it with a Cursor
            with self.conn.cursor() as cursor:
                # Set sql to be the MySQL code to be executed <table>
                sql = table['sql']
                cursor.execute(sql)

                # Save and commit the changes to the DB
                self.conn.commit()

                self.logger.create_log(location="database",
                                       message=f"SUCCESS: Table [{table['name']}] has been created {self.emojis['success']}")
        except Exception as e:
            self.logger.create_log(location="database",
                                    message=f"ERROR: {e} {self.emojis['error']}")


    # Drop a given table in the DB
    def drop_table(self, table: dict[str, Any]) -> None:
        try:
            # Open the DB connection and initialize it with a Cursor
            with self.conn.cursor() as cursor:
                # Set sql to be the MySQL code to be executed
                sql = f"drop table {table['name']};"
                cursor.execute(sql)
    
                # Save and commit the changes to the DB
                self.conn.commit()

                self.logger.create_log(location="database",
                                       message=f"SUCCESS: Table [{table['name']}] has been dropped {self.emojis['success']}")
        except Exception as e:
            self.logger.create_log(location="database",
                                   message=f"ERROR: {e} {self.emojis['error']}")


    # Load the credentials into the given table
    def load_users(self, data: dict[str, Any]) -> None:
        try:
            # Open the DB connection and initialize it with a Cursor
            with self.conn.cursor() as cursor:
                # Set sql to be the MySQL code to be executed
                sql = "insert into users (username, password, role, api_key) values (%s, %s, %s, %s);"
                cursor.execute(sql, (data['username'], data['password'], data['role'], data['api_key']))

                # Save and commit the changes to the DB
                self.conn.commit()

                self.logger.create_log(location="database",
                                       message=f"SUCCESS: Data has been added to users table {self.emojis['success']}")
        except Exception as e:
            self.logger.create_log(location="database",
                                    message=f"ERROR: {e} {self.emojis['error']}")


    # ------ Database: Requests ------

    # Pull credentials from crafty.credentials
    def pull_user_credentials(self, user_id: int = 1) -> tuple[str, str]:
        try:
            # Open the DB connection and initialize it with a Cursor
            with self.conn.cursor() as cursor:
                # Set sql to be the MySQL code to be executed
                sql = "select username, password from users where id=%s;"
                cursor.execute(sql, user_id)

                # Fetch data returned from execution
                data = cursor.fetchone()

                self.logger.create_log(location="database",
                                       message=f"ALERT: Pulled credentials for user with ID [{user_id}] {self.emojis['alert']}")
        except Exception as e:
            self.logger.create_log(location="database",
                                    message=f"ERROR: {e} {self.emojis['error']}")

        # Return the data collected
        return data['username'], data['password'] # type: ignore

    # Pull API Key from crafty.credentials
    def pull_user_key(self, user_id: int = 1) -> str:
        try:
            # Open the DB connection and initialize it with a Cursor
            with self.conn.cursor() as cursor:
                # Set sql to be the MySQL code to be executed
                sql = "select api_key from users where id=%s;"
                cursor.execute(sql, user_id)

                # Fetch data returned from execution
                data = cursor.fetchone()

                self.logger.create_log(location="database",
                                       message=f"ALERT: Pulled API Key for user with ID [{user_id}] {self.emojis['alert']}")
        except Exception as e:
            self.logger.create_log(location="database",
                                       message=f"ERROR: {e} {self.emojis['error']}")

        # Return the api_key
        return data['api_key'] # type: ignore


def main():
    # Load local JSON files
    crafty_users = load_json("./JSON/credentials/crafty-users.json")


    crafty_db = Database()

    # Set tables as dict types {'name': <name of table>, 'sql': <sql code to be executed>}
    _users = {
        "name": "users",
        "sql": """
        create table users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(150) NOT NULL,
            password VARCHAR(150) NOT NULL,
            role VARCHAR(150) NOT NULL,
            api_key VARCHAR(300) NOT NULL
        ) ENGINE=INNODB;
        """
    }

    # Drop all tables
    crafty_db.drop_table(_users)
    
    # Create all tables
    crafty_db.create_table(_users)

    # Load local file data into tables
    crafty_db.load_users(crafty_users)


if __name__ == "__main__":
    main()