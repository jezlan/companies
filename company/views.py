from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import login,companydb,appilcantdb,qualification,experience,vaccancy,application,interview
from datetime import date
from datetime import timedelta
import _datetime

# Create your views here.
def home(request):
    auth.logout(request)
    return render(request,'index.html')
def logins(request):
    auth.logout(request)
    return render(request,'login.html')
def usrlogins(request):
    auth.logout(request)
    return render(request,'userlogin.html')
def cmplogins(request):
    auth.logout(request)
    return render(request,'companylogin.html')
def inithmecmp(request):
    return render(request,'initialhmecmp.html')
def inithmeappl(request):
    return render(request,'initialhmeappl.html')
@login_required(login_url='/')
def regsitercmp(request):
    return render(request,'cmpnregistration.html')
@login_required(login_url='/')
def regsiterappl(request):
    return render(request,'aplcntregister.html')
@login_required(login_url='/')
def cmpregister(request):
    name= request.POST['name']
    email=request.POST['email']
    desc=request.POST['desc']
    phno=request.POST['phno']
    address=request.POST['addrs']
    uname=request.POST['usname']
    pwd=request.POST['pswd']
    obb = login()
    obb.username = uname
    obb.password = pwd
    obb.type = 'company'
    obb.save()
    ob=companydb()
    ob.lid=obb
    ob.name=name
    ob.email=email
    ob.description=desc
    ob.phno=phno
    ob.address=address
    ob.save()
    return redirect('cmplogins')
@login_required(login_url='/')
def applregister(request):
    name= request.POST['name']
    email=request.POST['email']
    gender=request.POST['gender']
    phno=request.POST['phno']
    address=request.POST['addrs']
    uname=request.POST['usname']
    pwd=request.POST['pswd']
    obb = login()
    obb.username = uname
    obb.password = pwd
    obb.type = 'applicant'
    obb.save()
    ob=appilcantdb()
    ob.lid=obb
    ob.name=name
    ob.email=email
    ob.gender=gender
    ob.phno=phno
    ob.address=address
    ob.save()
    return redirect('usrlogins')
def loginfunc(request):
    uname = request.POST['usname']
    pswd = request.POST['pswd']
    try:
        ob = login.objects.get(username=uname, password=pswd)
        usr=auth.authenticate(username='admin', password='admin')
        auth.login(request,usr)
        request.session['rid'] = ob.id
        if ob.type == 'admin':
            print(uname, pswd)
            return redirect('/ahome')
        elif ob.type == 'company':
            cb=companydb.objects.get(lid=ob)
            print(uname, pswd)
            return redirect('/cmphome')
        else:
            ab = appilcantdb.objects.get(lid=ob)
            print(uname, pswd)
            return redirect('/candhome')

            # obb = login.objects.get(id=request.session['rid'])
            # print(obb)
            # oba = appilcantdb.objects.get(lid_id=obb)
            # print(oba)
            # apb = qualification.objects.filter(aid=ab)
            # print(apb)
            # vid = []
            # for r in apb:
            #     vid.append(r.aid.id)
            # print(vid)
            # return render(request, 'applcanthome.html',{'data':ab,'vid':vid})
    except Exception as e:
        print(e)
        return HttpResponse("<script>alert('Invalid Username or Password');window.location='/'</script>")
@login_required(login_url='/')
def ahome(request):
    return render(request,'adminhome.html')
@login_required(login_url='/')
def cmphome(request):
    ob = login.objects.get(id=request.session['rid'])
    cb = companydb.objects.get(lid=ob)
    return render(request, 'companyhome.html',{'data':cb})
@login_required(login_url='/')
def candhome(request):
    ob = login.objects.get(id=request.session['rid'])
    ab = appilcantdb.objects.get(lid=ob)
    apb = qualification.objects.filter(aid=ab)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request, 'applcanthome.html', {'data': ab, 'vid': vid})
@login_required(login_url='/')
def likeEmail(request):
    email = request.GET['post_id']
    print(email)
    data = {
        'is_taken': companydb.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this Email Id already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)
@login_required(login_url='/')
def likeEmailappl(request):
    email = request.GET['post_id']
    print(email)
    data = {
        'is_taken': appilcantdb.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this Email Id already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)
@login_required(login_url='/')
def likePhone(request):
    phnum = request.GET['post_id']
    print(phnum)
    data = {
        'is_taken': companydb.objects.filter(phno__iexact=phnum).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this Phone number already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)
