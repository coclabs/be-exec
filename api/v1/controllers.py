from models import Code
from fastapi import Request
from services.code_execute_service import ExecuteService


async def send_pong(item: Request):
    return await item.json()


async def execute_code(item: Code):
    common_exceptions = Exception, SystemExit
    try:
        result = ExecuteService(item.code, item.context).service()
        response_data = {
            'errors': result.errors,
            'failures': result.failures,
            'successes': result.scores,
            'total': result.total
        }
    except common_exceptions:
        import traceback
        import sys
        exc_limit = -1
        exc_info = {k: v for k, v in
                    [(ek, ev) for ek, ev in
                     zip(['type', 'value', 'tb'],
                         [ex for ex in sys.exc_info()])]}
        exc_type = exc_info.get('type')
        exc_value = exc_info.get('value')
        exc_only = traceback.format_exception_only(exc_type, exc_value)
        if len(exc_only) > 1:
            exc_limit = 0
        elif hasattr(exc_type, 'response_tb_limit'):
            exc_limit = exc_type.response_tb_limit
        response_data = {
            'code': 500,
            'reason': traceback.format_exc(limit=exc_limit, chain=False)
        }
    return response_data
