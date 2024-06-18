import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Menu, Item
from app import db

class MenuType(SQLAlchemyObjectType):
    class Meta:
        model = Menu

class ItemType(SQLAlchemyObjectType):
    class Meta:
        model = Item

class CreateMenu(graphene.Mutation):
    menu = graphene.Field(MenuType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, name, description=None):
        menu = Menu(name=name, description=description)
        db.session.add(menu)
        db.session.commit()
        return CreateMenu(menu=menu)

class AddItem(graphene.Mutation):
    item = graphene.Field(ItemType)

    class Arguments:
        menu_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Float(required=True)
        category = graphene.String(required=True)
        image_url = graphene.String()

    def mutate(self, info, menu_id, name, description, price, category, image_url=None):
        menu = Menu.query.get(menu_id)
        if not menu:
            raise ValueError("Menu not found")

        item = Item(name=name, description=description, price=price, category=category, image_url=image_url, menu_id=menu.id)
        db.session.add(item)
        db.session.commit()
        return AddItem(item=item)

class Query(graphene.ObjectType):
    menu = graphene.Field(MenuType, id=graphene.Int())
    menus = graphene.List(MenuType)
    items = graphene.List(ItemType, menu_id=graphene.Int())

    def resolve_menu(self, info, id):
        return Menu.query.get(id)

    def resolve_menus(self, info):
        return Menu.query.all()

    def resolve_items(self, info, menu_id):
        return Item.query.filter_by(menu_id=menu_id).all()

class Mutation(graphene.ObjectType):
    create_menu = CreateMenu.Field()
    add_item = AddItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
