from instapy import InstaPy
from instapy import smart_run

my_username = 'jarvis_yvetal'
my_password = 'jarvisfridaym46'

session = InstaPy(username = my_username,
                  password = my_password,
                  headless_browser = False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=500,
                                    min_followers=30,
                                    min_following=50)

    session.like_by_tags(['anime','cars','4k'],amount=50)