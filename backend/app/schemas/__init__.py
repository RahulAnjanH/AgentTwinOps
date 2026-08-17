"""Schemas package — shared Pydantic models for request/response shapes."""

from app.schemas.responses import (
    ApiResponse,
    ErrorResponse,
    HealthResponse,
    RootResponse,
    VersionResponse,
)

__all__ = [
    "ApiResponse",
    "ErrorResponse",
    "HealthResponse",
    "RootResponse",
    "VersionResponse",
]
