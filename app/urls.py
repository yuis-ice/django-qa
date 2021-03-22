from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# from main.views import IndexPageView, ChangeLanguageView
from main.views import QuestionList, ChangeLanguageView
from main.views import UserQuestionList
from main.views import QuestionView
from main.views import MetaView
# from main.views import QuestionEditView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', IndexPageView.as_view(), name='index'),
    # path('', QuestionList.as_view(), name="home"),
    path('', QuestionList.as_view(), name="index"),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    path('qaapp/', include('qaapp.urls')),
    # path('questions/<user_id>/', UserQuestionList.as_view()),
    path('<user_id>/questions', UserQuestionList.as_view(), name='questions_by_user'),
    path('questions/<question_id>/', QuestionView.as_view(), name='question'),
    # path('questions/edit/<question_id>/', QuestionEditView.as_view(), name='question_edit'),

    path('meta/', MetaView.as_view(), name='meta'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
