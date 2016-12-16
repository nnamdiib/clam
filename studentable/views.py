from django.shortcuts import render

from .models import Course

from .forms import CourseCodesForm

# *************
# Main views
# *************

def index(request):
  #code_list = []
  if request.method == 'POST':
    form = CourseCodesForm(request.POST)
    if form.is_valid():
      code_list = request.POST.getlist("code")
      return showTimetable(request, code_list)
  else:
    form = CourseCodesForm()
    
  return render(request, 'studentable/index.html', {'form': form})


def showTimetable(request, code_list):
  courses = [] # will contain course objects

  for course_code in code_list:
    courses += Course.objects.filter(code = str(course_code).lower())

  clashes = get_schedule_conflicts(courses)
  payload = {'courses': courses, 'is_custom': True, 'clashes': clashes}
  return render(request, 'studentable/timetable.html', payload)


# ***********
# Helper functions
# ***********

def get_schedule_conflicts(course_objects):
  # Gets all courses with scheduling conflicts for each day. 
  monday = []
  tuesday = []
  wednesday = []
  thursday = []
  friday = []

  mon_courses = [course for course in course_objects if course.mon != ' ']
  mon_clashes = []
  for course in mon_courses:
    existing = [(int(c.mon[:2]) + int(c.mon[5:7]), c) for c in mon_courses if c != course]
    present = int(course.mon[:2]) + int(course.mon[5:7])
    clash = []
    for s in existing:
      if (s[0] == present) or (s[0] == present-1) or (s[0] == present+1):
        mon_clashes.append((course.code, s[1].code))
  m = sort_list_of_tups(mon_clashes)
  for tup in m:
    if tup not in monday:
      monday.append(tup)

  tue = [course for course in course_objects if course.tue != ' ']
  tue_clashes = []
  for course in tue:
    existing = [(int(c.tue[:2]) + int(c.tue[5:7]), c) for c in tue if c != course]
    present = int(course.tue[:2]) + int(course.tue[5:7])
    clash = []
    for s in existing:
      if (s[0] == present) or (s[0] == present-1) or (s[0] == present+1):
        tue_clashes.append((course.code, s[1].code))
  m = sort_list_of_tups(tue_clashes)
  for tup in m:
    if tup not in tuesday:
      tuesday.append(tup)


  wed = [course for course in course_objects if course.wed != ' ']
  wed_clashes = []
  for course in wed:
    existing = [(int(c.wed[:2]) + int(c.wed[5:7]), c) for c in wed if c != course]
    present = int(course.wed[:2]) + int(course.wed[5:7])
    clash = []
    for s in existing:
      if (s[0] == present) or (s[0] == present-1) or (s[0] == present+1):
        wed_clashes.append((course.code, s[1].code))
  m = sort_list_of_tups(wed_clashes)
  for tup in m:
    if tup not in wednesday:
      wednesday.append(tup)


  thu = [course for course in course_objects if course.thu != ' ']
  thu_clashes = []
  for course in thu:
    existing = [(int(c.thu[:2]) + int(c.thu[5:7]), c) for c in thu if c != course]
    present = int(course.thu[:2]) + int(course.thu[5:7])
    clash = []
    for s in existing:
      if (s[0] == present) or (s[0] == present-1) or (s[0] == present+1):
        thu_clashes.append((course.code, s[1].code))
  m = sort_list_of_tups(thu_clashes)
  for tup in m:
    if tup not in thursday:
      thursday.append(tup)


  fri = [course for course in course_objects if course.fri != ' ']
  fri_clashes = []
  for course in fri:
    existing = [(int(c.fri[:2]) + int(c.fri[5:7]), c) for c in fri if c != course]
    present = int(course.fri[:2]) + int(course.fri[5:7])
    clash = []
    for s in existing:
      if (s[0] == present) or (s[0] == present-1) or (s[0] == present+1):
        fri_clashes.append((course.code, s[1].code))
  m = sort_list_of_tups(fri_clashes)
  for tup in m:
    if tup not in friday:
      friday.append(tup)

  if monday or tuesday or wednesday or thursday or friday:
    clashesDict = {'monday':monday,
                   'tuesday':tuesday,
                   'wednesday':wednesday,
                   'thursday':thursday,
                   'friday':friday
                  }
  else:
    clashesDict = None

  return clashesDict


def sort_list_of_tups(lot):
  return [sorted(tup) for tup in lot]