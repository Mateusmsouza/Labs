import os
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import UpdateRowsEvent, WriteRowsEvent
import pymysql

# Configuração do banco de dados
MYSQL_SETTINGS = {
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT", 0)),
    "user": os.getenv("MYSQL_USER"),
    "passwd": os.getenv("MYSQL_PASSWORD")
}
print(MYSQL_SETTINGS)
print("Listening for bug changes...")

# Processa os eventos recebidos
def process_event(event):
    for row in event.rows:
        if isinstance(event, WriteRowsEvent):
            print(f"[NEW BUG] {row}")
        elif isinstance(event, UpdateRowsEvent):
            print(f"[BUG UPDATED] {row}")

while True:
    print("Starting listener")
    # Conectar ao stream de logs binários
    stream = BinLogStreamReader(
        connection_settings=MYSQL_SETTINGS,
        server_id=100,
        only_schemas=["bugzilla"],
        only_tables=["bugs"],
        blocking=True,
        only_events=[WriteRowsEvent, UpdateRowsEvent]
    )


    try:
        print("Startig listening...")
        for binlog_event in stream:
            process_event(binlog_event)
    except KeyboardInterrupt:
        print("Stopping listener...")
    finally:
        stream.close()
