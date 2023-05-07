from decimal import Decimal
from typing import ItemsView
from rest_framework import serializers
from django.http import QueryDict
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from django.views import View
from .models import Cart
from django.contrib import admin
from django.core.paginator import EmptyPage, Paginator
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view  # permission token secret
from rest_framework.decorators import permission_classes, renderer_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage
from .models import MenuItem,Category, Cart, Order, OrderItem
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
#from .throttles import TenCallsPerMinute
from datetime import timedelta
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import authentication
from djoser.views import TokenCreateView, TokenDestroyView #, UserCreateView, UserDeleteView, UserDetailView, UserListCreateView
from rest_framework import viewsets
from .throttles import FiveCallsPerMinute 
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication



#***

#**********************************************************
# class MenuItemsView(generics.ListCreateAPIView): 
#     queryset = MenuItem.objects.all()   # retrieves all the records in the database
#     serializer_class = MenuItemSerializer #display the shit properly
#     ordering_fields = ['price', 'title', 'featured', 'category']
#     filterset_fields = ['price', 'title', 'featured', 'category']
#     search_fields = ['title'] 

# class SingleMenuItemView(generics.RetrieveAPIView,generics.DestroyAPIView):
#      permission_classes = [IsAuthenticated]
#      queryset = MenuItem.objects.all()
#      serializer_class = MenuItemSerializer

#***********************************************************

# @api_view()
# def menu_items(request): 
#     items = MenuItem.objects.select_related('category').all()
#     #items = MenuItem.objects.all()
#     #serialized_item = MenuItemSerializer(items,many=True,context={'request': request})
#     serialized_item=MenuItemSerializer(items, many=True) #essentials when converting list to json
#     return Response(serialized_item.data)
# @api_view()
# def single_item(request, id): 
#     item = MenuItem.objects.get(pk=id)
#     serialized_item = MenuItemSerializer(item) #doesn't use many = true because it's not required to convert a single object 
#     return Response(serialized_item.data)

#*****************************************
#HyperlinkedRelatedField 
# 

# def category_detail(request,pk): 
#     category = get_object_or_404(Category,pk=pk) 
#     serialized_category = CategorySerializer(category) 
#     return Response(serialized_category.data) 


#path(category<int:pk>',views.category_detail,name ='category-detail')

#******************************************
   
   
   
    # permission_classes = [IsAuthenticated]
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method != 'GET':
    #         permission_classes = [IsAuthenticated]
    #         return [permission() for permission in permission_classes]

        # Check if the user is authenticated



    
    #def post(self, request): 
        #permission_classes = [IsAuthenticated]
        #title= request.GET.get('title')
        # if(title): 
        #     return Response({"message":"list of the foods " + title}, status.HTTP_200_OK),
        #return Response ({"title": "list of MenuItems"}, status.HTTP_200_OK)
        # queryset = MenuItem.objects.all()
        # serializer_class = MenuItemSerializer
        # ordering_fields = ['price', 'title']
        # filterset_fields = ['price', 'title']
        # search_fields = ['title']
         
    # def post(self,request):
    #     return Response({"title":"food"}, status.HTTP_201_CREATED)
    


    #  #def get(self,request,pk): 
    #     return Response({"message:single book with id " +str(pk)}, status.HTTP_200_OK)
     
    #  #def post (self,request): 
    #     return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED) 

    #  def put(self,request,pk): 
    #     return Response({"title":request.data.get("title")}, status.HTTP_200_OK)
    # # def put(self,request,pk):
    # #     return Response
#--------------

# class SingleCategoryItemView(generics.RetrieveAPIView): 
#       permission_classes = [IsAuthenticated]
#       queryset = Category.objects.all()
#       serializer_class= CategorySerializer 

# class CategoriesView(generics.ListAPIView,generics.RetrieveUpdateDestroyAPIView):
#        permission_classes = [IsAuthenticated]
#        queryset = Category.objects.all()
#        serializer_class = CategorySerializer

#-------------


#CHAT GPT 

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # queryset = Cart.objects.all()
    # serializer_class = CartSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


#***********************************************

# class CartViewCreate(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# class CartViewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes =[IsAuthenticated]
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# class CartView(generics.CreateAPIView,generics.RetrieveUpdateDestroyAPIView):
#     permissions_classes = [IsAuthenticated]
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer 
#        
#******************************************

# class orderView(generics.ListCreateAPIView, generics.DestroyAPIView): 
#     permissions_classes = [IsAuthenticated]
#     queryset = order.objects.all()
#     serializer_class = OrderSerializer
 
# class OrderItemView(generics.ListAPIView,generics.CreateAPIView, generics.RetrieveDestroyAPIView): 
#      permisson_classes = [IsAuthenticated]
#      queryset = OrderItem.objects.all()
#      serializer_class = OrderItemSerializer
#      class OrderView(generics.ListCreateAPIView):
#          queryset = order.objects.all()
#          serializer_class = OrderSerializer  
#          def get(self, request, *args, **kwargs):
            # return Response ("new response")

#----------functional based views-------> 



#----------->

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manager(request):
    username = request.data['username']
    if username: 
        user = get_object_or_404(User,username=username)
        delivery_crew = Group.objects.get(name = "Manager")         #managers.user_set.add(user)
        return Response({"message":"Success"}, status.HTTP_200_OK)
    return Response ({"message" : " error "}, status.HTTP_400_BAD_REQUEST)

