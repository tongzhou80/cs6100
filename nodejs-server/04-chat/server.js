// server.js
const express = require('express');
const http = require('http');
const path = require('path');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server }); // Attach WS to HTTP server

// Serve static files (HTML, JS, etc.)
app.use(express.static(path.join(__dirname, 'public')));

// WebSocket handling
wss.on('connection', (ws) => {
    console.log('Client connected');
    ws.send('Hello from server!');

    ws.on('message', (message) => {
        console.log(`Received: ${message}`);
        ws.send(`Server received: ${message}`);
    });

    ws.on('close', () => {
        console.log('Client disconnected');
    });
});

// Start HTTP + WebSocket server
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
