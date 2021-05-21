import unittest

from typing import NoReturn
from types import TracebackType

from .enum import ScoringEnum
from .type import ScoreType


_score_format = {
    'pass': (unittest.TestCase, ScoreType),
    'fail': (unittest.TestCase, TracebackType, ScoreType)
}


class ScoringTestResult(unittest.TestResult):
    """"""

    def __init__(self, mode: ScoringEnum, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.scores = []
        self.total = 0
        self.mode = mode

    def addSuccess(self, test: unittest.TestCase) -> NoReturn:
        self.total += test.pass_score
        self.scores.append({
            'case': test.test_name,
            'score': test.pass_score,
            'hidden': test.test_hidden
        })

    def addError(self, test, err):
        self.errors.append({
            'case': test.test_name,
            'reason': self._exc_info_to_string(err, test)
        })
        # self._mirrorOutput = True

    def addFailure(self, test, err):
        self.total += test.fail_score
        self.failures.append({
            'case': test.test_name,
            'reason': self._exc_info_to_string(err, test),
            'score': test.fail_score,
            'hidden': test.test_hidden
        })
        # self._mirrorOutput = True

    def stopTestRun(self) -> NoReturn:
        if self.mode is ScoringEnum.ALLPASS and not self.wasSuccessful():
            self.total = 0