# api_view()
# @permission_classes([IsAuthenticated])
# def manager_view(request):
#      if request.user.groups.filter(name = 'username').exists():
#          return Response({ "message": "only manager should see this"})
#      else: return Response({"message" : " You are not Authorized"}, 403)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def managers(request): 
    return Response({"message":"all good"})

@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.username)

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(requests): 
    return Response({"message" : "message for the logged in users only"})

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request): 
         return Response('all good')
        
# @api_view() 
# @renderer_classes ([TemplateHTMLRenderer])
# #def lemon(request):
#  # type: ignore    items = MenuItem.objects.select_related('category').all()
#    # serialized_item = MenuItemSerializer(ItemsView, many=True)
#     return Response({'data':serialized_item.data}, template_name='lemon.html')

def lemon(request): 
    return render(request, "lemon.html")





# #@api_view(['GET', 'POST])
# def books(request): 
#     return Response 

# class BookList(APIView):
#     def get(self, request): 
#         author = request.GET.get('author')
#         if(author): 
#             return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
        
#         return Response({'title' : request. data.get('title')}, status.HTTP_201_CREATED)
    
#     def post(self,request): 
#         return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED)

# class Book(APIView): 
#     def get(self, request,pk): 
#         return Response({"message":"single book with id"+ str(pk)}, status.HTTP_200_OK)

#     def put(self, request, pk):
#         return Response({"titile": request.data.get('title')}, status.HTTP_200_OK) #{"title:"SeaWolf"}

    
    
    # CRUD 

# class AddToCartView(View):
#     def post(self, request, *args, **kwargs):
#         menuitem_id = request.POST.get('menuitem_id')
#         quantity = request.POST.get('quantity')
#         unit_price = request.POST.get('unit_price')

#         if not request.user.is_authenticated:
#             return JsonResponse({'error': 'You need to be logged in to add items to the cart.'}, status=401)

#         menuitem = get_object_or_404(MenuItem, id=menuitem_id)

#         try:
#             cart = Cart.objects.get(user=request.user, menuitem=menuitem)
#             cart.quantity += int(quantity)
#             cart.price += float(unit_price) * int(quantity)
#             cart.save()
#             except Cart.DoesNotExist:
#             cart = Cart.objects.create(user=request.user, menuitem=menuitem, quantity=quantity, unit_price=unit_price, price=float(unit_price) * int(quantity))

#         return JsonResponse({'success': 'Item added to the cart.'}, status=200)


# class CartView(): 
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer


# class orderView(generics.CreateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
#      queryset = order.objects.all()
#      serializer_class = OrderSerializer
#      permission_classes = [IsAuthenticated]
#      def get_queryset(self):
#          return order.objects.all().filter(user=self.request.user)

# @api_view()
# def single_item(request,id): #APIVIEWITHSERIALISATION
#      item=get_object_or_404(MenuItem,pk=id)
#      serialized_item = MenuItemSerializer(item)
#      return Response(serialized_item.data)

# class OrderView(generics.ListCreateAPIView):
#      queryset = Order.objects.all()
#      serializer_class = OrderSerializer  
#      def get(self, request, *args, **kwargs):
#         return Response(‘new response’)



# class CartViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

    # username = request.data['username']
    # if username: 
    #     user = get_object_or_404(User,username=username)
    #     managers = Group.objects.get(name = "manager")
    #     #managers.user_set.add(user)
    #     return HttResponse({"message":"ok"})
    # return Response ({"message" : " error "}, status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])


# class CategoriesView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# @api_view()        #APIVIEWWITHSERIALIZATION      
# def menu_items(request): 
#     items = MenuItem.objects.all()
#     serialized_item = MenuItemSerializer(items,many=True)#import when converting to JSON
#     #return Response(items.values())
#     return Response(serialized_item.data)

# @api_view()
# def single_item(request,id): #APIVIEWITHSERIALISATION
#     item=get_object_or_404(MenuItem,pk=id)
#     serialized_item = MenuItemSerializer(item)
#     return Response(serialized_item.data)


# @api_view()
# @permission_classes([IsAuthenticated])
# def manager_view(request):
#     if request.user.groups.filter(name = 'Manager').exists():
#         return Response({ "message": "only manager should see this"})
#     else: return Response({"message" : " You are not Authorized"}, 403)


#------------------------------------------------------
#Generics module retrieveAPIView,DestroyAPIVIEW,UPDATE APIVIEW,
#CreateAPIVIEW = POST(Create a new Resource)
#ListAPIView = GET(Display Resource collection)
#RetrieveAPIView = GET(Single Resource) 
#DestroyAPIView = DELETE(Single Resource)
#UpdateAPIView = PUT and PATCH(Replace or partially update a single resource)
#ListCreateAPIView GET,POST(Display Resource Collections and create a new resource)
#RetrieveUpdateAPIVIew(GET,PUT,PATCH)(Displace a single Resource and replace or partially update it) 
#RetrieveDestroyAPIView(Display a single resource and delete it)
#RetrieveUpdateDestroyAPIview (GET,PUT,PATCH,DELETE)
#--------------------------------------------------------

#class MenuItemView(generics.ListAPIView, generics.CreateAPIView)
#class MenuItemView(generics.ListCreateAPIView)
# needs queryset and serializers to perform database operations. 

