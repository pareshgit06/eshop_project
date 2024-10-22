from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True) 
    email = models.EmailField(null=True,blank=True) 
    otp = models.IntegerField(default=0,null=True,blank=True)
    password = models.CharField(max_length=500,default="default_password")

    def __str__(self) -> str:
        return self.name
    
# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

# SubCategory Model
class SubCategory(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    main_cid = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories',null=True,blank=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    main_cid = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',null=True,blank=True)
    sub_cid = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(default="Krishna", null=True, blank=True)
    color = models.CharField(max_length=50,null=True, blank=True)  # Add this line for color field
    size = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Add_to_cart(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Add_to_Wishlist(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to="media",null=True,blank=True)
    original_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.name
