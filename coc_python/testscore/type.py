from typing import Union, Callable, Any, Protocol

ScoreType = Union[int, float]
WrapperType = Callable[..., Any]


class ScoringType(Protocol):
    """"""
    def __call__(self, *args, pass_score: ScoreType, fail_score: ScoreType, **kwargs) -> Any: ...
