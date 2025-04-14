from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/nodes")
def list_nodes():
    return [{"name": "minipc4", "ip": "100.75.172.22", "group": "tailscale"}]

@app.get("/api/status")
def get_status():
    return {"rsync": "ok", "timer": "active"}

@app.get("/api/connect/{conn_id}")
def connect(conn_id: str):
    return {"url": f"http://localhost:8080/guacamole/#/client/{conn_id}"}