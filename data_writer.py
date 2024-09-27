import os
import pandas as pd


class data_file:
    def __init__(self):
        self.path = os.getcwd()
        self.namefile = 'data.txt'
        self.param_file = 'param.txt'

    def write_file(self):
        self.data.to_csv(self.param_file,
                         sep='\t',
                         index=False,
                         header=False)

    # Read the data from the txt  file with pandas
    def read_pandas(self):
        self.data = pd.read_csv(os.path.join(self.path, self.namefile))

    def change_variable(self, var, value):
        self.data.loc[self.data['Variable'] == var, 'Value'] = value


if __name__ == '__main__':
    data_piv = data_file()
    data_piv.read_pandas()
    column_names = data_piv.data.columns
    print(column_names)
    data_piv.change_variable('Input_typedata', 'TWO')
    data_piv.write_file()
