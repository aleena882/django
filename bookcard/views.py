from django.shortcuts import render, redirect
from bookcard.models import Book
from bookcard.models import Register


# Create your views here.


def books(request):
    if request.method == 'POST':
        users = Book()
        users.book_id = request.POST.get('book_id')
        users.author = request.POST.get('author')
        users.about = request.POST.get('about')
        users.price = request.POST.get('price')
        users.image = request.FILES.get('image')  # Handle image upload
        users.save()
        return redirect('/cards')
    return render(request, 'add.html')


def dis_book(request):
    books1 = Book.objects.all()
    return render(request, "cards.html", {'books1': books1})


def book_search(request):
    query = request.GET.get('search')  #capture the search qurey. should be on name
    if query:
        books = Book.objects.filter(bookname_icontain=query)
    else:
        books = Book.objects.all()
        return render(request, 'cards.html', {'books': books})


def register(request):
    if request.method == 'POST':
        reg_obj = Register()
        reg_obj.username = request.POST.get("name")
        reg_obj.email = request.POST.get('email')
        reg_obj.password = request.POST.get('password')
        reg_obj.contact = request.POST.get('contact')
        reg_obj.save()
        return redirect('login/')
    return render(request, 'register.html')


# def login(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         password = request.POST.get('password')
#         user = Register.objects.filter(username=name, password=password)
#         if user:
#             request.session['name'] = name
#             return redirect('cards/')
#         else:
#             return redirect('login/')
#         return render(request, 'add.html')
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if user exists in the database
        user = Register.objects.filter(username=username, password=password).first()
        if user:
            # If user is found, create a session and redirect
            request.session['name'] = username
            return redirect('/cards/')  # Update as needed for your actual page
        else:
            # Redirect back to login on failure, or add an error message
            return redirect('cards/', {'error': "Invalid username or password."})
    # If the request method is GET, render the login page
    return render(request, 'login.html')


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'more.html', {"book": book})


def delete(request, id):
    book_to_delete = Book.objects.get(id=id)
    book_to_delete.delete()
    return redirect('/cards')

def update(request, id):
    book_to_update = Book.objects.get(id=id)
    if request.method == 'POST':
        Book()
        users = Book.objects.get(book_id=book_id)
        users.book_id = request.POST.get('book_id')
        users.author = request.POST.get('author')
        users.about = request.POST.get('about')
        users.price = request.POST.get('price')
        users.image = request.FILES.get('image')  # Handle image upload
        users.save()
        return redirect('/add')
    return render(request, 'add.html', {'users': book_to_update})


def home(request):
    return render(request, 'home.html')
