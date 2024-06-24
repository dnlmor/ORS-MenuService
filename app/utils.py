# app/utils.py

import re
from decimal import Decimal
from flask import current_app
import logging

# Set up logging
logger = logging.getLogger(__name__)

def validate_dish_name(name):
    """
    Validate the dish name.
    - Must be between 2 and 100 characters
    - Can only contain letters, numbers, spaces, and hyphens
    """
    if not 2 <= len(name) <= 100:
        raise ValueError("Dish name must be between 2 and 100 characters")
    if not re.match(r'^[a-zA-Z0-9\s-]+$', name):
        raise ValueError("Dish name can only contain letters, numbers, spaces, and hyphens")
    return name

def validate_dish_description(description):
    """
    Validate the dish description.
    - Must be between 10 and 500 characters
    """
    if not 10 <= len(description) <= 500:
        raise ValueError("Dish description must be between 10 and 500 characters")
    return description

def validate_dish_price(price):
    """
    Validate the dish price.
    - Must be a positive number
    - Must have at most two decimal places
    """
    try:
        price = Decimal(str(price)).quantize(Decimal('0.01'))
    except:
        raise ValueError("Invalid price format")
    
    if price <= 0:
        raise ValueError("Price must be a positive number")
    
    return float(price)

def format_price(price):
    """Format the price to always show two decimal places"""
    return f"{price:.2f}"

def log_dish_operation(operation, dish_id=None, dish_name=None):
    """Log dish operations for auditing purposes"""
    message = f"Dish {operation}"
    if dish_id:
        message += f" (ID: {dish_id})"
    if dish_name:
        message += f" - {dish_name}"
    logger.info(message)

def is_valid_image_url(url):
    """
    Validate if the provided URL is a valid image URL.
    This is a basic check and can be expanded based on specific requirements.
    """
    return url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

def generate_dish_slug(name):
    """Generate a URL-friendly slug for the dish name"""
    return re.sub(r'[^\w]+', '-', name.lower()).strip('-')

def calculate_dish_calories(ingredients):
    """
    Calculate the total calories of a dish based on its ingredients.
    This is a placeholder function and should be implemented based on actual data.
    """
    # Placeholder implementation
    return sum(ingredient.get('calories', 0) for ingredient in ingredients)

def is_dish_available(dish):
    """Check if a dish is currently available (e.g., not out of stock)"""
    # Placeholder implementation
    return dish.in_stock > 0 if hasattr(dish, 'in_stock') else True

def apply_discount(price, discount_percentage):
    """Apply a discount to the dish price"""
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discounted_price = price * (1 - discount_percentage / 100)
    return round(discounted_price, 2)

def get_dish_category(dish_name):
    """
    Determine the category of a dish based on its name or ingredients.
    This is a placeholder function and should be implemented based on actual categorization logic.
    """
    # Placeholder implementation
    if 'pizza' in dish_name.lower():
        return 'Pizza'
    elif 'salad' in dish_name.lower():
        return 'Salad'
    elif 'pasta' in dish_name.lower():
        return 'Pasta'
    else:
        return 'Other'

# Add more utility functions as needed
