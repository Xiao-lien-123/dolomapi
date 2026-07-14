"""Exceptions for the DolomAPI"""


class DolomAPIError(Exception):
    """Base exception for DolomAPI errors"""
    pass


class AuthenticationError(DolomAPIError):
    """Raised when authentication fails"""
    pass


class ValidationError(DolomAPIError):
    """Raised when request validation fails"""
    pass


class RateLimitError(DolomAPIError):
    """Raised when rate limit is exceeded"""
    pass


class APIError(DolomAPIError):
    """Raised when the API returns an error"""
    
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")
