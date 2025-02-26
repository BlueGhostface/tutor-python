import pandas as pd


data = [[101, "Ulysses", 13], [53, "William", 10], [128, "Henry", 6], [3, "Henry", 11]]

def createDataframe( inputDataframe ):
    column_names = ["student_id","name", "age"]
    data = pd.DataFrame(inputDataframe, columns=column_names)
    return data

def getDataframeSize(inputDataframe):
    return [inputDataframe.shape[0], inputDataframe.shape[1]]

def selectFirstRows(inputDataframe):
    return inputDataframe.head(3)

def selectSpecificData(inputDataframe):
    return inputDataframe.loc[inputDataframe['student_id'] == 101, ['name','age']]





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

main()