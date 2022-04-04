#!/usr/bin/node

if (argv.$1 === null){
	console.log ('Not a number');
}else{
	argv.$1 = (int) argv.$1;

	if (typeof argv.$1 === "number"){
		console.log(argv.$1);
	}else{
		console.log('Not a number');
	}
}
