from users import User
from random import choice, randrange

# Init User Objects
Alice = User("Alice")
Bob = User("Bob")
Charlie = User("Charlie")
Dan = User("Dan")
Erin = User("Erin")
Frank = User("Frank")
Grace = User("Grace")
Heidi = User("Heidi")
Mike = User("Mike")
Nick = User("Nick")
Olivia = User("Olivia")
Patty = User("Patty")
Ralph = User("Ralph")
Sam = User("Sam")
Trudy = User("Trudy")
Victor = User("Victor")
Walter = User("Walter")

users_list = [Alice, Bob, Charlie, Dan, Erin, Frank, Grace, Heidi,
              Mike, Nick, Olivia, Patty, Ralph, Sam, Trudy, Victor, Walter]


# Generate List of Movies
movies_list = []
with open("movies.txt", "r") as movies:
    for movie in movies:
        movies_list.append(movie.strip())


# Seed Users and Establish Relationships
for user in users_list:
    for _ in range(3, 15):
        user.add_favorite_movie(choice(movies_list))
    for _ in range(5):
        user.add_friend(
            choice([friend for friend in users_list if friend != user]))


print(Nick.get_network_movies())
print("==========================")
print(Nick.get_network_favorite_movie())
