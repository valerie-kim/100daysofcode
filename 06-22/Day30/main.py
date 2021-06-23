"""
try, except, else, finally
"""

#FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"Key": "Value"}
    print(a_dictionary["sdf"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

# except clauses can be implemented multiple times.
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
    
else: #if everything succeeds and no fails.
    content = file.read()
    print(content)

finally: #runs no matter what happens
    file.close()
    print("File was closed")


"""
Raise Exceptions
"""

height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / (height ** 2)
print(bmi)

#---------------------------IndexError----------------------------

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit Pie")
  else:
    print(fruit, "pie")

make_pie(2)

#---------------------------KeyError----------------------------
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
        # total_likes += 0

print(total_likes)