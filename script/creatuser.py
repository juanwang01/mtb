#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtbao.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtb.settings")
django.setup()

from apps.base import models

models.UserInfo.objects.create(
    name="wupeiqi",
    password="123123"
)