#!/usr/bin/node

if (argv.$1 === null){
	console.log('Missing number of occurrences');
}else{
	argv.$1 = (int) argv.$1;
	if (typeof argv.$1 === int){
		for (let i = 0; i < argv.$1; i++){
			console.log('C is fun');
		}
	}
}

