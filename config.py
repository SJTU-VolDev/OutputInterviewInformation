#获取cookies方法：用短信平台的jac，登录后F12获取cookies
cookies = {
    "sjtu_token":"eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJjaGFubmVsIjoiamFjY291bnQiLCJleHAiOiIyMDI0LTA0LTExVDIyOjUxOjA3LjUyNjMyNzc5NSswODowMCIsInN1YiI6IjI5ZWRlYTljLTlmZTctNGVkZS05OGI2LTgxMjJhMDExZjQxZiJ9.i7lZKW_jSt2xHh230kxEXMAzJWGKH5Co19wGZMeT9fmNxeVDLG0RBnuI4gXZk5rYG5Hnxw8E6Iqkznv0A8z5WUWzL4IzzCxWWmXgHQL8WS06AMcbTwbr80A8n1BY9giWsZUO_Fn7Ao6V9xdsTCgndyVNjZI1aT3juSckByyHHT2HoFidUJb5tVhDmCqA7hN2njF_J42xJHdQSF-1Lr9TIw5boVi79JqS_kH26HPRkjh4UqFSKPbS0JYlDGRAVAjou3fT_WHw9Rw_azsneGKKJNtOf0eQ-FPYJ7zWj6dKQhQtJAvwrtuasZYD_clIG4fhpgMbCS5HIcIpVS8vxEu35Q"
}

#问卷编号（列表）
QuestionDataList = [53862,53863,53864]

#问卷表头字段
QuestionDataHeader = {
    "面试官": "Q1. 面试官姓名",
    "面试时间": "Q2. 面试时间段",
    "面试打分表": "Q3. 请上传面试结果",
}

#打分表表头字段
ScoreDataHeader = {
    "姓名": "姓名",
    "学号": "学号",
    "总分": "总分(15)",
    "归一化得分": "归一化分数",
}
