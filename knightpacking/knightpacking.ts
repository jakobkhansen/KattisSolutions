import * as fs from "fs";

function main(lines: string[]) {
  let num = parseInt(lines[0]);
  if (num % 2 == 0) {
    console.log("second");
  } else {
    console.log("first");
  }
}

let input = fs.readFileSync("/dev/stdin").toString().split("\n");

main(input);
