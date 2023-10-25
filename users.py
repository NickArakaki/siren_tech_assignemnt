from collections import deque


class User:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.favorite_movies = set()

    def add_friend(self, friend):
        """
            Add user to current user's friends set and add current user to other user's friends set
        """
        self.friends.add(friend)
        friend.friends.add(self)

    def remove_friend(self, friend):
        """
            If friend is on user's friends list, should remove them from
            cur user's friends list and remove cur user from other friend's list
        """
        friend.friends.discard(self)
        self.friends.discard(friend)

    def get_friends(self):
        """
            Return list of current users' friends
        """
        return list(self.friends)

    def add_favorite_movie(self, movie):
        """
            Should add movie to list of cur user's favorite movies set
        """
        self.favorite_movies.add(movie)

    def get_favorite_movies(self):
        """
            Should return list of user's favorite movies
        """
        return list(self.favorite_movies)

    def remove_favorite_movie(self, movie):
        """
            Should remove the movie from cur user's list of favorite movies if it exists.
        """
        self.favorite_movies.discard(movie)

    def get_network_movies(self):
        """
            Return favorite movies of every user in current user's network including friend of friends
        """
        queue = deque()
        queue.append(self)
        visited = set()
        visited.add(self)
        network_movies = {}

        while queue:
            user = queue.popleft()
            network_movies[user] = user.get_favorite_movies()
            for friend in user.get_friends():
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)

        return network_movies

    def get_network_favorite_movie(self):
        """
            Return the most popular movie among cur user's friend group,
            including friend of friends
        """
        # create dict to track num occurances of specific movie
        movie_counter = {}

        # run bfs on user's friends and friends of friends
        queue = deque()
        queue.append(self)
        visited = set()
        visited.add(self)

        while queue:
            user = queue.popleft()
            for movie in user.favorite_movies:
                movie_counter[movie] = movie_counter.get(movie, 0) + 1

            for friend in user.get_friends():
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)

        # return the key with the largest value
        return max(movie_counter, key=movie_counter.get)

    def __repr__(self) -> str:
        fav_movies = " ".join(self.get_favorite_movies())
        return f"{self.name}'s favorite movies are: {fav_movies}"
