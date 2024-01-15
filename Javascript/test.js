const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('hallå där!!!!!!')
})

app.listen(port, () => {
    console.log('Example appp listeinng on port ${port}')
})

app.get('/kanelbulle', (req, res) => {
    res.send('aajajj')
})