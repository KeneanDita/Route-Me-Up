from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RouteRequest(BaseModel):
    start: str
    end: str
    waypoints: list[str] = []


@app.post("/route")
async def get_route(request: RouteRequest):
    try:
        route = {
            "start": request.start,
            "end": request.end,
            "waypoints": request.waypoints,
            "distance": 42.0,
            "duration": 3600,
        }
        return JSONResponse(content=route)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
