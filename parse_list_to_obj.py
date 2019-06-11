from typing import List

from marshmallow import fields, Schema, post_load


class User:
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name

    def __repr__(self):
        return 'Okved(code={self.phone!r}, name={self.name!r})'.format(self=self)


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


class UserListSchema(Schema):
    user_list = fields.Nested(UserSchema, many=True, data_key='users')

    @post_load
    def make_user(self, data):
        return UserList(**data)


user1 = {'phone_number': '9998887766', 'user_name': 'user_name 9998887766'}
user2 = {'phone_number': '9998886655', 'user_name': 'user_name 9998886655'}
user_dict = dict(users=[user1, user2])

user_list_schema = UserListSchema()

user_list_obj = user_list_schema.load(user_dict)
print(type(user_list_obj), user_list_obj)
users_dict = user_list_schema.dump(user_list_obj)
print(type(users_dict), users_dict)
