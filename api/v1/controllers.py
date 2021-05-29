from models import Any, Code
from services.code_execute_service import ExecuteService


async def send_pong(item: Any):
    return item


async def execute_code(item: Code):
    result = ExecuteService(item.code, item.context).service()
    response_data = {
        'errors': result.errors,
        'failures': result.failures,
        'successes': result.scores,
        'total': result.total
    }
    return response_data
