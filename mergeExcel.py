import pandas as pd
import math
import os
class Interviewee:
    name = ""
    id = ""
    score = 0
    def __init__(self, name, id, score):
        self.name = name
        self.id = id
        self.score = score


def mergeExcel():
    from config import ScoreDataHeader
    from methods import calculateScore
    from methods import standardTable
    Outputdata = {
        "姓名": [],
        "学号": [],
        "归一化得分":[],
    }
    data = []
    days = len(os.listdir(r"./面试官打分表"))
    for day in range(1, days+1):
        table_path = os.path.join(r"./面试官打分表", r"Day "+str(day))
        file_list = os.listdir(table_path)
        tot = len(file_list)
        it = 0
        for file in file_list:
            it += 1
            print("正在处理\"" + file.split("_")[0] + "\"的面试官打分表,第" + str(day) + "天进度 " + str(it) + " / " + str(tot))
            table = pd.read_excel(os.path.join(table_path, file),dtype=str)
            table = standardTable(table)
            table = calculateScore(table)
            for i in range(len(table)):
                if pd.isnull(table[ScoreDataHeader["姓名"]][i]):
                    continue
                data.append(Interviewee(
                    name=table[ScoreDataHeader["姓名"]][i], 
                    id=table[ScoreDataHeader["学号"]][i], 
                    score=table[ScoreDataHeader["归一化得分"]][i]
                    ))
    for x in data:
        x.score = float(x.score)
    data.sort(key=lambda x:x.score, reverse=True)
    for item in data:
        Outputdata["姓名"].append(item.name)
        if len(item.id) == 11:
            Outputdata["学号"].append("0" + str(item.id))
        else:
            Outputdata["学号"].append(str(item.id))
        Outputdata["归一化得分"].append(item.score)
    pd.DataFrame(Outputdata).to_excel(r"./面试汇总表.xlsx", index=False)