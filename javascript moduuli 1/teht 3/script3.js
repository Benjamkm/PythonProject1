'use strict';
const a = +prompt('Give first number');
const b = +prompt('Give second number');
const c = +prompt('Give third number');
const product = a * b * c;
const sum = a+b+c;
const avg = sum /3;

document.querySelector('#target').innerHTML = `sum: ${sum} product: ${product} average: ${avg}`;
