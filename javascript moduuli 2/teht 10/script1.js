'use strict';

const ehdokasnum = +prompt('How many candidates?');

const ehdokkaat = [];

for (let i = 0; i < ehdokasnum; i++) {
    const nimi = prompt(`Enter name for candidate ${i + 1}:`);
    ehdokkaat.push({ name: nimi, votes: 0 });
}

const voterCount = +prompt('How many voters?');

for (let i = 0; i < voterCount; i++) {
    const vote = prompt('Who do you vote for? (enter name)');

    if (vote === '') continue;

    for (let ehdokas of ehdokkaat) {
        if (ehdokas.name === vote) {
            ehdokas.votes++;
        }
    }
}

ehdokkaat.sort((a, b) => b.votes - a.votes);

const maxVotes = ehdokkaat[0].votes;
const winners = ehdokkaat.filter(e => e.votes === maxVotes);

if (winners.length === 1) {
    console.log(`The winner is ${winners[0].name} with ${winners[0].votes} votes.`);
} else {
    const names = winners.map(e => e.name).join(', ');
    console.log(`It's a tie between: ${names} with ${maxVotes} votes both.`);
}

console.log('results:');
for (let ehdokas of ehdokkaat) {
    console.log(`${ehdokas.name}: ${ehdokas.votes} votes`);
}