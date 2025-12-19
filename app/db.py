def get_conn():
    conn = sqlite3.connect("db.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS deals (
            id TEXT PRIMARY KEY,
            crm_id TEXT,
            raw_text TEXT,
            created_at TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS battlecards (
            id TEXT PRIMARY KEY,
            competitor TEXT,
            json TEXT,
            created_at TEXT
        )
    """)

    conn.commit()