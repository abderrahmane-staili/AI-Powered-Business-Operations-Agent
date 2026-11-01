from services import db
from services.playwright_client import run_browser_actions
from utils.logger import get_logger

log = get_logger("orchestrator")

SENSITIVE = {"send_email", "delete", "payment"}

async def handle_sales(payload):     return {"note": "sales agent not implemented yet"}
async def handle_support(payload):   return {"note": "support agent not implemented yet"}
async def handle_email(payload):     return {"note": "email agent not implemented yet"}
async def handle_analytics(payload): return {"note": "analytics agent not implemented yet"}

async def handle_browser(payload):
    return await run_browser_actions(payload.get("actions", []))

AGENTS = {
    "sales": handle_sales,
    "support": handle_support,
    "email": handle_email,
    "analytics": handle_analytics,
    "browser": handle_browser,
}

async def dispatch(task: dict) -> dict:
    agent = task["agent"]
    payload = task["payload"]
    handler = AGENTS.get(agent)
    if not handler:
        db.update_task(task["id"], "failed", error=f"Unknown agent: {agent}")
        return {"status": "failed", "error": f"Unknown agent: {agent}"}

    if payload.get("action") in SENSITIVE:
        db.update_task(task["id"], "awaiting_approval")
        return {"status": "awaiting_approval"}

    try:
        db.update_task(task["id"], "running")
        result = await handler(payload)
        db.update_task(task["id"], "done", result=result)
        return {"status": "done", "result": result}
    except Exception as e:
        log.exception("Task %s failed", task["id"])
        db.update_task(task["id"], "failed", error=str(e))
        return {"status": "failed", "error": str(e)}
