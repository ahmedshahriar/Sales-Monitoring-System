from django.contrib import admin
from .models import Income


# Register your models here.
class IncomeAdmin(admin.ModelAdmin):
	list_display = (
		'district_name', 'district_code', 'month', 'income_by_month', 'income_last_month', 'income_difference',
		'income')


admin.site.register(Income, IncomeAdmin)
