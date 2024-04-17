const db = require("./services/db")

const express = require("express")
const app = express()
const port = 3000

app.get("/", (req, res) => {
  res.send("Hello World!")
})

app.get("/users", async (req, res) => {
  let users = await db.getUsers()

  users.forEach((user) => {
    console.log(user.username, user.name)
  })
  res.send(`Antal users =  ${users.length}`)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})