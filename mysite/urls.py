
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse   # ✅ add this

# ✅ create a view function
def home(request):
    return HttpResponse("🚀 Welcome Sahil! This is my Django website")

urlpatterns = [
    path('', home),                    # ✅ homepage
    path('admin/', admin.site.urls),
]
