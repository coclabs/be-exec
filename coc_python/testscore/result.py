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
        self.mode = mode

    def addSuccess(self, test: unittest.TestCase) -> NoReturn:
        pass_score = test.pass_score
        self.scores.append((test, pass_score))

    def stopTestRun(self) -> NoReturn:
        if self.mode is ScoringEnum.PASSONLY and not self.wasSuccessful():
            self.scores = [(score[0], 0) for score in self.scores]
