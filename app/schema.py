import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import MenuItem as MenuItemModel
from app import db

class MenuItem(SQLAlchemyObjectType):
    class Meta:
        model = MenuItemModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_menu_items = SQLAlchemyConnectionField(MenuItem.connection)

schema = graphene.Schema(query=Query)
