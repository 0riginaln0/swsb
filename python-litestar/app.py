print("hello world")

from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "hello!"


app = Litestar(route_handlers=[index])
