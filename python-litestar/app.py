print("hello world")

from litestar import Litestar, get
from litestar.logging import LoggingConfig


@get("/")
async def index() -> str:
    return "hello!"


logging_config = LoggingConfig(
    root={"level": "CRITICAL"},
    loggers={
        "litestar": {"level": "CRITICAL"},
        "uvicorn": {"level": "CRITICAL"},
    },
)

app = Litestar(route_handlers=[index], logging_config=logging_config)
