from collections import deque


class User:
    def __init__(self, name):
        self.name = name
        self.friends = set() # sets to prevent accidental duplicates, can be replaced with lists and some error handling
        self.favorite_movies = set()


    def add_friend(self, friend):
        """
            Add user to current user's friends set and add current user to other user's friends set
        """
        self.friends.add(friend)
        friend.friends.add(self)


    def add_favorite_movie(self, movie):
        """
            Should add movie to list of cur user's favorite movies set
        """
        self.favorite_movies.add(movie)


    def get_network_favorite_movie(self, degree=float("inf")):
        """
            Return the most popular movie among cur user's friend network, limited by n degree of separation
        """
        # create dict to track num occurances of specific movie
        movie_counter = {}

        # run bfs on user's friends and friends of friends
        queue = deque()
        queue.append((0, self))
        visited = {self}

        while queue:
            degree_from_start, user = queue.popleft()
            for movie in user.favorite_movies:
                movie_counter[movie] = movie_counter.get(movie, 0) + 1

            if degree_from_start < degree:
                for friend in user.friends:
                    if friend not in visited:
                        queue.append((degree_from_start + 1, friend))
                        visited.add(friend)

        # return the key with the largest value
        values = list(movie_counter.values())
        keys = list(movie_counter.keys())
        return keys[values.index(max(values))]


    def __repr__(self) -> str:
        fav_movies = " ".join(list(self.favorite_movies))
        return f"{self.name}'s favorite movies are: {fav_movies}"
