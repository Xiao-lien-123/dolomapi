# DolomAPI - 豆宝/Grace AI API Python Wrapper

A comprehensive Python wrapper for the 豆宝 (DolomerAI/Grace AI) API.

## Features

- Easy-to-use Python interface for the 豆宝 API
- Support for multiple model types and completions
- Async support for non-blocking API calls
- Error handling and retry logic
- Type hints for better IDE support

## Installation

```bash
pip install dolomapi
```

## Quick Start

```python
from dolomapi import DolomClient

# Initialize the client
client = DolomClient(api_key="your-api-key")

# Create a completion
response = client.completions.create(
    model="grace-ai",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

## Documentation

For detailed documentation, see the [docs](./docs) directory.

## License

MIT License - see [LICENSE](./LICENSE) for details
