class User:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.favorite_movies = set()


    def add_friend(self, friend):
        """
            If not already friends, should add friend to cur user's
            friends list and add cur user to friend's list
        """
        if friend not in self.friends:
            self.friends.add(friend)
            friend.friends.add(self)
        else:
            return f'{friend.name} is already your friend'


    def remove_friend(self, friend):
        """
            If friend is on user's friends list, should remove them from
            cur user's friends list and remove cur user from other friend's list
        """
        friend.friends.discard(self)
        self.friends.discard(friend)


    def add_favorite_movie(self, movie):
        """
            Should add movie to list of cur user's favorite movies list, if not already
            there
        """


    def remove_favorite_movie(self, movie):
        """
            Should remove the movie from cur user's list of favorite movies if it exists.
            If not, should return str 'Movie not found in your favorite movie list'
        """
        if movie in self.favorite_movies:
            self.favorite_movies.remove(movie)
            return f'{movie} was successfully removed from your favorite movies list'
        else:
            return f'{movie} could not be found in your list of favorite movies'


    def get_network_favorite_movie(self):
        """
            Return the most popular movie among cur user's friend group,
            including friend of friends (1 degree of separation)
        """