$.ajax({
  type: "GET",
  url: "api/room/get",
  dataType: "json",
  success: function (response) {
    console.log(response.roomId);
    let rid = response.roomId;
    playing = false;

    findPlayer = setInterval(() => {
      $.getJSON("api/room/" + rid + "/opponent", (data) => {
        if (data["a"]) {
          $("#player1Name").html(data["a"]);
        }
        if (data["b"]) {
          $("#player2Name").html(data["b"]);
        }

        console.log("finding nemo");

        if (data["a"] && data["b"]) {
          console.log("full");
          $("#status").remove();
          playing = true;
          clearInterval(findPlayer);
        }
      });
    }, 1000);

    checkPlaying = setInterval(() => {
      if (!findPlayer) {
        playing = true;
        console.log(playing);
        clearInterval(checkPlaying);
      }
    }, 1000);
  },
});
