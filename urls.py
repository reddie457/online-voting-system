"""online_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from online_voting_app import views as v
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('about/', v.about, name="about"),
    path('contact/', v.contact, name="contact"),

#Customer Urls
    path('customer/', v.customer, name="customer"),
    path('customer_loginpage/', v.customer_loginpage, name="customer_loginpage"),
    path('regpage/', v.regpage, name="regpage"),
    path('customer_reg/', v.customer_reg, name="customer_reg"),
    path('customer_login/', v.customer_login, name="customer_login"),
    path('customer_change/', v.customer_change, name="customer_change"),
    path('customer_display/', v.customer_display, name="customer_display"),
    path('customer_edit/<str:email>', v.customer_edit, name="customer_edit"),
    path('customer_update/', v.customer_update, name="customer_update"),
    path('customer_delete/<str:email>', v.customer_delete, name="customer_delete"),
    path('customer_view_survey/', v.customer_view_survey, name="customer_view_survey"),
    path('customer_view_election/', v.customer_view_election, name="customer_view_election"),
    path('view_feedback/', v.view_feedback, name="view_feedback"),
    path('add_nomination/<int:id>/', v.add_nomination, name="add_nomination"),
    path('view_my_nomination/', v.view_my_nomination, name="view_my_nomination"),
    path('customer_edit_nomination/<int:id>', v.customer_edit_nomination, name="customer_edit_nomination"),
    path('customer_update_nomination/', v.customer_update_nomination, name="customer_update_nomination"),
    path('my_nomination_delete/<int:id>', v.my_nomination_delete, name="my_nomination_delete"),
    path('view_options/<int:id>', v.view_options, name="view_options"),
    path('view_nomination/<int:id>', v.view_nomination, name="view_nomination"),
    path('customer_view_results/<int:id>', v.customer_view_results, name="customer_view_results"),
    path('admin_view_results/<int:id>', v.admin_view_results, name="admin_view_results"),
    path('customer_election_view_results/<int:id>', v.customer_election_view_results,
         name="customer_election_view_results"),
    path('election_view_results/<int:id>', v.election_view_results, name="election_view_results"),
    path('vote/<int:id>', v.vote, name="vote"),
    path('customer_logout/', v.customer_logout, name="customer_logout"),
    path('unknown/', v.unknown, name="unknown"),

#Admin Urls
    path('administration/', v.administration, name="administration"),
    path('admin_login/', v.admin_login, name="admin_login"),
    path('admin_change/', v.admin_change, name="admin_change"),
    path('add_category/', v.add_category, name="add_category"),
    path('manage_category/', v.manage_category, name="manage_category"),
    path('category_delete/<int:id>', v.category_delete, name="category_delete"),
    path('add_election/', v.add_election, name="add_election"),
    path('view_election/', v.view_election, name="view_election"),
    path('add_survey/', v.add_survey, name="add_survey"),
    path('view_survey/', v.view_survey, name="view_survey"),
    path('survey_edit/<int:id>', v.survey_edit, name="survey_edit"),
    path('survey_update/', v.survey_update, name="survey_update"),
    path('election_edit/<int:id>', v.election_edit, name="election_edit"),
    path('election_update/', v.election_update, name="election_update"),
    path('survey_delete/<int:id>', v.survey_delete, name="survey_delete"),
    path('election_delete/<int:id>', v.election_delete, name="election_delete"),
    path('admin_view_nomination/<int:id>', v.admin_view_nomination, name="admin_view_nomination"),
    path('accept_nomination/<int:id>', v.accept_nomination, name="accept_nomination"),
    path('reject_nomination/<int:id>', v.reject_nomination, name="reject_nomination"),
    path('admin_add/<int:id>', v.admin_add, name="admin_add"),
    path('admin_logout/', v.admin_logout, name="admin_logout"),
    path('unknownadmin/', v.unknownadmin, name="unknownadmin"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)