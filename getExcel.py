import requests
import os
import pandas as pd
from config import QuestionDataList
from config import cookies
from config import QuestionDataHeader

def download_file(url, cookies, save_path, name):
    if os.path.exists(os.path.join(save_path,name)):
        return
    response = requests.get(url,
                            cookies=cookies,
                            )
    if response.status_code == 200:
        os.makedirs(save_path, exist_ok=True)

        with open(os.path.join(save_path,name), 'wb') as file:
            file.write(response.content)

def getQuestionaire():
    if os.path.exists("./问卷数据"):
        return
    for day in range(len(QuestionDataList)):
        url = "https://wj.sjtu.edu.cn/api/v1/manage/questionnaire/created/" + str(QuestionDataList[day]) + "/data/table-export/excel?params={}"
        print("正在下载第"+ str(day+1) + "天的问卷数据...")
        os.makedirs("./问卷数据", exist_ok=True)
        download_file(url, cookies, "./问卷数据","Day " + str(day + 1)+".xlsx")
    
def getExcelfromQuestionaire():
    if os.path.exists("./面试官打分表"):
        return
    file_list = os.listdir("./问卷数据")
    day = 0
    Interviewer_data = {
        "面试官":[],
        "面试时间":[],
    }
    excelwriter = pd.ExcelWriter(r"./面试官信息.xlsx", engine='xlsxwriter')
    for file in file_list:
        day += 1
        table = pd.read_excel(r"./问卷数据/"+file)
        Interviewer_data["面试官"]=(list(table[QuestionDataHeader["面试官"]]))
        Interviewer_data["面试时间"]=(list(table[QuestionDataHeader["面试时间"]]))
        tot = len(table[QuestionDataHeader["面试官"]]) #总数
        for i in range(tot):
            interviewer = table[QuestionDataHeader["面试官"]][i]
            interview_time = table[QuestionDataHeader["面试时间"]][i]
            url_list = table[QuestionDataHeader["面试打分表"]][i].split("\n")
            print("正在下载\""+str(interviewer)+"\"的面试官打分表, 第"+str(day)+"天进度 "+str(i)+" / "+str(tot))
            dfs = []
            for url in url_list:
                file_name = str(interviewer)+"_"+str(interview_time)+"_"+str(i)+".xlsx"
                save_path = r"./面试官打分表/Day "+str(day)
                download_file(
                    url=url, 
                    cookies=cookies, 
                    save_path=save_path, 
                    name=file_name
                ) 
                dfs.append(pd.read_excel(os.path.join(save_path,file_name)))
                os.remove(os.path.join(save_path,file_name))
            pd.concat(dfs,axis = 0).to_excel(os.path.join(save_path,file_name), index=False)
        pd.DataFrame(Interviewer_data).to_excel(excelwriter, sheet_name="Day "+str(day),index=False)
    excelwriter.close()

def getExcel():
    getQuestionaire()
    getExcelfromQuestionaire()
