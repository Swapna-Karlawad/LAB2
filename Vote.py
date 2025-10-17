def check_voting_eligibility():
    try:
      age = int(input("Enter your age:"))
      if age >=18:
        print("you are eligible to vote.")
      else:
        print("you are not eligible to vote.")
    except valueError:
       print("Invalid input.Please enter valid input")
if__name__=="__main__"
  check_voting_eligibility()
