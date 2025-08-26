# database_connections.py

import pyodbc
from config import DSN_CONFIG

def get_db_connection(dsn_name: str):
    """
    Creates and returns a pyodbc database connection.

    Args:
        dsn_name (str): The key for the DSN in the config file (e.g., 'v12live').

    Returns:
        A pyodbc connection object or None if an error occurs.
    """
    dsn = DSN_CONFIG.get(dsn_name)
    if not dsn:
        print(f"❌ DSN '{dsn_name}' not found in config.")
        return None
    
    try:
        cnxn_str = f'DSN={dsn}'
        connection = pyodbc.connect(cnxn_str)
        print(f"✅ Connection successful to '{dsn_name}' ({dsn}).")
        return connection
    except pyodbc.Error as ex:
        print(f"❌ Failed to connect to '{dsn_name}' ({dsn}).")
        sqlstate = ex.args[0]
        print(f"    DB-Error: {sqlstate}")
        return None