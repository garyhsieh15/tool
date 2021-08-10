
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
        print("show columns: %s" % columns)
        print("show columns[0]: %s" % columns[0])
        print("show columns[1]: %s" % columns[1])


if __name__ == "__main__":
    df_PP = ExcelPandasOP(df)
