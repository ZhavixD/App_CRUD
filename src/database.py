import pyodbc

# --- Configuración (Modifica estos valores) ---
SERVER_NAME = 'localhost'       # O tu instancia, ej: '.\SQLEXPRESS'
DATABASE_NAME = 'App_CRUD'    # Nombre de tu base de datos
USERNAME = 'sa'                 # Tu usuario de SQL Server
PASSWORD = 'admin'              # Tu contraseña REAL de SQL Server

# --- Conexión ---
# CONNECTION_STRING = (
#     f'DRIVER={{ODBC Driver 17 for SQL Server}};' # Nombre del driver que tienes
#     f'SERVER={SERVER_NAME};'
#     f'DATABASE={DATABASE_NAME};'
#     f'UID={USERNAME};'
#     f'PWD={PASSWORD}'
# )