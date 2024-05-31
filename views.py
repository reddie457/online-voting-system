import datetime

from django.db.models import Count
from django.shortcuts import render, redirect

from online_voting_app.forms import ContactForm, CustomerForm, AdminForm, CategoryForm, SurveyForm, VoteForm, AddForm, View_optionForm, Add_ElectionForm, NominationForm, View_NominationForm
from online_voting_app.models import Contact, Customer, Admin, Category, Surveys, Votes, Add, View_options, Add_Election, Nomination, View_Nomination

import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    if request.method == "POST":
        print("hii")
        form = ContactForm(request.POST)
        print("hii")
        if form.is_valid():
            form.save()
        return render(request, "contact.html", {"msg": "Success"})
    return render(request, "contact.html", {})

#Customer Views
def customer(request):
    return render(request, "customer.html", {})

def customer_loginpage(request):
    return render(request, "customer_login.html", {"msg": ""})

def regpage(request):
    return render(request, "customer_reg.html", {})

def customer_reg(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
    return render(request, "customer_login.html", {"msg": ""})

def customer_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session["email"] = email
            return render(request, "customer.html", {"msg": email})
        else:
            return render(request, "customer_login.html", {"msg": "email or password not exist"})
    return render(request, "customer_login.html", {})

def is_customer_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def customer_change(request):
    if is_customer_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                customer = Customer.objects.get(email=email, password=password)
                customer.password = newpassword
                customer.save()
                msg = "Password Updated Successfully"
                return render(request, "customer_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "customer_change.html", {"msg": msg})
        return render(request, "customer_change.html", {})
    else:
        return render(request, "customer_change.html", {})

def customer_display(request):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    print("hello")
    return render(request, "customer_display.html", {"customer": customer})

def customer_edit(request, email):
    customer = Customer.objects.get(email=email)
    return render(request, "customer_edit.html", {"customer": customer})

def customer_update(request):
    if request.method == "POST":
        email = request.POST["email"]
        customer = Customer.objects.get(email=email)
        customer = CustomerForm(request.POST, instance=customer)
        if customer.is_valid():
            customer.save()
        return redirect("/customer_display")
    return redirect("/customer_display")

def customer_delete(request, email):
    customer = Customer.objects.get(email=email)
    customer.delete()
    return redirect("/customer_reg")

def customer_view_survey(request):
    survey = Surveys.objects.filter(status=1)
    print("hello")
    return render(request, "customer_view_survey.html", {"survey": survey})

def customer_view_results(request,id):
    view_option = View_options.objects.filter(surveys_id=id)
    result = (View_options.objects.values('title')).filter(surveys_id=id).annotate(total=Count('title')).order_by('title')
    print("res ",result)
    print("hello")
    return render(request, "customer_view_results.html", {"view_option": view_option,"result":result})



def unknown(request):
    return render(request,"customer.html",{})

def unknownadmin(request):
    return render(request,"administration.html",{})

def view_options(request,id):
    email = request.session['email']
    print(email)
    customer = Customer.objects.get(email=email)
    surveys = Surveys.objects.get(id=id)
    add = Add.objects.filter(surveys_id=id)
    print("hiii0")
    if request.method == "POST":
        print("hii1")
        print(customer.email)
        if View_options.objects.filter(customer_id=email).exists():
            print("email already taken")
            return render(request, "view_options.html", {"msg": "you have already voted for this survey", "surveys": surveys.id, "customer": customer.email, "add": add})
        else:
            view_options = View_optionForm(request.POST)
            print("hii2", view_options.errors)
            if view_options.is_valid():
                view_options.save()
                return render(request, "view_options.html", {"msg": "Success", "surveys": surveys.id, "customer": customer.email, "add": add})
        return render(request, "view_options.html", {"surveys": surveys.id, "customer": customer.email, 'add':add})
    return render(request, "view_options.html", {"surveys": surveys.id, "customer": customer.email, "add": add})

def admin_view_results(request,id):
    view_options = View_options.objects.filter(surveys_id=id)
    results = (View_options.objects.values('title')).filter(surveys_id=id).annotate(total=Count('title')).order_by('title')
    print("res ",results)
    print("hello")
    return render(request, "admin_view_results.html", {"view_options": view_options,"results":results})


def vote(request,id):
    email = request.session['email']
    print(email)
    customer = Customer.objects.get(email=email)
    surveys = Surveys.objects.get(id=id)
    print(surveys)
    if request.method == "POST":
        print("hii")
        print(customer.email)
        vote = VoteForm(request.POST)
        print("hii", vote.errors)
        if vote.is_valid():
            vote.save()
        return render(request, "vote.html", {"msg": "Success", "surveys": surveys.id,  "customer": customer.email})
    return render(request, "vote.html", {"surveys": surveys.id,  "customer": customer.email})

# def vote(request):
#     votes = Votes.objects.all()
#     print("hello")
#     return render(request, "vote.html", {"votes": votes})


def customer_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
    return render(request, "customer_login.html", {"email": email})

#Admin Views
def administration(request):
    return render(request, "administration.html", {})

def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        admin = Admin.objects.filter(email=email, password=password)
        if admin.exists():
            print("hello")
            request.session["email"] = email
            return render(request, "administration.html", {"msg": email})
        else:
            return render(request, "admin_login.html", {"msg": "Invalid Email or Password"})
    return render(request, "admin_login.html", {"msg": ""})

def is_admin_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def admin_change(request):
    if is_admin_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                admin = Admin.objects.get(email=email, password=password)
                admin.password = newpassword
                admin.save()
                msg = "Password Updated Successfully"
                return render(request, "admin_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "admin_change.html", {"msg": msg})
        return render(request, "admin_change.html", {})
    else:
        return render(request, "admin_change.html", {})

def add_category(request):
    if request.method == "POST":
        print("hii")
        form = CategoryForm(request.POST)
        print("hii")
        if form.is_valid():
            form.save()
        return render(request, "add_category.html", {"msg": "Success"})
    return render(request, "add_category.html", {})

def manage_category(request):
    category = Category.objects.all()
    print("hello")
    return render(request, "manage_category.html", {"category": category})

def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("/add_category")

def add_survey(request):
    if request.method == "POST":
        print("hii")
        form = SurveyForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
        return render(request, "add_survey.html", {"msg": "Success"})
    category = Category.objects.all()
    return render(request, "add_survey.html", {"category": category})

def view_survey(request):
    survey = Surveys.objects.all()
    print("hello")
    return render(request, "view_survey.html", {"survey": survey})

def survey_edit(request, id):
    survey = Surveys.objects.get(id=id)
    category = Category.objects.all()
    return render(request, "survey_edit.html", {"survey": survey, "category": category})

def survey_update(request):
    if request.method == "POST":
        surveyid = request.POST["id"]
        survey = Surveys.objects.get(id=surveyid)
        survey = SurveyForm(request.POST, instance=survey)
        print("errors", survey.errors)
        if survey.is_valid():
            survey.save()
            print("hell2.0")
            return redirect("/view_survey")
    return redirect("/view_survey")

def survey_delete(request, id):
    survey = Surveys.objects.get(id=id)
    survey.delete()
    return redirect("/add_survey")

# def admin_add(request, id):
#     survey = Surveys.objects.get(id=id)
#     return render(request, "admin_add.html", {"survey": survey})
#
# def admin_add_update(request):
#     if request.method == "POST":
#         surveyid = request.POST["id"]
#         survey = Surveys.objects.get(id=surveyid)
#         survey = SurveyForm(request.POST, instance=survey)
#         if survey.is_valid():
#             survey.save()
#         return redirect("/view_survey")
#     return redirect("/view_survey")
def admin_add(request,id):
    # email = request.session['email']
    # print(email)
    # customer = Customer.objects.get(email=email)
    surveys = Surveys.objects.get(id=id)
    print(surveys)
    if request.method == "POST":
        print("hii")
        # print(customer.email)
        add = AddForm(request.POST)
        print("hii", add.errors)
        if add.is_valid():
            add.save()
        return render(request, "admin_add.html", {"msg": "Success", "surveys": surveys.id, 'title':surveys.title})
    return render(request, "admin_add.html", {"surveys": surveys.id,  'title':surveys.title})

def admin_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
    return render(request, "admin_login.html", {"email": email})

def add_election(request):
    if request.method == "POST":
        print("hii")
        form = Add_ElectionForm(request.POST)
        print("hii")
        if form.is_valid():
            form.save()
        return render(request, "add_election.html", {"msg": "Success"})
    return render(request, "add_election.html", {})


def view_election(request):
    election = Add_Election.objects.all()
    print("hello")
    return render(request, "view_election.html", {"election": election})

def election_edit(request, id):
    election = Add_Election.objects.get(id=id)
    return render(request, "election_edit.html", {"election": election})

def election_update(request):
    if request.method == "POST":
        electionid = request.POST["id"]
        election = Add_Election.objects.get(id=electionid)
        election = Add_ElectionForm(request.POST, instance=election)
        print("errors", election.errors)
        if election.is_valid():
            election.save()
            print("hell2.0")
            return redirect("/view_election")
    return redirect("/view_election")

def election_delete(request, id):
    election = Add_Election.objects.get(id=id)
    election.delete()
    return redirect("/add_election")

def customer_view_election(request):
    elections = Add_Election.objects.all()
    print("hello")
    today = datetime.datetime.today()
    return render(request, "customer_view_election.html", {"elections": elections,"today":today})

# def add_nomination(request,id):
#     email = request.session['email']
#     customer = Customer.objects.get(email=email)
#     election = Add_Election.objects.get(id=id)
#     if request.method == "POST":
#         nomination = NominationForm(request.POST, request.FILES, instance=nomination)
#         if nomination.is_valid():
#             nomination.save()
#             return render(request, "add_nomination.html", {"msg": "not valid", "election": election.id, "customer": customer.email})
#     return render(request, "add_nomination.html", {"msg": "not Success", "election": election.id, "customer": customer.email})

def add_nomination(request,id):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    election = Add_Election.objects.get(id=id)
    if request.method == "POST":
        nomination = NominationForm(request.POST, request.FILES)
        if nomination.is_valid():
            nomination.save()
        else:
            print(nomination.errors)
            return render(request, "add_nomination.html", {"msg": "Success", "election": election,  "customer": customer, "id": id})
    return render(request, "add_nomination.html", {"election": election,  "customer": customer, "id": id})

def admin_view_nomination(request,id):
    nomination = Nomination.objects.filter(election_id=id)
    election = Add_Election.objects.get(id=id)
    print("hello")
    return render(request, "admin_view_nomination.html", {"nomination": nomination, "election":election})

def accept_nomination(request,id):
    accept = Nomination.objects.get(id=id)
    accept.status='Accepted'
    accept.save()
    election = Add_Election.objects.all()
    return render(request, "view_election.html", {"election":election})

def reject_nomination(request,id):
    reject = Nomination.objects.get(id=id)
    reject.status = 'Rejected'
    reject.save()
    election = Add_Election.objects.all()
    return render(request, "view_election.html", {"election": election})
def view_my_nomination(request):
    email = request.session["email"]
    nomination = Nomination.objects.filter(email=email)
    print("hello")
    return render(request, "view_my_nomination.html", {"nomination": nomination})

def view_nomination(request,id):
    email = request.session['email']
    print(email)
    customer = Customer.objects.get(email=email)
    election = Add_Election.objects.get(id=id)
    nomination = Nomination.objects.filter(election_id=id, status="Accepted")
    print("hiii0")
    if request.method == "POST":
        print("hii1")
        print(customer.email)
        if View_Nomination.objects.filter(customer_id=email,election_id=id).exists():
            print("email already taken")
            return render(request, "view_nomination.html", {"msg": "you have already nominate for this nominations", "election": election.id, "customer": customer.email})
        else:
            nomination = View_NominationForm(request.POST)
            print("hii2", nomination.errors)
            if nomination.is_valid():
                nomination.save()
                return render(request, "view_nomination.html", {"msg": "Success", "election": election.id, "customer": customer.email, "nomination":nomination})
        return render(request, "view_nomination.html", {"election": election.id, "customer": customer.email, "nomination":nomination})
    return render(request, "view_nomination.html", {"election": election.id, "customer": customer.email, "nomination":nomination})

def customer_election_view_results(request,id):
    view_nominations = View_Nomination.objects.filter(election_id=id)
    results = (View_Nomination.objects.values('name')).filter(election_id=id).annotate(total=Count('name')).order_by('name')
    print("res ",results)
    print("hello")
    return render(request, "customer_election_view_results.html", {"view_nominations": view_nominations,"results":results})

def election_view_results(request,id):
    view_nomination = View_Nomination.objects.filter(election_id=id)
    results = (View_Nomination.objects.values('name')).filter(election_id=id).annotate(total=Count('name')).order_by('name')
    print("res ",results)

    lablelist=[]
    valuelist=[]
    for item in results:
        lablelist.append(item["name"])
        valuelist.append(item["total"])
    index = np.arange(len(lablelist))
    barlist = plt.bar(index, valuelist)
    barlist[0].set_color('r');
    barlist[1].set_color('b');
    plt.xlabel('Candidates', fontsize=5)
    plt.ylabel('No of Votes', fontsize=5)
    plt.xticks(index, lablelist, fontsize=20, rotation=0)
    plt.title('Results')
    # plt.legend(label)
    # plt.show()
    plt.plot()
    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph = base64.b64encode(buf.read())
    print("hello")
    return render(request, "election_view_results.html", {"view_nomination": view_nomination,"results":results,"graph":graph.decode('utf-8')})
#8008587665

def customer_edit_nomination(request, id):
    nomination = Nomination.objects.get(id=id)
    return render(request, "customer_edit_nomination.html", {"nomination": nomination})

def customer_update_nomination(request):
    if request.method == "POST":
        nominationid = request.POST["id"]
        nomination = Nomination.objects.get(id=nominationid)
        nomination = NominationForm(request.POST, instance=nomination)
        print("errors", nomination.errors)
        if nomination.is_valid():
            nomination.save()
            print("hell2.0")
            return redirect("/view_my_nomination")
    return redirect("/view_my_nomination")

def my_nomination_delete(request, id):
    nomination = Nomination.objects.get(id=id)
    nomination.delete()
    return redirect("/view_my_nomination")


def view_feedback(request):
    feedback = Contact.objects.all()
    print("hello")
    return render(request, "view_feedback.html", {"feedback": feedback})

def customer_view_survey(request):
    survey = Surveys.objects.all()
    return render(request, "customer_view_survey.html", {"survey":survey})
