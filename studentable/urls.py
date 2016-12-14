from django.conf.urls import url
import studentable.views

urlpatterns = [
							url(r'^$', studentable.views.index, name='index')
]