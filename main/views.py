from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoL, Items
from .form import CreateNewList


# Create your views here.

def index(response, id):
    ls = ToDoL.objects.get(id=id)

    # {'save':['save'],'c1':['clicked']}
    if response.method == 'POST':
        if response.POST.get("save"):
            for item in ls.items_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    # Model.objects.filter(id = 223).update(field1 = 2)
                    ls.items_set.filter(id=item.id).update(complete=True)
                else:
                    ls.items_set.filter(id=item.id).update(complete=False)
        else:
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.items_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "main/view_list.html", {"ls": ls})


def home(response):
    ls = ToDoL.objects.all()
    return render(response, "main/home.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoL(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
