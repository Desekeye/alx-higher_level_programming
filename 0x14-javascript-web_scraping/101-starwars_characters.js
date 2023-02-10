#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
<<<<<<< HEAD
    const characters = JSON.parse(body).characters;
=======
    let characters = JSON.parse(body).characters;
>>>>>>> d2d6d43b762672e361cac5933bd42d6279d278a1
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
<<<<<<< HEAD
	 if (!error) {
		 console.log(JSON.parse(body).name);
		 if (index + 1 < characters.length) {
			 printCharacters(characters, index + 1);
		 }
	 }
=======
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
>>>>>>> d2d6d43b762672e361cac5933bd42d6279d278a1
  });
}
