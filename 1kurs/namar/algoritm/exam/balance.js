class Transition {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
  info() {
    this.turul = `${this instanceof Income ? "орлого" : "зарлага"}`;
    console.log(`
Төрөл: ${this.turul}
Үнэ: ${this.price}₮
нэр: ${this.name}\n`);
  }
  static dollar_hansh() {
    console.log("2000$");
  }
}
class Income extends Transition {}
class Expense extends Transition {
  constructor(name, price, zaaval = false) {
    super(name, -price);
    this.zaaval = zaaval;
  }
}
arr = [];
arr.push(new Expense("hutga", 100));
arr.push(new Income("ajil", 100));
arr.push(new Expense("hutga", 200, true));
arr.push(new Expense("hutga", 100, true));
arr.push(new Income("tsalin", 1000));

arr.forEach((e) => e.info());
console.log(
  `zaaval: ${arr.filter((e) => e.zaaval).reduce((sum, e) => sum + e.price, 0)}`
);
console.log(`uldegdel: ${arr.reduce((sum, e) => sum + e.price, 0)}`);
Transition.dollar_hansh();

let word = "java script script";
let words = word.split(" ");
let myDict = new Map();
words.forEach((el) => myDict.set(el, 1));
console.log(myDict.size);
console.log(words);

const originalObject = { key1: "value1", key2: "value2" };
const copyObject = { ...originalObject };

console.log(copyObject);
