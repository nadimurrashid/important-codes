import json
import csv

steps = []
new_steps = []
initial_steps = None
old_val = None
def csv_generator():
    with open(r"C:\Users\Sazid\Desktop\json_converter\Import_Test_Cases_for_Zeuz.csv",encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

for row in csv_generator():
    row['issuekey'] = row.pop('\ufeffissuekey')
    row['Summary'] = row['Summary'].replace("'",'"')
    row["TestStep"] = row['TestStep'].replace("'",'"')


    if row['issuekey'] != old_val and old_val != None and row['issuekey'] != '':

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

        lst["TestCases"] += [
            {
                "Title": f"{key_temp + ' > ' + summary_temp}",
                "Folder": "HUB",
                "Feature": "HUB",
                "Dependencies": {},
                "Steps": steps
            }
        ]
        steps = []
        # filename = r"C:\Users\Sazid\Desktop\json_converter\{}.csv".format(key_temp + ' > ' + summary_temp)
        temp = r"C:\Users\Sazid\Desktop\json_converter\{}.json".format(key_temp)
        filename = temp
        with open(filename, mode='w') as f:
            json.dump(lst, f)
            print(lst)
            lst = None

    if row['Summary'] != '':
        # initial_steps = {"Step name": row["TestStep"],
        #                  "Step description": row["Test Data"],
        #                  "Step expected": row["Test Result"],
        #                  "Step type": "linked",
        #                  "Step actions": []}
        key_temp = row['issuekey']
        summary_temp = row['Summary']
        old_val = row['issuekey']
        steps.append({"Step name": row["TestStep"],
                      "Step description": row["Test Data"],
                      "Step expected": row["Test Result"],
                      "Step type": "linked",
                      "Step actions": []})

    if row['Summary'] == '':
        if initial_steps != None:
            # if steps[0] == initial_steps:
            #     initial_steps = None
            # else:
            steps = [initial_steps]
            initial_steps = None
        else:
            pass
        steps.append({"Step name": row["TestStep"],
                         "Step description": row["Test Data"],
                         "Step expected": row["Test Result"],
                         "Step type": "linked",
                         "Step actions": []})

if old_val != None:
    print('reached')
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
    lst["TestCases"] += [
        {
            "Title": f"{key_temp + '>' + summary_temp}",
            "Folder": "HUB",
            "Feature": "HUB",
            "Dependencies": {},
            "Steps": steps
        }
    ]
    temp = r"C:\Users\Sazid\Desktop\json_converter\{}.json".format(key_temp)
    filename = temp
    with open(filename, mode='w') as f:
        json.dump(lst, f)





