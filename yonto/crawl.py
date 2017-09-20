from yonto.models import *
# coding: utf-8
import requests as req
import bs4
import sqlite3

def getMile(hakgi, hakno, bb, sbb):

	sess= req.Session()

	yshs_hyhg = hakgi

	yshs_hakno = hakno

	yshs_bb = bb

	yshs_sbb = sbb

	response= sess.post(url="http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop_mileage_result01.jsp",
	                    data={"yshs_domain":"H1", "yshs_hyhg":yshs_hyhg, "yshs_hakno":yshs_hakno, "yshs_bb":yshs_bb, "yshs_sbb":yshs_sbb})

	url = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop_mileage_result01.jsp?yshs_domain=%s&yshs_hyhg=%d&yshs_hakno=%s&yshs_bb=%s&yshs_sbb=%s'%('H1',2017,yshs_hakno,yshs_bb,yshs_sbb)
	# with open('output.html','w') as w:
	#     w.write(response.text)

	text = bs4.BeautifulSoup(response.text, 'html.parser')
	try:
		tables = text.find_all('table')

		hakgi = yshs_hyhg

		basis = tables[1]

		basis_1 = basis.find_all('tr')[2].find('tr')

		class_data=basis_1.find_all('td')

		c_s_l = class_data[0].text

		# c_s_l

		tit = class_data[1].text

		cre = class_data[2].text

		prof = class_data[3].text

		room = class_data[5].text

		qu = class_data[6].text

		part = class_data[7].text

		mi = class_data[15].text

		ma =  class_data[16].text

		av =  class_data[17].text

		# part = c_s_l.split('-')

		title = part[0]

		basis2 = tables[2]

		basis2_1 = basis.find_all('tr')[2].find('tr')

		arr = basis2.find_all('tr')

		arr2 = arr[1].find_all('tr')

		def yn(yn):
		    if 'Y' in yn or 'O' in yn:
		        return 1
		    else:
		        return 0

		Course_model = Course.objects.create(hakgi=int(hakgi), hakno=str(yshs_hakno), bb=str(yshs_bb), sbb=str(yshs_sbb), title=str(tit), room=str(room), max_student=int(qu), participation=int(part), min_mile=int(mi), max_mile=int(ma), avr_mile=float(av), credit=int(cre), professor = str(prof), analysis=False)

		Course_model.save()


		for row in arr2:
			MileResult_model = MileResult.objects.create(rank=int(ra), mileage=int(mile), isMajor=yn(isMajor), numEnroll=yn(enrol), graduation=yn(gra), first=yn(fir), credit=float(cre), pre=float(prev), grade=int(gr), result=yn(res), course=int(Course_model.pk))
			MileResult_model.save()

		return url
	except:
		return False
	# try:
	#     exit()
	#     conn = sqlite3.connect('db.sqlite')
	#     cur = conn.cursor()
	    
	#     sql = "INSERT INTO Class(year_hakgi, code_sec_lab, title, quota, participants, minimum, maximum, average) VALUES (%d, '%s', '%s', %d, %d, %d, %d, %f)" % (int(hakgi), str(c_s_l), str(tit), int(qu), int(part), int(mi), int(ma), float(av)) 
	    
	#     cur.execute(sql)
	    
	#     lowid = cur.lastrowid
	    
	#     conn.commit()
	# except:
	#     print("err")
	#     exit()
	    


	# In[21]:


	# conn.close()


	# In[22]:


	# for row in arr2:
	#     ra = row.find_all('td')[0].text
	#     mile = row.find_all('td')[1].text
	#     ism = row.find_all('td')[2].text
	#     enrol = row.find_all('td')[3].text
	#     gra = row.find_all('td')[4].text
	#     fir = row.find_all('td')[5].text
	#     cre = row.find_all('td')[6].text
	#     prev = row.find_all('td')[7].text
	#     gr = row.find_all('td')[8].text
	#     res = row.find_all('td')[9].text
	#     sql = "INSERT INTO MileageResult(class_id, rank, mileage, major, enrolled, graduation, first, credit, previous, grade, result) VALUES (%d, %d, %d, %d, %d, %d, %d, %f, %f, %d, %d)"% (int(lowid), int(ra), int(mile), yn(ism), int(enrol), yn(gra), yn(fir), float(cre), float(prev), int(gr), yn(res))
	    
	#     cur.execute(sql)
	# conn.commit()


	# In[23]:


	# conn.close()

