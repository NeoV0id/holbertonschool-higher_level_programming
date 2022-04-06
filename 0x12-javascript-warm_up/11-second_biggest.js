#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log(0);
} else if (process.argv[3] === undefined || isNaN(process.argv[3])) {
  console.log(0);
} else {
  for (let i = 0; i < process.argv.length; i++) {
    if (i = 0) {
	    if (process.argv[i] > process.argv[i + 1]) {
	    	result = process.argv[i + 1];
	    } else {
		    result = process.argv[i];
	    }
    }
    console.log(result);
  }
}
