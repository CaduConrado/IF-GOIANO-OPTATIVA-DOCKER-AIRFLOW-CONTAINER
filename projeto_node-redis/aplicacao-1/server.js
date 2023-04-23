const express = require("express");
const redis = require("redis");
const app = express();

const redisClient = redis.createClient({
  host: "test-redis",
  port: 6379,
});

app.get("/", function (req, res) {
  redisClient.get("numVisits", function (err, numVisits) {
    numVisitsToDisplay = parseInt(numVisits) + 1;

    if (isNaN(numVisitsToDisplay)) {
      numVisitsToDisplay = 1;
    }

    res.send(`Aplicacao-1: O numero de visitantes é: ${numVisitsToDisplay}`);
    numVisits++;
    redisClient.set(`numVisists`, numVisistsToDisplay);
  });

  app.listen(5000, function () {
    console.log(`Aplicacao-1 esta escutando a porta 5000`);
  });
});
