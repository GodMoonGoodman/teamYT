from django.shortcuts import render, redirect
from yonto.models import *
from yonto.crawl import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import datetime
from django.contrib.auth.views import logout


# Create your views here.

#--- ListView

def CouseLV(request):
	courses = Course.objects.all()
	return render(request,'yonto/course_list.html',{'courses':courses})

def Main(request):
	base='http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop_mileage_result01.jsp?'#yshs_domain=%s&yshs_hyhg=%d&yshs_hakno=%s&yshs_bb=%s&yshs_sbb=%s'%('H1',20171,hak[0], hak[1], hak[2]))
	ret=bool()
	# print(request.method)
	if request.method == "POST":

		post = dict(request.POST.lists())
		# print(post)

		keyword = post['hakno'][0]
		# print(hak)

		if '-' in keyword:
			hak = keyword.split('-')
			CLASSMODEL = Course.objects.filter(hakno=hak[0], bb=hak[1], sbb=hak[2]).count()
			if CLASSMODEL == 0:
				print("수업이 없음")
				ret = getMile(20172, hak[0], hak[1], hak[2])
				if ret == False:
					return render(request,'yonto/info.html', {'keyword': keyword ,'len':len(keyword), 'noyscec':ret})

			else:
				print("수업이 있음!!")

			CLASSMODEL = Course.objects.filter(hakno=hak[0], bb=hak[1], sbb=hak[2])
			return render(request,'yonto/search.html', {'keyword': keyword, 'count':CLASSMODEL.count(),'course':CLASSMODEL,'base':base})
		elif len(keyword) == 0:
			return render(request,'yonto/info.html', {'keyword': keyword ,'len':len(keyword), 'noyscec':ret})


		else:
			print(keyword)
			print("과목명으로 검색")
			CLASSMODEL_count = Course.objects.filter(title=keyword).count()

			if CLASSMODEL_count == 0:
				print("수업이 없음")
				return render(request,'yonto/info.html', {'keyword': keyword ,'len':len(keyword), 'noyscec':ret})
			else:
				print("수업이 있음")
				CLASSMODEL = Course.objects.filter(title=keyword)
				
				return render(request,'yonto/search.html', {'keyword': keyword, 'count':CLASSMODEL_count,'course':CLASSMODEL,'base':base})
	else:
		return render(request,'yonto/main.html')

def Search(request):
	return render(request,'yonto/search.html')


def Register(request):
	if request.method == "POST":
		username = request.POST['username']
		email	 = request.POST['email']
		password = request.POST['password']
		print(username, email, password)
		USERMODEL = User.objects.create_user(username=username, email=email, password=password, is_active=False, last_login=datetime.date.today())
		print(USERMODEL)
		print("성공?")
		return redirect('/')

	else:
	# form = LoginForm()
		return render(request,'yonto/register.html')

def Login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		print(username, password)
		user = authenticate(username = username, password = password)
		print(user)
	
		if user is not None:
			login(request, user)
			print(user,"로그인 성공")
			return redirect('/')
		else:
			print("로그인 실패")
			return render(request,'yonto/login.html')
	else:
	# form = LoginForm()
		return render(request,'yonto/login.html')


def Logout(request):
	logout(request)
	return render(request,'yonto/logout.html')

def Whatis(request):
	return render(request,'yonto/whatis.html')

def My(request):
	return render(request,'yonto/my.html')