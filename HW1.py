import pandas as pd
df = pd.read_csv('中央警察大學106年各班期報考人數統計表-utf8.csv',encoding='utf-8')
print(df)
#1.考試種類
print('#1.考試種類')
exam_type_list=[]
for exam in df['Exam']:
    if('博'in str(exam)):
        exam_type_list.append('博')
    elif('碩'in str(exam)):
        exam_type_list.append('碩')
    elif('學士'in str(exam)):
        exam_type_list.append('學士')
    elif('警佐'in str(exam)):
        exam_type_list.append('警佐')
    elif('消佐'in str(exam)):
        exam_type_list.append('消佐')
print(f"本資料共紀錄博士班報考人數{exam_type_list.count('博')}筆;碩士班報考人數{exam_type_list.count('碩')}筆;學士班報考人數{exam_type_list.count('學士')}筆;警佐班報考人數{exam_type_list.count('警佐')}筆;消佐班報考人數{exam_type_list.count('消佐')}筆")

#2.招收類別數量統計
print('#2.招收類別數量統計')
type_list=[]
for i in df['Candidate']:
    if('一'in str(i)):
        type_list.append('一')
    elif("專"in str(i)):
        type_list.append('專')
    elif('海洋法'in str(i)):
        type_list.append('海洋法')
    elif('海洋科'in str(i)):
        type_list.append('海洋科')
    elif('犯'in str(i)):
        type_list.append('犯')
    elif('刑事司法'in str(i)):
        type_list.append('刑事司法')
    elif('化'in str(i)):
        type_list.append('化')
    elif('偵'in str(i)):
        type_list.append('偵')
    elif('警察行政'in str(i)):
        type_list.append('警察行政')
    elif('警察法學組'in str(i)):
        type_list.append('警察法學組')
    elif('刑事警察'in str(i)):
        type_list.append('刑事警察')
    elif('交'in str(i)):
        type_list.append('交')
    elif('消'in str(i)):
        type_list.append('消')
    elif('水'in str(i)):
        type_list.append('水')
print(f"本資料共紀錄\n專案名額{type_list.count('專')}筆\n一般名額{type_list.count('一')}筆\n海洋法制組{type_list.count('海洋法')}筆\n海洋科技組{type_list.count('海洋科')}筆\n犯罪防治組{type_list.count('犯')}筆\n刑事司法組{type_list.count('刑事司法')}筆\n化學物理組{type_list.count('化')}筆\n偵查科學組{type_list.count('偵')}筆\n")
print(f"警察行政組及行政警察學系{type_list.count('警察行政')}筆\n警察法學組{type_list.count('警察法學組')}筆\n交通學系{type_list.count('交')}筆\n消防學系{type_list.count('消')}筆\n水上警察學系{type_list.count('水')}筆\n")

#3.找出最多和最少的報名人數及項目
print('#3.找出最多和最少的報名人數及類別')
result_dict={}
for i in range(len(df)):
    exam_category = df.loc[i, 'Exam']
    try:
        num_applicants = int(df.loc[i, 'Number of applicants'])
        if exam_category in result_dict:
            result_dict[exam_category] += num_applicants
        else:
            result_dict[exam_category] = num_applicants
    except ValueError:
        print(f"數據非有效整數: {df.loc[i, 'Number of applicants']}")

max_category = max(result_dict, key=result_dict.get)
min_category = min(result_dict, key=result_dict.get)

print(f"最多報名人數的項目為 {max_category}，共 {result_dict[max_category]} 人")
print(f"最少報名人數的項目為 {min_category}，共 {result_dict[min_category]} 人")
#4.找出最多和最少的錄取人數及項目
print('#4.找出最多和最少的錄取人數及類別')
result_dict={}
for i in range(len(df)):
    exam_category = df.loc[i, 'Exam']
    try:
        admission = int(df.loc[i, 'Admission number'])
        if exam_category in result_dict:
            result_dict[exam_category] += admission
        else:
            result_dict[exam_category] = admission
    except ValueError:
        print(f"數據非有效整數: {df.loc[i, 'Admission number']}")

max_category = max(result_dict, key=result_dict.get)
min_category = min(result_dict, key=result_dict.get)

print(f"最多錄取人數的項目為 {max_category}，共 {result_dict[max_category]} 人")
print(f"最少錄取人數的項目為 {min_category}，共 {result_dict[min_category]} 人")
#5.錄取率由多到少進行排序並製作長條圖
print('#5.錄取率由多到少進行排序並製作長條圖')
import matplotlib.pyplot as plt
import numpy as np

df['Admission rate'] = df['Admission rate'].astype(str)

# 排序數據
df_sorted = df.sort_values(by='Admission rate', ascending=False)

# 創建長條圖表
plt.figure(figsize=(10, 6))
plt.barh(df_sorted['Exam'], np.array(df_sorted['Admission rate'], dtype=float))
plt.xlabel('錄取率')
plt.ylabel('考試項目') 
plt.title('錄取率由高到低的考試項目排名')
plt.gca().invert_yaxis()
plt.show()

#6.做出學士班二年制技術系五個學系的圓餅圖
print('#6.做出學士班二年制技術系五個學系的圓餅圖')
data = {
    "行政警察學系": 838,
    "刑事警察學系": 341,
    "交通學系": 157,
    "消防學系": 118,
    "水上警察學系": 89
}
labels = data.keys()
sizes = data.values()

