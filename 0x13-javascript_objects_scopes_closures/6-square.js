#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
		    }
	charPrint (c) {
		if (c === undefined) {
			for (let i = 0; i < this.height; i++) {
				for (let j = 0; j < this.width; j++) {
					process.stdout.write('X');
				}
				process.stdout.write('\n');
			}
		} else {
			for (let i = 0; i < this.height; i++) {
				for (let j = 0; j < this.width; j++) {
					process.stdout.write(c);
				}
				process.stdout.write('\n');
			}
		}
	}
}
module.exports = Square;
