from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from schools.api.viewsets import SchoolViewset
from students.api.viewsets import StudentViewset

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewset)
router.register(r'students', StudentViewset)

schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentViewset)

urlpatterns = [
    url(r'^', include(schools_router.urls)),
]

urlpatterns += router.urls
