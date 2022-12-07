from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,GetUserView,Signup
from enrolled.views import EnrolledByUser
from grades.views import GradesBySubject,GradesBySubjectAll
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/user/', GetUserView.as_view(), name='auth_data'),
    path('api/v1/grades-subject/', GradesBySubject.as_view(), name='auth_data'),
    path('api/v1/enrolled-user/', EnrolledByUser.as_view(), name='auth_data'),
    path('api/v1/grades-subject-all/', GradesBySubjectAll.as_view(), name='auth_data'),
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/student/', include('student.urls')),
    path('api/v1/subject/', include('subject.urls')),
    path('api/v1/settings/', include('settings.urls')),
    path('api/v1/grades/', include('grades.urls')),
    path('api/v1/enrolled/', include('enrolled.urls')),
    # path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
]