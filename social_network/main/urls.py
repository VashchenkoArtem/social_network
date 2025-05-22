from django.urls import path
from social_network.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import DeleteView, EditView


urlpatterns = [
    path('delete/<int:pk>', DeleteView.as_view(), name = "delete"),
    path('edit/<int:pk>', EditView.as_view(), name='edit')
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)