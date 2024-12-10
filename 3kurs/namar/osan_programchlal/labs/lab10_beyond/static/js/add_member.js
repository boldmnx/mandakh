let isDataLoaded = false;
let cashedData = [];
let error = {};

// search-results
const searchBox = document.getElementById("search-box");
const searchResults = document.getElementById("search-results");
let existingInput = document.getElementById("additional-input");

let paragraphContainer = document.getElementById("paragraph-container");

searchBox.addEventListener("input", () => {
  const query = searchBox.value;
  if (query.length > 0) {
    fetch(`http://127.0.0.1:3000/json?m=${query}`)
      .then((response) => response.json())
      .then((data) => {
        searchResults.innerHTML = "";
        if (data.movies.length > 0) {
          data.movies.forEach((item) => {
            const div = document.createElement("div");
            div.textContent = item;
            div.classList.add(
              "px-4",
              "py-2",
              "hover:bg-gray-200",
              "cursor-pointer"
            );
            div.addEventListener("click", () => {
              searchBox.value = item;
              searchResults.style.display = "none";
            });
            searchResults.appendChild(div);
          });
          searchResults.style.display = "block";
        } else {
          searchResults.style.display = "none";
        }
      })
      .catch((e) => console.log(`Сервер талдаа: ${e}`));
  } else {
    searchResults.style.display = "none";
  }
});

const searchPerson = document.getElementById("search-person");
const searchPersonResults = document.getElementById("search-person-results");

searchPerson.addEventListener("input", () => {
  const query = searchPerson.value;
  if (query.length > 0) {
    fetch(`http://127.0.0.1:3000/json?p=${query}`)
      .then((response) => response.json())
      .then((data) => {
        searchPersonResults.innerHTML = "";
        if (data.people.length > 0) {
          data.people.forEach((i) => {
            const div = document.createElement("div");
            div.textContent = i;
            div.classList.add(
              "px-4",
              "py-2",
              "hover:bg-gray-200",
              "cursor-pointer"
            );
            div.addEventListener("click", () => {
              searchPerson.value = i;
              searchPersonResults.style.display = "none";
            });
            searchPersonResults.appendChild(div);
          });
          searchPersonResults.style.display = "none";
        }
        searchPersonResults.style.display = "block";
      })
      .catch((e) => console.log(`Сервер алдаа: ${e}`));
  } else {
    searchPersonResults.style.display = "none";
  }
});

// Relationship section
const selectRel = document.getElementById("role");

selectRel.addEventListener("focus", () => {
  fetch(`http://127.0.0.1:3000/json`)
    .then((res) => res.json())
    .then((data) => {
      if (!isDataLoaded) {
        cashedData.push(data.rel);
        populateSelect(data.rel);
        isDataLoaded = true;
      } else {
        populateSelect(cashedData);
      }
    });
});

function populateSelect(data) {
selectRel.innerHTML = '<option value="">-- Үүрэг сонгох --</option>';
  data.forEach((i) => {
    const selectOption = document.createElement("option");
    selectOption.value = i.id;
    selectOption.textContent = i.name;
    selectRel.appendChild(selectOption);
  });

  // Listen for changes on the select element
  selectRel.addEventListener("change", function () {
    if (existingInput) {
      existingInput.remove();
    }
    if (selectRel.value === "ACTED_IN") {
      const input = document.createElement("input");
      input.id = "additional-input";
      input.type = "text";
      input.placeholder = "Role оруулна уу";
      input.classList.add(
        "px-4",
        "py-2",
        "rounded",
        "bg-gray-800",
        "text-gray-300",
        "w-full"
      );
      paragraphContainer.appendChild(input);
      existingInput = input; // Ensure existingInput points to the newly created input
      console.log("existingInput:", existingInput);

    }
    
  });
}

const submit = document.getElementById("form");

submit.addEventListener("submit", (event) => {
  const myClientJson = {
    title: searchBox.value,
    name: searchPerson.value,
    rel: selectRel.value,
    role: existingInput ? existingInput.value.split(",") : [], // Use existingInput to get the value
  };

  console.log("Form data being submitted:", myClientJson); // Debugging role value

  event.preventDefault(); // Prevent the default form submission behavior
  fetch("http://127.0.0.1:3000/add_member", {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(myClientJson),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      alertMsg(data);
    })
    .catch((e) => console.log(`Сервер алдаа: ${e}`));
});

function alertMsg(data) {
  const alertBox = document.getElementById("alert-message");

  alertBox.textContent = data.error ? data.error : "Амжилттай!";
  alertBox.className = data.error
    ? "p-4 rounded mb-4 bg-red-100 text-red-700"
    : "p-4 rounded mb-4 bg-green-100 text-green-700";

  setTimeout(() => {
    alertBox.classList.add("hidden");
  }, 4000);
}
