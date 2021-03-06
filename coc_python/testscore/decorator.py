from typing import Any, Optional

from .type import ScoreType, ScoringType, WrapperType


class TestCaseDecorator:
    """"""

    class Scoring:
        """"""

        def __new__(cls, pass_score: ScoreType, fail_score: ScoreType = 0) -> WrapperType:
            def outer_wrapper(method: ScoringType) -> WrapperType:
                def inner_wrapper(*args, **kwargs) -> Optional[Any]:
                    if not isinstance(kwargs.get('pass_score'), (int, float)):
                        kwargs.update({'pass_score': pass_score})
                    if not isinstance(kwargs.get('fail_score'), (int, float)):
                        kwargs.update({'fail_score': fail_score})
                    return method(*args, **kwargs)

                return inner_wrapper

            return outer_wrapper

    class TestMethodName:
        ...
