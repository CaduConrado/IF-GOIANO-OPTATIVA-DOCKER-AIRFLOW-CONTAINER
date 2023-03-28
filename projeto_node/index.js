const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Oieee! tudo bem?");
});

app.listen(8080, () => {
  console.log("Escutando a porta 8080");
});
