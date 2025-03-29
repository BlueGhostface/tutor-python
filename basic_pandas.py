import pandas as pd


data = [[101, "Ulysses", 13], [53, "William", 10], [128, "Henry", 6],]

def createDataframe( inputDataframe ):
    column_names = ["student_id","name", "age"]
    data = pd.DataFrame(inputDataframe, columns=column_names) # create a dataframe with the data and column names
    return data

def getDataframeSize(inputDataframe):
    return [inputDataframe.shape[0], inputDataframe.shape[1]] # return the number of rows and columns

def selectFirstRows(inputDataframe):
    return inputDataframe.head(3) # select the first 3 rows

def selectSpecificData(inputDataframe):
    return inputDataframe.loc[inputDataframe['student_id'] == 101, ['name','age']] # select the name and age of the student with id 101

def createScoreColumn(inputDataframe):

    inputDataframe['score'] = [100, 200, 100] # create a new column called score
    return inputDataframe

def createtotalColumn(inputDataframe):
    inputDataframe['total'] = inputDataframe['score'] * 1.5 # multiply the score by 1.5
    return inputDataframe

def dropMissingData(inputDataframe):
    #first adding data with an emtpy field
    data = pd.DataFrame({"student_id": [7], "age": [10]})
    inputDataframe = pd.concat([inputDataframe, data])
    print("\n dataframe with empty data")
    print(inputDataframe)
    inputDataframe.dropna(subset=['name'], inplace=True)
    print("\n dataframe without empty data")
    print(inputDataframe)




def modifyScoreColumn(inputDF):
    inputDF['score'] = inputDF['score'] * 2
    return inputDF

def main():
    students = createDataframe(data)

    print("\nstudents")
    print(students)

    print("\nstudents size")
    print(getDataframeSize(students))

    print("\nfirst rows")
    print(selectFirstRows(students))

    print("\nselect data")
    print(selectSpecificData(students))

    print("\ncreate score column")
    print(createScoreColumn(students))

    print("\ncreate total column")
    print(createtotalColumn(students))

    print("\n drop name column")
    dropMissingData(students)

    print("\n modify score column")
    print(modifyScoreColumn(students))

main()