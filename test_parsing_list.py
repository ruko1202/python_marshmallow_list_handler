from hamcrest import assert_that, equal_to

from parse_list_to_obj import UserListSchema, User, UserSchema, UserList


def test_parse_user_to_object():
    user_schema = UserSchema()

    user = User(phone='9998887766', name='user_name 9998887766')
    user_dict = {'phone_number': '9998887766', 'user_name': 'user_name 9998887766'}
    user_obj = user_schema.load(user_dict)
    assert_that(user_obj, equal_to(user))

def test_parse_dict_with_list_to_objects_list():
    user_list_schema = UserListSchema()

    user1 = User(phone='9998887766', name='user_name 9998887766')
    user2 = User(phone='9998886655', name='user_name 9998886655')
    users = UserList([user1, user2])

    user_dict1 = {'phone_number': '9998887766', 'user_name': 'user_name 9998887766'}
    user_dict2 = {'phone_number': '9998886655', 'user_name': 'user_name 9998886655'}
    user_dict = dict(users=[user_dict1, user_dict2])
    users_list = user_list_schema.load(user_dict)

    assert_that(users_list, equal_to(users))



