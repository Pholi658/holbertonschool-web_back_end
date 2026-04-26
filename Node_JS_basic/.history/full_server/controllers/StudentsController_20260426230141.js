import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response, db) {
    readDatabase(db)
      .then((studentsByField) => {
        response.write('This is the list of our students\n');
        let strStudents = '';

        for (const field in studentsByField) {
          if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
            const strList = studentsByField[field].join(', ');
            strStudents += `Number of students in ${field}: ${studentsByField[field].length}. List: ${strList}\n`;
          }
        }

        response.write(strStudents.slice(0, -1));
        response.end(); // ✅ correct way to end response
      })
      .catch(() => {
        response.statusCode = 500;
        response.end('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response, db) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.statusCode = 500;
      response.end('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(db)
      .then((fields) => {
        const students = fields[major];
        response.statusCode = 200;
        response.end(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        response.statusCode = 500;
        response.end('Cannot load the database');
      });
  }
}
