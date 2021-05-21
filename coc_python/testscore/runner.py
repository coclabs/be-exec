import unittest

from typing import NoReturn

from .enum import ScoringEnum
from .result import ScoringTestResult


class ScoringTestRunner(unittest.TextTestRunner):
    """"""

    def __init__(self, mode: ScoringEnum, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.mode = ScoringEnum(mode)

    def _makeResult(self) -> unittest.TestResult:
        _args = [self.stream, self.descriptions, self.verbosity]
        if self.resultclass is ScoringTestResult:
            _args.insert(0, self.mode)
        return self.resultclass(*_args)
