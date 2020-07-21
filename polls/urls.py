from django.urls import path
from . import views

#增加命名空間
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/

    # the 'name' value as called by the {% url %} template tag

    path('<int:pk>/',views.DetailView.as_view(), name='detail'),

    # 改变投票详情视图的 URL，比如想改成 polls/specifics/12/
    # path('specifics/<int:pk>/',views.ResultsView.as_view(), name='detail'),

    path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]