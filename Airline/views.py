from .forms import ProductForm, OrderForm
from .models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(from .forms import ProductForm, OrderForm
from .models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp\product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'imageapp\product.html', {'form': form})

def products(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request, 'imageapp\products.html', context)

def order(request, id):
    obj = get_object_or_404(Product, id =id)
    form = OrderForm(request.POST or None, instance = obj)
    data = Product.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'form':form, 'data':data}
    return render(request, 'imageapp/order.html', context)

def kart(request):
    Ordered_items = Product.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Product.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'imageapp/kart.html', context)
        form = ProductForm()
    return render(request, 'imageapp\product.html', {'form': form})

def products(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request, 'imageapp\products.html', context)

def order(request, id):
    obj = get_object_or_404(Product, id =id)
    form = OrderForm(request.POST or None, instance = obj)
    data = Product.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'form':form, 'data':data}
    return render(request, 'imageapp/order.html', context)

def kart(request):
    Ordered_items = Product.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Product.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'imageapp/kart.html', context)