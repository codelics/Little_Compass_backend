from fastapi import APIRouter
from ..models import MessageRequest, MessageResponse
from ..utils.logger import log_conversation
from ..services.vectorshift import call_vectorshift

router = APIRouter()

@router.post("/chat", response_model=MessageResponse)
async def chat(req: MessageRequest):
    # 1. log incoming
    log_conversation(req.message, "", latest_user_message=True)

    # 2. call Vectorshift
    resp = await call_vectorshift(req.message)
    if "error" in resp:
        return {"reply": resp["error"]}

    output = resp.get("outputs", {}).get("output_0", "No response provided.")
    output = str(output)

    # 3. log bot reply
    log_conversation(req.message, output)

    return {"reply": output}
