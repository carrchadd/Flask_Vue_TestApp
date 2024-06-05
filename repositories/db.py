from psycopg_pool import ConnectionPool

pool = None

def get_pool():
    global pool
    if pool is None:
        pool = ConnectionPool(
            conninfo=os.getenv('DB_CONN_STRING', ''),
        )
    return pool