#AUTHENTICATION and Selective AUTHENTICATION 
# Permission_classes = [IsAuthenticated] 
# to selectively enable authentication for some calls like POST PUT PATCH DELETE you override permissions 
#   
# def get_permssions (self): 
#       permission_classes = []
#       if self.request.method !='GET': 
#           permission_classes = [isAuthenticated]
#       return[permission() for permission in permission_classes] 
# IN this code anyone will be able to do a GET call, but POST PUT PATCH will require Authentication
# 
# 
#Return Items for Authenticated user Only 
# # 
# class OrderView(generics.ListCreateAPIview): 
#     queryset = Order.objects.all() 
#     serializer_class = OrderSerializer 
#     permission_classes = [isAuthenticated]
#     def get_queryset(self): 
#          return Order.objects.all().filter(user=self.request.user)
#--------------------------------------------------------------------
#Generic views will automate everything, but you can override on the default methods. 

#class OrderView(generics.ListCreateAPIView): 
    #queryset = Order.object.all()
    #serializer_class = OrderSerializer 
    #def get(self, request, *args*, *qwargs*) use def post(), def post, put(), patch() delete()

#https://www.coursera.org/learn/apis/supplement/dT8q4/solution-convert-booklist-api-project-to-drf this is an example of using Meta and request class based.  
#------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------
#fuctional view 
# @api_view(['GET', 'POST']) #api decorator, gives it restview, Post allows for Posts to the Rest Framework.
# def book(request): 
#     return Response('list of the books', status= status.HTTP_201_OK) #gives you rest_frameworkview
#     #return HttpResponse('list of the books', status=status.HTTP_201_OK) Gives you Html view

#routing to class method 
#@staticmethod 
#@api_view() 
#@ def ListOrders(request): 
    #return Response({'message : 'list of orders')}, status. HTTP_200_OK)   
#-----------------------------------------------------------------------------------
#class based Views AUTHORS  you can add POST to an A. You can view it in browser. HTTP Response. S
# SEARCH BY AUTHOR 
# #  
# class (APIView):
#     def get(self, request):
#         author = request.GET.get('author')
#         if(author): 
#             return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
#         return Response({"message":"list of books"}, status.HTTP_200_OK)
#
#    #def post (self, request, pk) # the post will send you to api/books and show post content  
#    #return Response({"title":request.data.get('title), status.HTTP_200_OK) 
    
# visit 127.0.0.1:8000/api/books?author=Hemingway
# if you visit :8000/api/books, youll have the option to post content 

#use request.data.get(' ')

# it will lead to JSON data aka Payload" where you can enter data via JSON

    #{ 
    #   "title" :"Seawolf"
    # }

#   def post(self, request): to return title from the payload. To the database. 
        #return Response({"message" : "new book created"}, status.HTTP_201_CREATED)
     #return Response({"title":request.data.get('title')} , status.HTTP_201_CREATED) # to return title to the payload AUTHOR

#using keys in Class Based Views, Routing 
#class BookList(APIViews) 
    #def get(self, request, pk): 
        #return Response({"message": "single book with id " + str(pk)}, status. HTTP_200_OK)

#go to URLS.PY file path('books', views.BookList.as_view()), path('books/<int : pk>, views.Book.as_view)

#class Book(APIView):  
    #def get(self,request, pk): 
        #return Response({ "message":"single book with id " + str(pk)}, status.HTTP_200_OK)
#Open URL  add path('books', views.BookList.as_view()) in urls.py of Booklist API. 
              #path('books/<int: pk>, views.Book.as_view())
    #go to api/books/1 and you should get message "single book Id with one"
    #def put(self, request, pk): 
        #return Response ({"title" : request.data.get('title)}, status.HTTP_200_OK) go to api/books/1 will give you the ability to PUT, you change json title with nasty ID response with "title": "Seawolf". 

#class-based routing 
    #Class BookView(APIView): 
    #def get(self, request, pk):
        #def put(self, request, pk)
    #def put(self, request, pk)
        #def return 
        #return Response ({"title" : request.data.get('title')}, status. HTTTP_200_OK)
        # -----------------------------------    
#vewset.Viewsets extend APIView --> http response 

# class MenuItem(viewsets.ViewSet): 
#     def list(self, request):
#          return Response ({"message":"All Books"}, status.HTTP_200_OK)
#          def create(self,request):
#             return Response ({"message":"Creating Books"}, status.HTTP_201_CREATED)
#          def update(self, request, pk=None):
#             return Response({"message":"All Books"}, status.HTTP_200_OK)
#          def retrieve(self, request, pk = None):
#             return Response ({"message":"All Books"}, status.HTTP_200_OK)
#          def partial_update(self, request, pk=None):
#             return Response({"message":"partially updated"}, status.HTTP_200_OK)
#          def destroy(self, request, pk=None): 
#              return Response({"message" : "deleting a book"}, status.HTTP_200_OK)

# ViewSets 
# class MenuItemViewSet(viewsets.ViewSets) automatically extends Viewset class.  

#ModelViewSet then you add generics to do some work. 
    #class MenuItemView(viewsets.ModelViewSet)
    #readOnlyModelVIewSet  
    #ReadOnlyMenuItemView(viewsets.ReadOnlyModelViewset) Doesn't allow POST,PUT,PATCH or DELETE. 

