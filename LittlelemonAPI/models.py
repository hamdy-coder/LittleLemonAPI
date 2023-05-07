from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model): 
     slug = models.SlugField()
     title = models.CharField(max_length = 255, db_index=True)
     def __str__(self)-> str:
        return self.title

class MenuItem(models.Model): 
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default=1)# type: ignore #default = 1 
    def __str__(self)-> str:
        return self.title

class Cart(models.Model): 
    user= models.ForeignKey(User, on_delete=models.PROTECT) 
    menuitem= models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    class Meta: 
        unique_together=('menuitem','user')

class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(db_index=True, default= False)
    total = models.DecimalField(max_digits=6, decimal_places=2) 
    date = models.DateField(db_index= True)
    

class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete= models.CASCADE) 
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta: 
        unique_together = ('order', 'menuitem')

# Create your models here.
#------------------------------------
#Serializers.MenuItem, week 2, serializers step 1 makemodels, step 2 go to views 
# go to --> Models.py --> enter class --> then go to views.py
#class MenuItem(models.Model); 
    #title = models.CharField(max_length = 255)
    #price = models.DecimalField(max_digits = 6, decimal places = 2)
    #inventory = modles.SmallIntegerField()
#------------------------------------
#from django.db import models 
#MODEL Serializers makes things easier 

#class MenuItem(models.Model); 
    #title = models.CharField(max_length = 255)
    #price = models.DecimalField(max_digits = 6, decimal places = 2)
    #inventory = modles.SmallIntegerField()

#-----------------------------------------
#models.py 
#from django.db import(models.Model)

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

#migrate these items 





