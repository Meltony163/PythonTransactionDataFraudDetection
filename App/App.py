from DataManger.DataManger import DataManger
from TransactionCleaner.TransactionCleaner import TransactionCleaner
from FeatureBuilder.FeatureBuilder import FeatureBuilder
from RiskScorer.RiskScorer import RiskScorer
from ReportGenerator.ReportGenerator import ReportGenerator
from TransactionFlagger.TransactionFlagger import TransactionFlagger
import pandas as pd
class App(DataManger,TransactionCleaner,FeatureBuilder,RiskScorer,TransactionFlagger,ReportGenerator):
    def __init__(self, df=None):
        super().__init__(df)

    def GetNullsCountBeforeAndAfterTimestampConverstion(self,col):
        return (self.df[col].isnull().sum(),pd.to_datetime(self.df[col], errors='coerce', format='mixed').isnull().sum())

    def CheckForDataSet(self):
        if self.df is None:
            return False

        return True

    def GetNullPercentage(self,col):
        return self.df[col].isnull().sum()/self.df.shape[0]



