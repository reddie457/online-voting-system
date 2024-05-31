from django import forms
from online_voting_app.models import Contact, Customer, Admin, Category, Surveys, Votes, Add, View_options, Add_Election, Nomination, View_Nomination
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Surveys
        fields = ['title', 'description', 'category']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = "__all__"

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = "__all__"

class View_optionForm(forms.ModelForm):
    class Meta:
        model = View_options
        fields = "__all__"

class Add_ElectionForm(forms.ModelForm):
    class Meta:
        model = Add_Election
        fields = "__all__"

class NominationForm(forms.ModelForm):
    class Meta:
        model = Nomination
        fields = ["name", "gender", "age", "qualification", "about", "image", "idproof", "address", "mobile", "email", "election"]

class View_NominationForm(forms.ModelForm):
    class Meta:
        model = View_Nomination
        fields = "__all__"