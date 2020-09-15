from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import Account,Transactions
#from .forms import EditForm,AddForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views import View


# Create your views here.
class Account_list(ListView):
	model = Account
	template_name = 'Accounts/Account_list.html'

class Account_details(View):
	def get(self, request, *args, **kwargs):
		dt = Account.objects.get(pk=kwargs['pk'])
		trans = Transactions.objects.filter(from_account=dt)
		
		context = {
		'transactions':trans,
		'details': dt
		}
		return render(request,'Accounts/details.html',context)


class EditDetails(UpdateView):


	model = Transactions
	fields = ['from_account','amount','description','transaction_type']
	template_name = 'Accounts/edit_details.html'
	success_url = '/'



class DeleteDetails(DeleteView):
	model = Transactions
	template_name = 'Accounts/delete_details.html'
	success_url = '/'

# class AddTransactions(CreateView):
# 	model = Transactions
# 	fields = ['amount','description','transaction_type']
# 	success_url = reverse_lazy('Account_details')

