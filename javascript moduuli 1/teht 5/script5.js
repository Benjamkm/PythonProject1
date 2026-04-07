'use strict';
const year = +prompt('Enter a year');

let leapyear;
if (year % 4 === 0 && year % 100 !== 0) {
    leapyear = true;
} else if (year % 400 === 0) {
    leapyear = true;
} else {
    leapyear = false;
}
document.querySelector('#target').innerHTML = leapyear ? 'Leap year' : 'Not a leap year;'