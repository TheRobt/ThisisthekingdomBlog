from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(imagens_for_post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(postQuote)