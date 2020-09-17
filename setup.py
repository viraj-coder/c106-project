import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    student marks=[]  
    days present=[]
    with open(data_path)as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            studentmarks.append(float(row["Student Marks"]))
            dayspresent.append(float(row["\t Days present"]))

    return{"x":studentmarks,"y":dayspresent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between student marks and number of days present- \n--->",correlation[0,1])

def setup():
    data_path="/Student marks,_Days present.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()
