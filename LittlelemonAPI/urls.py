from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import CategoryList, CategoryDetail, MenuItemList, MenuItemDetail, CartList, CartDetail, OrderList, OrderDetail, OrderItemList, OrderItemDetail

urlpatterns = [ 

path('categories/', CategoryList.as_view()),
path('categories/<int:pk>/', CategoryDetail.as_view()),
path('menu-items/', MenuItemList.as_view()),
path('menu-items/<int:pk>/', MenuItemDetail.as_view()),
path('carts/', CartList.as_view()),
path('carts/<int:pk>/', CartDetail.as_view()),
path('orders/', OrderList.as_view()),
path('orders/<int:pk>/', OrderDetail.as_view()),
path('orderitems/', OrderItemList.as_view()),
path('orderitems/<int:pk>/', OrderItemDetail.as_view()),

    
#path('menu/',views.menu),
##path('menu-items/cart/', views.CartView.as_view()),
#path('secret/', views.secret),
#path('orders/<int:pk>/', views.orderView.as_view()),
# path("cart/", views.CartViewSet.as_view()),
# path('orders/', views.OrderViewset.as_view()),
# path('categories/', views.CategoriesView.as_view()),
# path('category/<int:pk>', views.SingleCategoryItemView.as_view()),
# path('order-items/<int:pk>', views.OrderItemViewSet.as_view()),
# #path('cart-items/<int:pk>',views.CartViewSet.as_view()),
# #path('cart/',views.CartViewCreate.as_view()),

#-----FUNCTIONAL-----*

#path('menu-items/', views.menu_items), 
#path('menu-items/<int:id>',views.single_item),
#path('menu-items/', views.menu_items),
#path('category/<int:pk>',views.category_detail, name ='category-detail'),

#--------------------*

#path('menu-items/', views.MenuItemsView.as_view()),

#-------->

#CLASS BASED VIEWS

#path('menu-items/', views.MenuItemsView.as_view()),
#path('menu-items/<int:pk>',views.SingleMenuItemView.as_view()),

#--------->

#path('cart/menu-items/<int:pk>',views.CartView.as_view()),
#path('cart/',views.CartViewCreate.as_view()),
#path('cart/menu-items/'views.CartVie)
#path('MenuItems', views.MenuItems.as_view()),
path('throttle-check-auth', views.throttle_check_auth),
path('api-token-auth/', obtain_auth_token),
path('groups/manager/users/', views.managers),
#path('groups/delivery-crew/users',views.delivery),

#------------->
path('lemon', views.lemon),
path('manager-view/', views.manager_view),
path('users/users/me/', views.me), 
path('manager-view/', views.manager_view),
#path('books/', views.BookList.as_view()),
#path('books/<int:pk>',views.Book.as_view()),
#------------>

]

#/users/userId/cart/menu-items
#users/user/userId/cart <--flush
#users/one cart/multiple items. 
#api/orders/{orderId} , 

#path('menu-items', views.MenuitemsViewSet.as_view({'get' :'list'})), 
#path('menu-itmes/<int:pk>)', views.MenuItemsViewset.as_view({'get': 'retrieve'})),


#class based urls.py 
#path('books/<int:pk>, views.BookView.as_view())


#------------------------------

#---------------------------------------
#Regular Routes 
#path('orders', views.Orders.listOrders),
#regular routes path('books, views.books),
#----------------------------------------

#CLASS BOOKVIEW
# path('books', views.BookView.as_view(
#         {
#             'get': 'list',
#             'post': 'create',
#         })
#     ),
#     path('books/<int:pk>',views.BookView.as_view(
#         {
#             'get': 'retrieve',
#             'put': 'update',
#             'patch': 'partial_update',
#             'delete': 'destroy',
#         })
#     )
#------------------------------------------------

#class based views with generics 
    #path('books', views.BookList.as_view())

#-------------------------------------------------------------

#Class Based Views with PK for BookAPIview  (SEARCH BY AUTHOR)
     
    #path('books/<int : pk>', views.Book.as_view)
    #path('books', views.Bo)

    # path('MenuItems', views.MenuItems.as_view()),
    # path('manager-view/', views.manager_view)

    # path('menu-items', views.MenuitemsViewSet.as_view({'get' :'list'})) 
    # path('menu-itmes/<int:pk>)', views.MenuItemsViewset.as_view({'get': 'retrieve'}))

    # path('throttle-check-auth', views.throttle_check_auth)

    #path('groups/manager/users',views.managers)

    #path('menu-items/', views.menu_items), 
    #path('menu-items/<int:id>', views.single_item)

    #path('api-token-auth/', obtain_auth_token)
    #path(manager-view/', views.manager_view), 


#-----------------------------------------------
# SimpleRouter 

# from rest_framework.routers import SimpleRouter
# router = SimpleRouter(trailing_slash=False)
# router.register('books', views.BookView, basename='books')
# urlpatterns = router.urls

# Default Router 

#from rest_framework.routers import DefaultRouter
# router = DefaultRouter(trailing_slash=False)
# router.register('books', views.BookView, basename='books')
# urlpatterns = router.urls
#------------------------------------------------------
