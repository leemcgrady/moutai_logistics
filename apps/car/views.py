from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth.hashers import check_password,make_password
import re
# Create your views here.
# Create your views here.

class IndexView(View):

    def get(self, request):

        return render(request, 'index.html')