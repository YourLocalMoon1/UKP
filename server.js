// server.js //

// UKP's server file //
// !EDIT IT IF YOU ARE A ADVANCED USER AND YOU KNOW WHAT YOU'RE DOING! //

const express = require('express');
const path = require('path')
const server = express();
const port = 3000; // The port of the server. (!DO NOT CHANGE IT!) //

server.use(express.static(path.join(__dirname, 'web'))) /*
^ This line allows the express module to use all the contents that are in the "web" folder.
| You can edit it to whatever you want, but make sure that you have changed the
| folder name that is contained in the project folder.
*/ 

let listener = server.listen(port, () => {
    console.log('Listening on the port %d ', listener.address().port)
});