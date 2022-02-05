
# -------------------------------------------------------------------------------------
# name       : ExcelPandasOP()
# description: edit excel file via pandas module.
#
#              PP -> post processing
#
# row_idx | col_idx0    col_idx1    ... ...
# -------------------------------------------------------------------------------------
# 0       | value       value       ... ...
# 1       | value       value       ... ...
# 2       | value       value       ... ...
# .       | value       value       ... ...
# .       | value       value       ... ...
# .       | value       value       ... ...
#
#
# date       : 20210810
# author     : garyhsieh
# -------------------------------------------------------------------------------------
class ExcelPandasOP:

    def __init__(self, _df):
        self.df = _df
    
    # 得到column idx的值．
    def get_col_header(self):
        columns = self.df.columns
        print(">>> show columns: %s" % columns)
        print(">>> show columns[0]: %s" % columns[0])
        print(">>> show columns[1]: %s" % columns[1])

    def get_info_df(self):
        self.df.info()

    def show_NaN_status(self):
        NaN_status = self.df.isnull()
        print(">>> show NaN status: %s" % NaN_status)

    # 得到總共有幾的column idx 
    def get_col_nums(self):
        columns = self.df.columns
        num_columns = len(columns)
        print(">>> show num of columns: %d" % num_columns)

    def get_row_col_size(self):
        row_col_shape = self.df.shape
        print(">>> show row x col shape: %s x %s" % row_col_shape)

    # 針對每個column去取得值，由指定的column上到下去取得值．
    def get_col_row_data(self, _col, _row):
        columns = self.df.columns

        #self.df[columns[0]][1]
        print(">>> show self.df[columns[%d]][%d]: %s" % (_col, _row, self.df[columns[_col]][_row]))
        print(">>> show len(self.df[columns[%d]]): %d" % (_col, len(self.df[columns[_col]])))
        for cell in self.df[columns[_col]]:
            print("show column cell: %s" % cell)

    # 從指定列由左至右抓取值． 
    def get_row_data(self, _row):
        for cell in self.df.loc[_row]:
            print("show row[%d] cell: %s" % (_row, cell))

    # 修改指定column與row的值．
    def modify_col_row_data(self, _col, _row, _cont):
        dc = self.df.columns
        print(">>> show dc[%d]: %s" % (_col, dc[_col]))
        print(">>> show self.df[dc[%d]][%d]: %s" % (0, 0, self.df[dc[0]][0]))
        print(">>> show self.df[dc[%d]][%d]: %s" % (0, 1, self.df[dc[0]][1]))
        self.df[dc[_col]][_row] = _cont
        print(">>> show after modify elf.df[dc[%d]][%d]: %s" % (_col, _row, self.df[dc[_col]][_row]))
        print(">>> show df: %s" % self.df)

    # 抓取row idx的值．
    def get_idx_data(self, _idx):
        _idx_data = self.df.index[_idx]
        print(">>> show idx_data[%d]: %s" % (_idx, _idx_data))

    # 抓取總共有多少的列
    def get_idx_len(self):
        idx_len = len(self.df.index)
        print(">>> show idx len: %s" % idx_len)

    def get_head_tail_data(self):
        print(">>> show head data: %s" % self.df.head(2))
        print(">>> show tail data: %s" % self.df.tail(4))

    # 透過指定列去逐一抓取資料，由左至右．
    def get_cell_value(self, _row_start, _row_end, _row_idx):
        print(">>> show _row_start: %s, _row_end: %s, _row_idx: %s" % (_row_start, _row_end, _row_idx))
        row_range_df = self.df[_row_start:_row_end]
        print("show row_range_df[%s:%s]:\n%s" % (_row_start, _row_end, row_range_df))

        row_range_df_idx = row_range_df.index[_row_idx]
        col_df_idx = row_range_df.columns
        print(" -----------------------------------------------------------------------------------------------------------")
        for col in col_df_idx:
            print(">>> show col idx: %14s, row idx %4s value: %14s" % (col, row_range_df_idx, row_range_df[col][row_range_df_idx]))

    # 刪除NaN的列．
    def del_NaN_row(self):
        df_dropna_result = self.df.dropna()
        print(">>> show df dropna result:\n%s" % df_dropna_result)

if __name__ == "__main__":
    df_PP = ExcelPandasOP(df)
