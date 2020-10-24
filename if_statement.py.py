#Name: Ana Timpano
#Course Code: ICS3U
#Description: An applicaion that will determine if a person is old enough to vote.

#Get the users voting age
voteage = int(input("Enter your age: "))

#Make a decision to determine if they are eligible to vote
if (voteage >= 18):
    print("You are eligible to vote.")
else:
    print("You are not old enough to vote.")
