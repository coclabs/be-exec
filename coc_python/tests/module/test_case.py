# import testscore
# testscore.assert_equal(actual, expected[, pass_score][, fail_score])
# testscore.assert_equal(hello_world(), 'hello world')
# testscore.assert_equal(hello_world(), 'hello world', pass_score=5)
# testscore.assert_equal(hello_world(), 'hello world!', fail_score=1)

import testscore
import random

calculator = Calculator()


def my_cal(_x, _y, _o):
    if _o == '+': return _x + _y
    if _o == '-': return _x - _y
    if _o == '*': return _x * _y
    if _o == '/': return _x / _y
    if _o == '%': return _x % _y


# fixed tests
testscore.assert_equal(calculator.calculate(3, 5, '+'), 8, pass_score=3)
testscore.assert_equal(calculator.calculate(3, 5, '-'), -2)
testscore.assert_equal(calculator.calculate(3, 5, '*'), 15)
testscore.assert_equal(calculator.calculate(3, 5, '/'), 0.6, pass_score=5)
testscore.assert_equal(calculator.calculate(3, 5, '%'), 3)

# error tests will not occurs in this releases

# failure tests
testscore.assert_equal(calculator.calculate(3, 5, '%'), 5)
testscore.assert_equal(calculator.calculate(3, 5, '-'), -4)

# random tests
for _ in range(random.randint(2, 5)):
    _x = random.random() * 100
    _y = random.random() * 100
    _o = ('+', '-', '*', '/', '%')[random.randint(0, 4)]
    _s = random.randint(0, 2)
    testscore.assert_equal(calculator.calculate(_x, _y, _o), my_cal(_x, _y, _o), pass_score=_s)
