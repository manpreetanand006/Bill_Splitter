import random
friends_dict = {}
number_of_friends = int(input("Enter the number of friends joining (including you):"))

if number_of_friends <= 0:
      print("No one is joining for the party!")

elif number_of_friends >=20:
      print("Maximum number of friends cannot be more than 20")

else:
      print("Enter the name of every friend (including you) each on a new line:")
      for i in range(number_of_friends):
            name = input()
            friends_dict[name] = 0


      total_bill_value = int(input("Enter the total Bill Value: "))


      while True :
            lucky_feature = input('Do you want to use the "Who is Lucky" feature? Write Yes/No: ').lower()

            if lucky_feature == "no":
                  print("No one is going to be lucky!")
                  split_bill_value = round(total_bill_value / number_of_friends, 2)
                  friends_dict = {key : split_bill_value for key in friends_dict}
                  print(friends_dict)
                  break

            elif lucky_feature == "yes":
                  random_bill_value = round(total_bill_value / (number_of_friends -1), 2)
                  lucky_person = random.choice(list(friends_dict.keys()))   
                  print(lucky_person, "is the lucky one!")
                  for key in friends_dict:
                        if key == lucky_person:
                              friends_dict[key] = 0
                        else: 
                              friends_dict[key] = random_bill_value
                  print(friends_dict)
                  break

            else:
                  print('Please reply with "Yes" or "No"')
            