@login_required(login_url='/')
def likePhoneappl(request):
    phnum = request.GET['post_id']
    print(phnum)
    data = {
        'is_taken': appilcantdb.objects.filter(phno__iexact=phnum).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this Phone number already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)
@login_required(login_url='/')
def pwdck(request):
    passwd=request.GET['pswd']
    if len(passwd)==0:
        return HttpResponse("")
    elif len(passwd)<5:
        return HttpResponse("Week password")
    elif len(passwd)<9:
        return HttpResponse("mediam password")
    else:
        return HttpResponse("strong password")
@login_required(login_url='/')
def confpswd(request):
    password =request.GET['pswd']
    confpswd=request.GET['cnfpwd']
    if(password==confpswd):
        return HttpResponse("")
    else:
        return HttpResponse("Password doesn't match")
@login_required(login_url='/')
def likePost(request):
    username = request.GET['post_id']
    print(username)
    data = {
        'is_taken': login.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this username already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)
@login_required(login_url='/')
def applicathome(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba=appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'applcanthome.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def companyhome(request):
    return render(request,'companyhome.html')
@login_required(login_url='/')
def adminhome(request):
    return render(request,'adminhome.html')
@login_required(login_url='/')
def exptoapplicanthome(request):
    return HttpResponse("<script>alert('Qualification added successfully ;<br> Experience Nill');window.location='viewmydetail'</script>")
@login_required(login_url='/')
def qualfaddpg(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba = appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'qualification.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def qualfplusaddpg(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba = appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'qualificationplstwo.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def qualfdegaddpg(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba = appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'qualifiacationdegengdipl.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def qualfpgaddpg(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba = appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'qualificationpg.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def yesorno(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba = appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'yesorno.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def exprnaddpg(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    oba = appilcantdb.objects.get(lid_id=obb)
    print(oba)
    apb = qualification.objects.filter(aid=oba)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)
    return render(request,'Experiance.html',{'data':oba,'vid':vid})
@login_required(login_url='/')
def qualftenadding(request):
    department=request.POST['qualify']
    clas=request.POST['cls']
    yearofpas=request.POST['year']
    institution=request.POST['inst']
    perofmark=request.POST['permark']
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)

    ob=qualification()
    ob.Department=department
    ob.yopass=yearofpas
    ob.institution=institution
    ob.perofmark=perofmark
    ob.clas=clas
    ob.aid=obc
    ob.save()
    return redirect('qualfplusaddpg')
@login_required(login_url='/')
def qualfplusadding(request):
    department=request.POST['qualify']
    clas=request.POST['cls']
    yearofpas=request.POST['year']
    institution=request.POST['inst']
    perofmark=request.POST['permark']
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)

    ob=qualification()
    ob.Department=department
    ob.yopass=yearofpas
    ob.institution=institution
    ob.perofmark=perofmark
    ob.clas=clas
    ob.aid=obc
    ob.save()
    return redirect('qualfdegaddpg')
@login_required(login_url='/')
def qualfadding(request):
    button = request.POST['button']
    if button == "Add":
        department=request.POST['qualify']
        clas=request.POST['cls']
        yearofpas=request.POST['year']
        institution=request.POST['inst']
        perofmark=request.POST['permark']
        obb = login.objects.get(id=request.session['rid'])
        obc = appilcantdb.objects.get(lid_id=obb)

        ob=qualification()
        ob.Department=department
        ob.yopass=yearofpas
        ob.institution=institution
        ob.perofmark=perofmark
        ob.clas=clas
        ob.aid=obc
        ob.save()
        return HttpResponse(
            "<script>alert('If you have Post Graduation Degree . pls click Next--> or click Finish');window.location='qualfdegaddpg'</script>")
    elif button == "Next-->":
        return redirect('qualfpgaddpg')
    else:
        return HttpResponse(
            "<script>alert('Qualifications Added Successfully...');window.location='yesorno'</script>")

@login_required(login_url='/')
def qualpgadding(request):
    department=request.POST['qualify']
    clas=request.POST['cls']
    yearofpas=request.POST['year']
    institution=request.POST['inst']
    perofmark=request.POST['permark']
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)

    ob=qualification()
    ob.Department=department
    ob.yopass=yearofpas
    ob.institution=institution
    ob.perofmark=perofmark
    ob.clas=clas
    ob.aid=obc
    ob.save()
    return redirect('yesorno')

