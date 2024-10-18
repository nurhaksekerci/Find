from django.http import JsonResponse, HttpResponse
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import *
from .serializers import *
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://127.0.0.1:8000/dj-rest-auth/google/"  # Callback URL API'nin kendisi olmalı


@csrf_exempt
def email_confirmation(request, key):
    # E-posta onayı başarılı olduğunda JSON yanıt döndür
    response_data = {
        "status": "success",
        "message": "Email confirmation successful.",
        "key": key
    }
    return JsonResponse(response_data)

@csrf_exempt
def reset_password_confirm(request, uid, token):
    # Şifre sıfırlama başarılı olduğunda JSON yanıt döndür
    response_data = {
        "status": "success",
        "message": "Password reset confirmation successful.",
        "uid": uid,
        "token": token
    }
    return JsonResponse(response_data)

def get_google_user_info(access_token):
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    user_info_response = requests.get(user_info_url, headers=headers)
    return user_info_response.json()

from allauth.account.models import EmailAddress

def google_callback(request):
    code = request.GET.get('code')
    
    if not code:
        return JsonResponse({"error": "Code not found"}, status=400)

    # Google'dan token alma işlemi
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': '161188250829-f6colr9fmt4thdbg380hshmpn3vb4dd9.apps.googleusercontent.com',
        'client_secret': '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',
        'redirect_uri': 'http://127.0.0.1:8000/dj-rest-auth/google/callback/',
        'grant_type': 'authorization_code'
    }

    token_response = requests.post(token_url, data=data)
    token_data = token_response.json()

    if 'access_token' in token_data:
        access_token = token_data['access_token']
        id_token = token_data['id_token']

        # Kullanıcı bilgilerini Google'dan almak için access_token kullan
        user_info = get_google_user_info(access_token)
        user = CustomUserModel.objects.get(email=user_info['email'])
        if not user:
            user = CustomUserModel.objects.create(email=user_info['email'], first_name=user_info['given_name'], last_name=user_info['family_name'])
            EmailAddress.objects.create(user=user, email=user.email, verified=user_info['verified_email'], primary=True)
        
        user_data = CustomUserModelSerializer(user).data
        return JsonResponse({
            "user": user_data,
            "access_token": access_token,
            "id_token": id_token,
            "user_info": user_info  # Google'dan gelen kullanıcı bilgileri
        })
    else:
        return JsonResponse({"error": "Token alma işlemi başarısız"}, status=400)