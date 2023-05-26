# Report | Отчет

Создаем базу данных с помощью терминала MongoShell

Создадим коллекцию students: 
```MongoShell
db.createCollection("students", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "ID", "GroupID", "FullName" ],
         properties: {
            ID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            GroupID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            FullName: {
               bsonType: "string",
               description: "must be a string and is required"
            }
         }
      }
   }
})
```
Создадим коллекцию disciplines:
db.createCollection("disciplines", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "ID", "Name" ],
         properties: {
            ID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            Name: {
               bsonType: "string",
               description: "must be a string and is required"
            }
         }
      }
   }
})

Создадим коллекцию groups

db.createCollection("groups", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "ID", "Name" ],
         properties: {
            ID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            Name: {
               bsonType: "string",
               description: "must be a string and is required"
            }
         }
      }
   }
})

Создадим коллекцию classrooms

db.createCollection("classrooms", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "ID", "office", "building" ],
         properties: {
            ID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            office: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            building: {
               bsonType: "string",
               description: "must be a string and is required"
            }
         }
      }
   }
})

Создадим коллекцию lessons
db.createCollection("lessons", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "ID", "DayOfWeek", "Start_Time", "EndTime", "ClassroomID", "GroupID", "DisciplineID", "TeacherID" ],
         properties: {
            ID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            DayOfWeek: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            Start_Time: {
               bsonType: "date",
               description: "must be a date and is required"
            },
            EndTime: {
               bsonType: "date",
               description: "must be a date and is required"
            },
            ClassroomID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            GroupID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            DisciplineID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            TeacherID: {
               bsonType: "int",
               description: "must be an integer and is required"
            }
         }
      }
   }
})


Создадим коллекцию teachers
db.createCollection("teachers", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "ID", "FullName" ],
         properties: {
            ID: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            FullName: {
               bsonType: "string",
               description: "must be a string and is required"
            }
         }
      }
   }
})

Заполним коллекции

