from App.App import App
from ConsoleApp.ConsoleApp import ConsoleApp
import pandas as pd


# ===================== Global Objects ===================== #
Mydf = App()
CA = ConsoleApp()


# ===================== Dataset ===================== #
def LoadDataset():
    Mydf.GetData('Data/bank_transactions_data_2.csv')
    CA.print_message('Data Loaded Successfully', (0, 255, 0))


# ===================== Data Cleaning ===================== #
def CleanData():
    if not Mydf.CheckForDataSet():
        CA.print_message('There Is No Data', (255, 0, 0))
        return

    MAIN_OPTIONS = [
        'Convert TimeStamp',
        'Handle Nulls',
        'Remove Duplicates',
        'Return'
    ]

    while True:
        main_choice = CA.output_screen(MAIN_OPTIONS)

        # -------- Convert Timestamp -------- #
        if main_choice == 0:
            categorical_columns = Mydf.GetCatigoricalColumns()+['Return']
            col_index = CA.output_screen(
                categorical_columns,
                'Choose Column To Convert To Time'
            )

            if col_index == len(categorical_columns)-1:
                return

            column_name = categorical_columns[col_index]

            nulls_before, nulls_after = (
                Mydf.GetNullsCountBeforeAndAfterTimestampConverstion(column_name)
            )

            confirm = CA.output_screen(
                ['Yes', 'No'],
                f'Nulls Before: {nulls_before} | After: {nulls_after}'
            )

            if confirm == 0:
                Mydf.ConvertTimeStamps(column_name)
                CA.print_message('Data Converted Successfully', (0, 255, 0))

        # -------- Handle Nulls -------- #
        elif main_choice == 1:
            while True:
                null_columns = Mydf.GetNullColumns()

                if not null_columns:
                    CA.print_message('There Are No Null Values', (0, 255, 0))
                    break

                null_columns.append('Return')
                selected = CA.output_screen(null_columns)
                column = null_columns[selected]

                if column == 'Return':
                    break

                null_percentage = Mydf.GetNullPercentage(column)

                if column in Mydf.GetCatigoricalColumns():
                    OPTIONS = [
                        'DropColumn',
                        'DropRows',
                        'ReplaceWithMode',
                        'DoNothing'
                    ]
                else:
                    OPTIONS = [
                        'DropColumn',
                        'DropRows',
                        'ReplaceWithMedian',
                        'ReplaceWithMean',
                        'ReplaceWithMode',
                        'DoNothing'
                    ]

                action = CA.output_screen(
                    OPTIONS,
                    f'Null Percentage: {null_percentage}%'
                )

                if OPTIONS[action] != 'DoNothing':
                    Mydf.CleanTheData(column, OPTIONS[action])

        # -------- Remove Duplicates -------- #
        elif main_choice == 2:
            Mydf.DropDuplicates()
            CA.print_message('Removed Duplicates Successfully', (0, 255, 0))

        else:
            return


# ===================== Feature Engineering ===================== #
def BuildFeature():
    if not Mydf.CheckForDataSet():
        CA.print_message('There Is No Data', (255, 0, 0))
        return

    MAIN_OPTIONS = [
        "AddTransactionCountPerCustomer",
        "AddTotalTransactionAmountPerCustomer",
        "AddMaxTransactionAmountPerCustomer",
        "AddAverageTransactionAmountPerCustomer",
        "AddTransactionPerDay",
        "Return"
    ]
    columns = [col for col in Mydf.GetColumns() if (col not in Mydf.GetZscoreColumns()) and (col not in Mydf.GetRiskBandColumns())]
    num_columns = [col for col in Mydf.GetNumericalColumns() if col not in Mydf.GetZscoreColumns()]
    while True:
        main_choice = CA.output_screen(MAIN_OPTIONS)

        if main_choice == 0:
            choice = CA.output_screen(columns, 'Select Customer Column')
            Mydf.AddTransactionCountPerCustomer(columns[choice])

        elif main_choice == 1:
            c_choice = CA.output_screen(columns, 'Select Customer Column')
            t_choice = CA.output_screen(num_columns, 'Select Transaction Column')
            Mydf.AddTotalTransactionAmountPerCustomer(
                columns[c_choice], num_columns[t_choice]
            )

        elif main_choice == 2:
            c_choice = CA.output_screen(columns, 'Select Customer Column')
            t_choice = CA.output_screen(num_columns, 'Select Transaction Column')
            Mydf.AddMaxTransactionAmountPerCustomer(
                columns[c_choice], num_columns[t_choice]
            )

        elif main_choice == 3:
            c_choice = CA.output_screen(columns, 'Select Customer Column')
            t_choice = CA.output_screen(num_columns, 'Select Transaction Column')
            Mydf.AddAverageTransactionAmountPerCustomer(
                columns[c_choice], num_columns[t_choice]
            )

        elif main_choice == 4:
            c_choice = CA.output_screen(columns, 'Select Customer Column')
            d_choice = CA.output_screen(columns, 'Select Date Column')
            Mydf.AddTransactionPerDay(columns[c_choice], columns[d_choice])

        else:
            return


