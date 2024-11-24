from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def greet_user(request):
    data = await request.json()
    name = data.get("name", "гость")
    return JSONResponse({"message": f"Привет!, {name}!"})


routes = [
    Route("/greet", greet_user, methods=["POST"]),
]

app = Starlette(routes=routes)
