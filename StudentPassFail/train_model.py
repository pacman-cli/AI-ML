from copyreg import pickle
from sklearn.neural_network import MLPClassifier
import pickle #-> save trained model in a file

#training data
x=[
    [2,60], #[hoursStudied, attendance]
    [4,65],
    [6,75],
    [8,85],
    [10,90]
]

#labels (expected output) (0=fail, 1=pass)
y=[
    0,
    0,
    1,
    1,
    1
]

#create the neural network
model = MLPClassifier(
    hidden_layer_sizes=(5,), #-> one hidden layer with 5 neurons
    activation='relu', #non-linear activation function(non-linear learning)
    max_iter=2000 #-> training iterations
)

# train the model
model.fit(x,y)

# save the trained
with open("student_pass_model.pkl","wb") as file: # wb -> write binary
    pickle.dump(model,file) #-> save the model to a file
