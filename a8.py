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

john.test(readme_data)
print("<<<<<<<<<<<<<<<<<[]>>>>>>>>>>>>>>>>>\n")

jane = NeuralNet(2,8,1)
jane.train(readme_data)

jane.test(readme_data)