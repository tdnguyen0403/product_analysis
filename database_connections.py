# database_connections.py

from sqlalchemy import create_engine
from config import DSN_CONFIG

def create_engines():
    """
    Creates a dictionary of SQLAlchemy engines based on the DSNs in config.py.

    Returns:
        dict: A dictionary where keys are the internal DSN names and values
              are the corresponding SQLAlchemy engine objects. Returns an empty
              dictionary if no DSNs are configured.
    """
    engines = {}
    if not DSN_CONFIG:
        print("⚠️ DSN configuration is empty. No engines created.")
        return engines

    for name, dsn in DSN_CONFIG.items():
        try:
            # The connection string format for MS SQL Server with pyodbc
            connection_string = f"mssql+pyodbc:///?odbc_connect=DSN={dsn}"
            engine = create_engine(connection_string)
            engines[name] = engine
            print(f"✅ Engine for '{name}' ({dsn}) created successfully.")
        except Exception as e:
            print(f"❌ Failed to create engine for '{name}' ({dsn}). Error: {e}")
            engines[name] = None
    return engines

# Create the engines when this module is imported
ENGINES = create_engines()