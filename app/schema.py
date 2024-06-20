import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Menu as MenuModel, Item as ItemModel

class Menu(SQLAlchemyObjectType):
    class Meta:
        model = MenuModel
        interfaces = (graphene.relay.Node, )

class Item(SQLAlchemyObjectType):
    class Meta:
        model = ItemModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_menus = SQLAlchemyConnectionField(Menu.connection)
    all_items = SQLAlchemyConnectionField(Item.connection)

schema = graphene.Schema(query=Query)
