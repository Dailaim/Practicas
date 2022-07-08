document
  .getElementsByTagName("button")[0]
  .addEventListener("click", function() {
    document
      .getElementsByTagName("h1")[0]
      .classList.add("animated", "rubberBand");
    setTimeout(function() {
      document
        .getElementsByTagName("h1")[0]
        .classList.remove("animated", "rubberBand");
    }, 1000);
  });
