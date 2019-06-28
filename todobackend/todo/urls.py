
from django.urls import path, include             # add this
from rest_framework import routers                    # add this
from todo import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this

urlpatterns = [    
    path('api/', include(router.urls))                # add this
]