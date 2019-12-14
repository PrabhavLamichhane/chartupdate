from django.urls import path

from . import views


urlpatterns = [
    path('', views.bar_graph, name='index'),
]
# from django.urls import path
# from . import views


# urlpatterns = [
#     path('bargraph/<int:year>',views.bargraph, name='bargraph' ),
# ]
