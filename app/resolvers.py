# app/resolvers.py
from .services import DishService
from .utils import format_price

def resolve_create_dish(info, name, description, price, image_url=None):
    return DishService.create_dish(name, description, price, image_url)

def resolve_update_dish(info, id, name=None, description=None, price=None, image_url=None):
    return DishService.update_dish(id, name, description, price, image_url)

def resolve_delete_dish(info, id):
    return DishService.delete_dish(id)

def resolve_get_dish(info, id):
    dish = DishService.get_dish_by_id(id)
    dish.formatted_price = format_price(dish.price)
    return dish

def resolve_list_dishes(info, category=None):
    dishes = DishService.list_dishes(category)
    for dish in dishes:
        dish.formatted_price = format_price(dish.price)
    return dishes

def resolve_apply_discount(info, id, discount_percentage):
    return DishService.apply_discount_to_dish(id, discount_percentage)

def resolve_get_available_dishes(info):
    dishes = DishService.get_available_dishes()
    for dish in dishes:
        dish.formatted_price = format_price(dish.price)
    return dishes

def resolve_search_dishes(info, query):
    dishes = DishService.search_dishes(query)
    for dish in dishes:
        dish.formatted_price = format_price(dish.price)
    return dishes
