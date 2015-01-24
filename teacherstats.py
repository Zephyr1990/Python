def most_classes(dictio):
  max_value=0
  winner=''
  for key, value in dictio.items():
    if len(value)>max_value:
      max_value = len(value)
      winner = key
  return winner

def num_teachers(dictio):
  return len(dictio)

def stats(dictio):
  teacherlist = []
  classlist = []
  number_of_classes = []
  statslist = []
  for key in dictio.keys():
    teacherlist.append(key)
    if key in dictio:
      numclass = len(dictio.get(key))
      classes = dictio.get(key)
      classlist.append(classes)
      number_of_classes.append(numclass)

  for value in range(len(teacherlist)):
    templist = []
    templist.append(teacherlist[key])
    templist.append(number_of_classes[key])
    statslist.append(templist)
  return statslist

def courses(teachers):
  total_courses = []
  end_result = []
  for key in teachers.items():
    total_courses.append(teachers.values())
  for courses_of_one_teacher in teachers.values():
    for course in courses_of_one_teacher:
      end_result.append(course)
  return end_result
