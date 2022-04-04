#!/usr/bin/node

function add(a, b){

	a = (int) argv.$1;
	b = (int) argv.$2;

	if (a === null){
		console.log ('NaN');
	}else if (b === null){
		console.log ('NaN');
	}else{
		console.log (a + b);
	}
}
