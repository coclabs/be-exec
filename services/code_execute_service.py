from coc_python import *

from .base_service import BaseService


class ExecuteService(BaseService):

    __slots__ = ('language', 'version', 'code',
                 'test', 'test', 'scoring', 'mode')

    def __init__(self, code, context):
        self.language = code.language
        self.version = code.version
        self.code = code.value
        self.test = context.test
        self.scoring = context.scoring
        self.mode = context.mode

    def service(self, *args, **kwargs):
        exec_result = main(code=self.code, test=self.test, score=self.scoring, verbosity=0)
        return exec_result

