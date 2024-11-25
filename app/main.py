from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route


async def greet_user(request: Request) -> JSONResponse:
    name = (await request.json()).get("name", "гость")
    return JSONResponse({"message": f"Привет, {name}!"})


async def list_routes(request: Request) -> HTMLResponse:
    routes_html = "<ul>"
    for route in app.routes:
        methods = ", ".join(route.methods)
        routes_html += f'<li><strong>{route.path}</strong> - [{methods}]</li>'
    routes_html += "</ul>"
    return HTMLResponse(f"<h1>Список маршрутов</h1>{routes_html}")

app = Starlette(routes=[
    Route("/", list_routes),
    Route("/greet", greet_user, methods=["POST"]),
])
