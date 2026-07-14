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

## Disclaimer

⚠️ **This is an unofficial, third-party wrapper for the 豆宝/Grace AI API.**

- This project is **NOT** developed, endorsed, or supported by ByteDance or the official 豆宝 team.
- This wrapper is provided as-is for educational and community use.
- Use at your own risk. The authors are not responsible for any issues arising from the use of this wrapper.
- Please refer to the official 豆宝 API documentation and terms of service for the latest and most accurate information.

## License

MIT License - see [LICENSE](./LICENSE) for details
