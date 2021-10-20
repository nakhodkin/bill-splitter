import random


# write your code here
print("Enter the number of friends joining (including you):")
number_of_people = int(input())

if number_of_people > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    friend_names = [input() for _ in range(number_of_people)]

    print("Enter the total bill value:")
    bill_value = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature = input()

    friends = dict.fromkeys(friend_names, 0.0)

    if lucky_feature == "Yes":
        lucky_one = random.choice(friend_names)
        friend_names.remove(lucky_one)
        print(f"{lucky_one} is the lucky one!")
    else:
        print("No one is going to be lucky")

    bill_value_mean = round(bill_value / len(friend_names), 2)
    bill_payers = dict.fromkeys(friend_names, bill_value_mean)
    friends.update(bill_payers)

    print(friends)
else:
    print("No one is joining for the party")
