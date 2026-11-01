import json
import psycopg
from psycopg.rows import dict_row
from utils.config import DATABASE_URL

def connect():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)

def create_task(source: str, agent: str | None, payload: dict) -> dict:
    with connect() as conn:
        return conn.execute(
            "INSERT INTO tasks (source, agent, payload) VALUES (%s, %s, %s) RETURNING *",
            (source, agent, json.dumps(payload)),
        ).fetchone()

def get_task(task_id: int) -> dict | None:
    with connect() as conn:
        return conn.execute("SELECT * FROM tasks WHERE id = %s", (task_id,)).fetchone()

def update_task(task_id: int, status: str, result: dict | None = None, error: str | None = None):
    with connect() as conn:
        conn.execute(
            "UPDATE tasks SET status=%s, result=%s, error=%s, updated_at=now() WHERE id=%s",
            (status, json.dumps(result) if result is not None else None, error, task_id),
        )
