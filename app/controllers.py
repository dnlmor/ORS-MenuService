# app/controllers.py
from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

menu_blueprint = Blueprint('menu', __name__)

menu_blueprint.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
