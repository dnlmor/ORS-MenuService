# app/services.py

from .models import Dish
from .database import db_session
from .utils import (
    validate_dish_name, validate_dish_description, validate_dish_price,
    format_price, log_dish_operation, generate_dish_slug, is_valid_image_url,
    calculate_dish_calories, is_dish_available, apply_discount, get_dish_category
)
from sqlalchemy.exc import IntegrityError

class DishService:
    @staticmethod
    def create_dish(name, description, price, image_url=None):
        try:
            name = validate_dish_name(name)
            description = validate_dish_description(description)
            price = validate_dish_price(price)
            
            if image_url and not is_valid_image_url(image_url):
                raise ValueError("Invalid image URL")

            slug = generate_dish_slug(name)
            category = get_dish_category(name)
            
            dish = Dish(
                name=name,
                description=description,
                price=price,
                slug=slug,
                image_url=image_url,
                category=category
            )
            db_session.add(dish)
            db_session.commit()
            
            log_dish_operation("created", dish_id=dish.id, dish_name=dish.name)
            return dish
        except IntegrityError:
            db_session.rollback()
            raise ValueError("A dish with this name already exists")

    @staticmethod
    def update_dish(id, name=None, description=None, price=None, image_url=None):
        dish = Dish.query.get(id)
        if not dish:
            raise ValueError("Dish not found")
        
        if name:
            dish.name = validate_dish_name(name)
            dish.slug = generate_dish_slug(name)
        if description:
            dish.description = validate_dish_description(description)
        if price is not None:
            dish.price = validate_dish_price(price)
        if image_url:
            if not is_valid_image_url(image_url):
                raise ValueError("Invalid image URL")
            dish.image_url = image_url
        
        dish.category = get_dish_category(dish.name)
        
        try:
            db_session.commit()
            log_dish_operation("updated", dish_id=dish.id, dish_name=dish.name)
            return dish
        except IntegrityError:
            db_session.rollback()
            raise ValueError("A dish with this name already exists")

    @staticmethod
    def delete_dish(id):
        dish = Dish.query.get(id)
        if not dish:
            raise ValueError("Dish not found")
        
        db_session.delete(dish)
        db_session.commit()
        log_dish_operation("deleted", dish_id=id, dish_name=dish.name)
        return True

    @staticmethod
    def get_dish_by_id(id):
        dish = Dish.query.get(id)
        if not dish:
            raise ValueError("Dish not found")
        return dish

    @staticmethod
    def list_dishes(category=None):
        query = Dish.query
        if category:
            query = query.filter_by(category=category)
        return query.all()

    @staticmethod
    def apply_discount_to_dish(id, discount_percentage):
        dish = Dish.query.get(id)
        if not dish:
            raise ValueError("Dish not found")
        
        original_price = dish.price
        discounted_price = apply_discount(original_price, discount_percentage)
        dish.price = discounted_price
        db_session.commit()
        
        log_dish_operation(f"applied {discount_percentage}% discount", dish_id=dish.id, dish_name=dish.name)
        return dish

    @staticmethod
    def get_available_dishes():
        return [dish for dish in Dish.query.all() if is_dish_available(dish)]

    @staticmethod
    def search_dishes(query):
        return Dish.query.filter(Dish.name.ilike(f'%{query}%') | Dish.description.ilike(f'%{query}%')).all()