@login_required(login_url='/')
def exprnadding(request):
    button=request.POST['button']
    if button=="Add":
        companyname=request.POST['cmpnme']
        strtdte=request.POST['strtdate']
        enddte=request.POST['enddate']
        obb = login.objects.get(id=request.session['rid'])
        obc = appilcantdb.objects.get(lid_id=obb)


        ob=experience()
        ob.companynme=companyname
        ob.strtdate=strtdte
        ob.enddate=enddte
        ob.aid=obc
        ob.save()
        return HttpResponse(
            "<script>alert('Experiance added successfully :- if you have more experience ,pls add it or click finish to complete it ......!');window.location='exprnaddpg'</script>")
    else:
        return HttpResponse(
            "<script>alert('Experiances added successfully...! ');window.location='viewmydetail'</script>")

@login_required(login_url='/')
def viewcmpanies(request):
    plist = companydb.objects.all()
    return render(request, 'viewcompanies.html', {'data': plist})
@login_required(login_url='/')
def viewcandidates(request):

    plist = appilcantdb.objects.all()
    return render(request, 'viewcandidates.html', {'data': plist})
@login_required(login_url='/')
def viewexpcand(request,id):
    obb=appilcantdb.objects.get(lid_id=id)
    ob =experience.objects.filter(aid_id=obb)

    print(ob)
    return render(request,'viewxpcand.html',{'data':ob})
@login_required(login_url='/')
def viewqualycand(request,id):
    obb = appilcantdb.objects.get(lid_id=id)
    ob =qualification.objects.filter(aid_id=obb)

    print(ob)
    return render(request,'viewqualycand.html',{'data':ob,'n':obb})
@login_required(login_url='/')
def vacancyaddpg(request):
    return render(request,'vaccancyadd.html')
@login_required(login_url='/')
def vaccancyadd(request):
    vacncy =request.POST['noofvac']
    jobdet=request.POST['jbdet']
    qualy=request.POST['qlfreq']
    salary=request.POST['slary']
    exprnce = request.POST['exp']
    status=request.POST['sts']
    today= date.today()
    obb = login.objects.get(id=request.session['rid'])
    obc=companydb.objects.get(lid_id=obb)

    ob = vaccancy()
    ob.noofvaccany=vacncy
    ob.jobdetail=jobdet
    ob.qualification=qualy
    ob.salary=salary
    ob.Experiance=exprnce
    ob.status=status
    ob.date=today
    ob.cmp_id=obc
    ob.save()

    return redirect('viewvacanciescmp')
@login_required(login_url='/')
def viewvacancy(request):
    obb = login.objects.get(id=request.session['rid'])
    oba = appilcantdb.objects.get(lid_id=obb)
    apb=application.objects.filter(aid=oba)
    lvid=[]
    for r in apb :
        lvid.append(r.vid.id)
    ob=vaccancy.objects.order_by('-noofvaccany')
    qpb = qualification.objects.filter(aid=oba)
    vid = []
    for r in qpb:
        vid.append(r.aid.id)
    print(vid)
    return  render(request,'viewvaccancy.html',{'datass':ob,'lvid':lvid,'data':oba,'vid':vid})
@login_required(login_url='/')
def apply(request,id):
    obb = login.objects.get(id=request.session['rid'])
    oba = appilcantdb.objects.get(lid_id=obb)
    obc=vaccancy.objects.get(id=id)
    if obc.status=='needed':
        today = date.today()
        status="pending"

        ob=application()
        ob.date=today
        ob.aid=oba
        ob.vid=obc
        ob.status=status
        ob.save()

        return HttpResponse(
            "<script>alert('Your application was added successfully..!  pls wait for the response from the company....  ');window.location='/applicathome'</script>")
    else:
        return HttpResponse(
            "<script>alert('Sorry ..! No vacancies left ');window.location='/viewvacancy'</script>")
@login_required(login_url='/')
def viewvacanciesadm(request):
    ob=vaccancy.objects.all()
    return render(request,'vacancyviewadm.html',{'data':ob})
@login_required(login_url='/')
def viewvacanciescmp(request):
    obb = login.objects.get(id=request.session['rid'])
    obc = companydb.objects.get(lid_id=obb)
    db=vaccancy.objects.filter(cmp_id=obc)
    return render(request,'vacancyviewcmp.html',{'data':db})
@login_required(login_url='/')
def applicationview(request):
    obb = login.objects.get(id=request.session['rid'])
    print(obb)
    obc = companydb.objects.get(lid_id=obb)
    print(obc)
    # db=vaccancy.objects.get(cmp_id=obc)
    # print(db)
    ob=application.objects.filter(vid__cmp_id=obc)
    print(ob)
    vob=vaccancy.objects.filter(cmp_id=obc)

    print(ob)
    return render(request,'applicationsview.html',{'data':ob,'vob':vob})
