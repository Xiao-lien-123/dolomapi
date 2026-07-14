"""Main client for interacting with the 豆宝 API"""

import os
from typing import Optional, List, Dict, Any
import httpx


class DolomClient:
    """Client for the 豆宝/Grace AI API"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.dolomai.com",
        timeout: float = 30.0,
    ):
        """
        Initialize the DolomClient.
        
        Args:
            api_key: API key for authentication. Defaults to DOLOM_API_KEY env var.
            base_url: Base URL for the API endpoint.
            timeout: Request timeout in seconds.
        """
        self.api_key = api_key or os.getenv("DOLOM_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key not provided. Pass it directly or set DOLOM_API_KEY environment variable."
            )
        
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.Client(
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            timeout=timeout,
        )
    
    def completions(self) -> "Completions":
        """Get the completions API handler."""
        return Completions(self)
    
    def close(self) -> None:
        """Close the HTTP client."""
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class Completions:
    """Completions API handler"""
    
    def __init__(self, client: DolomClient):
        self.client = client
    
    def create(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        top_p: float = 0.9,
        **kwargs: Any,
    ) -> "CompletionResponse":
        """
        Create a completion.
        
        Args:
            model: Model identifier (e.g., "grace-ai").
            messages: List of message dicts with "role" and "content" keys.
            temperature: Sampling temperature (0.0 to 2.0).
            max_tokens: Maximum tokens in the response.
            top_p: Nucleus sampling parameter.
            **kwargs: Additional parameters to pass to the API.
        
        Returns:
            CompletionResponse: The API response.
        """
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
        }
        
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        
        payload.update(kwargs)
        
        response = self.client.client.post(
            f"{self.client.base_url}/v1/chat/completions",
            json=payload,
        )
        response.raise_for_status()
        
        return CompletionResponse.from_dict(response.json())


class Message:
    """Represents a message in a completion response"""
    
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Message":
        return cls(role=data["role"], content=data["content"])


class CompletionResponse:
    """Represents a completion response from the API"""
    
    def __init__(
        self,
        id: str,
        object: str,
        created: int,
        model: str,
        choices: List[Dict[str, Any]],
        usage: Dict[str, int],
    ):
        self.id = id
        self.object = object
        self.created = created
        self.model = model
        self.choices = [Choice.from_dict(c) for c in choices]
        self.usage = usage
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CompletionResponse":
        return cls(
            id=data["id"],
            object=data["object"],
            created=data["created"],
            model=data["model"],
            choices=data["choices"],
            usage=data["usage"],
        )


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
            finish_reason=data["finish_reason"],
        )
