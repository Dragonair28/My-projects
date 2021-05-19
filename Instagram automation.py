from instapy import InstaPy

session = InstaPy(username = "jarvis_yvetal", password = "jarvisfridaym46")
session.login()

session.set_relationship_bounds(enabled = True,  max_followers = 200)

session.like_by_tags(['anime','cars','4k'], amount = 20)

session.end()