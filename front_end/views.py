from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import dataa,User_check
import csv
from django.core.paginator import Paginator
import pandas as pd
import psycopg2
from django.db.models import Q

# df=pd.read_csv(r"C:\Users\vinod\Desktop\front_end.csv")
# print(df.shape,'vinod' )
# conn=psycopg2.connect(database='v_db',user='postgres',password='vinod',host='127.0.0.1',port='5432')
# conn.autocommit = True
# cur = conn.cursor()
# df.to_sql('after_lockdown',con=conn)



# database="v_db"
# conn=psycopg2.connect(database=database,user='postgres',password='vinod',host='127.0.0.1',port='5432')
# conn.autocommit = True
# cur=conn.cursor()
# cur.execute('select * from after_lockdown')
# res=cur.fetchall()
# print(res)
def validate(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    try:
        a=User_check.objects.get(user_name=username,password=password)
        request.session['username']= a.user_name
        if a.type=='admin':
            return redirect('verification_page')
        elif a.type=='user':
            return redirect('hm')
    except User_check.DoesNotExist:
        messages.error(request,'Not valid user')
        return redirect('log_in')

# @login_required(login_url='log_in')

def hm(request):
    id=request.session.get('username')
    # print(id)
    search=request.POST.get('search')
    typ=User_check.objects.get(user_name=id)
    if search != None:
        if typ.type == 'user':
            result = dataa.objects.filter(Q(entity__icontains=search) | Q(organisation_name__icontains=search) | Q(doctor_name__icontains=search),is_submit=False)
            pageno=request.GET.get('pageno')
            pg=Paginator(result,10)
            if pageno == None:
                pag_obj=pg.page(1)
                return render(request, "user_submit.html", {"qs":pag_obj})
        else:
            result = dataa.objects.filter(Q(entity__icontains=search) | Q(organisation_name__icontains=search) | Q(doctor_name__icontains=search), is_submit=False)
            pageno = request.GET.get('pageno')
            pg = Paginator(result, 10)
            if pageno == None:
                pag_obj = pg.page(1)
                return render(request, "admin_hm.html", {"qs": pag_obj})

    if id != None:
        # if search:
        #     l = dataa.objects.filter(Q(entity__istartswith=search) | Q(organisation_name__istartswith=search) | Q(doctor_name__istartswith=search),is_submit=False)
        # else:

        l=dataa.objects.filter(is_submit=False)
        m=request.session.get('username')
        if m:
            pageno=request.GET.get('pageno')
            print(pageno)
            pg = Paginator(l, 10)
            if pageno == None:
                page_obj=pg.page(1)
                print(page_obj)
                return render(request, "user_submit.html", {"qs": page_obj})
            else:
                page_obj=pg.page(pageno)
                return render(request, "user_submit.html", {"qs": page_obj})

            # print(pg)
            # page_number = request.GET.get('entity')
            # page_obj = pg.get_page(page_number)
            # print((page_obj))
        else:
            return redirect('log_in')
    else:
        return redirect('log_in')
    # l = []
    # with open(r"C:\Users\vinod\Desktop\front_end.csv")as f:
    #     pf=csv.DictReader(f)
    #     for dat in pf:
    #         if dat['s_no'] in [str(x[0]) for x in dataa.objects.values_list('s_no')]:
    #             pass
    #         else:
    #             l.append(dat)
    #
    # return render(request,"user_submit.html",{"qs":l})

def verification(request):
    id = request.session.get('username')
    if id:
        df=dataa.objects.filter(is_submit=True, is_verify=False)
        pageno = request.GET.get('pageno')
        print(pageno)
        pg = Paginator(df, 10)
        if pageno == None:
            page_obj = pg.page(1)
            print(page_obj)
            return render(request, "verify.html", {"qs": page_obj})
        else:
            page_obj = pg.page(pageno)
            return render(request, "verify.html", {"qs": page_obj})
        # return render(request, 'verify.html', {'qs':df})
    else:
        return redirect('log_in')

def update(request,id):
    user1=request.session.get('username')
    z = dataa.objects.get(s_no=id)
    z.is_verify = True
    z.entity = request.POST.get('entity', z.entity)
    z.total_count = request.POST.get('total_count', z.total_count)
    z.entity_sections = request.POST.get('e section', z.entity_sections)
    z.organisation_name = request.POST.get('o_name', z.organisation_name)
    z.doctor_name = request.POST.get('doctor name', z.doctor_name)
    z.recommended_coding_system = request.POST.get('recommended coding system', z.recommended_coding_system)
    z.recommended_code = request.POST.get('recommended code', z.recommended_code)
    z.recommended_token = request.POST.get('recommended token', z.recommended_token)
    z.is_recommended = request.POST.get('select recommended', z.is_recommended)
    z.correct_text = request.POST.get('correct text')
    z.code = request.POST.get('code', z.code)
    z.applicable_for_which = request.POST.get('applicable_for_which')
    z.is_submit=request.POST.get('is_submit',z.is_submit)
    z.submit_username = request.POST.get('subm',z.submit_username)
    z.verify_username = user1
    if z.is_verify and z.is_submit:
        z.flag_for_discussion = True
    z.save()
    return redirect('verification')

#     with open(r"C:\Users\vinod\Desktop\front_end.csv")as f:
#         pf=csv.DictReader(f)
#         id_no=[data for data in pf if data['s_no']==str(id) ]
#
#
#         if id_no[0]['s_no']==str(id):
#             id_no[0]['total_count']=request.POST.get('total_count',0)
#             id_no[0]['doctor_name']=request.POST.get('doctor_name',None)
#         print(id_no)
#         return render(request,'verify.html',{'dat':id_no})

def save(request,id):
    # l=[]
    # with open(r"C:\Users\vinod\Desktop\front_end.csv")as f:
    #     pf = csv.DictReader(f)
    #     for dat in pf:
    #         if str(id)==dat['s_no']:
    #             a=dataa.objects.create(s_no=id,entity=dat['entity'],total_count=dat['total_count'],entity_sections=dat['entity_sections'],organisation_name=dat['organisation_name'],
    #                                  doctor_name=dat['doctor_name'],recommended_coding_system=dat['recommended_coding_system'],recommended_code=dat['recommended_code'],
    #                                  recommended_token=dat['recommended_token'], is_recommended=request.POST.get('select recommended'),coding_system=request.POST.get('applicable for which'),
    #                                  code=request.POST.get('code'),corrected_code_corrected_token=request.POST.get('correct text'),is_submit=True,is_verify=False,flag_for_discussion=False,)
    #             a.save()
    # #
    user=request.session.get('username')
    typ = User_check.objects.get(user_name=user)

    if typ.type=='user':
        z = dataa.objects.get(s_no=id)
        z.is_submit=True
        z.entity=request.POST.get('entity',z.entity)
        z.total_count=request.POST.get('total_count',z.total_count)
        z.entity_sections=request.POST.get('e section',z.entity_sections)
        z.organisation_name=request.POST.get('o_name',z.organisation_name)
        z.doctor_name=request.POST.get('doctor name',z.doctor_name)
        z.recommended_coding_system=request.POST.get('recommended coding system',z.recommended_coding_system)
        z.recommended_code=request.POST.get('recommended code',z.recommended_code)
        z.recommended_token=request.POST.get('recommended token',z.recommended_token)
        try:
            pl = request.POST['select_recommended']
            if pl == 'false':
                z.is_recommended=False
            else:
                z.is_recommended = True
        except:
            z.is_recommended = False
        z.correct_text = request.POST.get('correct text')
        z.code=request.POST.get('code')
        z.applicable_for_which=request.POST['applicable_for_which']
        z.is_verify=False
        z.flag_for_discussion=False
        z.submit_username=user
        z.verify_username=None
        z.save()


        # qss=dataa(s_no=s_no,entity=entity,total_count=total_count,entity_sections=entity_sections,organisation_name=organisation_name,doctor_name=doctor_name,
        #      recommended_coding_system=recommended_coding_system,recommended_code=recommended_code,recommended_token=recommended_token,is_recommended=is_recommended,
        #     coding_system=coding_system,code=code,corrected_code_corrected_token=corrected_code_corrected_token,applicable_sections=applicable_sections,is_submit=is_submit,is_verify=is_verify, flag_for_discussion=flag_for_discussion)
        # print(qss)

        return redirect('hm')
    elif typ.type=='admin':
        z = dataa.objects.get(s_no=id)
        z.is_submit = True
        z.entity = request.POST.get('entity', z.entity)
        z.total_count = request.POST.get('total_count', z.total_count)
        z.entity_sections = request.POST.get('e section', z.entity_sections)
        z.organisation_name = request.POST.get('o_name', z.organisation_name)
        z.doctor_name = request.POST.get('doctor name', z.doctor_name)
        z.recommended_coding_system = request.POST.get('recommended coding system', z.recommended_coding_system)
        z.recommended_code = request.POST.get('recommended code', z.recommended_code)
        z.recommended_token = request.POST.get('recommended token', z.recommended_token)
        # z.is_recommended = request.POST.get('select recommended', True)
        try:
            pl = request.POST['select_recommended']
            if pl == 'false':
                z.is_recommended = False
            else:
                z.is_recommended = True
        except:
            z.is_recommended = False
        z.correct_text = request.POST.get('correct text')
        z.code = request.POST.get('code')
        z.applicable_for_which = request.POST.get('applicable_for_which')
        z.is_verify = False
        z.flag_for_discussion = False
        z.submit_username = user
        z.verify_username = None
        z.save()

        return redirect('admin_hm')

    else:
        return redirect('log_in')

# def download_csv():
#     response = HttpResponse(content_type="text/csv")
#     response['content-disposition'] = 'attachment;filename="output.csv"'
#     op = dataa.objects.all()
#     writer = csv.writer(response)
#     for dt in op:
#         writer.writerow([dt.s_no, dt.entity, dt.total_count, dt.entity_sections, dt.organisation_name, dt.doctor_name,
#                          dt.r_coding_system, dt.r_code,dt.r_token])
#     return response


def log_out(request):
    if request.session.get('username'):
        del request.session['username']
        print("un", request.session.get("username"))
        return redirect('log_in')
    return redirect('log_in')


def verification_page(request):
    return render(request,'verification_page.html')


def add_new_user(request):
    user_name=request.POST.get('user_name')
    password=request.POST.get('password')
    type=request.POST.get('user_type')
    User_check(user_name=user_name,password=password,type=type).save()
    return render(request,"add_new_user.html")


def admin_hm(request):
    l = dataa.objects.filter(is_submit=False)
    pageno = request.GET.get('pageno')
    print(pageno)
    pg = Paginator(l, 10)
    if pageno == None:
        page_obj = pg.page(1)
        print(page_obj)
        return render(request, "admin_hm.html", {"qs": page_obj})
    else:
        page_obj = pg.page(pageno)
        return render(request, "admin_hm.html", {"qs": page_obj})

    # return render(request,'admin_hm.html',{"qs":l})

#
# def search(request):
#     search=request.POST.get('search')
#     print(search)
#     result=dataa.objects.filter(Q(entity=search) | Q(organisation_name=search) | Q(doctor_name=search))
#
#     print(result)
#     return None
