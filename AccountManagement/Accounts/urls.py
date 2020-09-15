from django.urls import path
from . import views

urlpatterns = [
	path('',views.Account_list.as_view(),name = 'Account_list'),
	path('User/<int:pk>/',views.Account_details.as_view(),name = 'Account_details'),
	path('Transaction/Edit/<int:pk>/',views.EditDetails.as_view(),name = 'EditDetails'),
	path('Transaction/Delete/<int:pk>/',views.DeleteDetails.as_view(),name = 'DeleteDetails'),
	# path('ADD/<int:id1>/',views.Add_transaction,name='Add_transaction'),
]