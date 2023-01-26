import json

f1 = open('following.json')
f2 = open('following.json')

followingJson = json.load(f1)
followsJson = json.load(f2)

followingSet = {}

for following in followingJson["relationships_following"]:
        followingSet.add(following["string_list_data"][0]["value"])

for follower in followsJson["relationships_followers"]:
        if follower["string_list_data"][0]["value"] in followingSet:
                followingSet.remove(follower["string_list_data"][0]["value"])


for user in followingSet:
        print(user)