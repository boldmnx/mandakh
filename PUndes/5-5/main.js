btn.onclick = function () {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const male = document.getElementById("male").checked;
  const female = document.getElementById("female").checked;
  const country = document.getElementById("country").value;
  const password1 = document.getElementById("password").value;

  if (name == "") {
    alert("Name field is empty!");
  } else {
    let passwordInput = document.getElementById("password");

    if (passwordInput.value.length < 8) {
      alert("Password must be at least 8 characters long.");
      event.preventDefault();
    } else if (
      !/\d/.test(passwordInput.value) ||
      !/[a-zA-Z]/.test(passwordInput.value)
    ) {
      alert("Password must contain at least one letter and one number.");
      event.preventDefault();
    } else {
      window.location.href = "./index1.html";
      event.preventDefault();
    }
  }
  if (email == "") {
    alert("Email field is empty!");
  }
  if (phone == "") {
    alert("Phone field is empty!");
  }
  if (!male && !female) {
    alert("Please select a gender!");
  }
  if (country == "") {
    alert("Please select a country!");
  }
  if (password1 == "") {
    alert("Password field is empty!");
  }
};

const inputs = document.querySelectorAll("input");
inputs.forEach(function (input) {
  input.addEventListener("mouseover", function () {
    this.style.backgroundColor = "plum";
  });

  input.addEventListener("mouseout", function () {
    this.style.backgroundColor = "";
  });
});

// function Register() {
//   if (document.getElementById("name").value == 0) {
//     document.getElementById("para").innerHTML = "хоосон бүртгэхгүй";
//   } else {
//     document.getElementById("para").innerHTML = "";

//     let pass = document.getElementById("password");
//     let temdegt = /\d[@#$%^&+=]/;
//     if (pass != temdegt) {
//       console.log(pass.value);

//       document.getElementById("para").innerHTML =
//         "8aas bagagui pass oruulna uu";
//     } else {
//       document.getElementById("para").innerHTML = "";
//       window.location.href = "index1.html";
//       // event.preventDefault();
//     }
//   }
// }
// document.getElementById("name").addEventListener("mouseover", () => {
//   document.getElementById("name").style.backgroundColor = "green";
// });
