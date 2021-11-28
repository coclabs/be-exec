from ktypes import List
from pydantic import BaseModel


class ErrorMixin(BaseModel):
    code: int
    reason: str


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
        score: float
        reason: str
        description: str
        hidden: bool

    class CodeExecFailure(BaseModel):
        case: str
        reason: str
        score: float
        description: str
        hidden: bool

    class CodeExecSuccess(BaseModel):
        case: str
        score: float
        description: str
        hidden: bool

    errors: List[CodeExecError]
    failures: List[CodeExecFailure]
    successes: List[CodeExecSuccess]
    total: float
