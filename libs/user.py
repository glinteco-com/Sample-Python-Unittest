from libs.facebook_api import FacebookAPI


def is_registered_user(username):
    user_info = FacebookAPI().get_userinfo(username)
    return user_info != {}
