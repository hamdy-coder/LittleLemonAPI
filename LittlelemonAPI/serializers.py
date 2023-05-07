from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem
from rest_framework.validators import UniqueValidator
from decimal import Decimal
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title','price','featured','category']

class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer()
    class Meta:
        model = Cart
        fields = ['id','user', 'menuitem', 'quantity','unit_price','price']


class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer
    class Meta:
        model = OrderItem
        fields = ['order', 'menuitem', 'quantity', 'price', 'unit_price']


class OrderSerializer(serializers.ModelSerializer):
    #order_items = OrderItemSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['user', 'delivery_crew', 'status', 'total', 'date']
        
# class MenuItemSerializer(serializers.ModelSerializer): 
#     category = serializers.StringRelatedField() #adds category to menu-items
#     stock = serializers.IntegerField(source = 'featured') #removed feature function and added this
#     price_after_tax = serializers.SerializerMethodField(method_name ='calculate_tax')
#     category = CategorySerializer()
#     class Meta: 
#         model = MenuItem 
#         fields = ['id', 'title', 'price', 'category']#'stock', 'price_after_tax'
    
#     def calculate_tax(self, product:MenuItem): 
#         return product.price * Decimal(1.1)


# #  class MenuItemSerializer(serializers.ModelSerializer): #must have ever item in the menu_item field
# #       title = serializers.CharField(max_length=255)
# #       validators=[UniqueValidator(queryset=MenuItem.objects.all())]

# class MenuItemSerializer(serializers.ModelSerializer): 
#     title = serializers.CharField(max_length=255)
#     validators=[UniqueValidator(queryset=MenuItem.objects.all())]

# #      class Meta:
# #         category = CategorySerializer()
# #         model = MenuItem
# #         fields = ['id','title', 'price',  'featured', 'category']

# # class MenuItemSerializer(serializers.Serializer): 
# #     id = serializers.IntegerField()
# #     title = serializers.CharField(max_length=255)
# #     price = serializers.DecimalField(max_digits=6, decimal_places=2)

# class CartSerializer(serializers.ModelSerializer):
#         menuitem = MenuItemSerializer(read_only=True)
#         class Meta:
#             model = Cart
#             fields = ['user', 'menuitem', 'quantity', 'unit_price','price']

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['user','delivery_crew','status', 'total', 'date'] #supposed to say either pending or delivered.

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         menuitem = MenuItemSerializer()
#         model = OrderItem
#         fields = ['order','menuitem','quantity','unit_price','price']

# #
# # categories = Category.objects.all()
# # serialized_categories = serializers.serialize("json", categories)

# # menu_items = MenuItem.objects.all()
# # serialized_menu_items = serializers.serialize("json", menu_items)

# # carts = Cart.objects.all()
# # serialized_carts = serializers.serialize("json", carts)

# # orders = order.objects.all()
# # serialized_orders = serializers.serialize("json", orders)

# # order_items = OrderItem.objects.all()
# # serialized_order_items = serializers.serialize("json", order_items)


# # #from .models import Cart

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255) #you can bring back the removed items in serializers by adding them again.
#     price=serializers.DecimalField(max_digits = 6, decimal_places = 2)
#     featured=serializers.BooleanField()
#     category = serializers.CharField(max_length=256)


# #     #-------------------------
# #     #Model Serializers
# #     #from rest_framework import serializers

# #     #this goes into serializers.py green it out and add class Meta
# #     #class MenuItemSerializer(serializers.Serializer)
# #     #id = serializers.IntegerField()
# #     #title = serializers.CharField(max_length=255)
# #     #price serializers.DecimalField(max_digits = 6, decimal_places = 2)
# #     #inventory = serializers.IntegerField()

# #     #in serializers.py als have: from_restframework import serializers,
# #     # from .models import MenuItem,
# #     # from decimal import Decimal
# #     # from .models import Category


# # # class CategorySerializer (serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Category
# # #         fields = ['id','title']

# # # class MenuItemSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = MenuItem
# # #         fields = ['title','price','featured','category']#'category

# # # class CartSerializer(serializers.ModelSerializer):
# # #       class Meta:
# # #         model = Cart
# # #         fields = ['user', 'menuitem','quantity','unit_price','price']

# # # class OrderSerializer(serializers.ModelSerializer):
# # #       class Meta:
# # #         model = order
# # #         fields = ['user','delivery_crew','menuitem', 'quantity', 'unit_price', 'price']
# # # #     #     #fields = '__all__'

# # # #class OrderItemSerizializer(serializers.ModelSerializer):
# # #     # class Meta:
# # #     #     unique_together = ('order', 'menuitem')
# # #     #     model =  OrderItem
# # #     #     fields=('order','menuitem','quantity','unit_price', 'quantity','unity_price', 'price')
# # #     #     #fields = '__all__'




# # # #DESERIALIZERS
# # # #category_id = serialziers.IntegerField(write_only=True)>---DESERIALIZATION after adding this to MenuItemSerializer, you add the field, 'category_id' into meta, go to the website but it's outside the rest of the API MenuItems list. go to category ID and add (write_only=TRUE)
# # # #s

# # # #class MenuItemSerializer(serializers.ModelSerializers):  #Came here from Desialization made Category Serializer Read only to be able to post on menuitems api. should work now
# # #    #stock = serializers.IntegerField(source = 'inventory') again changing the inventory part.
# # #    #after calculate tax Method # price_after_tax = serializers.SerialzerMehodField(method_name = 'calculate_tax)
# # #     #fields = ['id','title', 'price', 'inventory'] information is in the database, but it will show the json items
# # #     #new change is fields  = ['id', 'title', 'price' 'stock', 'price_after_stock, 'category']
# # #     #category = serializers.StringRelatedField()>erase this line and put CategorySerializer() <----- this will show category with sub categories id slug and icecream relationship serializers in DRF.
# # #     #category_id = serialziers.IntegerField(write_only=True) add this to show category ID --> DESERIALZIATION after adding this everything should be in line.
# # #     #class Meta:
# # #         #model = MenuItem
# # #         #fields = ['id','title', 'price', 'inventory', 'category_id'] information is in the database, but it will show the json items DESERIALIZATION CHANGE
# # #     # add a new method
# # #         #def calculate_tax(self, product:MenuItem):
# # #             #return product.price * Decimal(1.1) < decimal module for this. Link this with MenuItemSerializer

# # # #
# # #     #RELATIONSHIP SERIALIZER ********
# # #         #
# # #     #---------------

# # # #DESERIALIZER

# # # #COPY PASTA FROM THIS
# # # #----Validators
# # #     #@api_vew(['GET','POST'])
# # #     #def menu_items(request):
# # #         #items = MenuItem.objects.select_related('category').all()
# # #         #serialized_item = MenuItemSerializer(items, many = TRUE)
# # #         #return Response(serialized_item.data)

# # #     #@api_view()
# # #         #def single_item(request,id):
# # #             #item = get_object_or_404(MenuItem,pk = id)
# # #             #serialized_item MenuItemSerializer
# # #             #return Response(serialized_item.data)

# # # #----------------------------------





