import html

from django import template
from ..models import Income

register = template.Library()


# @register.simple_tag
# def total_districts():
# 	return Income.objects.all.count()


def fill_color(code):
	inc = round(Income.objects.filter(district_code=code)[0].income_last_month)
	
	# default color white
	color = "#fff"
	
	# Given range
	inc_range_one = 2000
	inc_range_two = 4000
	inc_range_three = 6000
	inc_range_four = 8000
	
	# color palette - https://colorpalettes.net/color-palette-2632/
	if inc <= inc_range_one:
		color = "#621216"
	if inc in range(inc_range_one, inc_range_two):
		color = "#d93436"
	if inc in range(inc_range_two, inc_range_three):
		color = "#f06d6e"
	if inc in range(inc_range_three, inc_range_four):
		color = "#6b9235"
	if inc >= inc_range_four:
		color = "#232d1a"
	return color


# income per month


def total_income_by_month(district_code):
	return Income.objects.filter(district_code=district_code)[0].income_by_month

# Top Income districts


@register.simple_tag
def top_sales_income_list():
	return [elem[0] for elem in list((Income.objects.values_list('income_last_month').order_by('income_last_month').reverse()[:10]))]


@register.simple_tag
def top_sales_district_list():
	return [str(elem[0])for elem in list((Income.objects.values_list('district_name').order_by('income_last_month').reverse()[:10]))]

# Top Sales difference districts


@register.simple_tag
def top_sales_difference_income_list():
	return [elem[0] for elem in list((Income.objects.values_list('income_difference').order_by('income_difference').reverse()[:10]))]


@register.simple_tag
def top_sales_difference_district_list():
	return [str(elem[0])for elem in list((Income.objects.values_list('district_name').order_by('income_difference').reverse()[:10]))]

# register the custom filters


register.filter("top_sales_income_list", top_sales_income_list)
register.filter("total_income_by_month", total_income_by_month)
register.filter("fill_color", fill_color)
