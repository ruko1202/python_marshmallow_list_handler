from typing import List

from marshmallow import fields, Schema, post_load


class User:
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name

    def __repr__(self):
        return 'User(code={self.phone!r}, name={self.name!r})'.format(self=self)

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.phone == other.phone and self.name == other.name


class UserSchema(Schema):
    phone = fields.String(data_key='phone_number')
    name = fields.String(data_key='user_name')

    @post_load
    def make_user(self, data):
        return User(**data)


class UserList:
    def __init__(self, user_list: List[User]):
        self.user_list = user_list

    def __repr__(self):
        return 'UserList(list={self.user_list!r})'.format(self=self)

    def __eq__(self, other):
        if not isinstance(other, UserList):
            return NotImplemented

        return self.user_list == other.user_list


class UserListSchema(Schema):
    user_list = fields.Nested(UserSchema, many=True, data_key='users')

    @post_load
    def make_user(self, data):
        return UserList(**data)
