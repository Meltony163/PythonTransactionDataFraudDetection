import pandas as pd
from Exception.Exception import  DataManagerFailed
from Parent.Parent import DataFrameParent


class DataManger(DataFrameParent):

    def __init__(self, df=None):
        super().__init__(df)
    def GetData(self,path):
        try:
            self.df=pd.read_csv(path)
        except:
            raise DataManagerFailed("Can't Load Data")
    def PrintData(self):
        print(self.df.head())