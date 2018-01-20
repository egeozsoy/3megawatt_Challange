from django.shortcuts import render
from sitesScreen.models import Stuff
from django.db.models import Sum, Avg
# Create your views here.

def index(request):
	return render(request , 'sitesScreen/header.html')

def site(request):
	objects = Stuff.objects.all()
	objectsArray = []

	requestUrl = request.get_full_path()
	numberOfSite = requestUrl[-1]
	#filter can be used as an alternative
	for o in objects:
		if (numberOfSite == '1' and o.Site_Name == "Demo Site") or (numberOfSite == '2' and o.Site_Name == "ABC Site") or (numberOfSite == '3' and  o.Site_Name == "XYZ Site"):
			objectsArray.append(o)
	if numberOfSite == '1':
		headerName = 'Site Details - Demo Site'
	elif numberOfSite == '2':
		headerName = 'Site Details - ABC Site'
	else:
		headerName = 'Site Details - XYZ Site'

	myDatas = {'myDatas' : objectsArray , 'headerName' : headerName}
	myHtmlURL = 'sitesScreen/site.html'
	return render(request , myHtmlURL , myDatas) 

#by default, django aggregates are used(I asume Sql Queries are faster then python)
def summary(request):
	demo_site_objects = Stuff.objects.all().filter(Site_Name= 'Demo Site')
	abc_site_objects = Stuff.objects.all().filter(Site_Name='ABC Site')
	xyz_site_objects = Stuff.objects.all().filter(Site_Name='XYZ Site')

	demo_a_sum = float(demo_site_objects.aggregate(Sum('A_Value'))['A_Value__sum'])
	demo_b_sum = float(demo_site_objects.aggregate(Sum('B_Value'))['B_Value__sum'])
	abc_a_sum = float(abc_site_objects.aggregate(Sum('A_Value'))['A_Value__sum'])
	abc_b_sum = float(abc_site_objects.aggregate(Sum('B_Value'))['B_Value__sum'])
	xyz_a_sum = float(xyz_site_objects.aggregate(Sum('A_Value'))['A_Value__sum'])
	xyz_b_sum = float(xyz_site_objects.aggregate(Sum('B_Value'))['B_Value__sum'])
	myDatas = {'myDatas': [["Demo Site", (demo_a_sum, demo_b_sum)], ["ABC Site", (abc_a_sum, abc_b_sum)],
					["XYZ Site", (xyz_a_sum, xyz_b_sum)]]}
	return render(request, 'sitesScreen/summary.html', myDatas)

def average(request):
	demo_site_objects = Stuff.objects.all().filter(Site_Name= 'Demo Site')
	abc_site_objects = Stuff.objects.all().filter(Site_Name='ABC Site')
	xyz_site_objects = Stuff.objects.all().filter(Site_Name='XYZ Site')

	demo_a_sum = float(demo_site_objects.aggregate(Avg('A_Value'))['A_Value__avg'])
	demo_b_sum = float(demo_site_objects.aggregate(Avg('B_Value'))['B_Value__avg'])
	abc_a_sum = float(abc_site_objects.aggregate(Avg('A_Value'))['A_Value__avg'])
	abc_b_sum = float(abc_site_objects.aggregate(Avg('B_Value'))['B_Value__avg'])
	xyz_a_sum = float(xyz_site_objects.aggregate(Avg('A_Value'))['A_Value__avg'])
	xyz_b_sum = float(xyz_site_objects.aggregate(Avg('B_Value'))['B_Value__avg'])
	myDatas = {'myDatas': [["Demo Site", (demo_a_sum, demo_b_sum)], ["ABC Site", (abc_a_sum, abc_b_sum)],
					["XYZ Site", (xyz_a_sum, xyz_b_sum)]]}
	print(myDatas)
	return render(request, 'sitesScreen/summary.html', myDatas)



#this is the python implementation, without using the aggregate functions of django
def python_summary(request):
	objects = Stuff.objects.all()
	objectsDic = {}


	for o in objects:
		siteName = str(o.Site_Name)
		if siteName in objectsDic:
			print("already there")
			currentArray = objectsDic[siteName]
			elementsToAppend = (float(o.A_Value), float(o.B_Value))
			currentArray.append(elementsToAppend)
			objectsDic[siteName] = currentArray
		else:
			print("not there")
			objectsDic[siteName] = [(float(o.A_Value), float(o.B_Value))]

	print(objectsDic)
	myDatas = {'myDatas' : [["Demo Site" , sumLogic(objectsDic["Demo Site"])] , ["ABC Site" , sumLogic(objectsDic["ABC Site"])] , ["XYZ Site" , sumLogic(objectsDic["XYZ Site"])]] }
	return render(request, 'sitesScreen/summary.html' , myDatas)


def python_average(request):
	objects = Stuff.objects.all()
	objectsDic = {}


	for o in objects:
		siteName = str(o.Site_Name)
		if siteName in objectsDic:
			print("already there")
			currentArray = objectsDic[siteName]
			elementsToAppend = (float(o.A_Value), float(o.B_Value))
			currentArray.append(elementsToAppend)
			objectsDic[siteName] = currentArray
		else:
			print("not there")
			objectsDic[siteName] = [(float(o.A_Value), float(o.B_Value))]

	print(objectsDic)
	myDatas = {'myDatas' : [["Demo Site" , avgLogic(objectsDic["Demo Site"])] , ["ABC Site" , avgLogic(objectsDic["ABC Site"])] , ["XYZ Site" , avgLogic(objectsDic["XYZ Site"])]] }
	return render(request, 'sitesScreen/summary.html' , myDatas)


def sumLogic(dataArray):
	suma = 0
	sumb = 0
	for elem in dataArray:
		suma += elem[0]
		sumb += elem[1]
	return  (suma,sumb)

def avgLogic(dataArray):
	suma = 0
	sumb = 0
	counter = 0

	for elem in dataArray:
		suma += elem[0]
		sumb += elem[1]
		counter += 1
	avga = suma/counter
	avgb = sumb/counter

	return  (avga,avgb)

