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

# add movies to Users
Alice.add_favorite_movie("Toy Story")
Alice.add_favorite_movie("Jumanji")
Alice.add_favorite_movie("Heat")
Alice.add_favorite_movie("The Princess Bride")
Alice.add_favorite_movie("The Pirates of the Caribbean")

Bob.add_favorite_movie("The Lord of the Rings: Fellowship of the Ring")
Bob.add_favorite_movie("The Lord of the Rings: Return of the King")
Bob.add_favorite_movie("The Lord of the Rings: The Two Towers")
Bob.add_favorite_movie("The Princess Bride")
Bob.add_favorite_movie("Harry Potter and the Prisoner of Azkaban")

Charlie.add_favorite_movie("John Wick")
Charlie.add_favorite_movie("John Wick Chapter 2")
Charlie.add_favorite_movie("John Wick Chapter 3")
Charlie.add_favorite_movie("Crouching Tiger, Hidden Dragon")
Charlie.add_favorite_movie("Everything, Everywhere, All At Once")

Dan.add_favorite_movie("Spiderman Into the Spiderverse")
Dan.add_favorite_movie("Avengers Infinity War")
Dan.add_favorite_movie("Avengers Endgame")
Dan.add_favorite_movie("Spiderman Across the Spiderverse")
Dan.add_favorite_movie("Harry Potter and the Prisoner of Azkaban")

Grace.add_favorite_movie("Spirited Away")
Grace.add_favorite_movie("My Neighbor Totoro")
Grace.add_favorite_movie("Kiki's Delivery Service")
Grace.add_favorite_movie("Your Name")
Grace.add_favorite_movie("Suzume")

Frank.add_favorite_movie("Young Frankenstein")
Frank.add_favorite_movie("Blazing Saddle")
Frank.add_favorite_movie("Spaceballs")
Frank.add_favorite_movie("Robin Hood: Men in Tights")
Frank.add_favorite_movie("The Producers")

Heidi.add_favorite_movie("Spirited Away")
Heidi.add_favorite_movie("My Neighbor Totoro")
Heidi.add_favorite_movie("Everything Everywhere All At Once")
Heidi.add_favorite_movie("The Princess Bride")

# Add establish friendships
Alice.add_friend(Erin)
Alice.add_friend(Charlie)
Alice.add_friend(Bob)
Bob.add_friend(Dan)
Dan.add_friend(Grace)
Grace.add_friend(Frank)
Grace.add_friend(Heidi)


print(Alice.get_network_favorite_movie(3))
