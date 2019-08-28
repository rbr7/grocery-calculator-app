from django.shortcuts import render, redirect
from gtracker.forms import SignupForm
from gtracker.forms import LoginForm
from django.http import HttpResponse
from gtracker.models import NewUser
from gtracker.models import ProductList
from gtracker.models import LoggedinUser
from gtracker.forms import AddgForm
from gtracker.forms import AddgOwnForm
import json
import datetime


# Create your views here.
def home(request):
    return render(request,"home.html",{})

def signup(request):
    username="not signed up"
    emailid="not signed up"
    password="not signed up"
    phoneno="not signed up"

    if(request.method=="POST"):
        MySignupForm=SignupForm(request.POST)
        if MySignupForm.is_valid():
            MyNewUser=NewUser()
            (username,emailid,phoneno,password)=MySignupForm.clean_message()
            MyNewUser.username=username
            MyNewUser.password=password
            MyNewUser.emailid=emailid
            MyNewUser.phoneno=phoneno
            MyNewUser.save()
            MyProductList=ProductList()
            MyProductList.emailid=emailid
            MyProductList.save()
            user_list=NewUser.objects.all()
            print("user_list in sign up" , user_list)
            return render(request, "signedup.html")
        else:
            text  = "Invalid data. Please enter again"
            return render(request, "signup.html", {"text":text})


def login(request):
    emailid = "not logged in"
    password="not logged in"
    user_list=NewUser.objects.all()
    l=len(user_list)
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            (emailid, password)=MyLoginForm.clean_message()
            for i in range(0,l):
                if(emailid==user_list[i].emailid):
                    if(password==user_list[i].password):
                        b3=user_list[i].emailid
                        LoggedinUser.objects.all().delete()
                        MyLoggedinUser= LoggedinUser()
                        MyLoggedinUser.emailid= emailid
                        MyLoggedinUser.save()
                        return redirect(details,b3=b3)
                    else:
                        text="Password is incorrect "
                        return render(request,'login.html',{"text":text})
                else:
                    if(i==(l-1)):
                        text="You are not an existing user. Please sign up."
                        return render(request, "signup.html",{"text": text} )
                    else:
                        continue

def addg(request):
    t= datetime.datetime.now().date().strftime("%Y-%m-%d")
    poplist=[]
    if request.method=="POST":
        MyAddgForm= AddgForm(request.POST)
        if MyAddgForm.is_valid():
            (dc,dr,ds,dp) = MyAddgForm.clean_message()
            a=ProductList.objects.all()
            b=LoggedinUser.objects.all()
            b3 = b[0].emailid
            for i in a:
                if(b3==i.emailid):
                    l1=i.myList
                    if(l1==None):
                        break
                    else:
                        l1 =json.loads(l1)
                        l2 = len(l1)
            a1=dc.get("coffee")
            a1.append(t)
            a2=dr.get("rice")
            a2.append(t)
            a3=ds.get("sugar")
            a3.append(t)
            a4=dp.get("pulses")
            a4.append(t)
            if(l1==None):
                if(i.emailid==b[0].emailid):
                    poplist.append(dc)
                    poplist.append(dr)
                    poplist.append(ds)
                    poplist.append(dp)
                    i.myList=json.dumps(poplist)
                    i.save()
            else:
                poplist=[]
                for i in a:
                    if(i.emailid==b[0].emailid):
                        if(a1[0]==True):
                            poplist.append(dc)
                        else:
                            poplist.append(l1[0])

                        if(a2[0]==True):
                            poplist.append(dr)
                        else:
                            poplist.append(l1[1])

                        if(a3[0]==True):
                            poplist.append(ds)
                        else:
                            poplist.append(l1[2])

                        if(a4[0]==True):
                            poplist.append(dp)
                        else:
                            poplist.append(l1[3])
                        i.myList=json.dumps(poplist)
                        i.save()
            return redirect(details, b3=b3)

