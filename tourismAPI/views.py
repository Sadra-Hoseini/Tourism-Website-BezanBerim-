from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer , AgencySerializer , TourSerializer
from tourism.models import Customer,Agency,Tour
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage



@api_view(['POST' , 'GET'])
def customers_list(request):
    if request.method == 'GET':
        
        customers = Customer.objects.all()
           
        search = request.query_params.get('search')
        perpage = request.query_params.get('perpage' , default = 2)
        page = request.query_params.get('page' , default = 1)

            
        if search:
            customers = customers.filter(first_name__contains = search)

        paginator = Paginator(customers , per_page=perpage )
        if int(perpage) > 8 :
            return Response( status=status.HTTP_400_BAD_REQUEST) 
        
        try:
            customers = paginator.page(number=page)
        except PageNotAnInteger:
            customers = paginator.page(1)    
        except EmptyPage:
            customers = []
            return Response( status=status.HTTP_400_BAD_REQUEST)  

        
        serializer = CustomerSerializer(customers , many = True)
        
    
        return Response(serializer.data )
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','PATCH','DELETE']) 
def customer_detail(request, pk): 
    try: 
        customer = Customer.objects.get(pk=pk) 
    except customer.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
  
    if request.method == 'GET': 
        serializer = CustomerSerializer(customer) 
        return Response(serializer.data) 
  
    elif request.method == 'PUT': 
        serializer = CustomerSerializer(customer, data=request.data) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    elif request.method == 'PATCH': 
        serializer = CustomerSerializer(customer, data=request.data, partial=True) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
    elif request.method == 'DELETE': 
        customer.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)






@api_view(['POST' , 'GET'])
def agencies_list(request):
    if request.method == 'GET':
        
        agencies = Agency.objects.all()


        search = request.query_params.get('search')
        perpage = request.query_params.get('perpage' , default = 2)
        page = request.query_params.get('page' , default = 1)

            
        if search:
            agencies = agencies.filter(agency_name__contains = search)

        paginator = Paginator(agencies , per_page=perpage )
        if int(perpage) > 8 :
            return Response( status=status.HTTP_400_BAD_REQUEST) 
        
        try:
            agencies = paginator.page(number=page)
        except PageNotAnInteger:
            agencies = paginator.page(1)    
        except EmptyPage:
            agencies = []
            return Response( status=status.HTTP_400_BAD_REQUEST) 

        
        serializer = AgencySerializer(agencies , many = True)
        
        
        return Response(serializer.data )
    
    elif request.method == 'POST':
        serializer = AgencySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','PATCH','DELETE']) 
def agency_detail(request, pk): 
    try: 
        agency = Agency.objects.get(pk=pk) 
    except agency.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
  
    if request.method == 'GET': 
        serializer = AgencySerializer(agency) 
        return Response(serializer.data) 
  
    elif request.method == 'PUT': 
        serializer = AgencySerializer(agency, data=request.data) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    elif request.method == 'PATCH': 
        serializer = AgencySerializer(agency, data=request.data, partial=True) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
    elif request.method == 'DELETE': 
        agency.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)






@api_view(['POST' , 'GET'])
def tours_list(request):
    if request.method == 'GET':
        
        tours = Tour.objects.all()

        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage' , default = 2)
        page = request.query_params.get('page' , default = 1)




        if to_price:
            tours = tours.filter(price__lte = to_price)
            
        if search:
            tours = tours.filter(name__contains = search)


        if ordering:
            ordering_list = ordering.split(",")
            tours = tours.order_by(*ordering_list)



        paginator = Paginator(tours , per_page=perpage )
        if int(perpage) > 8 :
            return Response( status=status.HTTP_400_BAD_REQUEST) 
        
        try:
            tours = paginator.page(number=page)
        except PageNotAnInteger:
            tours = paginator.page(1)    
        except EmptyPage:
            tours = []
            return Response( status=status.HTTP_400_BAD_REQUEST)  

        
        serializer = TourSerializer(tours , many = True)
        
        
        return Response(serializer.data )
    
    elif request.method == 'POST':
        serializer = TourSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','PATCH','DELETE']) 
def tour_detail(request, pk): 
    try: 
        tour = Tour.objects.get(pk=pk) 
    except tour.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
  
    if request.method == 'GET': 
        serializer = TourSerializer(tour) 
        return Response(serializer.data) 
  
    elif request.method == 'PUT': 
        serializer = TourSerializer(tour, data=request.data) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    elif request.method == 'PATCH': 
        serializer = TourSerializer(tour, data=request.data, partial=True) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
    elif request.method == 'DELETE': 
        tour.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
