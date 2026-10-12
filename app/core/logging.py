import sys
import logging
import structlog
from app.core.config import Settings, get_settings


def configure_logging():
    app_settings: Settings = get_settings()

    shared_processors = [
        structlog.contextvars.merge_contextvars, # for concurrent requests avoid log overriding with isolated logging context per request
        structlog.processors.add_log_level, # adds level like Debug, Info
        structlog.processors.TimeStamper(fmt="iso", utc=True), # Add timestamp to log in ISO format.
        structlog.processors.format_exc_info,
    ]

    renderer_processor = None
    if app_settings.ENVIRONMENT == "development":
        renderer_processor = structlog.dev.ConsoleRenderer(colors=True)
    else:
        renderer_processor = structlog.processors.JSONRenderer() # convert the log into JSON string

    processors = shared_processors + [renderer_processor]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer_processor,
        ]
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    # Suppress Uvicorn's default verbose loggers and route them to root
    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.propagate = True

