import pandas
import numpy

# create numpy array
data = numpy.array([[1, 4], [2, 5], [3, 6]])

# data frame
panda = pandas.DataFrame(data, index=["row1", "row2", "row3"], columns=["col1", "col2"])

# show in the terminal
print(panda)


# now the same with a list
state = [
    "Arizona",
    "California",
    "Nevada",
]
population = ["60mil", "2mil", "30mil"]
dict_states = {"States": state, "Fake Population": population}


panda = pandas.DataFrame(dict_states)

print(panda)
