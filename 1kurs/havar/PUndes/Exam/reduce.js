arr = [25, 14, 36, 20, 45, 96];
res = arr.reduce((t, e) => (t < e ? e : t));
console.log(res);
