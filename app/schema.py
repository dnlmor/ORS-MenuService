# app/schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Dish as DishModel
from .resolvers import (
    resolve_create_dish, resolve_update_dish, resolve_delete_dish,
    resolve_get_dish, resolve_list_dishes
)

class Dish(SQLAlchemyObjectType):
    class Meta:
        model = DishModel

class Query(graphene.ObjectType):
    get_dish = graphene.Field(Dish, id=graphene.Int(required=True))
    list_dishes = graphene.List(Dish)

    def resolve_get_dish(self, info, id):
        return resolve_get_dish(info, id)

    def resolve_list_dishes(self, info):
        return resolve_list_dishes(info)

class CreateDish(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)

    dish = graphene.Field(lambda: Dish)

    def mutate(self, info, name, description, price):
        return resolve_create_dish(info, name, description, price)

class UpdateDish(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()
        price = graphene.Float()

    dish = graphene.Field(lambda: Dish)

    def mutate(self, info, id, name=None, description=None, price=None):
        return resolve_update_dish(info, id, name, description, price)

class DeleteDish(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        return resolve_delete_dish(info, id)

class Mutation(graphene.ObjectType):
    create_dish = CreateDish.Field()
    update_dish = UpdateDish.Field()
    delete_dish = DeleteDish.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
