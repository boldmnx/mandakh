function fnasync() {
  setTimeout(() => console.log("middle"), 1000);
}

//Sequential
function fn1() {
  console.log("start");
  console.log("middle");
  console.log("end");
}

//Concurrency
function fn2() {
  console.log("start");
  fnasync();
  console.log("end");
}

fn2();