# Create your views here.First serializers
#--------------------
#
#serializer lab, #came from models.py week 2 came from models serializers >step # 2 
#have this in views from rest_framework.response import Response 

                #from rest_framework.response import Response 
                #from rest_framework.decorators import api_view
                #from .models import MenuItem 
                #from .serializers import MenuItemSerializer 
                #from django.shortcuts import get_object_or_404 

    #self.str slug      #@api_view() 
                        #items = MenuItem.objects.all() --> -MenuItem.object.select_related('category').all()
                        #serialized_item = MenuItemSerializer(items, many = true)
                        #return Response(serialized_items.values()) 
               # goto --> api/menu-items     #after serialization, only id and title is shown. 


                #go to---> #@api_view() 
                    #def single_item(request,id): 
                    #item = get_object_or_404(MenuItem, pk=id) # this will show the JSON error "detail: "not found."
                    #item = MenuItem.objects.get(pk = id) cut this so that a 404 is shown instead of diagnostics
                    #serialized item = MenuItemSerializer(item)<--not using many(item)
                    #return Response(serialized_item.data) <---she calls this single_item method 

                #go to----> urls.py from LLAPI--> 
                    # from django.urls import path 
                    # from . import views 

                        # urlpatterns = [
                            #path('menu-items/', views.menu_items), 
                            #path('menu-items/<int:id>', views.single_item)
                        # 
                        # ] api/menu-items/ 

                        #this will show single items with the values of serializers as a single item, single website. 

            # go to api/menu_items/ it'll show all menu-items in database. with id, title, price 
            # to hide information use the serializer--> go to serializers.py

#----------------------------------------------
#DESERIALIZERS VIEW

#api_view(['GET','POST']) #HERE IS DESERIALIZATION adding get and post 
#Deserialization process. 
#def menu_items(request):  
    #if request.method = 'GET':

      # items = MenuItem.objects.select_related('category').all()
      # serialized_item = MenuItemSerializer(items, many=True)
      #return Response(serialized_items.data)

    #if request.method == 'POST':
      #serialized_item = MenuItemSerializer(data = request.data) Here is DESRIALIZATION
      #serialized_item.is_valid(raise_exception=True) HERE IS DESIRALIZATION
      #serialized_item.validated_data HERE IS DESERIALISATION 
      #serialzied_item.save() HERE IS DESERIALIZATION
      #return Response(serialized_item.data, status.HTTP_201_CREATED) HERE IS DESERIALIZATION 

    #after DESERIALIZATION changes, go to the restframework /api/menu-items 
    # make a post call 
    # {
    #   
    # "title":"Beef Steak", 
      #'price':"2.50"
      # "stock": 100   
    # 
    # 
    # } 
# then hit post there will be an Error category go to MenuItemSerializer in serializers.py 
#category = CategorySerializer(read_only=true) You can comment out the line will hide field from GET request. other option is to put (read_only=True) DESERIALIZER

#@api_view()
    #def single_item(request, id): 
    #item = get_object_404(MenuItem, pk = id)
    #serialized_item = MenuItemSerializer 
    #return Response(serialized_item.data)

    #go to @api_view add (['GET','POST'])

# -----------------------------

# I added if request.method for get and post 

# @api_view(['GET','POST'])
# def menu_items(request): 
#     if request.method == 'GET': 
#         items = MenuItem.objects.select_related('category').all()
#         serialized_item = MenuItemSerializer(items, many = True)
#         return Response(serialized_item.data)      
#     if request.method == 'POST': 
#         serialized_item = MenuItemSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception = True)#--> #is valid invokes the serializer 
#         serialized_item.validated() #data cut this to save data 
#         serialized_item.save()
# this bitch went ahead and added beef steak price and stock to JSON but category field is required.you can pound out or do the write only thing

    #@api_view()
        #def single_item(request,id): 
            #item = get_object_or_404(MenuItem,pk = id)
            #serialized_item MenuItemSerializer 
            #return Response(serialized_item.data)
#RENDERERS 

#XML, YAML, JSON RENDERER 
#renderers 
# 'rest_framework.renderers.JSONRenderer', 
#  'rest_framework.renderers.BrowsableAPIRenderer',
# 
#djangorestframework-xml --> make sure you are in the virtual environment 
# pipenv install djangorestframework. INSTALLED 
#GO TO SETTINGS.PY file after installing djangorfxml

#pipenv install djangorestframework-csv, 
  #in views.py  #from rest_framework_csv.renderers import CSVRenderer, 
  #@renderer_classes([CSVRenderer]) in rests youll see an odd organization of the menuitems. 

#YAML RENDERER 
#pipenv install djangorestframework-yaml 
#put @renderer classes([YAMLRenderer]) below api_view decorator above the function. @api_views()
                                                                                    #@renderer_classes([YAMLRenderer])

#go to global settings. in DEFAULT_RENDERER_CLASSES add --> go to settings. 

# go to settings  in Default_renderer Classes'



#in the Header 
    #Accept: application/json 
    #Go to Insomnia 
    #in the header section  add Accept  and value = text/html click send and DJANGO restFramework interface. 
           
#-------------
#week 3 filtering and searching
#MODELSFILTERING
#class Category(models.Model): 
    #slug = models.Slugfield()
    #title = models.CharField()

    #def __str__(self)--> str: 
        #return self.title.  after you do this go to views @api_view() def menu_items(request)

