import pyodbc

# --- Configuración (Modifica estos valores) ---
SERVER_NAME = 'localhost'       # O tu instancia, ej: '.\SQLEXPRESS'
DATABASE_NAME = 'App_CRUD'    # Nombre de tu base de datos
USERNAME = 'sa'                 # Tu usuario de SQL Server
PASSWORD = 'admin'              # Tu contraseña REAL de SQL Server

# --- 1. Crear la cadena de conexión con el DRIVER correcto ---
# NOTA: Asegúrate de que el nombre del DRIVER sea exacto, usando el "ODBC Driver 17 for SQL Server" 
# o el nombre que encontraste en tu Administrador ODBC.
CONNECTION_STRING = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER_NAME};'
    f'DATABASE={DATABASE_NAME};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD}'
)

# --- 2. Establecer la conexión y manejar posibles errores ---
try:
    # Intenta establecer la conexión
    conn = pyodbc.connect(CONNECTION_STRING)
    print("¡Conexión exitosa a SQL Server!")

    # Si la conexión es exitosa, puedes trabajar con la base de datos aquí
    # Por ejemplo, para crear un cursor:
    # cursor = conn.cursor()
    
    # 3. Cerrar la conexión
    conn.close()
    print("Conexión cerrada.")

except pyodbc.Error as ex:
    # Muestra el error específico si falla (credenciales incorrectas, driver, etc.)
    sqlstate = ex.args[0]
    print(f"ERROR DE CONEXIÓN: No se pudo conectar a la base de datos.")
    print(f"Detalles del error: {sqlstate}")
    