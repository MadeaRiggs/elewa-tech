#######OOP IN PYTHON
###CREATING CLASSES IN PYTHON

#creating a class holding human attributes
class human:

    #features
    feature_1= "legs"
    feature_2= "eyes"
    feature_3= "hands"
    feature_4= "dimples"

#creating an object
anne= human()
print(anne)

#to print a particular feature
print(anne.feature_1)

#creating class chicken
class chicken:

    #features
    feat_1= "feathers"
    feat_2= "thighs"
    feat_3= "wings"
    feat_4= "beak" 

    #activities
    act_1= "lay eggs"
    act_2= "crow"
    act_3= "sleep"

#create chicken object
chick= chicken()
print(chick.act_2)


#creating class car
class car:

    #car parts
    part_1= "dashboard"
    part_2= "wheels"
    part_3= "hood"
    part_4= "bumper"
    part_5= "brake shoe"
    part_6= "car engine"


    #car model
    model_1= "audi"
    model_2= "benz"
    model_3= "volvo"
    model_4= "toyota"
    model_5= "ford"
    model_6= "porshe"
    model_7= "bentley"

#creating object
car_mine= car()
print(car_mine.part_3)
print(car_mine.model_4)
