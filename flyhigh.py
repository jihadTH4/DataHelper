import pandas as pd

class DataHelper:
    
    def convert(self, data_frame: pd.DataFrame, file_name: str, file_type: str) -> None:
        # The extension of the file should be with its name
        if file_type == "csv":
            data_frame.to_csv(file_name + ".csv", index=False)
            print("Your CSV file is Done")
        elif file_type == "excel":
            data_frame.to_excel(file_name + ".xlsx", index=False)
            print("Your Excel file is Done")
        else:
            print(f"<!> Sorry, There is no extension called {file_type} <!>")
    def read_csv(self, file_name: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_name + ".csv")
        except FileNotFoundError:
            print(f"<!> File {file_name}.csv not found <!>")
            return None

    def read_excel(self, file_name: str) -> pd.DataFrame:
        try:
            return pd.read_excel(file_name + ".xlsx")
        except FileNotFoundError:
            print(f"<!> File {file_name}.xlsx not found <!>")
            return None

    def analyze_data(self, data_frame: pd.DataFrame) -> None:
        print("Basic Statistics:")
        print(data_frame.describe())

# Example usage:
my_data = {
    "Name": ["Jihad", "Ahmed"],
    "Age": [19, 18]
}

myDf = pd.DataFrame(my_data) 
DH = DataHelper()

xlsx = DH.read_excel("C:\\Users\HP\\OneDrive\\Desktop\\testy")
print(xlsx)
print("="*60)
print(DH.analyze_data(xlsx))
print("="*60)

