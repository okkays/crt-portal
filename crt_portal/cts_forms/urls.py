from django.urls import path

from .views import (ActionsView, index_view, ShowView, ProFormView,
                    SaveCommentView, TrendView, ResponseView,
                    PrintView, ProfileView, SaveReportAttachmentView)
from .forms import ProForm

app_name = 'crt_forms'


urlpatterns = [
    path('view/<int:id>/', ShowView.as_view(), name='crt-forms-show'),
    path('view/<int:id>/response', ResponseView.as_view(), name='crt-forms-response'),
    path('view/<int:id>/print', PrintView.as_view(), name='crt-forms-print'),
    path('view/', index_view, name='crt-forms-index'),
    path('view/update-profile', ProfileView.as_view(), name='cts-forms-profile'),
    path('new/', ProFormView.as_view([ProForm]), name='crt-pro-form'),
    path('actions/', ActionsView.as_view(), name='crt-forms-actions'),
    path('actions/print', PrintView.as_view(), name='crt-forms-print'),
    path('comment/report/<int:report_id>/', SaveCommentView.as_view(), name='save-report-comment'),
    path('attachment/report/<int:report_id>/', SaveReportAttachmentView.as_view(), name='save-report-attachment'),
    path('trends/', TrendView.as_view(), name='trends'),
]
