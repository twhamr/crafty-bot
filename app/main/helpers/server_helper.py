# ------ Libraries ------
from typing import Any
from app.main.classes.servers import ServerRequests


# ------ Classes ------
api_server = ServerRequests()


# ------ Functions ------
def pull_servers() -> list[dict[str, Any]]:
    """
    Pull all servers from Crafty Controller

    Returns
    -------
    servers: list[dict[str, Any]]
        List of servers
    """
    servers = []

    raw_servers = api_server.get_all_servers()

    for server in raw_servers:
        temp = {}
        temp['server_id'] = server['server_id']
        temp['server_name'] = server['server_name']
        temp['server_ip'] = server['server_ip']
        temp['server_port'] = server['server_port']
        temp['type'] = server['type']
        temp['created'] = server['created']

        servers.append(temp)

    return servers


def pull_online() -> list[dict[str, Any]]:
    """
    Pull the online servers in Crafty Controller

    Returns
    -------
    online: list[dict[str, Any]]
        List of online servers
    """
    online = []
    servers = api_server.get_all_servers()

    for server in servers:
        stats = api_server.get_server_stats(server_id=server['server_id'])
        
        if stats['running']:
            temp = {}
            temp['server_id'] = server['server_id']
            temp['server_name'] = server['server_name']
            temp['type'] = server['type']
            temp['started'] = stats['started']
            temp['cpu'] = stats['cpu']
            temp['mem'] = stats['mem']
            temp['mem_percent'] = stats['mem_percent']
            temp['online'] = stats['online']

            online.append(temp)

    return online