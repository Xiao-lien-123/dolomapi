"""Data models for API responses"""

from typing import Any, Dict, List


class Message:
    """Represents a message in a completion response"""
    
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Message":
        return cls(role=data["role"], content=data["content"])
    
    def __repr__(self) -> str:
        return f"Message(role={self.role!r}, content={self.content[:50]!r}...)"


class Choice:
    """Represents a choice in a completion response"""
    
    def __init__(self, index: int, message: Message, finish_reason: str):
        self.index = index
        self.message = message
        self.finish_reason = finish_reason
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Choice":
        return cls(
            index=data["index"],
            message=Message.from_dict(data["message"]),
            finish_reason=data.get("finish_reason", "stop"),
        )


class CompletionResponse:
    """Represents a completion response from the API"""
    
    def __init__(
        self,
        id: str,
        object: str,
        created: int,
        model: str,
        choices: List[Choice],
        usage: Dict[str, int],
    ):
        self.id = id
        self.object = object
        self.created = created
        self.model = model
        self.choices = choices
        self.usage = usage
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CompletionResponse":
        return cls(
            id=data["id"],
            object=data["object"],
            created=data["created"],
            model=data["model"],
            choices=[Choice.from_dict(c) for c in data["choices"]],
            usage=data["usage"],
        )
    
    def __repr__(self) -> str:
        return (
            f"CompletionResponse(id={self.id!r}, model={self.model!r}, "
            f"choices={len(self.choices)} items)"
        )
