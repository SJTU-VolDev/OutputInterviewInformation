# 面试官打分表收集+合并

## 功能
+ 从问卷平台下载面试官打分表
+ 合并多个面试官打分表
+ 按归一化分数排序输出

## 使用方法
### 安装依赖
```shell
pip install -r requirements.txt
```

### 配置
+ 登录问卷平台，F12获取`cookies`，填入`config.py`中的`cookies`
+ 将结果收集问卷的编号填入`config.py`中的`QuestionDataList`（编号即问卷地址栏的数字）
+ 将问卷表头字段填入`config.py`中的`QuestionDataHeader`
+ 将打分表的表头字段填入`config.py`中的`ScoreDataHeader`

### 运行
```shell
python main.py
```

### 输出
+ `面试官信息.xlsx` - 面试官信息表
+ `面试汇总表.xlsx` - 合并+排序的面试官打分表
