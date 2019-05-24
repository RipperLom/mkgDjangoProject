# coding=utf-8
# Version:python3.6.4
# Tools:Pycharm 2017.3.2
__date__ = '2019/5/23 11:17'
__author__ = 'DongHao'

import json
import csv

# 构建建立三元组的类
class Triad(object):

    def getIllnessAnotherNames(self, filepath1, filepath2):  # 获取疾病名字与别名之间的三元组
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'same_name', 'illness_name'])
                datas = json.load(fr)
                for data in datas:
                    if data['another_names'][0] != '':
                        for i in data['another_names']:
                            if str(i).strip() != str(data['illness_name']).strip():
                                strs = str(data['illness_name']) + '%%' + 'another_names' + '%%' + str(i)
                                csv_writer.writerow(strs.split('%%'))

    def gitIllnessClassicalSymptom(self, filepath1, filepath2):  # 构建疾病与典型症状的三元组关系
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'classical_symptom', ' symptom_name'])
                datas = json.load(fr)
                for data in datas:
                    count = 0
                    index = 0
                    for i in range(len(data['baseList'])):
                        if "典型症状" in data['baseList'][i]:
                            if data['baseList'][i]['典型症状'] != "":
                                count = 1
                                index = i
                    if count == 1:
                        for i in data['baseList'][index]['典型症状'].split(' '):
                            strs = str(data['illness_name']) + '%%' + 'illness_classical_symptom' + '%%' + str(i)
                            csv_writer.writerow(strs.split('%%'))

    def getIllnessComplication(self, filepath1, filepath2):  # 构建疾病与并发症之间的三元组
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'complication', 'sickness'])
                datas = json.load(fr)
                for data in datas:
                    count = 0
                    index = 0
                    for i in range(len(data['baseList'])):
                        # print(i)
                        if "并发症" in data['baseList'][i]:
                            if data['baseList'][i]['并发症'] != "":
                                count = 1
                                index = i
                    if count == 1:
                        for i in data['baseList'][index]['并发症'].split(' '):
                            strs = str(data['illness_name']) + '%%' + 'illness_complication' + '%%' + str(i)
                            csv_writer.writerow(strs.split('%%'))

    def getIllnessExamination(self, filepath1, filepath2):  # 构建疾病与相关检查的三元组关系
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'examination', 'examination_name'])
                datas = json.load(fr)
                for data in datas:
                    count = 0
                    index = 0
                    for i in range(len(data['baseList'])):
                        if "临床检查" in data['baseList'][i]:
                            if data['baseList'][i]['临床检查'] != "":
                                count = 1
                                index = i
                    if count == 1:
                        for i in data['baseList'][index]['临床检查'].split(' '):
                            strs = str(data['illness_name']) + '%%' + 'illness_examination' + '%%' + str(i)
                            csv_writer.writerow(strs.split('%%'))

    def getIllnessPathogenicSite(self, filepath1, filepath2):  # 构建疾病与发病部位之间的三元组
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                datas = json.load(fr)
                csv_writer.writerow(['illness_name', 'pathogenic_site', 'parts_name'])
                for data in datas:
                    # print(data['baseList'])
                    count = 0
                    index = 0
                    for i in range(len(data['baseList'])):
                        # print(i)
                        if "发病部位" in data['baseList'][i]:
                            if data['baseList'][i]['发病部位'] != "":
                                count = 1
                                index = i
                    if count == 1:
                        for i in data['baseList'][index]['发病部位'].split(' '):
                            strs = str(data['illness_name']) + '%%' + 'illness_pathogenic_site' + '%%' + str(i)
                            csv_writer.writerow(strs.split('%%'))

    def getIllnessRegularMedication(self, filepath1, filepath2):  # 构建疾病与常用药品之间的三元组关系
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'regular_medication', 'medication_name'])
                datas = json.load(fr)
                for data in datas:
                    # print(data['baseList'])
                    count = 0
                    index = 0
                    for i in range(len(data['baseList'])):
                        # print(i)
                        if "常用药品" in data['baseList'][i]:
                            if data['baseList'][i]['常用药品'] != "":
                                count = 1
                                index = i
                    if count == 1:
                        for i in set(data['baseList'][index]['常用药品'].split(' ')):
                            strs = str(data['illness_name']) + '%%' + 'llness_regular_medication' + '%%' + str(i)
                            csv_writer.writerow(strs.split('%%'))

    def getIllnessSurgeriesName(self, filepath1, filepath2):  # # 构建疾病与手术的三元组关系
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'surgeries', 'surgeries_name'])
                datas = json.load(fr)
                for data in datas:
                    if len(data['relevant_illness']) != 0:
                        for i in range(len(data['relevant_illness'])):
                            csv_writer.writerow([str(data['relevant_illness'][i]), 'surgeries', data['surgery_name']])

    def getIllnessTreatmentOfDepartment(self, filepath1, filepath2):  # 构建疾病与治疗科室的三元组关系
        with open(filepath1, 'r', encoding='utf-8') as fr:
            with open(filepath2, 'a', newline='', encoding='utf-8') as fw:
                csv_writer = csv.writer(fw, dialect='excel')
                csv_writer.writerow(['illness_name', 'Treatment_of_department', 'Department_name'])
                datas = json.load(fr)
                for data in datas:
                    count = 0
                    index = 0
                    for i in range(len(data['baseList'])):
                        if "挂号科室" in data['baseList'][i]:
                            if data['baseList'][i]['挂号科室'] != "":
                                count = 1
                                index = i
                    if count == 1:
                        for i in data['baseList'][index]['挂号科室'].split(' '):
                            strs = str(data['illness_name']) + '%%' + 'Treatment_of_department' + '%%' + str(i)
                            csv_writer.writerow(strs.split('%%'))

if __name__ == "__main__":
    triad = Triad()