# def viewexpcmp(request,id):
#     ob =experience.objects.filter(aid_id=id)
#     print(ob)
#     return render(request,'viewxpcand.html',{'data':ob})
@login_required(login_url='/')
def viewqualycmp(request,id):
    vap = application.objects.get(id=id)
    print(vap)
    ob =qualification.objects.filter(aid_id=vap.aid)
    print(ob)
    expob = experience.objects.filter(aid_id=vap.aid)
    print(expob)
    obb=appilcantdb.objects.get(id=vap.aid_id)
    print(obb)
    # vap=application.objects.get(aid=obb)
    request.session['aplid'] = id
    print(ob)
    return render(request,'viewfulldetailcmp.html',{'data':ob,'n':obb,'exp':expob,'apl':vap})
@login_required(login_url='/')
def deleteusr(request,id):
    ob = login.objects.get(id=id)
    ob.delete()
    return redirect('viewcandidates')
@login_required(login_url='/')
def deletecompany(request,id):
    ob = login.objects.get(id=id)
    ob.delete()
    return redirect('viewcmpanies')
@login_required(login_url='/')
def deletevacancy(request,id):
    ob = vaccancy.objects.get(id=id)
    ob.delete()
    return redirect('viewvacanciesadm')
@login_required(login_url='/')
def updatevacancy(request, id):
    ob = vaccancy.objects.get(id=id)
    return render(request, 'vacancyupdate.html', {'data': ob})
@login_required(login_url='/')
def vacancypdate(request):
    id = request.POST['id']
    vacncy = request.POST['noofvac']
    jobdet = request.POST['jbdet']
    qualy = request.POST['qlfreq']
    salary = request.POST['slary']
    exprnce = request.POST['exp']
    status = request.POST['sts']
    today = date.today()
    obb = login.objects.get(id=request.session['rid'])
    obc = companydb.objects.get(lid_id=obb)

    ob = vaccancy.objects.get(id=id)
    ob.noofvaccany = vacncy
    ob.jobdetail = jobdet
    ob.qualification = qualy
    ob.salary = salary
    ob.Experiance = exprnce
    ob.status = status
    ob.date = today
    ob.cmp_id = obc
    ob.save()

    return redirect('viewvacanciescmp')
@login_required(login_url='/')
def myapplicationview(request):
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)
    # db=vaccancy.objects.get(cmp_id=obc)
    ob=application.objects.filter(aid=obc)

    print(obb)

    print(obc)
    apb = qualification.objects.filter(aid=obc)
    print(apb)
    vid = []
    for r in apb:
        vid.append(r.aid.id)
    print(vid)

    print(ob)
    return render(request,'myapplications.html',{'data':obc,'datass':ob,'vid':vid})
@login_required(login_url='/')
def accept(request):
    ob=application.objects.get(id=request.session['aplid'])
    request.session['aplintid'] = ob.id
    print(ob)
    ob.status="Accepted"
    ob.save()
    return redirect('interviewaddpg')
@login_required(login_url='/')
def reject(request):
    ob = application.objects.get(ad=request.session['aplid'])
    ob.status = "Rejected"
    ob.save()
    return redirect('applicationview')
@login_required(login_url='/')
def interviewaddpg(request):
    return render(request,'interviewadding.html')
@login_required(login_url='/')
def interviewadding(request):
    place=request.POST['place']
    date=request.POST['date']
    time=request.POST['time']
    obb = application.objects.get(id=request.session['aplintid'])

    ob=interview()
    ob.place=place
    ob.date=date
    ob.time=time
    ob.apid=obb
    ob.save()
    return redirect('applicationview')
@login_required(login_url='/')
def viewinterviewdet(request, id):
    ob = interview.objects.get(apid_id=id)
    return render(request, 'viewinterview.html', {'data': ob})
@login_required(login_url='/')
def cancel(request,id):
    ob=application.objects.get(vid=id)
    ob.delete()
    return redirect('myapplicationview')
@login_required(login_url='/')
def appliedcandadm(request,id):
    ob=application.objects.filter(vid=id)
    return render(request,'applied candidates.html',{'data':ob})
@login_required(login_url='/')
def viewinterviewdetad(request,id):
    ob = interview.objects.get(apid_id=id)
    return render(request, 'viewinterviewadmn.html', {'data': ob})
