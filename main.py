from DataHandler import DataHandler
from Utils import euclideanDistance, getNeighbors, performDemocracy, getAccuracy

trainingSet = []
testSet = []

DataHandler.getData(trainingSet, testSet)
predictions=[]
k = 5
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = performDemocracy(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
