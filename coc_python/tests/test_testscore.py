import unittest
import testscore


class TestReturnResult(unittest.TestCase):
    """"""

    @classmethod
    def setUpClass(cls) -> None:
        testscore.assert_equal(1, 1, pass_score=2)
        testscore.assert_equal(1, 2, fail_score=1)
        cls._test_result = testscore.main()

    def test_result_type(self):
        self.assertIsInstance(TestReturnResult._test_result, unittest.TestResult)

    def test_result_score_success(self):
        self.assertTrue(hasattr(TestReturnResult._test_result, 'scores'))

    def test_result_score_failure(self):
        self.assertTrue(len(TestReturnResult._test_result.failures[0]) == 3)
