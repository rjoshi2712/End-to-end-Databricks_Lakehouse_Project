

class reusable:

    def dropColumns(self, df, columns):
        df = df.drop(*columns)
        return df
  

    def dropDuplicates(self, df, columns):
        return df.dropDuplicates(columns)