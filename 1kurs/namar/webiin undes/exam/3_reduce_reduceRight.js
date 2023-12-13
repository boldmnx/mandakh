numbers = [44, 44, 11];

ssum = numbers.reduce((p, c) => p + c);
right = numbers.reduceRight((p, c) => p + c);
console.log(right);
