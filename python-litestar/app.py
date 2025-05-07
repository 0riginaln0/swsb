print("hello world")

from litestar import Litestar, get
from litestar.logging import LoggingConfig


@get("/")
async def index() -> str:
    return "hello!"


app = Litestar(route_handlers=[index])
