# from django.shortcuts import render
# from django.http import JsonResponse

# # Create your views here.



# def home(request):
#     return JsonResponse({
#         "message": "Welcome to Core API"
#     })





import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Product


# ===========================
# GET ALL PRODUCTS
# ===========================

@csrf_exempt
def list_product(req):

    if req.method == "GET":

        # Database se saara data lao
        products = Product.objects.all()
        print(products)
        print(type(products))

        # QuerySet ko List me convert karo
        p_data = list(products.values())
        print(p_data)
        print(type(p_data))

        # Python List -> JSON String
        j_data = json.dumps(p_data)
        print(j_data)
        print(type(j_data))

        return HttpResponse(j_data, content_type="application/json")

    d = {"msg": "Invalid Request"}
    j_data = json.dumps(d)

    return HttpResponse(j_data, content_type="application/json")









@csrf_exempt
def single_product(req, id):

    if req.method == "GET":

        try:

            # Particular Product lao
            product = Product.objects.get(id=id)
            print(product)
            print(type(product))

            # Model Object -> Dictionary
            p_data = {
                "id": product.id,
                "name": product.name,
                "brand": product.brand,
                "price": float(product.price),
                "stock": product.stock,
                "description": product.description,
                "created_at": str(product.created_at)
            }

            print(p_data)
            print(type(p_data))

            # Dictionary -> JSON
            j_data = json.dumps(p_data)
            print(j_data)
            print(type(j_data))

            return HttpResponse(j_data, content_type="application/json")

        except Product.DoesNotExist:

            d = {"msg": "Product Not Found"}

            return HttpResponse(json.dumps(d), content_type="application/json")

    d = {"msg": "Invalid Request"}

    return HttpResponse(json.dumps(d), content_type="application/json")










@csrf_exempt
def create_product(req):

    if req.method == "POST":

        # Raw Bytes
        data = req.body
        print(data)
        print(type(data))

        # Bytes -> Dictionary
        p_data = json.loads(data)
        print(p_data)
        print(type(p_data))

        # Data nikalo
        n = p_data.get("name")
        b = p_data.get("brand")
        p = p_data.get("price")
        s = p_data.get("stock")
        d = p_data.get("description")

        print(n, b, p, s, d)

        # Database me save
        Product.objects.create(
            name=n,
            brand=b,
            price=p,
            stock=s,
            description=d
        )

        msg = {"msg": "Product Created Successfully"}

        # Dictionary -> JSON
        j_data = json.dumps(msg)

        return HttpResponse(j_data, content_type="application/json")

    d = {"msg": "Invalid Request"}

    return HttpResponse(json.dumps(d), content_type="application/json")









@csrf_exempt
def update_product(req, id):

    if req.method == "PUT":

        try:

            product = Product.objects.get(id=id)
            print(product)
            print(type(product))

            # Raw Bytes
            data = req.body
            print(data)
            print(type(data))

            # Bytes -> Dictionary
            p_data = json.loads(data)
            print(p_data)
            print(type(p_data))

            # Complete Update
            product.name = p_data.get("name")
            product.brand = p_data.get("brand")
            product.price = p_data.get("price")
            product.stock = p_data.get("stock")
            product.description = p_data.get("description")

            product.save()

            d = {"msg": "Product Updated Successfully"}

            j_data = json.dumps(d)

            return HttpResponse(j_data, content_type="application/json")

        except Product.DoesNotExist:

            d = {"msg": "Product Not Found"}

            return HttpResponse(json.dumps(d), content_type="application/json")

    d = {"msg": "Invalid Request"}

    return HttpResponse(json.dumps(d), content_type="application/json")









@csrf_exempt
def patch_product(req, id):

    if req.method == "PATCH":

        try:

            product = Product.objects.get(id=id)
            print(product)
            print(type(product))

            data = req.body
            print(data)
            print(type(data))

            p_data = json.loads(data)
            print(p_data)
            print(type(p_data))

            # Sirf bheje hue fields update honge
            product.name = p_data.get("name", product.name)
            product.brand = p_data.get("brand", product.brand)
            product.price = p_data.get("price", product.price)
            product.stock = p_data.get("stock", product.stock)
            product.description = p_data.get("description", product.description)

            product.save()

            d = {"msg": "Product Patched Successfully"}

            j_data = json.dumps(d)

            return HttpResponse(j_data, content_type="application/json")

        except Product.DoesNotExist:

            d = {"msg": "Product Not Found"}

            return HttpResponse(json.dumps(d), content_type="application/json")

    d = {"msg": "Invalid Request"}

    return HttpResponse(json.dumps(d), content_type="application/json")









@csrf_exempt
def delete_product(req, id):

    if req.method == "DELETE":

        try:

            product = Product.objects.get(id=id)
            print(product)
            print(type(product))

            product.delete()

            d = {"msg": "Product Deleted Successfully"}

            j_data = json.dumps(d)

            return HttpResponse(j_data, content_type="application/json")

        except Product.DoesNotExist:

            d = {"msg": "Product Not Found"}

            return HttpResponse(json.dumps(d), content_type="application/json")

    d = {"msg": "Invalid Request"}

    return HttpResponse(json.dumps(d), content_type="application/json")


