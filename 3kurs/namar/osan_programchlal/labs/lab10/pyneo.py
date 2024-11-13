from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", auth=("neo4j", "admin123"))

# graph.delete_all()

alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")

friends_with = Relationship(alice, "FRIENDS_WITH_Neo", bob)

graph.create(alice | bob | friends_with)

result = graph.run("MATCH (p:Person) RETURN p.name AS name").data()
print(result)
