from Parent.Parent import DataFrameParent
from scipy.stats import zscore

class RiskScorer(DataFrameParent):
    def AddRiskScore(self,col):
        if self.df is None or col not in self.GetNumericalColumns():
            return 0

        self.df[f'ZscoreFor{col}']=zscore(self.df[col])
        if f'ZscoreFor{col}' not in self.ZscoreColumns:
            self.ZscoreColumns.append(f'ZscoreFor{col}')
        return 1

    @staticmethod
    def __classify_risk(z):
        z = abs(z)
        if z < 1:
            return "Low"
        elif z < 2:
            return "Medium"
        elif z < 3:
            return "High"
        else:
            return "Critical"
    def AddRiskBandClassification(self,col):
        if self.df is None or col not in self.GetNumericalColumns():
            return 0

        self.df[f'RiskBandFor{col}']=zscore(self.df[col])
        self.df[f'RiskBandFor{col}']=self.df[f'RiskBandFor{col}'].apply(self.__classify_risk)
        if f'RiskBandFor{col}' not in self.RiskBandColumns:
            self.RiskBandColumns.append(f'RiskBandFor{col}')
        return 1