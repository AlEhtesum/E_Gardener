from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from capb import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from .helpers import send_forget_password_mail
import uuid
from .models import Profile
from .models import Post
from .models import Contact
import re


# from .models import checkout

# Create your views here.
def home(request):
    if request.method == "POST":
        print("Hello")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create and save the Contact object with the provided data
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return HttpResponse("<h1>Thanks For Contacting Us</h1>")    
    return render(request, "authentication\index.html")


def about(request):
    return render(request, "authentication\pabout.html")


def team(request):
    return render(request, "authentication\pteam.html")


def blog(request):
    posts = Post.objects.all()

    return render(request, "authentication/pblog.html", {"posts": posts})


def services(request):
    return render(request, "authentication\services.html")

def flower(request):
    return render(request, "authentication/flower.html")

def fruit(request):
    return render(request, "authentication/fruit.html")

def herb(request):
    return render(request, "authentication/herb.html")

def shurb(request):
    return render(request, "authentication/shurb.html")

def climbing(request):
    return render(request, "authentication/climbing.html")

def vegetable(request):
    return render(request, "authentication/vegetable.html")

def products(request):
    return render(request, "authentication\products.html")

def modern(request):
    return render(request, "authentication\modern.html")

def city(request):
    return render(request, "authentication\city.html")

def formal(request):
    return render(request, "authentication/formal.html")

def rock(request):
    return render(request, "authentication/rock.html")

def japan(request):
    return render(request, "authentication\japan.html")

def trad(request):
    return render(request, "authentication/trad.html")
def tips(request):
    return render(request, "authentication/tips.html")

def care(request):
    return render(request, "authentication/care.html")

def disease(request):
    return render(request, "authentication/disease.html")

def checkout(request):
    return render(request, "authentication/checkout.html")



def post_read(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, "authentication/post-read.html", {"post": post})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        error_messages = validate_signup_data(username, pass1, pass2, email)
        if error_messages:
            for error_message in error_messages:
                messages.error(request, error_message)
            return render(request, "authentication\signup.html")
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            token = str(uuid.uuid4())

            profile = Profile(user=myuser, forget_password_token=token)
            profile.save()

            myuser.is_active = False
            myuser.save()

        messages.success(
            request,
            "Your account has been successfully created. We have sent you a confirmation email. Pleasee confirm your email in order to activate youre account.",
        )

        subject = "Welcome to rooftopGardenershub Login!!"
        message = (
            "Hello"
            + myuser.first_name
            + "!!\n"
            + "Welcome to E-Gardener. \n Thank you for visiting our website. \n Web have also sent you a confirmation email. \n Please confirm to activate your account."
        )
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]

        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)

        email_subject = "Confirm your email @ E-Gardener Login!"
        message2 = render_to_string(
            "email_confirmation.html",
            {
                "name": myuser.first_name,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(myuser.pk)),
                "token": generate_token.make_token(myuser),
            },
        )

        email = EmailMessage(
            email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email]
        )
        email.send()
        email.fail_silently = True

        return redirect("signin")

    return render(request, "authentication\signup.html")


def validate_signup_data(username, pass1, pass2, email):
    error_messages = []

    if len(username) > 30:
        error_messages.append("The username must be under 30 characters")

    if pass1 != pass2:
        error_messages.append("* The password and confirm password did not match")

    if not username.isalnum():
        error_messages.append("The username should be Alpha-Numeric")

    if User.objects.filter(username=username).exists():
        error_messages.append("The Username is already in use. Please try another")

    if User.objects.filter(email=email).exists():
        error_messages.append("This email is already in use. Please try another")

    if len(pass1) < 10:
        error_messages.append("* Password should be at least 10 characters long")

    if not re.search(r"[A-Z]", pass1):
        error_messages.append("* Password should contain at least one capital letter")

    if not re.search(r"[a-z]", pass1):
        error_messages.append("* Password should contain at least one small letter")

    if not re.search(r"\d", pass1):
        error_messages.append("* Password should contain at least one number")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pass1):
        error_messages.append(
            "* Password should contain at least one special character"
        )

    return error_messages


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {"fname": fname})

        else:
            messages.error(request, "Bad credentials.")
            return redirect("signin")

    return render(request, "authentication\signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
        profile = Profile.objects.get(user=myuser)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        fname = myuser.first_name
        return render(request, "authentication/index.html", {"fname": fname})

    else:
        return render(request, "activation_failed.html")


def ChangePassword(request, token):
    context = {}

    try:
        profile_obj = Profile.objects.filter(forget_password_token=token).first()
        context = {"user_id": profile_obj.user.id}

        if request.method == "POST":
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("reconfirm_password")
            user_id = request.POST.get("user_id")

            if user_id is None:
                messages.success(request, "No user id found.")
                return redirect(f"/change-password/{token}/")

            if new_password != confirm_password:
                messages.success(request, "both should  be equal.")
                return redirect(f"/change-password/{token}/")

            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect("signin")

    except Exception as e:
        print(e)
    return render(request, "change-password.html", context)


def ForgetPassword(request):
    try:
        if request.method == "POST":
            username_or_email = request.POST.get("username_or_email")

            # Check if the input is a valid email
            if "@" in username_or_email:
                user_obj = User.objects.filter(email=username_or_email).first()
            else:
                user_obj = User.objects.filter(username=username_or_email).first()

            if not user_obj:
                messages.error(
                    request, "No user found with the provided username or email."
                )
                return redirect("ForgetPassword")

            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, "An email is sent.")
            return redirect("forget-password")

    except Exception as e:
        print(e)
    return render(request, "forget-password.html")

# def checkout(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         address = request.POST.get('address')
#         payment_method = request.POST.get('payment')

#         # Save the order information to the database
#         checkout = checkout(name=name, email=email, contact=contact, address=address, payment_method=payment_method)  # Adjust the model name
#         checkout.save()

#         # Redirect to a thank you page or any other appropriate page
#         return redirect('thank_you_page')

#     return render(request, 'checkout.html')
