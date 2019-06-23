# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def Dashboard(request):
    return render(request, 'dashboard.html')