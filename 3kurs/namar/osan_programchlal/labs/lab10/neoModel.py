from neomodel import config, StructuredNode, StringProperty, RelationshipTo, RelationshipFrom

config.DATABASE_URL = 'bolt://neo4j:admin123@localhost:7687'

class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    friends = RelationshipTo("Person", "FRIENDS_WITH")

alice = Person(name="Alice").save()
bob = Person(name="Bob").save()

alice.friends.connect(bob)

for friend in alice.friends.all():
    print(friend.name)
