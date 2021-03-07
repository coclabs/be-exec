"""
Topic: Your very first simple Calculator!
Difficulty: Very Easy
Score: 5
Mode: Normal
Category: Arithmetic, Operator, Python

Write a simple class Calculator which take no extra arguments to the init and /
contains method calculate that capable of producing output of simple formula and /
simple operation includes +, -, *, /, %.

Example test cases
> assert_equal(calculator.calculate(x, y, '+', z)
> assert_equal(calculator.calculate(x, y, '-', z)
> assert_equal(calculator.calculate(x, y, '*', z)
> assert_equal(calculator.calculate(x, y, '/', z)
> assert_equal(calculator.calculate(x, y, '%', z)
"""

# Simple solution
from numbers import Number
from typing import Union, Final, NoReturn

SimpleNumber: Final = Union[int, float]


class Calculator:
    """A very simple Calculator"""

    class Operator:
        """A very simple Operator class for Calculator"""

        supported_operation = ('+', '-', '*', '/', '%')

        class OperatorNotSupported(Exception):
            pass

        def __init__(self, _o: str) -> NoReturn:
            try:
                self._o = next(filter(lambda _e: _e == _o, self.supported_operation))
            except StopIteration:
                raise self.OperatorNotSupported(
                    f'Operator {_o} not supported, must be one of {", ".join(self.supported_operation)}')

        def operate(self, _x: SimpleNumber, _y: SimpleNumber) -> Number:
            return eval(f'_x {self._o} _y')  # Eval is evil and must be avoided as much as possible

    def calculate(self, _x: SimpleNumber, _y: SimpleNumber, _o: str) -> Number:
        operation = self.Operator(_o)
        return operation.operate(_x, _y)
