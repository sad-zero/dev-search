import logging

from fastmcp import FastMCP
from fastmcp.server.middleware.timing import TimingMiddleware
from fastmcp.server.middleware.logging import LoggingMiddleware
from fastmcp.server.middleware.caching import ResponseCachingMiddleware
from fastmcp.server.middleware.rate_limiting import RateLimitingMiddleware
from fastmcp.server.middleware.error_handling import ErrorHandlingMiddleware

from dev_search.config import DIContainer, Settings, configure_log


def mcp() -> FastMCP:
    """
    Entrypoint.
    """

    settings = Settings()
    with open("logging.yaml", "r") as fd:
        configure_log(fd)

    logger = logging.getLogger("dev_search")
    logger.info(
        f"load {settings.environment}", extra={"environment": settings.environment}
    )

    mcp: FastMCP = DIContainer().mcp()

    # tools

    # middlewares.
    mcp.add_middleware(
        ErrorHandlingMiddleware(
            include_traceback=True,
            logger=logging.getLogger("dev_search.middlewre.error_handler"),
        )
    )
    mcp.add_middleware(
        TimingMiddleware(
            logger=logging.getLogger("dev_search.middleware.timing"),
        )
    )
    mcp.add_middleware(
        LoggingMiddleware(
            logger=logging.getLogger("dev_search.middleware.logging"),
            include_payloads=True,
        )
    )
    mcp.add_middleware(ResponseCachingMiddleware())
    mcp.add_middleware(
        RateLimitingMiddleware(
            max_requests_per_second=settings.tool_call_limit_per_second,
        )
    )

    return mcp