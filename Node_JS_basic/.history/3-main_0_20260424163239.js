const countStudents = require('./3-read_file_async');

countStudents("data.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });