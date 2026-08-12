import asyncio
import datetime
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()

# --- 1. Connection Manager (For Broadcast) ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# --- 2. WebSocket Endpoint (/ws) ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcasting echoes the message back to the sender AND everyone else
            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client left the chat")

# --- 3. SSE Endpoint (/events) ---
async def event_generator():
    counter = 0
    while True:
        # Pause for 1 second to simulate a live ticking clock
        await asyncio.sleep(1)
        counter += 1
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # SSE format strictly requires `data: {payload}\n\n`
        yield f"data: Tick {counter} | Time: {current_time}\n\n"

@app.get("/events")
async def sse_endpoint():
    return StreamingResponse(event_generator(), media_type="text/event-stream")


# --- 4. Testing UI (HTML/JS Client) ---
html = 
<!DOCTYPE html>
<html>
    <head>
        <title>Week 3: Real-Time Endpoints</title>
        <style>
            body { font-family: sans-serif; max-width: 600px; margin: 40px auto; line-height: 1.6;}
            .box { border: 1px solid #ccc; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
            #sse-data { font-family: monospace; font-size: 1.2em; color: #d93025; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>WebSocket Broadcast Chat (/ws)</h2>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" id="messageText" autocomplete="off" placeholder="Type a message..."/>
                <button>Send</button>
            </form>
            <ul id='messages'></ul>
        </div>
        
        <div class="box">
            <h2>SSE Live Clock (/events)</h2>
            <div id="sse-data">Waiting for events...</div>
        </div>
        
        <script>
            // Initialize WebSocket
            // Note: In production, dynamically grab the host using window.location.host
            const ws = new WebSocket(`ws://${window.location.host}/ws`);
            
            ws.onmessage = function(event) {
                const messages = document.getElementById('messages');
                const message = document.createElement('li');
                message.textContent = event.data;
                messages.appendChild(message);
            };
            
            function sendMessage(event) {
                event.preventDefault();
                const input = document.getElementById("messageText");
                ws.send(input.value);
                input.value = '';
            }

            // Initialize Server-Sent Events (SSE)
            const eventSource = new EventSource("/events");
            
            eventSource.onmessage = function(event) {
                document.getElementById("sse-data").textContent = event.data;
            };
        </script>
    </body>
</html>


@app.get("/")
async def get_test_page():
    return HTMLResponse(html)