@login_required(login_url='/')
def viewmydetail(request):
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)
    ob =qualification.objects.filter(aid_id=obc)
    print(ob)
    expob = experience.objects.filter(aid_id=obc)
    print(expob)

    print(obb)
    # vap=application.objects.get(aid=obb)
    return render(request,'viewmydetails.html',{'data':ob,'n':obc,'exp':expob})
@login_required(login_url='/')
def qualyupdatepg(request,id):
    ob = qualification.objects.get(id=id)
    if ob.clas=='10th':
        return render(request, 'qualifupdate10th.html', {'data': ob})
    elif ob.clas=='12th':
        return render(request, 'qualifupdate12th.html', {'data': ob})
    elif ob.clas=='Degree/Engineering/Diploma':
        return render(request, 'qualifupdatedegr.html', {'data': ob})
    else:
        return render(request, 'qualifupdatepg.html', {'data': ob})
@login_required(login_url='/')
def qualfupdating(request):
    id=request.POST['id']
    department=request.POST['qualify']
    clas=request.POST['cls']
    yearofpas=request.POST['year']
    institution=request.POST['inst']
    perofmark=request.POST['permark']
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)

    ob=qualification.objects.get(id=id)
    ob.Department=department
    ob.yopass=yearofpas
    ob.institution=institution
    ob.perofmark=perofmark
    ob.clas=clas
    ob.aid=obc
    ob.save()
    return redirect('viewmydetail')
@login_required(login_url='/')
def expupdatepg(request,id):
    ob=experience.objects.get(id=id)
    return render(request, 'experianceupdate.html', {'data': ob})
@login_required(login_url='/')
def exprupdating(request):
    id=request.POST['id']
    companyname=request.POST['cmpnme']
    strtdte=request.POST['strtdate']
    enddte=request.POST['enddate']
    obb = login.objects.get(id=request.session['rid'])
    obc = appilcantdb.objects.get(lid_id=obb)


    ob=experience.objects.get(id=id)
    ob.companynme=companyname
    ob.strtdate=strtdte
    ob.enddate=enddte
    ob.aid=obc
    ob.save()
    return redirect('viewmydetail')
@login_required(login_url='/')
def userupdatepg(request,id):
    obb = login.objects.get(id=request.session['rid'])
    ob=appilcantdb.objects.get(id=id)
    return render(request, 'usrupdate.html', {'data': ob,'lob':obb})
@login_required(login_url='/')
def usrupdating(request):
    id=request.POST['id']
    lid=login.objects.get(id=request.session['rid'])
    name= request.POST['name']
    email=request.POST['email']
    gender=request.POST['gender']
    phno=request.POST['phno']
    address=request.POST['addrs']
    uname=request.POST['usname']
    pwd=request.POST['pswd']
    obb = login.objects.get(id=lid.id)
    obb.username = uname
    obb.password = pwd
    obb.type = 'applicant'
    obb.save()
    ob=appilcantdb.objects.get(id=id)
    ob.lid=obb
    ob.name=name
    ob.email=email
    ob.gender=gender
    ob.phno=phno
    ob.address=address
    ob.save()
    return redirect('viewmydetail')

@login_required(login_url='/')
def search(request):
    sd=request.GET['searchdata']
    print(sd)
    obb = login.objects.get(id=request.session['rid'])
    oba = appilcantdb.objects.get(lid_id=obb)
    ob=vaccancy.objects.filter(jobdetail__istartswith=sd).order_by('-noofvaccany')
    apb = application.objects.filter(aid=oba)
    lvid = []
    for i in apb:
        lvid.append(i.vid.id)
    data=[]
    for r in ob:
        v=1
        if r.id in lvid:
            v=2
        row={"apid":v,"id":r.id,"noofvaccany":r.noofvaccany,"jobdetail":r.jobdetail,"date":r.date,"qualification":r.qualification,"salary":r.salary,"Experiance":r.Experiance,"status":r.status,"cmpidname":r.cmp_id.name }
        data.append(row)

    res={"res":data}
    print(data)
    return JsonResponse(res)
@login_required(login_url='/')
def searchapplication(request):
    sd = request.GET['searchdata']
    ob=application.objects.filter(vid__jobdetail=sd)
    data = []
    for r in ob:
        row={"name":r.aid.name,"jobdetail":r.vid.jobdetail,"status":r.status,"date":r.date,"id":r.id}
        data.append(row)
    res = {"res": data}
    print(data)

    return JsonResponse(res)









