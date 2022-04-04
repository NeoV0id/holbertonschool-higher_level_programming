#!/usr/bin/node

if (argv.$1 === null){
	console.log('Missing size');
}else{
	argv.$1 = (int) argv.$1;
	if (typeof argv.$1 === int){
		for (let i = 0; i < argv.$1; i++){
			for (let j = 0; j < argv.$1; j++){
				console.log ('X');
			}
			console.log ('\n');
		}
	}
}
