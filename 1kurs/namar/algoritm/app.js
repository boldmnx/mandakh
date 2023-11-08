fetch("https://forkify-api.herokuapp.com/api/search?q=pizza")
  .then((e) => e.json())
  .then((e) =>
    e.recipes.forEach((e, i) => {
      if (i < 5) {
        // div = document.createElement("div");

        title = document.createElement("h3").style.border = "2px solid";
        img = document.createElement("img").width = 100;
        img.src = e.source_url;

        id = document.createElement("p").innerHTML = e.recipe_id;
        rank = document.createElement("p").innerHTML = e.social_rank;
        a = document.createElement("a").href = e.source_url;

        div.appendChild(title);
        div.appendChild(img);
        div.appendChild(id);
        div.appendChild(rank);
        div.appendChild(a);
        document.body.appendChild(div);
        console.log(e);
      }
    })
  );
