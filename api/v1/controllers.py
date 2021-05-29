from models import Code
from fastapi import Request
from services.code_execute_service import ExecuteService


async def send_pong(item: Request):
    return await item.json()


async def execute_code(item: Code):
    result = ExecuteService(item.code, item.context).service()
    response_data = {
        'errors': result.errors,
        'failures': result.failures,
        'successes': result.scores,
        'total': result.total
    }
    return response_data
