import sys
import signal

from coc_python import *
from exceptions import CodeExecutionTimeout

from .base_service import BaseService


class ExecuteService(BaseService):

    __slots__ = ('language', 'version', 'code',
                 'test', 'test', 'scoring', 'mode')

    def __init__(self, code, context, timeout=10):
        self.language = code.language
        self.version = code.version
        self.code = code.value
        self.test = context.test
        self.scoring = context.scoring
        self.mode = context.mode
        self.timeout = timeout

    def _timeout_handler(self, signum, frame):
        raise CodeExecutionTimeout(f'Execution time exceeds {self.timeout} seconds')

    def _timeout_init(self):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(self.timeout)

    def service(self, *args, **kwargs):
        if sys.platform.startswith('linux'):
            self._timeout_init()

        exec_result = main(code=self.code, test=self.test, score=self.scoring, verbosity=0)
        return exec_result

