# -*- coding: utf-8 -*-

"""
This file is part of the Ingram Micro Cloud Blue Connect SDK.
Copyright (c) 2019 Ingram Micro. All Rights Reserved.
"""

from marshmallow import fields, post_load

from .base import BaseModel, BaseSchema


class Product(BaseModel):
    pass


class ProductSchema(BaseSchema):
    name = fields.Str()

    @post_load
    def make_object(self, data):
        return Product(**data)


class Item(BaseModel):
    pass


class ItemSchema(BaseSchema):
    global_id = fields.Str()
    mpn = fields.Str()
    old_quantity = fields.Integer()
    quantity = fields.Integer()

    @post_load
    def make_object(self, data):
        return Item(**data)
