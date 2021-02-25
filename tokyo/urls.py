from django.urls import path
from .import views
'''import系はたくさん書いてもエラーがでない'''
from .views import AboutView, ExperiencesView, WorksView, SkillsView, ContactsView



app_name = 'tokyo'
urlpatterns = [
    path('', views.index, name='index'),
    # path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('experiences', ExperiencesView.as_view(), name='experiences'),
    path('works', WorksView.as_view(), name='works'),
    path('skills', SkillsView.as_view(), name='skills'),
    path('contacts', ContactsView.as_view(), name='contact'),

    # path('detail/<int:post_id>/', views.detail, name='detail'), 
   
]