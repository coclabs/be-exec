from models import Code
from fastapi import Request
from services.code_execute_service import ExecuteService


async def send_pong(item: Request):
    return await item.json()


async def execute_code(item: Code):
    try:
        result = ExecuteService(item.code, item.context).service()
        response_data = {
            'errors': result.errors,
            'failures': result.failures,
            'successes': result.scores,
            'total': result.total
        }
    except SyntaxError:
        import traceback
        import json
        response_data = {
            'code': 500,
            'reason': traceback.format_exc(limit=0, chain=False)
        }
    return response_data
