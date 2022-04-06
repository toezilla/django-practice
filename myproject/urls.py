# 우리의 시나리오: 사용자가 접속할 떄, home, create, read로 접속했을 때 어떻게 하는가
# http://127.0.0.1
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/

from django.contrib import admin
from django.urls import path, include

# 이 안에는 라우팅 관련 정보가 적혀 있어야 함.
# admin은 장고가 기본적으로 가지고 있는 관리자 화면으로 이동하기 위한 라우팅 설정
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),#myapp으로 경로를 위임
]


