from neural import *

print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")

readme_data = [
    ([0,0],[0]),
    ([0,1],[1]),
    ([1,0],[1]),
    ([1,1],[0])
]
john = NeuralNet(2,2,1)
john.train(readme_data)

john.test

print("")
print("<<<<<<<<<<< 8 HIDDEN NODES >>>>>>>>>>>\n")

jane = NeuralNet(2,8,1)
jane.train(readme_data)

print("")
print("<<<<<<<<<<< 1 HIDDEN NODES >>>>>>>>>>>\n")

jack = NeuralNet(2,1,1)
jack.train(readme_data)

print("")
print("<<<<<<<<<<<<  VOTER DATA  >>>>>>>>>>>>\n")

voter_data = [
    ([.9,.6,.8,.3,.1], [1]),
    ([.8,.8,.4,.6,.4], [1]),
    ([.7,.2,.4,.6,.3], [1]),
    ([.5,.5,.8,.4,.8], [0]),
    ([.3,.1,.6,.8,.8], [0]),
    ([.6,.3,.4,.3,.6], [0]),
]

voter_neurelnet = NeuralNet(5,10,1)
voter_neurelnet.train(voter_data)

voter_test = [
        [1,1,1,.1,1],
        [.5,.2,.1,.7,.7],
        [.8,.3,.3,.3,.8],
        [.8,.3,.3,.8,.3],
        [.9,.8,.8,.3,.6]
]

print(voter_neurelnet.test(voter_test))