#!/usr/bin/node
const mynumber = parseInt(Number(process.argv[2]));
if (isNaN(mynumber)) {
	console.log('Not a number');
} else {
	console.log(`My number: ${mynumber}`);
}
