from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import signup
from django.contrib.auth.hashers import make_password, check_password
import json

# ✅ User Signup API
@csrf_exempt
def user_signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # JSON Data Read Karein
            f_name = data.get('fname')
            l_name = data.get('lname')
            Password = data.get('password')  # 🔴 Spelling mistake fixed
            Mobile = data.get('mobile')
            email = data.get('email')

            # User Save Karein
            user = signup.objects.create(
                first_name=f_name,
                last_name=l_name,
                Password=make_password(Password),
                Mobile=Mobile,
                Email=email
            )
            return JsonResponse({"message": "User registered successfully!"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=200)

# ✅ User Login API
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            user = signup.objects.get(Email=email)
            if check_password(password, user.Password):
                return JsonResponse({"message": "Login successful", "user": user.first_name}, status=200)
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=200)

        except signup.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=200)

# ✅ Get All Users API
def get_users(request):
    users = signup.objects.all().values('first_name', 'last_name', 'Email', 'Mobile')
    return JsonResponse({"users": list(users)}, status=200)

