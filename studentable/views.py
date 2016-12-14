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
  # Gets all courses with time clashes for each day. 
  # returns this data struct ---> { 'monday': [ ('1-2 PM', [courses] ), 'tuesday': ... ]}
  mon_times = {}
  tue_times = {}
  wed_times = {}
  thu_times = {}
  fri_times = {}

  # get a dict with key-value pairs of class times(key) and a list of course codes(val).
  for course in course_objects:
    if course.mon:
      if len(course.mon.split(', ')) > 1:
        for t in course.mon.split(', '):
          mon_times.setdefault(t, []).append(course.__str__())
      else:
        mon_times.setdefault(course.mon, []).append(course.__str__())
    if course.tue:
      if len(course.tue.split(', ')) > 1:
        for t in course.tue.split(', '):
          tue_times.setdefault(t, []).append(course.__str__())
      else:
        tue_times.setdefault(course.tue, []).append(course.__str__())
    if course.wed:
      if len(course.wed.split(', ')) > 1:
        for t in course.wed.split(', '):
          wed_times.setdefault(t, []).append(course.__str__())
      else:
        wed_times.setdefault(course.wed, []).append(course.__str__())
    if course.thu:
      if len(course.thu.split(', ')) > 1:
        for t in course.thu.split(', '):
          thu_times.setdefault(t, []).append(course.__str__())
      else:
        thu_times.setdefault(course.thu, []).append(course.__str__())
    if course.fri:
      if len(course.fri.split(', ')) > 1:
        for t in course.fri.split(', '):
          fri_times.setdefault(t, []).append(course.__str__())
      else:
        fri_times.setdefault(course.fri, []).append(course.__str__())

  times = {
            "Monday":mon_times,
            "Tuesday":tue_times,
            "Wednesday":wed_times,
            "Thursday":thu_times,
            "Friday":fri_times
          }

  clash_dict = {}

  for day in times:
    for (time, courses) in times[day].items():
      if len(courses) > 1 and time != ' ':
        clash_dict.setdefault(day, []).append((time, courses))

  return clash_dict

