import csv

def get_headers_indices(file_path, headers_to_find):

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:

        csvreader = csv.reader(csvfile)

        headers = next(csvreader)

        indices = []

        for header in headers_to_find:
            if header in headers:
                indices.append(headers.index(header))
            else:
                raise ValueError(f"Header '{header}' not found in the CSV file")

        return indices



csv_file_path = r'A:\taxcalc_paths\Ltd Company Test CSV Year 1  - subsidiary2.csv'
headers_to_find = ['Account', 'Account Description', 'Debit','Credit']
selected_columns_file1 = get_headers_indices(csv_file_path, headers_to_find)
print(f"The indices of the headers are: {selected_columns_file1}")



app_file_path = r'A:\taxcalc_paths\group_tb_ZeuZUserEwLrLz.csv'
headers_to_find = ['Account', 'Account Description', 'compC_ZeuZUserEwLrLz']
selected_columns_file2 = get_headers_indices(app_file_path, headers_to_find)
print(f"The indices of the headers are: {selected_columns_file2}")



with open(r'A:\taxcalc_paths\Ltd Company Test CSV Year 1  - subsidiary2.csv', 'r') as file1, open(r'A:\taxcalc_paths\group_tb_ZeuZUserEwLrLz.csv', 'r') as file2:

    csv_reader1 = csv.reader(file1)
    csv_reader2 = csv.reader(file2)

    next(csv_reader1)
    next(csv_reader2)

    csv_file_numbers = []
    app_file_numbers = []
    app_data = []
    csv_data = []

    for row1, row2 in zip(csv_reader1, csv_reader2):
        selected_row1 = [row1[i] for i in selected_columns_file1]
        csv_data.append(selected_row1)

        selected_row2 = [row2[i] if i < len(row2) else 0 for i in selected_columns_file2]
        app_data.append(selected_row2)

        csv_file_numbers.append(int(selected_row1[0]))
        app_file_numbers.append(int(selected_row2[0]))


    print(len(csv_file_numbers))
    print(csv_file_numbers)
    print(app_file_numbers)

    for sapp_data in app_data:

        if int(sapp_data[0]) in sorted(csv_file_numbers):
            for scsv_data in csv_data:

                if scsv_data[0].startswith(str(int(sapp_data[0]))):

                    if (scsv_data[2] == '' or scsv_data[2] == '0')  and sapp_data[2] != '':
                        if str(sapp_data[2]).startswith('(') and str(sapp_data[2]).endswith(')'):

                            if scsv_data[1] == sapp_data[1]:

                                if str(scsv_data[3]) == sapp_data[2].replace('(','').replace(')',''):
                                    with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                        file3.write(f'Account Description and Credit got matched  -- from csv file -> {scsv_data} and from app -> {sapp_data} \n')
                                elif float(scsv_data[3].replace(',','')) == float(sapp_data[2].replace('(','').replace(')','').replace(',','')):
                                    with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                        file3.write(f'The credit value in the app has two floating point number "00" and Credit got matched  -- from csv file -> {scsv_data} and from app -> {sapp_data} \n')
                            else:
                                if str(scsv_data[3]) == sapp_data[2].replace('(','').replace(')',''):
                                    with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                        file3.write(f'Account Description is different and Credit got matched  -- from csv file -> {scsv_data} and from app -> {sapp_data} \n')
                                elif float(scsv_data[3].replace(',','')) == float(sapp_data[2].replace('(','').replace(')','').replace(',','')):
                                    with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                        file3.write(f'The credit value in the app has two floating point number "00" , Credit got matched  -- from csv file -> {scsv_data} and from app -> {sapp_data} and account description is different \n')



                    elif scsv_data[2] == sapp_data[2]:
                        if scsv_data[1] == sapp_data[1]:
                            with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                file3.write(f'Account Description and Debit got matched  -- from csv file -> {scsv_data} and from app -> {sapp_data} \n')
                        else:
                            with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                file3.write(f'Account Description is different and Debit got matched  -- from csv file -> {scsv_data} and from app -> {sapp_data} \n')

                    elif float(scsv_data[2]) == float(sapp_data[2].replace(',','')):
                        if scsv_data[1] == sapp_data[1]:
                            with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                file3.write(f'The debit value in the app has additional ".00" value  -- from csv file -> {scsv_data} and from app -> {sapp_data} \n')
                        else:
                            with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                                file3.write(f'The debit value in the app has additional ".00" value  -- from csv file -> {scsv_data} and from app -> {sapp_data} and the account descriptionis different \n')

        else:
            with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                file3.write(f'A new row got added in the app -> {sapp_data} \n')


    def find_differences(list1, list2):
        set1 = set(list1)
        set2 = set(list2)

        unique_to_list1 = set1 - set2
        unique_to_list2 = set2 - set1

        return unique_to_list1, unique_to_list2

    differences1, differences2 = find_differences(csv_file_numbers, app_file_numbers)

    print("Elements unique to list1:", differences1)
    print("Elements unique to list2:", differences2)
    d_list = list(differences1)
    d2_list = list(differences2)

    for scsv_data in csv_data:
        if d_list != []:
            if scsv_data[0] == str(d_list[0]):
                with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                    file3.write(f'A new row got added in the csv file  -> {scsv_data} \n')
                    d_list.pop(0)

    for sapp_data in app_data:
        if d2_list != []:
            if sapp_data[0] == str(d2_list[0]):
                with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                    file3.write(f'A new row got added in the app data  -> {sapp_data} \n')
                    d2_list.pop(0)

    from collections import Counter

    from collections import defaultdict


    def find_duplicates_with_details(lst):
        counts = defaultdict(int)
        positions = defaultdict(list)

        for index, item in enumerate(lst):
            counts[item] += 1
            positions[item].append(index)

        duplicates = {}
        for item, count in counts.items():
            if count > 1:
                duplicates[item] = {'count': count, 'positions': positions[item]}

        return duplicates


    def find_last_index(lst):
        if not lst:
            return -1
        return len(lst) - 1



    last_index = find_last_index(app_file_numbers)
    print(f"The index of the last item is {last_index}")

    with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
        file3.write(" ------------------------------------> \n")
        file3.write(" Find duplicate values \n")
        file3.write(" ------------------------------------> \n")



    duplicates = find_duplicates_with_details(app_file_numbers)
    for item, details in duplicates.items():
        print(f"Item {item} appears {details['count']} times at positions {details['positions']} in the app")
        with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
            file3.write(f"Item {item} appears {details['count']} times at positions {details['positions']} in the app \n")
            if item == 0 and details['count'] == 2 and details['positions'][-1] == last_index and details['positions'][0] == 0:
                file3.write("Ignore the count number for zero as the last index value zero doesn't represent duplication in the app \n")

    with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
        file3.write(" ------------------------------------> \n")
        file3.write(" Compare group total with the sum of three column \n")
        file3.write(" ------------------------------------> \n")

    import csv, itertools

    csv_file_path = r'A:\taxcalc_paths\group_tb_ZeuZUserEwLrLz.csv'
    with open(csv_file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        sum_total_of_three_column = []
        group_total = []

        for row in csv_reader:
            if (row['Account']) != "Total":
                sum_total_of_three_column.append((row['Account'], ' -> ', float(
                    row['Parent'].replace('(', '').replace(')', '').replace(',', '')) + float(
                    row['compC_ZeuZUserEwLrLz'].replace('(', '').replace(')', '').replace(',', '')) + float(
                    row['compB_ZeuZUserEwLrLz'].replace('(', '').replace(')', '').replace(',', ''))))
                group_total.append((row['Account'], ' -> ',
                                    float(row['Group Total'].replace('(', '').replace(')', '').replace(',', ''))))

            else:
                break




        print(sum_total_of_three_column)
        print(group_total)

        for a, b in itertools.zip_longest(sum_total_of_three_column, group_total, fillvalue=None):
            if b is None:
                with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                    file3.write(f"Extra element in sum total of three column : {a} \n")
            elif a is None:
                with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                    file3.write(f"Extra element in group total : {a} \n")
            else:
                with open(r"C:\Users\Sazid\Desktop\comparison_report.txt", 'a') as file3:
                    if a[2] == b[2]:
                        file3.write(f"sum total of three column  ->  {a} and group total amount - {b} got matched \n")
                    else:
                        file3.write(f"sum total of three column  ->  {a} and group total amount - {b} didn't match \n")










