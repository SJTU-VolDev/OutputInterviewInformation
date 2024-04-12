import pandas as pd
from config import ScoreDataHeader
def calculateScore(table):
    '''
    该函数用于计算归一化得分
    '''
    n = len(table)
    avg = 0
    stderr = 0
    #计算平均值和标准差
    for i in range(n):
        avg += float(table[ScoreDataHeader["总分"]][i])
    avg /= n
    for i in range(n):
        stderr += (float(table[ScoreDataHeader["总分"]][i])-avg)**2
    stderr = (stderr/n)**0.5
    #计算归一化得分
    for i in range(n):
        table[ScoreDataHeader["归一化得分"]][i] = (float(table[ScoreDataHeader["总分"]][i])-avg) / stderr
    return table

def standardTable(table):
    '''
    该函数用于标准化表格，去除空白行
    '''
    df = pd.DataFrame(columns=table.columns)
    for i in range(len(table)):
        if pd.isnull(table[ScoreDataHeader["姓名"]][i]) or pd.isnull(table[ScoreDataHeader["学号"]][i]):
            continue
        df = pd.concat([df,pd.DataFrame([table.loc[i]])],ignore_index=True)
    return df

if __name__ == "__main__":
    table = pd.read_excel("面试官打分表\Day 3\王琨_18：00-20：00、20：00-22：00_26.xlsx",dtype=str)
    table = standardTable(table)