const fs = require('fs');

// Function to append text to a file
function appendToFile() {
    // Text to be appended
    const text = "hi\n";

    // Append text to the file
    fs.appendFile('example.txt', text, (err) => {
        if (err) throw err;
        console.log('Text appended to file');
    });
}

// Create a text file with initial text
fs.writeFile('example.txt', '', (err) => {
    if (err) throw err;
    console.log('File created');

    // Append text to the file every 10 seconds
    setInterval(appendToFile, 10000);
});
