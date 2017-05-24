# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from OA import models
# Create your views here.

def index(request):
	return render(request, 'home.html')

def generic(request):
	return render(request, 'generic.html')

def consultencyservice(request):
	return render(request, 'consultencyservice.html')

def consultencysubmitted(request):
	if request.method =='POST' and request.POST['element_4'].strip() == 'OfferComes':
		candidateName = request.POST['element_5'].strip()
		q1 = request.POST.get('element_1', None)
		q2 = request.POST.get('element_2', None)	
		q3 = request.POST.get('element_3', None)	
		q4 = request.POST.get('element_6', None)	
		q5 = request.POST.get('element_7', None)	
		

		models.consultencyService.objects.create(name = candidateName, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
		return render(request, 'resultsubmitted.html')
	else:
		pass

	return render(request, 'consultencyservice.html')

def customerservice(request):
	return render(request, 'customerservice.html')

def customersubmitted(request):
	if request.method =='POST' and request.POST['element_4'].strip() == 'OfferComes':
		candidateName = request.POST['element_5'].strip()
		q1 = request.POST.get('element_1', None)
		q2 = request.POST.get('element_2', None)	
		q3 = request.POST.get('element_3', None)	

		models.customerService.objects.create(name = candidateName, q1=q1, q2=q2, q3=q3)
		return render(request, 'resultsubmitted.html')
	else:
		pass

	return render(request, 'customerservice.html')


def resultsubmitted(request):
	return render(request, 'resultsubmitted.html')

def manageruser(request):
	if request.method =='POST':
		username = request.POST['username'].strip()
		password = request.POST['passwd'].strip()
		models.userinfo.objects.create(user = username, passwd = password)
	else:
		pass
	userinfo = models.userinfo.objects.all()
	return render(request, 'manageruser.html',{'userinfo':userinfo})

def genericsubmitted(request):
	if request.method =='POST' and request.POST['element_11'].strip() == 'OfferComes':
		candidateName = request.POST['element_12'].strip()
		q1 = request.POST.get('element_1', None)
		q2 = request.POST.get('element_2', None)	
		q3 = request.POST.get('element_3', None)	
		q4 = request.POST.get('element_4', None)	
		q5 = request.POST.get('element_5', None)	
		q6 = request.POST.get('element_6', None)	
		q7 = request.POST.get('element_7', None)	
		q8 = request.POST.get('element_8', None)	
		q9 = request.POST.get('element_9', None)
		
		c1 = request.POST.get('element_10_1',False)

		c2 = request.POST.get('element_10_2',False)
		c3 = request.POST.get('element_10_3',False)
		c4 = request.POST.get('element_10_4',False)
		c5 = request.POST.get('element_10_5',False)
		c6 = request.POST.get('element_10_6',False)
		c7 = request.POST.get('element_10_7',False)
		c8 = request.POST.get('element_10_8',False)
		c9 = request.POST.get('element_10_9',False)
		c10 = request.POST.get('element_10_10',False)
		c11 = request.POST.get('element_10_11',False)
		c12 = request.POST.get('element_10_12',False)
		c13 = request.POST.get('element_10_13',False)
		c14= request.POST.get('element_10_14',False)
		c15= request.POST.get('element_10_15',False)
		c16= request.POST.get('element_10_16',False)
		c17= request.POST.get('element_10_17',False)
		c18= request.POST.get('element_10_18',False)
		c19= request.POST.get('element_10_19',False)
		c20= request.POST.get('element_10_20',False)
		c21= request.POST.get('element_10_21',False)

		c22= request.POST.get('element_10_22',False)
		c23= request.POST.get('element_10_23',False)
		c24= request.POST.get('element_10_24',False)
		c25= request.POST.get('element_10_25',False)
		c26= request.POST.get('element_10_26',False)
		c27= request.POST.get('element_10_27',False)
		c28= request.POST.get('element_10_28',False)
		c29= request.POST.get('element_10_29',False)
		c30= request.POST.get('element_10_30',False)
		c31= request.POST.get('element_10_31',False)
	
		c32 = request.POST.get('element_10_32',False)
		c33 = request.POST.get('element_10_33',False)
		c34= request.POST.get('element_10_34',False)
		c35= request.POST.get('element_10_35',False)
		c36= request.POST.get('element_10_36',False)
		c37= request.POST.get('element_10_37',False)
		c38= request.POST.get('element_10_38',False)
		c39= request.POST.get('element_10_39',False)
		
		c40 = request.POST.get('element_10_40',False)
		c41 = request.POST.get('element_10_41',False)
		c42 = request.POST.get('element_10_42',False)
		c43 = request.POST.get('element_10_43',False)
		c44= request.POST.get('element_10_44',False)
		c45= request.POST.get('element_10_45',False)
		c46= request.POST.get('element_10_46',False)
		c47= request.POST.get('element_10_47',False)
		c48= request.POST.get('element_10_48',False)
		c49= request.POST.get('element_10_49',False)
		
		c50 = request.POST.get('element_10_50',False)
		c51 = request.POST.get('element_10_51',False)
		c52 = request.POST.get('element_10_52',False)
		c53 = request.POST.get('element_10_53',False)
		c54= request.POST.get('element_10_54',False)
		c55= request.POST.get('element_10_55',False)
		c56= request.POST.get('element_10_56',False)
		c57= request.POST.get('element_10_57',False)
		c58= request.POST.get('element_10_58',False)
		c59= request.POST.get('element_10_59',False)

		c60 = request.POST.get('element_10_60',False)
		c61 = request.POST.get('element_10_61',False)
		c62 = request.POST.get('element_10_62',False)
		c63 = request.POST.get('element_10_63',False)
		c64= request.POST.get('element_10_64',False)
		c65= request.POST.get('element_10_65',False)
		c66= request.POST.get('element_10_66',False)
		c67= request.POST.get('element_10_67',False)
		c68= request.POST.get('element_10_68',False)
		c69= request.POST.get('element_10_69',False)

		c70 = request.POST.get('element_10_70',False)
		c71 = request.POST.get('element_10_71',False)
		c72 = request.POST.get('element_10_72',False)
		c73 = request.POST.get('element_10_73',False)
		c74= request.POST.get('element_10_74',False)
		c75= request.POST.get('element_10_75',False)
		c76= request.POST.get('element_10_76',False)
		c77= request.POST.get('element_10_77',False)
		c78= request.POST.get('element_10_78',False)
		c79= request.POST.get('element_10_79',False)

		c80 = request.POST.get('element_10_80',False)
		c81 = request.POST.get('element_10_81',False)
		c82 = request.POST.get('element_10_82',False)
		c83 = request.POST.get('element_10_83',False)
		c84= request.POST.get('element_10_84',False)
		c85= request.POST.get('element_10_85',False)
		c86= request.POST.get('element_10_86',False)
		c87= request.POST.get('element_10_87',False)
		c88= request.POST.get('element_10_88',False)
		c89= request.POST.get('element_10_89',False)


		c90 = request.POST.get('element_10_90',False)
		c91 = request.POST.get('element_10_91',False)
		c92 = request.POST.get('element_10_92',False)
		c93 = request.POST.get('element_10_93',False)
		c94= request.POST.get('element_10_94',False)
		c95= request.POST.get('element_10_95',False)
		c96= request.POST.get('element_10_96',False)
		c97= request.POST.get('element_10_97',False)
		c98= request.POST.get('element_10_98',False)
		c99= request.POST.get('element_10_99',False)

		c100 = request.POST.get('element_10_100',False)
		c101 = request.POST.get('element_10_101',False)
		c102 = request.POST.get('element_10_102',False)
		c103 = request.POST.get('element_10_103',False)
		c104= request.POST.get('element_10_104',False)
		c105= request.POST.get('element_10_105',False)
		c106= request.POST.get('element_10_106',False)
		c107= request.POST.get('element_10_107',False)
		c108= request.POST.get('element_10_108',False)
		c109= request.POST.get('element_10_109',False)
		
		c110 = request.POST.get('element_10_110',False)
		c111 = request.POST.get('element_10_111',False)
		c112 = request.POST.get('element_10_112',False)
		c113 = request.POST.get('element_10_113',False)
		c114= request.POST.get('element_10_114',False)
		c115= request.POST.get('element_10_115',False)
		c116= request.POST.get('element_10_116',False)
		c117= request.POST.get('element_10_117',False)
		c118= request.POST.get('element_10_118',False)
		c119= request.POST.get('element_10_119',False)


		models.generic.objects.create(name = candidateName, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,c15=c15,c16=c16,c17=c17,c18=c18,c19=c19,c20=c20,c21=c21,c22=c22,c23=c23,c24=c24,c25=c25,c26=c26,c27=c27,c28=c28,c29=c29,c30=c30,c31=c31,c32=c32,c33=c33,c34=c34,c35=c35,c36=c36,c37=c37,c38=c38,c39=c39,c40=c40,c41=c41,c42=c42,c43=c43,c44=c44,c45=c45,c46=c46,c47=c47,c48=c48,c49=c49,c50=c50,c51=c51,c52=c52,c53=c53,c54=c54,c55=c55,c56=c56,c57=c57,c58=c58,c59=c59,c60=c60,c61=c61,c62=c62,c63=c63,c64=c64,c65=c65,c66=c66,c67=c67,c68=c68,c69=c69,c70=c70,c71=c71,c72=c72,c73=c73,c74=c74,c75=c75,c76=c76,c77=c77,c78=c78,c79=c79,c80=c80,c81=c81,c82=c82,c83=c83,c84=c84,c85=c85,c86=c86,c87=c87,c88=c88,c89=c89,c90=c90,c91=c91,c92=c92,c93=c93,c94=c94,c95=c95,c96=c96,c97=c97,c98=c98,c99=c99,c100=c100,c101=c101,c102=c102,c103=c103,c104=c104,c105=c105,c106=c106,c107=c107,c108=c108,c109=c109,c110=c110,c111=c111,c112=c112,c113=c113,c114=c114,c115=c115,c116=c116,c117=c117,c118=c118,c119=c119)
		return render(request, 'resultsubmitted.html')
	else:
		pass

	return render(request, 'generic.html')
