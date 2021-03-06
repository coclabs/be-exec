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

    def __init__(self, pass_score, fail_score, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.pass_score = pass_score
        self.fail_score = fail_score


_testcase_class = _TestCodeScore
_test_suite = ScoringTestSuite()
_test_loader = unittest.defaultTestLoader
_test_result = ScoringTestResult
_test_runner = ScoringTestRunner


@TestCaseDecorator.Scoring(0)
def assert_equal(actual: Optional[Any], expected: Optional[Any],
                 pass_score: ScoreType, fail_score: ScoreType) -> NoReturn:
    _testcase_instance = _testcase_class(pass_score, fail_score)
    _testcase_instance.runTest = MethodType(lambda self: self.assertEqual(actual, expected), _testcase_instance)
    _test_suite.addTest(_testcase_instance)


def main(verbosity: int = 0):
    # Mock user module
    # user source
    # user_source = b'def hello_world():\n\tprint(\'hello world!\')\n\treturn \'hello world!\''
    # user_source_name = '<byte_str>'

    # tests wrappers
    # user_source += b'\nimport testscore'
    # user_source += b'\n'
    # user_source += b'\ntestscore.assert_equal(1, 1)'
    # user_source += b'\nprint("="*50);print(globals());print("="*50)'

    # compiled to code object and exec
    # compiled_source = compile(user_source, user_source_name, 'exec')
    # exec(compiled_source, locals(), locals())

    # Tester
    # assert_equal(locals()['hello_world'](), 'hello world!', pass_score=10)
    # assert_equal(3, 3, pass_score=10)

    _runner = _test_runner(resultclass=_test_result)
    _result = _runner.run(_test_suite)

    if verbosity > 0:
        print(_result.errors)
        print(_result.failures)
        print(_result.scores)

    return _result
