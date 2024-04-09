class MovieGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, movie, actor):
        # Add edge between movie and actor
        if movie not in self.graph:
            self.graph[movie] = []
        self.graph[movie].append(actor)
        # Add edge between actor and movie
        if actor not in self.graph:
            self.graph[actor] = []
        self.graph[actor].append(movie)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", ", ".join(map(str, self.graph[node])))

# Example usage
if __name__ == "__main__":
    # Create a movie graph object
    movie_graph = MovieGraph()

    # Add edges (movies and actors)
    movie_graph.add_edge("The Shawshank Redemption", "Tim Robbins")
    movie_graph.add_edge("The Shawshank Redemption", "Morgan Freeman")
    movie_graph.add_edge("The Godfather", "Marlon Brando")
    movie_graph.add_edge("The Godfather", "Al Pacino")
    movie_graph.add_edge("The Godfather", "James Caan")
    movie_graph.add_edge("The Dark Knight", "Christian Bale")
    movie_graph.add_edge("The Dark Knight", "Heath Ledger")

    # Print the movie graph
    movie_graph.print_graph()
