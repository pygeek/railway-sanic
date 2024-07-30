from sanic import Sanic
from sanic.response import json

app = Sanic("ExampleApp")

@app.get("/")
async def index(request):
    return json({"choo choo": "Welcome to your Sanic app 🚅"})
