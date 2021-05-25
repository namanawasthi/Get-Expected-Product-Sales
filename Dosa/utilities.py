from . import models


def get_parent_category_id(pk):
    data = models.ParentCategory.objects.get(pk=int(pk))
    return data

def get_sub_category_id(pk):
    data = models.SubCategory.objects.get(pk=int(pk))
    return data



def get_parent_category_data():
    data = models.ParentCategory.objects.all()
    return data

def get_sub_category_detail(pk=None):
    parent = get_parent_category_id(pk)
    data = models.SubCategory.objects.filter(parent=parent)
    return data

def get_products(pk=None):
    sub_category = get_sub_category_id(pk)
    data = models.Product.objects.filter(sub_category=sub_category)
    return data

def get_product_detail(_id=None):
    data = models.Product.objects.get(pk=int(_id))
    return data

def done_vote(product_id=None,vote=None):
    prod = get_product_detail(product_id)
    product_vote,__ = models.ProductVoting.objects.get_or_create(product=prod)
    if(vote=="Yes"):
        current_vote =  product_vote.yes
        current_vote+=1
        product_vote.yes = current_vote
    elif(vote=="No"):
        current_vote =  product_vote.no
        current_vote+=1
        product_vote.no = current_vote
    current = product_vote.total_vote
    current+=1
    product_vote.total_vote = current
    product_vote.save()

def slider_data():
    data = models.Slider.objects.all()
    return data
        
    
