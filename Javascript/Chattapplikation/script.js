const express = require('express')
const app = express()
const http = require('http')
const server = http.createServer(app)
const { Server } = require('socket.io')
const io = new Server(server)

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html')
})

io.on('connection', (socket) => {
    socket.on('username set', (msg) => {
        socket.username = msg.username
        socket.broadcast.emit('connection', msg)
    })
    socket.on('username set 1', (msg) => {
        socket.emit('connection', msg)
    })
    socket.on('user sends message', (msg) => {
        io.emit('new message', msg);
    });
    socket.on('disconnect', () => {
        io.emit('connection', {username: socket.username, text: ' has disconnected'})
    })
});

server.listen(3000, () => {
    console.log('listening on *:3000')
})