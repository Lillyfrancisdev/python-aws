myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print('Print out each item in our list by their position')

print('1 = ',myFruitList[0])
print('2 = ',myFruitList[1])
print('3 = ',myFruitList[2])

print('Change cherry to orange')

myFruitList[2] = "orange"
print(myFruitList)

print('===============================')
print('Introducing the tuple data type')

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print('=============================')
print('Introducing the dictionary data type')

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print('Accessing a dictionary by name')

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
