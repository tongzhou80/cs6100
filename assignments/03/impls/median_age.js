const fs = require("fs");

const data = fs.readFileSync(process.argv[2], "utf-8").trim().split("\n");
data.shift(); // skip header

let ages = [];
for (const line of data) {
    const parts = line.split(",");
    ages.push(parseInt(parts[2], 10));
}

ages.sort((a, b) => a - b);
let median;
const n = ages.length;
if (n % 2 === 0) {
    median = (ages[n/2 - 1] + ages[n/2]) / 2.0;
} else {
    median = ages[Math.floor(n/2)];
}

console.log(median);
