"""
class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5) #meaning there are 5 seats in my car.
my_car.seats = 5
"""

class User:
    
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    
user_1 = User("001", "Valerie")
# print(user_1.id)
# print(user_1.username)
user_2 = User("002", "Hamid")
# print(user_2.id)
# print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)