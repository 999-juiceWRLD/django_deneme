from django.urls import path 
from . import views 

app_name = 'polls' # namespacing url names
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'), # /polls/index
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # /polls/5/results
    path('<int:question_id>/vote/', views.vote, name='vote') # /polls/5/vote/
] # generic views

'''
The next step is to point the root URLconf at 
the polls.urls module. In mysite/urls.py, add 
an import for django.urls.include and insert an 
include() in the urlpatterns list.
'''