# #class MenuItem(models.Model); 
    #title = models.CharField(max_length = 255)
    #price = models.DecimalField(max_digits = 6, decimal places = 2)
    #inventory = modles.SmallIntegerField()
 #make sure you add this to serializers.py so that it's seen in category
 #    #categry = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1) so that the category is not deleted before the other items. 
#---------------
#VIEWSFILTERING 
# @api_vew(['GET','POST'])
# def menu_items(request): 
#         if request.method == 'GET': 
#            items = MenuItem.objects.select_related('category').all()
#            category_name = reqquest.query_params.get('category') #FILTERORDERSEARCH added this.
#            to_price = request.query_params.get('to_price')#FILTERORDERSEARCH added this if you put category Icecream youll get a different out put based on criteria passed.          
#            search = request.query_params.get('search') FILTERADDITION Filters item with if statement. 
#            ordering = request.query_params.get('ordering')

           #ordering = request.query_params.get('ordering') ORDER OR SEROTING!!!!
           

           #if category_name: #FILTER 
                #items = items.filter(category__title=category_name) FILTER THING By title 
            
            #if to_price: #FILTER

            #   #items = items.filter(price__lte = to_price) lte = less than or equal to a value  

            #if search: 
            #  items = items.filter(title__contains(search) #filter object SORTED BY PRICE IN ASCENDING ORDER

            #if ordering: 
                #items = items.order_by(ordering) #remove this add the following lines.  
                  #ordering_fields = ordering.split(",") 
                  #items = items.order(*ordering_fields) 
       
           #serialized_item = MenuItemSerializer(items, many = TRUE)
           #return Response(serialized_item.data)
        #if request.method == 'POST': 
            #serialized_item = MenuItemSerializer(data=request.data)
            #serialized_item.is_valid(raise_exception = True)--> is valid invokes the serializer 
            #serialized_item.validated() data cut this to save data 
            #serialized_item.save()
# this bitch went ahead and added beef steak price and stock to JSON but category field is required.you can pound out or do the write only thing

    #@api_view()
        #def single_item(request,id): 
            #item = get_object_or_404(MenuItem,pk = id)
            #serialized_item MenuItemSerializer 
            #return Response(serialized_item.data)

#links: http://12.../api/menuitems/?category=main,?category=icecream,?to_price=3, 
#or api/menu-tems/?to_price=3&category=main. 
#http://127.0.0.1:8000/api/menu_items/?search=chocolate # will return all menuitems with chocolate. 
 
#--------------------
#ORDERING 
# function based views are def with decorators. 
# ascending or descending 
# django-filter package is mostly used with class based... 
#django native sorting will work with function.
#  
#http://127.../api/menu-items?ordering = price. 
# Just /api/menu-items?ordering = -price will alter to descending. 
# to change to descending 
#http://127 ... /api/menu-items?ordering = price,-inventory sorting like an asshole. 

# more sorting... http://.../api/menu-items?ordering=price,inventory #sorts by price and then inventory. 


#http://127../api/menu-items?ordering=price 

#--------
#MODELS.PYFILTERANDORDERING 
#use title to filter objects. 
#class Category(models.Model): 
    #slug = models.Slugfield()
    #title = models.CharField()

    #def __str__(self)--> str: 
        #return self.title.  after you do this go to views @api_view() def menu_items(request)

# #class MenuItem(models.Model); 
    #title = models.CharField(max_length = 255)
    #price = models.DecimalField(max_digits = 6, decimal places = 2)
    #inventory = modles.SmallIntegerField()
 #make sure you add this to serializers.py so that it's seen in category
 #    #category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1) so that the category is not deleted before the other items. 

#----------
#data
#pipenv install bleach 
#go to serializers.py import bleach 

#DATA SANTIZATION 
#PIPENV install bleach, import bleach(in serializers.py)
# sanitize using the validate field () and validate() inside the validation methods. 
# to sanitize, the title field write a validate_title() above the meta class 
# 
# def validate_title(self,value) 
#   return bleach.clean(value)


#go to insomnia send a POST request to menu-items 
#you can also santiize by validate method attrs['title'= bleach.clean(aatrs['title'])
# install bleach first. 
# you can sanitize multiple fields 
    #def validate(self, attrs): 
        #[attrs['title] = bleach.clean(attrs['title'])
        #if (attrs['price'<2): 
            #raise serializers.ValidationError('Prices should not bless than 2.0)
        #if(attrs [ 'inventory']<0): 
            #raise serializers.ValidationError('Stock cannot be negative')
        #return super().validate(attrs)

# preventing SQL injection. inject sql 

# limit = request.Get.get('limiit')
#MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', [limit])

#incorrect: Using String Formatting 

#1000 pages, but only first ten are necessary 
#pagination chuck resaults 
#/api/orders?perpage=4&page=10 serves a limited number of records. 
#first page is records 1 & 2, page 2 will be 3 & 4, page 3 5/6, page 4-78  
# limit ot 10 per page. needs to make two api calls 
#  /api/menu-tems? perpage=10#&page=3  record 21-31
#  /api/menu-items?perpage=10@page=4   records 31-40 
#50 in one single API call. It will send a 400 = BadRequest 

#----------- 
#Pagination 
#from django.core.paginator import Paginator,EmptyPage 


