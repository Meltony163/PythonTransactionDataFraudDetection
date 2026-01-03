from Parent.Parent import DataFrameParent

class FeatureBuilder(DataFrameParent):
    def AddTransactionCountPerCustomer(self,CustomersColumn):
        if self.df is None or CustomersColumn not in self.GetColumns():
            return 0

        self.df['TPC']=self.df.groupby(CustomersColumn).transform('size')

        return 1

    def AddTotalTransactionAmountPerCustomer(self,CustomersColumn,TransactionColumn):
        if self.df is None or CustomersColumn not in self.GetColumns() or TransactionColumn not in self.GetNumericalColumns():
            return 0

        self.df['TTAPC']=self.df.groupby(CustomersColumn)[TransactionColumn].transform('sum')

        return 1

    def AddMaxTransactionAmountPerCustomer(self,CustomersColumn,TransactionColumn):
        if self.df is None or CustomersColumn not in self.GetColumns() or TransactionColumn not in self.GetNumericalColumns():
            return 0

        self.df['MTAPC']=self.df.groupby(CustomersColumn)[TransactionColumn].transform('max')

        return 1

    def AddAverageTransactionAmountPerCustomer(self,CustomersColumn,TransactionColumn):
        if self.df is None or CustomersColumn not in self.GetColumns() or TransactionColumn not in self.GetNumericalColumns():
            return 0

        self.df['ATAPC']=self.df.groupby(CustomersColumn)[TransactionColumn].transform('mean')

        return 1

    def AddTransactionPerDay(self,CustomersColumn,DayColumn):
        if self.df is None or CustomersColumn not in self.GetColumns() or DayColumn not in self.GetColumns():
            return 0

        self.df['DTV'] = self.df.groupby([CustomersColumn, DayColumn]).transform('size')

        return 1