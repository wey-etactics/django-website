from django.contrib import admin

from .models import Portfolio

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['client_name']}),
        (None,                  {'fields': ['client_website']}),
        (None,                  {'fields': ['client_description']}),
        (None,                  {'fields': ['client_img']}),
    ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    search_fields = ['client_name']

admin.site.register(Portfolio, PortfolioAdmin)