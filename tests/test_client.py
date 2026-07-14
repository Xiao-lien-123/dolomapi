"""Tests for the DolomAPI client"""

import pytest
from dolomapi import DolomClient, CompletionResponse, Message
from dolomapi.exceptions import DolomAPIError


def test_client_initialization():
    """Test that DolomClient initializes correctly"""
    import os
    os.environ["DOLOM_API_KEY"] = "test-key"
    
    client = DolomClient()
    assert client.api_key == "test-key"
    assert client.base_url == "https://api.dolomai.com"
    client.close()


def test_client_initialization_with_explicit_key():
    """Test DolomClient initialization with explicit API key"""
    client = DolomClient(api_key="explicit-key")
    assert client.api_key == "explicit-key"
    client.close()


def test_client_initialization_no_key():
    """Test that DolomClient raises error when no API key is provided"""
    import os
    # Clear the environment variable
    os.environ.pop("DOLOM_API_KEY", None)
    
    with pytest.raises(ValueError):
        DolomClient()


def test_message_creation():
    """Test Message creation"""
    msg = Message(role="user", content="Hello")
    assert msg.role == "user"
    assert msg.content == "Hello"


def test_message_from_dict():
    """Test Message.from_dict"""
    data = {"role": "assistant", "content": "Hi there!"}
    msg = Message.from_dict(data)
    assert msg.role == "assistant"
    assert msg.content == "Hi there!"


def test_completion_response_from_dict():
    """Test CompletionResponse.from_dict"""
    data = {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1234567890,
        "model": "grace-ai",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": "Response content"},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
        }
    }
    
    response = CompletionResponse.from_dict(data)
    assert response.id == "chatcmpl-123"
    assert response.model == "grace-ai"
    assert len(response.choices) == 1
    assert response.choices[0].message.content == "Response content"
    assert response.usage["total_tokens"] == 30
