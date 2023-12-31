############# Program to help you perform an activity of your choice when you are studying. 
# Activities done during studying are:
# Listen to music
# Google and Watch a tutorial or read article
# Take notes
# Take a break
# Eat a snack or drink water

##### input: mood, duration, deadline, topic
##### output: activity

# base class
class Study:
    def __init__(self):
        self.smood= ""
        self.sduration= 0
        self.sdeadline= ""
        self.stopic_level= ""

    #method to get mood
    def getMood(self):
        while True:
            try:
                mood= input("Enter your mood (happy/sad): ").strip().lower()
                if mood in ["happy", "sad"]:
                    self.smood= mood
                    if mood == "happy":
                        print("Listen to House music while studying")
                    else:
                        print("Listen to RnB music while studying")
                    break
            except ValueError:
                print("Invalid mood. Please select 'happy' or 'sad'")

        return self.smood

    #method to get duration
    def getDuration(self):
        while True:
            try:
                duration= int(input("Enter the number of hours you intend to study: "))
                if duration <= 0:
                    print("Invalid duration. Please enter a positive number.")
                elif duration > 0 and duration <= 2:
                    print("Take 20 mins of break in between the hours and drink water")
                elif duration > 2 and duration <= 4:
                    print("Take 30 mins of break in between the hours and eat a snack")
                else:
                    print("Take 1 hour of break in between the hours and cook a meal")
                self.sduration= duration
                break

            except ValueError:
                print("Invalid duration. Please enter a positive number.")
        return self.sduration
    
    #method to get deadline
    def getDeadline(self):
        while True:
            deadline = input("Enter the deadline of the activity (today/tomorrow): ").strip().lower()
            if deadline in ["today", "tomorrow"]:
                self.sdeadline = deadline
                break
            else:
                print("Invalid deadline. Please select 'today' or 'tomorrow'")
    
        return self.sdeadline

    def getTopic(self):
        while True:
            topic_level= input("Enter the topic level (beginner/intermediate/advanced): ").strip().lower()
            if topic_level in ["beginner", "intermediate", "advanced"]:
                self.stopic_level= topic_level
                break
            else:
                print("Invalid topic level. Please select 'beginner' or 'intermediate' or 'advanced'")
        
        return self.stopic_level
    
# derived class
class Activity(Study):

    #constructor
    def __init__(self):
        Study.__init__(self)
        self.activity=""

    # constructor
    def getTask(self):
        if self.sdeadline == "today":
            if self.stopic_level == "beginner":
                activity= "Studying activity is: Read personal notes while studying" 
            elif self.stopic_level == "intermediate":
                activity= "Studying activity is: Read an article while studying"
            else:
                activity= "Studying activity is: Use ChatGPT while studying" 
            
        else:
            if self.stopic_level == "beginner":
                activity= "Studying activity is: Watch a tutorial on Youtube while studying" 
            elif self.stopic_level == "intermediate":
                activity= "Studying activity is: Have a discussion with a friend while studying"
            else:
                activity= "Studying activity is: Go to the library and carry out further research while studying" 

        self.activity= activity
        return self.activity
    
# object
studying= Study()
studying= Activity()

#calling methods
print(studying.getMood())
print(studying.getDuration())
print(studying.getDeadline())
print(studying.getTopic())
print(studying.getTask())