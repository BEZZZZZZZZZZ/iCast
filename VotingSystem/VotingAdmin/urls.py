from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Adminlogin', views.Adminlogin, name="Adminlogin"),
    path('Votingadmin', views.Votingadmin, name="Votingadmin"),
    path('upload_csv', views.upload_csv, name="Upload_CSV"),
    path('display_csv_data', views.display_csv_data, name="Display_data"),
    path('ManagePositions', views.ManagePositions, name="ManagePositions"),
    path('add_position_view', views.add_position_view, name="add_position"),
    path('generate_voter_accounts', views.generate_voter_accounts, name="generate_voter_accounts"),
    path('ManageParty', views.ManageParty, name="ManageParty"),
    path('add_party', views.add_party, name="add_party"),
    path('manage_fields', views.manage_fields, name="manage_fields"),
    path('edit_candidate_form', views.edit_candidate_form, name="edit_candidate_form"),
    path('field_create', views.field_create, name="field_create"),
    path('field_update/<int:field_id>', views.field_update, name="field_update"),
    path('field_delete/<int:field_id>', views.field_delete, name="field_delete"), 
    path('view_application/<int:pk>', views.view_application, name="generate_view"),
    path('approve_application/<int:pk>', views.approve_application, name="approved"),
    path('reject_application/<int:pk>', views.reject_application, name="reject"),
    path('manage_election', views.manage_election, name="manage_election"),
    path('stop_election/<int:election_id>/', views.stop_election, name="stop_election"),
    path('voting_page', views.voting_page, name="voting_page"),
    path('submit_vote', views.submit_vote, name="submit_vote"),
]
    

