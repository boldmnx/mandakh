function Register() {
  if (document.getElementById("name").value == 0) {
    document.getElementById("para").innerHTML = "хоосон бүртгэхгүй";
  } else {
    document.getElementById("para").innerHTML = "";

    let pass = document.getElementById("password");
    if (pass != "/(?=.*[0-9](?=.*[a-zA-Z])([a-zA-Z0-9])") {
      console.log(pass.value);

      document.getElementById("para").innerHTML =
        "8aas bagagui pass oruulna uu";
    } else {
      document.getElementById("para").innerHTML = "";
      window.location.href = "index1.html";
      // event.preventDefault();
    }
  }
}
document.getElementById("name").addEventListener("mouseover", () => {
  document.getElementById("name").style.backgroundColor = "green";
});
