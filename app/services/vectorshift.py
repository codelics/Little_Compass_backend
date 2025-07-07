import logging
import httpx
from fastapi import HTTPException
from ..config import settings

logger = logging.getLogger(__name__)

async def call_vectorshift(message: str) -> dict:
    url = "https://api.vectorshift.ai/v1/pipeline/6867374d406741292f75d20b/run"
    payload = {
        "inputs": {
            "input_0": {"description": message, "type": "string"}
        }
    }
    headers = {
        "Authorization": f"Bearer {settings.VECTORSHIFT_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            resp = await client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            logger.error("Vectorshift HTTP error", exc_info=e)
            raise HTTPException(status_code=502, detail="AI service returned error")
        except httpx.RequestError as e:
            logger.error("Vectorshift request failed", exc_info=e)
            raise HTTPException(status_code=502, detail="AI service request failed")
        except Exception as e:
            logger.error("Unexpected Vectorshift failure", exc_info=e)
            raise HTTPException(status_code=500, detail="Internal error")
