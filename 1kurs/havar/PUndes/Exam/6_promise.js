//Sequential
function sync_fn() {
  console.log("start");
  console.log("middle");
  console.log("end\n------------");
}
sync_fn();

async function middle_fn() {
  return new Promise((res, reg) => {
    setTimeout(() => console.log("midlle"), 2000);
    // reg("erorrrr");
  });
}

//Concurrency
async function async_fn() {
  console.log("start");
  try {
    middle_fn();
  } catch (e) {
    console.log("aldaa garlaa: " + e);
  }
  console.log("end");
}
async_fn();
