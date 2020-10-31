import xlrd

def readexcel(path):
    workbook=xlrd.open_workbook(path)
    table = workbook.sheets()[0]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    #dataMatrix=zeros((nrows,ncols))
    dataMatrix=[[] for i in range(nrows)]
    #for i in range(nrows):
        #for j in range(ncols):
    for i in range(nrows):
            #dataMatrix[i][j]=table.cell(i,j).value
        #col_values=table.col_values(i)
       # minVals=min(col_values)
        #maxVals=max(col_values)
        #cols1=matrix(col_values) # 把list转换为矩阵进行矩阵操作
        #ranges=maxVals-minVals
        #b=cols1-minVals
        #normcols = b / ranges  # 数据进行归一化处理
        #datamatrix[:, x] = normcols # 把数据进行存储
            print (table.col_values(i))
            
    return dataMatrix




def load_data_set():
    """
    Load a sample data set (From Data Mining: Concepts and Techniques, 3th Edition)
    Returns: 
        A data set: A list of transactions. Each transaction contains several items.
    """
    data_set = readexcel('D:\各种数据集\专利数据\INVT：CITY.xlsx')
    return data_set

if __name__ == "__main__":
    """
    Test
    """
    data_set = load_data_set()
