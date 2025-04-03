import pandas as pd


student_data = [[101, "Ulysses", 13], [53, "William", 10], [128, "Henry", 6],]

student_column_names = ["student_id","name", "age"]

product_data = [["salt",100, 2, 3],["sugar",200, 5, pd.NA],["pepper", 10, 5, pd.NA]]
product_column_names = ["product_name", "quantity", "price", "in_stock"]

student_data2 = [[101, "Marcus", 17, 100.0], [53, "Wilson", 15, 95.0], [128, "Tom", 19, 65.0],]
student_column_names2 = ["student_id","name", "age", "score"]

def createDataframe( inputDataframe, column_names):

    data = pd.DataFrame(inputDataframe, columns=column_names) # create a dataframe with the data and column names
    return data

def getDataframeSize(inputDataframe):
    return [inputDataframe.shape[0], inputDataframe.shape[1]] # return the number of rows and columns

def selectFirstRows(inputDataframe):
    return inputDataframe.head(3) # select the first 3 rows

def selectSpecificData(inputDataframe):
    return inputDataframe.loc[inputDataframe['student_id'] == 101, ['name','age']] # select the name and age of the student with id 101

def createScoreColumn(inputDataframe):

    inputDataframe['score'] = [100.0, 200.0, 100.0] # create a new column called score
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


def renameColumns(students):
    students = students.rename(
        columns={
            "id": "student_id",
            "name": "first_name",
            "age": "age_in_years",
            "score": "points"
        }
    )
    return students


def changeDatatype(students):
    students['score'] = students['score'].astype(int)
    return students


def fillMissingValues(products):

    # products['in_stock'].fillna(0, inplace=True)
    products.fillna({'in_stock': 0}, inplace=True)
    return products


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame):
    return pd.concat([df1, df2], axis=0)



def main():
    students = createDataframe(student_data , student_column_names)
    products = createDataframe(product_data , product_column_names)
    students2 = createDataframe(student_data2, student_column_names2)



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

    print("\n rename columns")
    print(renameColumns(students))

    print("\n change datatype")
    print(students['score'])
    print(changeDatatype(students))
    print(students['score'])


    print("\n fill missing values")
    print(products)
    print("now filling vallues")
    print(fillMissingValues(products))
    print(products)


    print("\n concatenate tables")
    print(concatenateTables(students, students2))
main()