# 創建圓餅圖
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# 添加標題
plt.title("學士班二年制技術系五個學系學生人數比例")

# 顯示圓餅圖
plt.show()


#7.報名人數和錄取人數間的關係
print('#7.報名人數和錄取人數間的關係')
applicants=df['Number of applicants']
admission=df['Admission number']
correlation=applicants.corr(admission)
if correlation >0:
    print(f'正相關，相關係數為{correlation}')
elif correlation==0:
    print(f'無相關，相關係數為0')
elif correlation<0:
    print(f'負相關，相關係數為{correlation}')

#8.警佐班和消佐班的平均錄取率哪個較高？
print('#8.警佐班和消佐班的平均錄取率哪個較高？')
police=df[df['Exam'].str.contains('警佐')]
fire=df[df['Exam'].str.contains('消佐')]
police_rate=police['Admission number'].sum()/police['Number of applicants'].sum()
fire_rate=fire['Admission number'].sum()/fire['Number of applicants'].sum()
if police_rate>fire_rate:
    print(f'警佐班更高(平均錄取率:{police_rate})')
elif fire_rate>police_rate:
    print(f"消佐班更高(平均錄取率:{fire_rate})")
else:
    print(f'平均錄取率相同，都是{police_rate}')

#9.博士班和碩士班的平均錄取率哪個較高？
print('#9.博士班和碩士班的平均錄取率哪個較高？')
doctor=df[df['Exam'].str.contains('博')]
master=df[df['Exam'].str.contains('碩')]
doctor_rate=doctor['Admission number'].sum()/doctor['Number of applicants'].sum()
master_rate=master['Admission number'].sum()/master['Number of applicants'].sum()
if doctor_rate>master_rate:
    print(f'博士班更高(平均錄取率:{doctor_rate})')
elif master_rate>doctor_rate:
    print(f'碩士班更高(平均錄取率{master_rate})')
else:
    print(f'平均錄取率相同，{doctor_rate}')

#10.哪一類別的平均錄取率最高
print('#10.哪一類別的平均錄取率最高')
data = {
    "Exam": ["(博)犯罪防治研究所甄試", "(碩)警察政策研究所甄試", "(碩)犯罪防治研究所甄試", "(碩)犯罪防治研究所甄試", "(碩)水上警察研究所甄試",
             "(碩)水上警察研究所甄試", "(碩)行政管理研究所甄試", "(碩)國境警察學系甄試碩士班", "(碩)公共安全研究所甄試", "(碩)公共安全研究所甄試",
             "(碩)鑑識科學研究所甄試", "(博)犯罪防治所", "(博)犯罪防治所", "(博)鑑識科學所", "(博)鑑識科學所", "(博)警察政策所", "(博)警察政策所",
             "(碩)警察政策研究所", "(碩)警察政策研究所", "(碩)刑事警察研究所", "(碩)刑事警察研究所", "(碩)犯罪防治研究所", "(碩)消防科學研究所",
             "(碩)鑑識科學研究所", "(碩)資訊管理研究所", "(碩)水上警察研究所", "(碩)水上警察研究所", "(碩)交通管理研究所", "(碩)行政管理研究所",
             "(碩)外事警察研究所", "(碩)國境警察學系碩士班", "(碩)公共安全研究所", "(碩)法律學研究所", "(碩)防災研究所", "學士班二年制技術系",
             "學士班二年制技術系", "學士班二年制技術系", "學士班二年制技術系", "學士班二年制技術系", "學士班四年制", "學士班四年制", "警佐班第37期第1類",
             "警佐班第37期第2類", "警佐班第37期第3類", "消佐班第21期第1類", "消佐班第21期第2類", "消佐班第21期第2類"],
    "Admission rate": [0.0, 0.53, 0.67, 1.0, 0.0, 0.5, 1.0, 0.67, 1.0, 1.0, 1.0, 0.6, 1.0, 0.0, 1.0, 0.75, 0.3, 0.75, 0.37, 0.11,
                      0.3, 0.3, 0.2, 0.29, 0.23, 0.38, 0.67, 0.28, 0.16, 0.23, 0.15, 0.28, 0.12, 0.24, 0.05, 0.06, 0.1, 0.12, 0.1,
                      0.22, 0.14, 0.19, 0.06, 0.09, 0.13, 0.04, 0.2]
}

df = pd.DataFrame(data)


categories = []
for exam in df['Exam']:
    if "(博)" in exam:
        categories.append("博士班")
    elif "(碩)" in exam:
        categories.append("碩士班")
    elif "學士班" in exam:
        categories.append("學士班")
    elif "警佐班" in exam:
        categories.append("警佐班")
    elif "消佐班" in exam:
        categories.append("消佐班")
    else:
        categories.append("其他")
df['Category'] = categories
category_avg_admission_rate = df.groupby('Category')['Admission rate'].mean().reset_index()
category_avg_admission_rate = category_avg_admission_rate.sort_values(by='Admission rate', ascending=False)
highest_avg_rate_category = category_avg_admission_rate.iloc[0]
print("最高平均錄取率的類別:", highest_avg_rate_category['Category'])


