import httpx
from utils.config import PLAYWRIGHT_URL, PLAYWRIGHT_API_KEY

async def run_browser_actions(actions: list[dict]) -> dict:
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(
            PLAYWRIGHT_URL,
            json={"actions": actions},
            headers={"x-api-key": PLAYWRIGHT_API_KEY},
        )
        r.raise_for_status()
        return r.json()