def addgown(request):
    t= datetime.datetime.now().date().strftime("%Y-%m-%d")
    def checker(productsofl2,l2,a):
        itemsofl2=[]
        j=0
        pos=-1
        while(j<len(productsofl2)):
            if(a==productsofl2[j]):
                i=0
                while(i<len(l2)):
                    temp= list(l2[i].keys())
                    itemsofl2.append(temp[0])
                    c=l2[i].get(itemsofl2[i])
                    if(c[0]==a):
                        pos=i
                        return(pos)
                    i=i+1
            j=j+1
        return(pos)
    poplist1=[]
    if request.method=="POST":
        MyAddgOwnForm= AddgOwnForm(request.POST)
        if MyAddgOwnForm.is_valid():
            (dg1,dg2,dg3)=MyAddgOwnForm.clean_message()
            a = ProductList.objects.all()
            b = LoggedinUser.objects.all()
            b3 = b[0].emailid
            for i in a:
                if (b3 == i.emailid):
                    l2 = i.myListOwn
                    if (l2 == None):
                        break
                    else:
                        l2 = json.loads(l2)
            a1 = dg1.get("g1")
            a1.append(t)
            a2 = dg2.get("g2")
            a2.append(t)
            a3 = dg3.get("g3")
            a3.append(t)

            if (l2 == None):
                if (i.emailid == b[0].emailid):
                    if(a1[0]==''):
                        pass
                    else:
                        poplist1.append(dg1)
                    if(a2[0]==''):
                        pass
                    else:
                        poplist1.append(dg2)
                    if(a3[0]==''):
                        pass
                    else:
                        poplist1.append(dg3)
                    i.myListOwn = json.dumps(poplist1)
                    i.save()

            else:
                poplist1 = l2
                itemsofl2=[]
                productsofl2 = []
                i=0
                while(i<len(l2)):
                    temp= list(l2[i].keys())
                    itemsofl2.append(temp[0])
                    c= l2[i].get(itemsofl2[i])
                    if(c[0]!=''):
                        productsofl2.append(c[0])
                    i=i+1
                for i in a:
                    if (i.emailid == b3):
                        if(a1[0]==''):
                            pass
                        else:
                            pos= checker(productsofl2,l2,a1[0])
                            if(pos==-1):
                                poplist1.append(dg1)
                            else:
                                poplist1[pos]= dg1
                        if(a2[0]==''):
                            pass
                        else:
                            pos= checker(productsofl2,l2,a2[0])
                            if(pos==-1):
                                poplist1.append(dg2)
                            else:
                                poplist1[pos]= dg2
                        if(a3[0]==''):
                            pass
                        else:
                            pos= checker(productsofl2,l2,a3[0])
                            if(pos==-1):
                                poplist1.append(dg3)
                            else:
                                poplist1[pos]= dg3
                    i.myListOwn = json.dumps(poplist1)
                    i.save()
            return redirect(details, b3=b3)


