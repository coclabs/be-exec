from ktypes import List
from pydantic import BaseModel


class Any(BaseModel):
    """Any model"""


class Code(BaseModel):
    """A schema for code payload"""

    class CodeObject(BaseModel):
        """A schema for code metadata for code execution."""
        language: str
        version: str
        value: str

    class CodeContext(BaseModel):
        """A schema for context for code execution."""
        test: str
        scoring: str
        mode: str

    code: CodeObject
    context: CodeContext


class CodeExecResult(BaseModel):
    class CodeExecError(BaseModel):
        case: str
        reason: str

    class CodeExecFailure(BaseModel):
        case: str
        reason: str
        score: float
        hidden: bool

    class CodeExecSuccess(BaseModel):
        case: str
        score: float
        hidden: bool

    errors: List[CodeExecError]
    failures: List[CodeExecFailure]
    successes: List[CodeExecSuccess]
    total: float
