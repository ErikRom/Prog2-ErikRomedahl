  var mysql = require("mysql2")

var connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb",
})

connection.connect(function (error) {
    if (error) throw error
    console.log("Connection to DB created successfully.")
  })