def details(request, b3):
    def explist(l1):
        len1 = len(l1)
        i = 0

        item = []
        itemn = []
        itemq = []
        itemuq = []
        itemwc = []
        itemuw = []
        while (i < len1):

            temp = list(l1[i].keys())
            item.append(temp[0])
            c = l1[i].get(item[i])
            if (c[0] == True):
                itemn.append(item[i])
                itemq.append(c[1])
                itemuq.append(c[2])
                itemwc.append(c[3])
                itemuw.append(c[4])

            i = i + 1
        plist = zip(itemn, itemq, itemuq, itemwc, itemuw)
        return plist


    def explist1(l2):
        len2= len(l2)
        i = 0
        item1 = []
        itemn1 = []
        itemq1 = []
        itemuq1 = []
        itemwc1 = []
        itemuw1 = []
        while (i < len2):
            temp1 = list(l2[i].keys())
            item1.append(temp1[0])
            c1 = l2[i].get(item1[i])
            if (c1[0] != ''):
                c2 = str(c1[0])
                itemn1.append(c2)
                itemq1.append(c1[1])
                itemuq1.append(c1[2])
                itemwc1.append(c1[3])
                itemuw1.append(c1[4])
            i = i + 1
        plist1 = zip(itemn1, itemq1, itemuq1, itemwc1, itemuw1)
        return plist1

    def qchecker(l1):
        t1 = datetime.datetime.now().date().strftime("%Y-%m-%d")
        t1 = datetime.datetime.strptime(t1, "%Y-%m-%d")
        l1=json.loads(l1)
        i=0
        item=[]
        datel1={}
        while (i < len(l1)):
            temp = list(l1[i].keys())
            item.append(temp[0])
            c = l1[i].get(item[i])
            if (c[0] == True):
                datel1[temp[0]] = c[5]
            i = i + 1
        item=[]
        for i in datel1:
            d1=datel1.get(i)
            d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            r=abs(d1-t1).days
            k=0
            while(k<len(l1)):
                t2 = datetime.datetime.now().date().strftime("%Y-%m-%d")
                temp = list(l1[k].keys())
                item.append(temp[0])
                c = l1[k].get(item[k])
                if (temp[0] == i):
                    c[1]=int(c[1])
                    c[3]= int(c[3])
                    c[1]=c[1]-(r*(c[3]/7))
                    c[5]= t2

                    a = ProductList.objects.all()
                    b = LoggedinUser.objects.all()
                    b3 = b[0].emailid
                    for j in a:
                        if (b3 == j.emailid):
                            l3 = l1
                            j.myList =  json.dumps(l1)
                            j.save()

                k=k+1
        return(l3)


    def qcheckerown(l2):
        t1 = datetime.datetime.now().date().strftime("%Y-%m-%d")
        t1 = datetime.datetime.strptime(t1, "%Y-%m-%d")
        l2=json.loads(l2)
        i=0
        item1=[]
        datel2={}
        while (i < len(l2)):
            temp1 = list(l2[i].keys())
            item1.append(temp1[0])
            c1 = l2[i].get(item1[i])
            c2 = str(c1[0])
            datel2[c2]=c1[5]
            i=i+1

        item1=[]
        for i in datel2:
            d2 = datel2.get(i)
            d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            r1 = abs(d2 - t1).days
            k = 0

            while (k < len(l2)):
                t2 = datetime.datetime.now().date().strftime("%Y-%m-%d")
                temp = list(l2[k].keys())
                item1.append(temp[0])
                c = l2[k].get(item1[k])
                if (c[0] == i):
                    c[1] = int(c[1])
                    c[3] = int(c[3])
                    c[1] = c[1] - (r1 * (c[3] / 7))
                    c[5]= t2
                    a = ProductList.objects.all()
                    b = LoggedinUser.objects.all()
                    b3 = b[0].emailid
                    for j in a:
                        if (b3 == j.emailid):
                            l4 = l2
                            j.myListOwn = json.dumps(l2)
                            j.save()

                k = k + 1
        return (l4)

    user_list=NewUser.objects.all()
    for i in user_list:
        if (i.emailid==b3):
            username=i.username
    emailid=b3
    a = ProductList.objects.all()
    for i in a:
        if i.emailid == emailid:
            l1=i.myList
            l2=i.myListOwn
            #print("here l1",l1)
            t1 = datetime.datetime.now().date().strftime("%Y-%m-%d")

            if(l1==None and l2==None):
                text = "Sorry no groceries yet!"
                return render(request, "userhome.html", {"plist":[], "text":text,
                    "username":username,"date":t1})


            elif(l2==None):
                l3=qchecker(l1)
                plist= explist(l3)
                return render(request, "userhome.html", {"plist": plist, "username": username, "date":t1})


            elif(l1==None):
                l4=qcheckerown(l2)
                plist1= explist1(l4)
                return render(request, "userhome.html", {"username": username, "plist1": plist1,"date":t1})


            else:
                l3=qchecker(l1)
                l4=qcheckerown(l2)
                plist=explist(l3)
                plist1= explist1(l4)
                return render(request, "userhome.html", {"plist": plist, "username": username,"plist1":plist1,"date":t1})


