from Parent.Parent import DataFrameParent
import pandas as pd
class TransactionCleaner(DataFrameParent):
    def CleanTheData(self, column, null_handling):
        if self.df is None:
            return 0


        if column not in self.GetColumns():
            return 0

        if null_handling == 'DropColumn':
            self.df.drop(columns=[column], inplace=True)

        elif null_handling == 'DropRows':
            self.df.dropna(subset=[column], inplace=True)

        elif null_handling == 'ReplaceWithMedian':
            self.df[column]=self.df[column].fillna(self.df[column].median())

        elif null_handling == 'ReplaceWithMean':
            self.df[column]=self.df[column].fillna(self.df[column].mean())

        elif null_handling == 'ReplaceWithMode':
            print("HII")
            self.df[column]=self.df[column].fillna(self.df[column].mode()[0])

        else:
            return 0

        return 1

    def ConvertTimeStamps(self,col):
        self.df[col]=pd.to_datetime(self.df[col], errors='coerce', format='mixed').dt.date

    def DropDuplicates(self):
        self.df.drop_duplicates(inplace=True)
