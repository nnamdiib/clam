from django.test import TestCase

from studentable.models import Course

# Create your tests here.
class StudentableTest(TestCase):
	def test_default_course_creation(self):
		code = 'abc123'
		self.course = Course.objects.create(code=code)
		self.assertEqual(self.course.mon, ' ')
		self.assertEqual(self.course.tue, ' ')
		self.assertEqual(self.course.wed, ' ')
		self.assertEqual(self.course.thu, ' ')
		self.assertEqual(self.course.fri, ' ')

	def test_nondefault_course_creation(self):
		code = 'abc123'
		time = '12pm-14pm'
		self.course = Course.objects.create(code=code, mon=time, fri=time)

		self.assertEqual(self.course.mon, time)
		self.assertEqual(self.course.tue, ' ')
		self.assertEqual(self.course.wed, ' ')
		self.assertEqual(self.course.thu, ' ')
		self.assertEqual(self.course.fri, time)