# ===================== Scoring ===================== #
def ScoreCustomers():
    if not Mydf.CheckForDataSet():
        CA.print_message('There Is No Data', (255, 0, 0))
        return

    MAIN_OPTIONS = [
        "AddRiskScore",
        "AddRiskBandClassification",
        "Return"
    ]
    num_columns=[col for col in Mydf.GetNumericalColumns() if col not in Mydf.GetZscoreColumns()]+["Return"]
    while True:
        main_choice = CA.output_screen(MAIN_OPTIONS)

        if main_choice == 0:
            choice = CA.output_screen(num_columns, 'Select Risk Column')
            Mydf.AddRiskScore(num_columns[choice])

        elif main_choice == 1:
            choice = CA.output_screen(num_columns, 'Select Risk Band Column')
            Mydf.AddRiskBandClassification(num_columns[choice])

        else:
            return


# ===================== Flagging ===================== #
def FlagSuspiciousTransactions():
    if not Mydf.CheckForDataSet():
        CA.print_message('There Is No Data', (255, 0, 0))
        return

    columns = (
        Mydf.GetZscoreColumns()
        + Mydf.GetRiskBandColumns()
        + ['Return']
    )

    if len(columns) == 1:
        CA.print_message('There Is No Z-score Or Risk Band Columns', (255, 0, 0))
        return

    while True:
        choice = CA.output_screen(columns, "Select Column To Flag Based On")

        if choice == len(columns) - 1:
            return

        Mydf.FlagTransaction(columns[choice])
        CA.print_message('Flagged Successfully', (0, 255, 0))


# ===================== Export ===================== #
def ExportReports():
    if not Mydf.CheckForDataSet():
        CA.print_message('There Is No Data', (255, 0, 0))
        return

    MAIN_OPTIONS = [
        "GenerateReportAboutNumericalColumns",
        "ExportFlaggedTransaction",
        "ExportNumberOfSuspiciousTransactions",
        "ExportModifiedDataSet",
        "Return"
    ]

    while True:
        main_choice = CA.output_screen(MAIN_OPTIONS)

        if main_choice == 0:
            Mydf.ExportNumericalDataReport()

        elif main_choice == 1:
            if Mydf.FlaggedColumn == "":
                CA.print_message('There Is No Flagged Columns', (255, 0, 0))
            else:
                Mydf.ExportFlaggedTransaction()

        elif main_choice == 2:
            if Mydf.FlaggedColumn == "":
                CA.print_message('There Is No Flagged Columns', (255, 0, 0))
            else:
                Mydf.ExportNumberOfSuspiciousTransactions()

        elif main_choice == 3:
            Mydf.ExportModifiedDataSet()

        else:
            return

        CA.print_message('Exported Successfully', (0, 255, 0))


# ===================== Main Menu ===================== #
if __name__ == "__main__":

    MENU_OPTIONS = [
        "Load dataset(s)",
        "Clean data",
        "Build features",
        "Score customers",
        "Flag suspicious transactions",
        "Export reports",
        "Exit application"
    ]

    while True:
        choice = CA.output_screen(MENU_OPTIONS)

        if choice == 0:
            LoadDataset()
        elif choice == 1:
            CleanData()
        elif choice == 2:
            BuildFeature()
        elif choice == 3:
            ScoreCustomers()
        elif choice == 4:
            FlagSuspiciousTransactions()
        elif choice == 5:
            ExportReports()
        else:
            exit()