db.disciplines.insertMany([   {      "ID": 1,      "Name": "Mathematics"   },   {      "ID": 2,      "Name": "Computer Science"   },   {      "ID": 3,      "Name": "Physics"   },   {      "ID": 4,      "Name": "Biology"   },   {      "ID": 5,      "Name": "Chemistry"   },   {      "ID": 6,      "Name": "History"   },   {      "ID": 7,      "Name": "Geography"   },   {      "ID": 8,      "Name": "Literature"   },   {      "ID": 9,      "Name": "Foreign Languages"   },   {      "ID": 10,      "Name": "Philosophy"   }])
db.classrooms.insertMany([   {      "ID": 1,      "office": "101",      "building": "Main Building"   },   {      "ID": 2,      "office": "102",      "building": "Main Building"   },   {      "ID": 3,      "office": "201",      "building": "New Building"   },   {      "ID": 4,      "office": "202",      "building": "New Building"   },   {      "ID": 5,      "office": "301",      "building": "Science Building"   }])
db.teachers.insertMany([   {      "ID": 1,      "FullName": "John Smith"   },   {      "ID": 2,      "FullName": "Alice Johnson"   },   {      "ID": 3,      "FullName": "Michael Lee"   },   {      "ID": 4,      "FullName": "Sarah Brown"   },   {      "ID": 5,      "FullName": "David Johnson"   }])
db.groups.insertMany([   {      "ID": 1,      "Name": "Group 1A"   },   {      "ID": 2,      "Name": "Group 1B"   },   {      "ID": 3,      "Name": "Group 2A"   },   {      "ID": 4,      "Name": "Group 2B"   },   {      "ID": 5,      "Name": "Group 3A"   }])
db.students.insertMany([   {      "ID": 1,      "GroupID": 1,      "FullName": "John Smith"   },   {      "ID": 2,      "GroupID": 1,      "FullName": "Alice Johnson"   },   {      "ID": 3,      "GroupID": 1,      "FullName": "Michael Lee"   },   {      "ID": 4,      "GroupID": 1,      "FullName": "Sarah Brown"   },   {      "ID": 5,      "GroupID": 1,      "FullName": "David Johnson"   },   {      "ID": 6,      "GroupID": 2,      "FullName": "Jessica Garcia"   },   {      "ID": 7,      "GroupID": 2,      "FullName": "Kevin Lee"   },   {      "ID": 8,      "GroupID": 2,      "FullName": "Megan Williams"   },   {      "ID": 9,      "GroupID": 2,      "FullName": "Ryan Martinez"   },   {      "ID": 10,      "GroupID": 2,      "FullName": "Emily Rodriguez"   },   {      "ID": 11,      "GroupID": 3,      "FullName": "Jacob Kim"   },   {      "ID": 12,      "GroupID": 3,      "FullName": "Samantha Hernandez"   },   {      "ID": 13,      "GroupID": 3,      "FullName": "William Davis"   },   {      "ID": 14,      "GroupID": 3,      "FullName": "Olivia Martinez"   },   {      "ID": 15,      "GroupID": 3,      "FullName": "Ethan Rodriguez"   },   {      "ID": 16,      "GroupID": 4,      "FullName": "Ava Wilson"   },   {      "ID": 17,      "GroupID": 4,      "FullName": "Benjamin Taylor"   },   {      "ID": 18,      "GroupID": 4,      "FullName": "Emma Brown"   },   {      "ID": 19,      "GroupID": 4,      "FullName": "Christopher Garcia"   },   {      "ID": 20,      "GroupID": 4,      "FullName": "Isabella Johnson"   }])
db.lessons.insertMany([
   {
      "ID": 1,
      "DayOfWeek": "Monday",
      "Start_Time": new Date("2023-04-24T09:00:00Z"),
      "EndTime": new Date("2023-04-24T10:30:00Z"),
      "ClassroomID": 1,
      "GroupID": 1,
      "DisciplineID": 1,
      "TeacherID": 1
   },
   {
      "ID": 2,
      "DayOfWeek": "Monday",
      "Start_Time": new Date("2023-04-24T10:45:00Z"),
      "EndTime": new Date("2023-04-24T12:15:00Z"),
      "ClassroomID": 2,
      "GroupID": 2,
      "DisciplineID": 2,
      "TeacherID": 2
   },
   {
      "ID": 3,
      "DayOfWeek": "Monday",
      "Start_Time": new Date("2023-04-24T13:00:00Z"),
      "EndTime": new Date("2023-04-24T14:30:00Z"),
      "ClassroomID": 3,
      "GroupID": 3,
      "DisciplineID": 3,
      "TeacherID": 3
   },
   {
      "ID": 4,
      "DayOfWeek": "Monday",
      "Start_Time": new Date("2023-04-24T14:45:00Z"),
      "EndTime": new Date("2023-04-24T16:15:00Z"),
      "ClassroomID": 4,
      "GroupID": 4,
      "DisciplineID": 4,
      "TeacherID": 4
   },
   {
      "ID": 5,
      "DayOfWeek": "Monday",
      "Start_Time": new Date("2023-04-24T16:30:00Z"),
      "EndTime": new Date("2023-04-24T18:00:00Z"),
      "ClassroomID": 5,
      "GroupID": 5,
      "DisciplineID": 5,
      "TeacherID": 5
   },
   {
      "ID": 6,
      "DayOfWeek": "Wednesday",
      "Start_Time": new Date("2023-04-26T09:00:00Z"),
      "EndTime": new Date("2023-04-26T10:30:00Z"),
      "ClassroomID": 1,
      "GroupID": 1,
      "DisciplineID": 6,
      "TeacherID": 1
   },
   {
      "ID": 7,
      "DayOfWeek": "Wednesday",
      "Start_Time": new Date("2023-04-26T10:45:00Z"),
      "EndTime": new Date("2023-04-26T12:15:00Z"),
      "ClassroomID": 2,
      "GroupID": 2,
      "DisciplineID": 7,
      "TeacherID": 2
   },
  {
    ID: 8,
    DayOfWeek: "Friday",
    Start_Time: ISODate("2023-05-05T09:00:00Z"),
    EndTime: ISODate("2023-05-05T10:30:00Z"),
    ClassroomID: 5,
    GroupID: 4,
    DisciplineID: 9,
    TeacherID: 4
  },
  {
    ID: 9,
    DayOfWeek: "Friday",
    Start_Time: ISODate("2023-05-05T10:45:00Z"),
    EndTime: ISODate("2023-05-05T12:15:00Z"),
    ClassroomID: 2,
    GroupID: 1,
    DisciplineID: 4,
    TeacherID: 3
  },
  {
    ID: 10,
    DayOfWeek: "Friday",
    Start_Time: ISODate("2023-05-05T12:30:00Z"),
    EndTime: ISODate("2023-05-05T14:00:00Z"),
    ClassroomID: 1,
    GroupID: 2,
    DisciplineID: 6,
    TeacherID: 2
  },
  {
    ID: 11,
    DayOfWeek: "Friday",
    Start_Time: ISODate("2023-05-05T14:15:00Z"),
    EndTime: ISODate("2023-05-05T15:45:00Z"),
    ClassroomID: 3,
    GroupID: 3,
    DisciplineID: 8,
    TeacherID: 1
  },
  {
    ID: 12,
    DayOfWeek: "Monday",
    Start_Time: ISODate("2023-05-08T09:00:00Z"),
    EndTime: ISODate("2023-05-08T10:30:00Z"),
    ClassroomID: 4,
    GroupID: 4,
    DisciplineID: 10,
    TeacherID: 5
  },
  {
    ID: 13,
    DayOfWeek: "Monday",
    Start_Time: ISODate("2023-05-08T10:45:00Z"),
    EndTime: ISODate("2023-05-08T12:15:00Z"),
    ClassroomID: 5,
    GroupID: 1,
    DisciplineID: 1,
    TeacherID: 4
  },
  {
    ID: 14,
    DayOfWeek: "Monday",
    Start_Time: ISODate("2023-05-08T12:30:00Z"),
    EndTime: ISODate("2023-05-08T14:00:00Z"),
    ClassroomID: 2,
    GroupID: 2,
    DisciplineID: 5,
    TeacherID: 3
  },
  {
    ID: 15,
    DayOfWeek: "Monday",
    Start_Time: ISODate("2023-05-08T14:15:00Z"),
    EndTime: ISODate("2023-05-08T15:45:00Z"),
    ClassroomID: 1,
    GroupID: 3,
    DisciplineID: 7,
    TeacherID: 2
  }])
