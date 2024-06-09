from flask import Blueprint, request, jsonify
from flask_graphql import GraphQLView
from app.models import MenuItem
from app.schema import schema
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    new_item = MenuItem(name=data['name'], price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Menu item added successfully'})

@bp.route('/menu', methods=['GET'])
def get_menu():
    items = MenuItem.query.all()
    return jsonify([{'name': item.name, 'price': item.price} for item in items])

bp.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)
