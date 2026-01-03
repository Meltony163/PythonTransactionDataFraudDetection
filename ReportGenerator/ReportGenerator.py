from Parent.Parent import DataFrameParent
import pandas as pd
class  ReportGenerator(DataFrameParent):
    def ExportNumericalDataReport(self):
        if self.df is None:
            return 0

        pd.DataFrame(self.df.describe()).to_csv('Reports/NumericalReport.csv')
        return 1

    def ExportFlaggedTransaction(self):
        if self.df is None or self.FlaggedColumn=='':
            return 0

        self.df[self.df[self.FlaggedColumn]==1].to_csv("Reports/FlaggedTransaction.csv")
        return 1

    def ExportNumberOfSuspiciousTransactions(self):
        if self.df is None or self.FlaggedColumn=='':
            return 0

        F=open("Reports/NumberOfFlaggedTransaction",'w')
        F.write(f"Number of Flagged Transaction is {self.df[self.df[self.FlaggedColumn]==1].shape[0]} out of {self.df.shape[0]}")
        return 1

    def ExportModifiedDataSet(self):
        if self.df is None:
            return 0

        self.df.to_csv("Reports/ModifedDataFrame,csv")
        return 1