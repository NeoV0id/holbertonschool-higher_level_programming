#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    } else {
      console.log((c.repeat(this.width) + '\n').repeat(this.height - 1) + c.repeat(this.width));
    }
  }
}
module.exports = Square;