# @api_vew(['GET','POST'])
    #def menu_items(request): 
        #if request.method == 'GET': 
           #items = MenuItem.objects.select_related('category').all()
           
           #category_name = reqquest.query_params.get('category') #FILTERORDERSEARCH added this.
           #to_price = request.query_params.get('to_price')#FILTERORDERSEARCH added this if you put category Icecream youll get a different out put based on criteria passed.          
           #search = request.query_params.get('search') FILTERADDITION Filters item with if statement. 
           #ordering = request.query_params.get('ordering')

           #ordering = request.query_params.get('ordering') ORDER OR SEROTING!!!!
  #PAGINAT #perpage = request.query_params.get('perpage', default=2)
  #paginat #perpage = request.query_params.get('page', default=1) if client doesn't give values default will be 2&1
#pag menu-items/api/menu-items?perpage=3&page=1 you get 3 menuItems
           #if category_name: #FILTER 
                #items = items.filter(category__title=category_name) FILTER THING By title 
            
            #if to_price: #FILTER

            #   #items = items.filter(price__lte = to_price) lte = less than or equal to a value  

            #if search: 
            #  items = items.filter(title__contains(search) #filter object SORTED BY PRICE IN ASCENDING ORDER

            #if ordering: 
                #items = items.order_by(ordering) #remove this add the following lines.  
                  #ordering_fields = ordering.split(",") 
                  #items = items.order(*ordering_fields) 

#PAGINAT   #paginator = Paginator(items, per_page=perpage
 #paginat  #try: 
 #              items=paginator.page(number = page)
 #         #except EMPTYPage: 
 #Pag           items=[]
 #              
           #serialized_item = MenuItemSerializer(items, many = TRUE)
           #return Response(serialized_item.data)
        #if request.method == 'POST': 
            #serialized_item = MenuItemSerializer(data=request.data)
            #serialized_item.is_valid(raise_exception = True)--> is valid invokes the serializer 
            #serialized_item.validated() data cut this to save data 
            #serialized_item.save()
# this bitch went ahead and added beef steak price and stock to JSON but category field is required.you can pound out or do the write only thing

    #@api_view()
        #def single_item(request,id): 
            #item = get_object_or_404(MenuItem,pk = id)
            #serialized_item MenuItemSerializer 
            #return Response(serialized_item.data)
#--------------------------
#VIEWS.py
#CLASSBASEDPAGINATION
# will return all menuitems with chocolate. 
#class based view 
# from rest_framework.response importResponse 
# from rest_framework import viewsets 
# from .models import MenuItem 
# from.serializers  import MenuItemSerializer 

#urls.py 
#from django.urls import path 
#from.import views 

#urlpatterns =  [ 
#       path('menu-items',views.MenuItemViewSet.as_view({'get':'list'}))
#       path('menu-items',views.MenuItemViewSet.as_view({'get':'retrieve'})) 
# 
# ]
 
#go to settings.py 
#class MenuItemsViewSet(viewsets.ModelViewSet): 
    #queryset = menuItem.objects.all()
    #serializer_class = MenuItemSerializer 
    #ordering_fields=['price,' 'inventory] Class based will show a filter button at the top of the RestFramework 

        #price -ascending 
        #price -descending 
        #invntory -ascending 
        #inventory descending 
# add sear by title field. 

# class MenuItemsViewSet(viewsets.ModelViewSet):
#     queryset = MenuItem.object.all()
#     serializer_class = MenuItemSerializer 
#     ordering_fields= ['price', 'inventory]
#     search_fields = 'title' 

#it will open up a searchfield

 #searching in Nested Fields 
    # class MenuItem.objects.all()
        #serializer_class = MenuItemSerializer 
        #orderingfields=['price', 'inventory] 
        #search_fields=['title', 'category_title'] by using this code, api clients can search for menu and category titles 
    
#Drf has built in pagination classes add lines to settings.py --> go to settings
#---------------------
#Caching 
    #cacheable saving resulting 
#refresher 
#Layered API infrastructure 
# visitor-> Firewall --Reverse proxy server --> Web Server---> Database Server 
# then database sends stuff in reverse. 
# will return cached data unless no changes are seen. 
# cache is sort in separate databas caching tools Redis, and Memchached 
#webserver hits database once cached information returns and then 1000*60*4 request not always a good idea because serverside scripts and the database 
#reverse proxy used to distribute even --reversy proxy saved for a certain about of time. So websservers aren't used for too much. Cahce request for a specific time. 
#---------
# token based authentication. 
    #Validate token, Match with user, 
    #authentication process practical. goto--> installed apps. add authtoken and then migrate 
    # 
    # manage.py createsuperuser
    # username admin,mike,john,jess,shawn
    # pw admin123! create token. 

#go to views.py file and add 
#@api_view()
# def secret(request): 
#     return Response({"message" : "some secret message"})

#in urls.py path('secret/', views.secret) api/secret to make it safe 

#import from rest_framework.permissions import IsAuthenticated 
#from rest_framework.decorators import permission_classes 

#add @api_view() go to insomnia GET api/secret "authentication details no provided 403 forbidden"
    #@permissions_classes([IsAuthenticated])
    #def secret(request)
        #return Response({"message ; "some sort of message"})--> go to settings
