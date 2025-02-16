rel = document.getElementById("rel");
role = document.getElementById("roleName");

rel.addEventListener("change", () => {
  if (rel.value.includes("ACTED_IN")) {
    role.style.display = "inline";
  } else {
    role.style.display = "none";
  }
});
