class DataFrameParent:
    def __init__(self, df=None):
        self.df = df
        self.ZscoreColumns=[]
        self.RiskBandColumns=[]
        self.FlaggedColumn=''

    def GetColumns(self):
        if self.df is None:
            return 0
        return list(self.df.columns)

    def GetNullColumns(self):
        if self.df is None:
            return 0
        return list(self.df.columns[self.df.isnull().sum() > 0])

    def GetNumericalColumns(self):
        if self.df is None:
            return 0
        return list(self.df.select_dtypes(include='number').columns)

    def GetCatigoricalColumns(self):
        if self.df is None:
            return 0
        return list(self.df.select_dtypes(include=['object', 'category']).columns)

    def GetRiskBandColumns(self):
        if self.df is None:
            return 0
        return self.RiskBandColumns

    def GetZscoreColumns(self):
        if self.df is None:
            return 0
        return self.ZscoreColumns