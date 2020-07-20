from django.urls import path
from . import views

#增加命名空間
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
        # ex: /polls/5/

        # the 'name' value as called by the {% url %} template tag

    path('<int:question_id>/',views.detail, name='detail'),

    # 改变投票详情视图的 URL，比如想改成 polls/specifics/12/
    # path('specifics/<int:question_id>/',views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]