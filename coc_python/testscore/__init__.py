from types import MethodType
from typing import Optional, Any

from .case import *
from .result import *
from .runner import *
from .loader import *
from .suite import *

from .decorator import TestCaseDecorator


class _TestCodeScore(TestCase):
    """"""

    def __init__(self, test_name, pass_score, fail_score, test_description, test_hidden, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.test_name = test_name
        self.pass_score = pass_score
        self.fail_score = fail_score
        self.test_description = test_description
        self.test_hidden = test_hidden


def main(code, test, score: ScoringEnum = ScoringEnum.ANYPASS, verbosity: int = 0) -> ScoringTestResult:
    from os import devnull

    _testcase_class = _TestCodeScore
    _test_suite = ScoringTestSuite()
    _test_loader = unittest.defaultTestLoader
    _test_result = ScoringTestResult
    _test_runner = ScoringTestRunner
    _test_counter = 0

    @TestCaseDecorator.Scoring(0)
    def assert_equal(actual: Optional[Any], expected: Optional[Any],
                     pass_score: ScoreType, fail_score: ScoreType,
                     description: str = '', hidden: bool = False) -> NoReturn:
        nonlocal _test_counter
        _test_counter += 1
        _testcase_instance = _testcase_class(f'testcase-{_test_counter}', pass_score, fail_score, description, hidden)
        _testcase_instance.runTest = MethodType(lambda self: self.assertEqual(actual, expected), _testcase_instance)
        _test_suite.addTest(_testcase_instance)

    _code_object = compile(code, f'<code>', 'exec', optimize=2)
    _test_code_object = compile(test, f'<test>', 'exec', optimize=2)
    exec(_code_object, locals(), locals())
    exec(_test_code_object, locals(), locals())

    _runner = _test_runner(stream=open(devnull, 'w'), resultclass=_test_result, mode=score)
    _result = _runner.run(_test_suite)
    _test_suite._tests = []
    _test_counter = 0

    if verbosity > 0:
        print('errors:', _result.errors)
        print('failures:', _result.failures)
        print('successes:', _result.scores)

    return _result
