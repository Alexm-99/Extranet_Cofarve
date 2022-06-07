#from readline import parse_and_bind
import os
from django.conf import settings
from multiprocessing import context
from traceback import format_stack
from urllib.request import Request
from django.shortcuts import render
from django.db import connection
from .models import TemasImportantes, link, linkSecond, Galeria, stockIcon
from .forms import PostForm, PostSubmenu,PostGaleria
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.core import serializers
from django.views.generic.edit import FormView
from django.http import JsonResponse,HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import json
# pon el import de la librerías mas arriba junto a tus otros imports
# ...



# Create your views here.





