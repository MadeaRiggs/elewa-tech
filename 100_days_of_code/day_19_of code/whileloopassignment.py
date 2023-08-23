# List of candidates
# candidates = ["Candidate A", "Candidate B", "Candidate C", "Candidate D"]

# a) Interview Process
person = 1
while person < 10:
    print("Interviewing", person)
    person += 1

# b) Candidate Evaluation
person = 1
while person < 10:
    # Evaluation criteria and scoring
    if person == 1:
        score = 80
    elif person == 2:
        score = 75
    else:
        score = 70
    print(person, "score:", score)
    person += 1

# c) Decision Making
person = 1
while person < 10:
    if person == 1:
        print("Person ", person, "is selected!")
    else:
        print("Person ", person, "is not selected.")
    person += 1

# d) Sending Notifications
person = 1
while person < 10:
    if person == 1:
        print("Sending congrats notification to person ", person)
    else:
        print("Sending regrets notification to person ", person)
    person += 1
