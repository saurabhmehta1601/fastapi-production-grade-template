import time
import structlog
from fastapi import status, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from uuid import uuid4

class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: callable):
        logger = structlog.getLogger()

        start = time.perf_counter()
        response: Response | None = None
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        request_id = request.headers.get("X-Request-ID", str(uuid4()))
        structlog.contextvars.bind_contextvars(requestID=request_id)

        try:
            response = await call_next(request)
            status_code = response.status_code
        except Exception as err:
            raise err
        finally:
            end = time.perf_counter()
            durationInMS = round((end-start) * 1000, 2)

            log_kwargs = {
                "requestID": request_id,
                "clientIP": request.client.host if request.client else "unknown",
                "path": request.url.path,
                "method": request.method,
                "durationInMS": durationInMS,
                "status_code": status_code
            }

            if status_code >= 500:
                logger.error("request_server_error", **log_kwargs) 
            elif status_code >= 400:
                logger.warning("request_client_error", **log_kwargs)
            elif status_code >= 200:
                logger.info("request_success", **log_kwargs)

        if response is not None:
            response.headers['X-Request-ID'] = request_id
        
        structlog.contextvars.clear_contextvars()
        
        return response