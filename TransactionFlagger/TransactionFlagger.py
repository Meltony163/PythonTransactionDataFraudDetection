from Parent.Parent import DataFrameParent
import pandas as pd
class TransactionFlagger(DataFrameParent):
    def FlagTransaction(self,col):
        if self.df is None or (col not in self.GetZscoreColumns() and col not in self.GetRiskBandColumns()) :
            return 0

        if self.FlaggedColumn=='':
            columns=self.GetColumns()
            ColName='GeneratedFlag'
            if ColName in columns:
                while ColName in columns:
                    i=0
                    ColName=f'GeneratedFlag{i}'
                    i+=1

            self.FlaggedColumn=ColName
            self.df[self.FlaggedColumn]=False

        if col in self.GetZscoreColumns():
            self.df[self.FlaggedColumn]=self.df[self.FlaggedColumn] | (self.df[col] > 3.0)

        else:
            self.df[self.FlaggedColumn] = self.df[self.FlaggedColumn] | (self.df[col] == "Critical")



