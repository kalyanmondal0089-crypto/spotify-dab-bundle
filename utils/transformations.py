kalyan_var=234

class reusable:
    
    def dropColumns(self,df,columns):
        df=df.drop(*columns)
        return df