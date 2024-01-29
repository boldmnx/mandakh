arr = [1, 2, 3, 4, 4];
copyArr = [];
arr.forEach((e) => (!copyArr.includes(e) ? copyArr.push(e) : {}));

console.log(copyArr.length === arr.length);
