
# -------------------------------------------------------------------------------------
# name       : ExcelPandasOP()
# description: edit excel file via pandas module.
#
#              PP -> post processing
#
# date       : 20210810
# author     : garyhsieh
# -------------------------------------------------------------------------------------
class ExcelPandasOP:

    def __init__(self, _df):
        self.df = _df

    def get_col_header(self):
        columns = self.df.columns
        print(">>> show columns: %s" % columns)
        print(">>> show columns[0]: %s" % columns[0])
        print(">>> show columns[1]: %s" % columns[1])

    def get_col_nums(self):
        columns = self.df.columns
        num_columns = len(columns)
        print(">>> show num of columns: %d" % num_columns)

    def get_col_row_data(self, _col, _row):
        columns = self.df.columns

        #self.df[columns[0]][1]
        print(">>> show self.df[columns[%d]][%d]: %s" % (_col, _row, self.df[columns[_col]][_row]))
        print(">>> show len(self.df[columns[%d]]): %d" % (_col, len(self.df[columns[_col]])))
        for cell in self.df[columns[_col]]:
            print("show column cell: %s" % cell)

    def get_row_data(self, _row):
        for cell in self.df.loc[_row]:
            print("show row[%d] cell: %s" % (_row, cell))

    def modify_col_row_data(self, _col, _row, _cont):
        dc = self.df.columns
        print(">>> show dc[%d]: %s" % (_col, dc[_col]))
        print(">>> show self.df[dc[%d]][%d]: %s" % (0, 0, self.df[dc[0]][0]))
        print(">>> show self.df[dc[%d]][%d]: %s" % (0, 1, self.df[dc[0]][1]))
        self.df[dc[_col]][_row] = _cont
        print(">>> show after modify elf.df[dc[%d]][%d]: %s" % (_col, _row, self.df[dc[_col]][_row]))

    def get_idx_data(self, _idx):
        _idx_data = self.df.index[_idx]
        print(">>> show idx_data[%d]: %s" % (_idx, _idx_data))
    
    def get_idx_len(self):
        idx_len = len(self.df.index)
        print(">>> show idx len: %s" % idx_len)

if __name__ == "__main__":
    df_PP = ExcelPandasOP(df)
