# ------ Libraries ------
from typing import Any
from app.main.api.servers import ServerRequests


# ------ Classes ------
api_server = ServerRequests()

class ActionError(Exception):
    pass


# ------ Functions ------
def pull_server(server_id: str) -> dict[str, Any]:
    """
    Pull the public data for a server

    Parameters
    ----------
    server_id: str
        Unique ID for the server

    Returns
    -------
    server.data: dict[str, Any]
        Server public data stored in a dict
    """
    server = api_server.get_server_public_data(server_id=server_id)
    
    return server['data']

def pull_servers() -> list[dict[str, Any]]:
    """
    Pull all servers from Crafty Controller

    Returns
    -------
    servers: list[dict[str, Any]]
        List of servers
    """
    servers = []
    raw = api_server.get_all_servers()
    
    for server in raw['data']:
        public_data = pull_server(server_id=server['server_id'])
        
        servers.append(public_data)
    
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

    for server in servers['data']:
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

def send_action(server_id: str, action: str) -> None:
    response = api_server.send_server_action(server_id=server_id, action=action)

    try:
        if response['status']:
            pass
    except:
        raise ActionError(f"The action [{action}] has failed")