#go to insomnia GET /api/secret select "bearer token" in Auth paste token in Token field and "Token" in prefix field. 
# it'll be senta as Authorization: Token 32432... 
#GET send request and should show secret message. 

#you can create a user and use that users token. 
#add from rest_framework.authtoken.view import obtain_auth_token
# path('api-token-auth/', obtain_auth_token) <--only accepts HTTP calls 
#  (in the  urls.py of API) 

#goto --> api/api-token-auth/ POST 
    #drf will ask you to supply username and PW. 
    #get a username from one of the ones you created with admin panel. 
    #goto --> form--> FORM URL ENCODED--> username = admin, password = 123... 
    #with right credential a token is produced.
    
#----> 

#---->
#AUTHORIZATION LAYER 
#Login as SUPERUSER ---> Type manager--> click save add --> create a user ---> scroll down click on manager 
#--> click on manager in groups --> assing to manager group--> great .
# 
# @api_view()
# @permission_classes([IsAuthenticated]) 
#   def me(request): 
#   return Response(request.user.email) 

#MANAGERVIEW #--> goto urls.py api --> use 

#---> go to insomnia POST api/api-token-auth/ 
    #put in username: and PW 
    #--> use username John Doe PW 
    #Token should popout --> get it username of user and save it by copy and pasting. 
    #---> send a GET request via /api/manager-view/ using johndoe token--> he is not manager, so will not see manager info. 
    #---> go back to views
    #@api_view()
    #@permissionclasses([IsAuthenticated])
#   def manager_view(request):
#       if request.user.groups.filter(name='Manager').exists(): #checks to see what group authenticated user belongs to. 
#           return Response({"message": "only Manager Should See This"})
#       else:  
#        #return Response({"message" : "You are not Authorized"}, 403)
#  ---> go to insomnia -- GET request via Bearer, pu Token and prefex --> Drf works now in authorization. 
#
#---------
# API THROTTLING 
# built in Anon users and authenticated.  
#@api_view()
#@def throttle(request)
    #return Response({message: "successful"})
    #path('throttle-check', views.throttle.check),

#from rest_framework.throttling import AnonRateThrottle, throttle_classes from rest_framework.decorators throttle_classes

#---> @api_view([AnonRateThrottle])
#@throttle_classes
  #def throttle_check(request)
    #return Response({"message": "succesful"})
#goto settings 
#after settings, go to api/throttle-check, will say "throttle check" multiply the number of clicks and you're get a request throttle. Too many requests

#for users 
#from rest_framework.throttling import UserRateThrottle 




#     #urlpatterns path('throttle-check-auth', views.throttle_check_auth)
# #         #after this go to settings--> 'user' : "/5minute"
#         # goto insomnia --->  go to ---> bearer--->use token prefix Token ---> api/throttle-check-auth (GET)---> preview will show throttle limit.  
#         # 2 for anon 
#         # 5 for user 
#         #----> go to throttles.py 

#@api_view()
#@permission_classes([IsAuthenticated])
#@throttle_classes([TenCallsPerMinute])
#def throttle_check_auth(request): 
#def throttle_check_auth 
    #return Response({"message":"message for the loggid in user only"}) 10 times, and will block any other calls 
#go to insomnia --> api/throttle-check-auth GET click ten times and 429 error, Request was throttled in 56 seconds. 


#class based throttling: 
    #from rest_framework.response import Response 
    #from rest_framework import viewsets 
    #from .models import MenuItem 
    #from .serializers import MenuItemSerializer 

    #open urls.py --> "path('menu-items', views.MenuitemsViewSet.as_view({'get' :'list'})) 
    #path('menu-itmes/<int:pk>)', views.MenuItemsViewset.as_view({'get': 'retrieve'})),
    #add support for throttleing 
    
    #CLASS BASED THROTTLING 
    
    #'DEFAULT_THROTTLE_CLASSES[ 
    #   'rest_framework.throttlin.AnonRateThrottle', 
     #  'rest_framework.throttling.UserRateThrottle', 
    # ]

    # class MenuItemsViewSet(viewsets.ModelViewSet): 
    #    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    #    queryset = MenuItemObjects.all()
    #    serializer_class = MenuItemSerializer   
    
    #-----
        #class MenuItemsViewset(viewsets.ModelViewSet): 
            #queryset = MenuItem.objects.all() 
            #serializer_class = MenuItemSerializer 

            #def get_throttles(self): 
                #if self.action == "create":
                    #throttle_classes = [UserRateThrottle]
                #else: 
                    #throttle_classes = []
                #return [throttle() for throttle in throttle_classes]
    #custom throttle 
    #from .throttles import TenCallsPerMinute 
    #throttle_classes = [TenCallsPerMinute]fb uses 200/hour, insta uses 200/hour, insta messanger 100/second what's app 80/sec

#-----DJOSER easiest authentiction :(
#-----Pipenv shell, pipenv install djoser
#---> create a new section djoser in settings. ALTER IT. Everything is already in there. 
#---> add urls path('auth/', include('djoser.urls')},  project level 
#              path('auth/', include('djoser.urls.authtoken))

#djoser lines /users/ 
#  
# /users/me/
# /users/confirm/
# users/resend_activation/
# /users/set_password/ 
# /users/reset_password_confirm 
# /users/set_username/ 
# /users/reset_username 
# /users/rest_username_confirm 
# /token/login/
# /token/logout/ 
# 
# http://127.0.0.1:8000/users/  
#  
# auth/users/ new button extra actions. it contains all of the djoser options in a panel. 

