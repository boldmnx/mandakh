let a = "jaAvascript";
b = a.replace(/a/gi, "f");
console.log(b);

friends = ["davka", "anugo"];

reFriends = friends.map((v) => (v === "davka" ? "bold" : v));
console.log(reFriends);