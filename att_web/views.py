# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404


def index(request):
    try:
        return render(request, 'att_web/index.html')
    except:
        raise Http404("Template does not exist")
