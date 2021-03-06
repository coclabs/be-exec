import unittest

from typing import NoReturn

from .result import ScoringTestResult


class ScoringTestRunner(unittest.TextTestRunner):
    """"""

    def __init__(self, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)

    def _makeResult(self) -> unittest.TestResult:
        _args = [self.stream, self.descriptions, self.verbosity]
        if self.resultclass is ScoringTestResult:
            from .enum import ScoringEnum
            _args.insert(0, ScoringEnum.PASSONLY)
        return self.resultclass(*_args)
