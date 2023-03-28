import json
import csv
import queue
from bs4 import BeautifulSoup

lst = {"TestCases": [
            {
                "Title": "",
                "Folder": "",
                "Feature": "",
                "Dependencies": {},
                "Steps": [
                    {
                        "Step name": "",
                        "Step description": "",
                        "Step expected": "",
                        "Step type": "linked",
                        "Step actions": [{
                            "Step name": "",
                            "Step description": "",
                            "Step expected": "",
                            "Step type": "linked",
                            "Step actions": []}
                        ]
                    }
                ]
            }]
         }
line_c = 0
line_d = 0


filename = r"C:\Users\Sazid\Desktop\json_converter\excl4.json"

with open(r"C:\Users\Sazid\Desktop\json_converter\Import_Test_Cases_for_Zeuz.csv",encoding="UTF-8") as f:
    reader = csv.DictReader(f)
    packet = []
    test_data = []
    step_expected = []
    steps = []
    initial_steps = None
    new_steps = None
    store_issuekey_temp = None
    store_summery_temp = None
    last_case_key = 'HUB-21328'
    demeter = None
    Folder_name = "HUB"
    Feature_name = "HUB"
    counter = 0



    for row in reader:
        row['issuekey'] = row.pop('\ufeffissuekey')

        if row['Summary'] != '':

            if initial_steps == None:

                if store_issuekey_temp and store_summery_temp != None:
                    s_key_temp = store_issuekey_temp
                    s_sum_temp = store_summery_temp
                    store_issuekey_temp = None
                    store_summery_temp = None
                    counter = counter + 1

                initial_steps = {"Step name": row["TestStep"],
                              "Step description": row["Test Data"],
                              "Step expected": row["Test Result"],
                              "Step type": "linked",
                              "Step actions": []}
                store_issuekey_temp = row['issuekey']
                store_summery_temp = row['Summary']
                if demeter != None:
                    demeter = demeter + 1
                else:
                    pass


            if counter == 1 or demeter == 7:
                new_steps = steps
                steps = None
                counter = 0
                print(new_steps)

        if row['Summary'] == '':
            steps.append({"Step name": row["TestStep"],
                          "Step description" : row["Test Data"],
                          "Step expected": row["Test Result"],
                          "Step type": "linked",
                          "Step actions": []})
            if initial_steps != None:
                steps.insert(0,initial_steps)
                new_steps = None

            else:
                pass

        if new_steps != None:
            lst["TestCases"] += [
                {
                    "Title": f"{s_key_temp + '>' + s_sum_temp}",
                    "Folder": "HUB",
                    "Feature": "HUB",
                    "Dependencies": {},
                    "Steps": new_steps
                }
            ]
            steps = []
            initial_steps = None

        # if row['issuekey'] != last_case_key:
        #
        #     if row['Summary'] != '':
        #
        #         if initial_steps != None:
        #
        #             if store_issuekey_temp and store_summery_temp != None:
        #                 s_key_temp = store_issuekey_temp
        #                 s_sum_temp = store_summery_temp
        #                 store_issuekey_temp = None
        #                 store_summery_temp = None
        #                 counter = counter + 1
        #
        #             initial_steps = {"Step name": row["TestStep"],
        #                              "Step description": row["Test Data"],
        #                              "Step expected": row["Test Result"],
        #                              "Step type": "linked",
        #                              "Step actions": []}
        #             store_issuekey_temp = row['issuekey']
        #             store_summery_temp = row['Summary']
        #
        #         if counter == 1:
        #             new_steps = steps
        #             steps = None
        #             counter = 0
        #
        #     if row['Summary'] == '':
        #         steps.append({"Step name": row["TestStep"],
        #                       "Step description": row["Test Data"],
        #                       "Step expected": row["Test Result"],
        #                       "Step type": "linked",
        #                       "Step actions": []})
        #         print(steps)
        #         if initial_steps != None:
        #             steps.insert(0, initial_steps)
        #             initial_steps = None
        #         else:
        #             pass
        # if new_steps != None:
        #     lst["TestCases"] += [
        #         {
        #             "Title": f"{s_key_temp + '>' + s_sum_temp}",
        #             "Folder": f"{s_sum_temp}",
        #             "Feature": f"{s_sum_temp}",
        #             "Dependencies": {},
        #             "Steps": new_steps
        #         }
        #     ]
        #     steps = []
        #     new_steps = None





        # print(row['Summary'] +'\n')
        #
        #
        # if row['Summary'] != '':
        #     packet.append(row['TestStep'])
        # else:
        #     pass
        # test_data.append(row['Test Data'].split('\n'))
        # step_expected.append(row['Test Result'].split('\n'))
        # print(packet)
        # row['issuekey'] = row.pop('\ufeffissuekey')
        #     # x = row['\ufeffissuekey']
        #
        #
        # if row['Summary'] != '':
        #     y = row['Summary']
        #
        # # hub_key = row['\ufeffissuekey'].replace('',x)
        # hub_sumry = row['Summary'].replace('',y)

#         def steps(packet,test_data,step_expected):
#             steps = []
#             q = queue.Queue()
#             for t in packet:
#                 q.put(t)
#             x = q.get()
#             r = queue.Queue()
#             for t_data in test_data:
#                 r.put(t_data)
#             y = r.get()
#             s = queue.Queue()
#             for t_expec in step_expected:
#                 s.put(t_expec)
#             z = s.get()
#             lenghth = (len(x))
#             for _ in range(len(x) - len(y)):
#                 y.append('0')
#             for _ in range(len(x) - len(z)):
#                 z.append('0')
#             counter = 0
#             while lenghth > counter:
#                 steps.append({"Step name": x[counter],
#                               "Step description": y[counter],
#                               "Step expected": z[counter],
#                               "Step type": "linked",
#                               "Step actions": []})
#                 counter = counter + 1
#
#                 if lenghth < counter:
#                     break
#
#             return steps
#         steps_item = steps(packet,test_data,step_expected)
#         packet.pop(0)
#
#         :
#             lst["TestCases"] += [
#                 {
#                     "Title": f"{row['issuekey'] +'>'+ row['Summary']}",
#                     "Folder": f"{row['Summary']}",
#                     "Feature": f"{row['Summary']}",
#                     "Dependencies": {},
#                     "Steps": steps_item
#                 }
#             ]
#         else:
#             lst["TestCases"] += [{
#             lst["TestCases"][0]["Steps"] : steps_item[0]
#             }]
#
#
#
# # test2 = [['one','folder1','feature1',['tri1','tr34'],['tr2'],'linked'],['two','folder2','feature2',['tri5','tr3oplmsn'],'tri2','tr3','linked']]
#
#
# # print(lst['TestCases'][0]['Steps'])
# i = 0
# # for test1 in test2:
# #
# #     print(lst)
#     # for step_data in test2:
#
# #     for i in step_data[3]:
# #         if len(i)>1:
# #             print(i)
# #             lst['TestCases'][0]['Steps'] += []
#
# #
#
#
with open(filename,mode='w') as f:
    json.dump(lst,f)
