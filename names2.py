def names(users):
    names = []
    for key, data in users.items():
        for value in data:
          temp = value["first_name"], value["last_name"]
          names.append(temp)
    print "Students:"
    i = 1
    for x in names:
        temp = x[0] + " " + x[1]
        if temp == "Michael Choi":
            print "Instructors:"
            i = 1
        print str(i) + " - " + temp.upper() + " - " + str(len(temp)-temp.count(' '))
        i = i + 1



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

names(users)