# use insomnia POST in form username : admin, password :  
    #with token send a post call and a token should popup. or use browsable api. 

# you can create your own tokens 127... /auth/token/login creat tokens. 
#use/auth/users/me GET in insomnia get user token and it will provide information about the authenticated user. 

#djoser also comes with JSON Web Token / JWT 

#-------

#JWT authentication endpoints with JWT 
    #djangorestframework-simplejwt 
    #pipenv install djangorestframework-simplejwt~=5.2.1
    #goto--> settings. py installed apps.

###***** GO to urls.py in project level 
#path('api/token/, TokenObtainPairView.as_view(), name = 'token_obtain_pair'), 
#path('api/token/refresh/', TokenRefreshVIew.as_view(), name = 'token_refresh'), 

#*** go to insomnia --> POST token /api/token/ use username : pw and a refresh and access token popup in insomnia. 
#copy and paste them so you can use them in future. expires after 5 mins 
#--> go to settings --> 

#----> /api/secret GET go to AUTH bearer token  put access token where the bearer is no prefix. 
#if you wait five minutes the access token will seem authenticated. 

# if you use the refresh token api/token/refresh POST send --> body form URL encoded --> 
#refresh : entertokenshere paste refresh token. a new access token will be regenerated 
# api/token/refresh/ POST FORMURLENCODED  refresh : refreshetoken 

#blacklist refresh token blacklist refresh token so that it can't be used again. 
#JWT has blacklist 
#goto --> settings --swt blacklist in installed apps --> migrate 

#go to project level urls --> add  in django.urls import path,include,re_path 
#                                 from rest_framework_simplejwt.views import TokenBlackListView
                                 # from rest_framework_simplejwt.views import TokenObtainPairVIew,TokenRefreshView 
#-> in project level path('api/', TokenBlacklistView.as_view(), name = 'token_blacklist'), 

#goto insomnia ---> POST /api/token/blacklist 
    #refresh : hit send.  drf returns {} cannot use refresh token it is blackliste token_not_valid.
#
# _----_____------
# ----> user registration DJOSER

#if you login to admin panesl-- then go to the auth/users cannot browse without a valid token. 
# but with a token from a user there will be users. 

#POST http://127.01:8000/auth/users/ POST  sends 201 created. 
#you need an endpoint for the superadmin 

#----> 
# @api_view(['POST'])
# @permission_classes() 
# def managers(request): 
#     return Response({"message" : "ok"}) #this can only be accessed by superadmin --> add 
# #---> from rest_framework.permissions import IsAdminUser 

# @api_view 
# def managers(request):
#      return Response({"message": "ok"})
#---> go to urls.py add path('groups/manager/users,views.managers)

#POST api/groups/manager/users, Bearer put in token, Token is prefix 
 #will sho {"message" : "ok"}

 #api_view(['POST'])
 #@permission_classes([IsAdminUser])
 #def managers = request.data['username']
    #username = request.data [ 'username']
    #return Response({"message" : "ok"})

#from django.contrib.auth.models import User,Group 

#--------

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def managers(request): 
#     username = request.data['username']
#     return Response({"message":"ok"})
#     if username: 
#         user=get_object_or_404(User,username=username)
#         managers= Group.objects.get(name = "manager")
#         managers.user_set.add(user)
#         return Response({"message:": 'ok'})
#     return Response({"message" : "error"}, status.HTTP_400_BAD_REQUEST)

#---> open insomnia POST /api/groups/managers/users use bearer token ok 

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def managers(request): 
#     username = request.data['username']
#     if username: 
#         user = get_object_or_400(User, username = username )
#     return Response({"message":"ok"})
#     if username: 
#         user=get_object_or_404(User,username=username)
#         managers= Group.objects.get(name = "manager")
#         managers.user_set.add(user)
#         return Response({"message":"ok"})
#     return Response({"message" : "error"}, status.HTTP_400_BAD_REQUEST)

#------

# @api_view([POST])
# def managers(request): 
#     username = request.data['username']
#     if username: user = get_object_or_404(User, username=username)
#         managers = group.objects.get(name = "Manager")
#     if request.method =='POST': #If the method is post add user to group
#         managers.user.set.add(user)
#     elif request.method =='DELETE': #delete's user from group. 
#         managers.user_set.remove(user) 
#     return Response('message' : "ok")] 
# return Response({"message" : "error"}, status.HTTP_400_BAD_REQUEST)

#----- 

#API project Introduction 
#create managers, Delivery crew and users 
#start with user authentication /api/users
#assign to groups api/users/userId/groups
#some
#  managers are allowed to use allowed API endpoints api/menu-items/, add, edit, remove menu-items
# Should be allowed to to assign users to a delivery person  
#api/users/userid/cart/menu-items/place an order, cart must be empty after successful purchase
# you can allso add a flush cart/api/userse/userid/cart 
#one customer, one cart. one cart should contain multiple menu-items 
#assign managers an api to brows assign filter
    #api/orders --> manager token
    #api/orders/{orderId}
#/api/orders?status=delivered Filtered orders(manager token)
#/api/order/status=pending (manager Token)

#/api/orders -->delivery (token)
#/api/orders/orderID 

#throttle 5 calls per minute

#customsers(all orders (customer token)