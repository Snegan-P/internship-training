import asyncio
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, StreamingResponse
from datetime import datetime

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()


html = """ 
<!DOCTYPE html>
<html>
    <head><title>Week 3 Real-time Test</title></head>
    <body>
        <h1>WebSocket Broadcast & SSE Test</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'></ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('li');
                var content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText");
                ws.send(input.value);
                input.value = '';
                event.preventDefault();
            }
        </script>
    </body>
</html>
"""

@app.get("/test-ui")
async def get():
    return HTMLResponse(html)

@app.get("/")
def read_root():
    return {"message": "Welcome to Week 3 API root!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Receive message from a client

            data = await websocket.receive_text()  
            
            # Broadcast it to ALL connected clients

            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client disconnected")


async def date_generator():
    while True:
        # Format required for SSE streaming format: "data: <value>\n\n"

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yield f"data: Live Clock Ticking -> {now}\n\n"
        await asyncio.sleep(1)     # stream every 1 second

@app.get("/events")
async def sse_endpoint():
    return StreamingResponse(date_generator(), media_type="text/event-stream")