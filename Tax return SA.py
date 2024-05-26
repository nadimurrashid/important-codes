from datetime import datetime
import calendar
def job_start_date_after_recurring_Tax_SA(current_job_start_date):

    SDate = int(current_job_start_date.split('/')[0])
    SMonth = int(current_job_start_date.split('/')[1])
    SYear = int(current_job_start_date.split('/')[-1])

    current_date = SDate
    current_month = SMonth
    get_year = SYear

    print(f"The current month is {current_month}.")
    print(f"The current year is {get_year}.")

    add_three_month = current_month + 1

    expected_month = 0
    if add_three_month > 12:

        substract_month = add_three_month - 12
        expected_month = substract_month
        get_year += 3

    else:
        get_year += 2
        expected_month = add_three_month

    last_day = calendar.monthrange(get_year, expected_month)[1]
    next_job_start_date = str(last_day) + "/" + str(expected_month).zfill(2) + '/' + str(get_year)
    return next_job_start_date

def job_due_date_after_recurring_vat_annual(current_job_due_date):

    SDate = int(current_job_due_date.split('/')[0])
    SMonth = int(current_job_due_date.split('/')[1])
    SYear = int(current_job_due_date.split('/')[-1])

    current_date = SDate
    current_month = SMonth
    get_year = SYear

    print(f"The current month is {current_month}.")
    print(f"The current year is {get_year}.")
    add_three_month = current_month + 2

    expected_month = 0
    if add_three_month > 12:

        substract_month = add_three_month - 12
        expected_month = substract_month
        get_year += 1

    else:
        expected_month = add_three_month

    last_day = calendar.monthrange(get_year, expected_month)[1]
    next_job_due_date = str(last_day) + "/" + str(expected_month).zfill(2) + '/' + str(get_year)
    return next_job_due_date


def task_due_date_after_recurring_vat_annual(current_task_start_date):
    SDate = int(current_task_start_date.split('/')[0])
    SMonth = int(current_task_start_date.split('/')[1])
    SYear = int(current_task_start_date.split('/')[-1])

    current_date = SDate
    current_month = SMonth
    get_year = SYear

    print(f"The current month is {current_month}.")
    print(f"The current year is {get_year}.")

    add_month = current_month + 1

    expected_month = 0
    if add_month > 12:

        substract_month = add_month - 12
        expected_month = substract_month
        get_year += 2

    else:
        expected_month = add_month

    next_task_due_date = "01" + "/" + str(expected_month).zfill(2) + '/' + str(get_year)
    return next_task_due_date

expected_job_start_date = job_start_date_after_recurring_Tax_SA("31/12/24")
expected_job_due_date = job_due_date_after_recurring_vat_annual("31/01/24")
expected_task_start_date = expected_job_start_date
expected_task_due_date = task_due_date_after_recurring_vat_annual("31/01/24")
print(expected_job_start_date)
print(expected_job_due_date)
print(expected_task_start_date)
print(expected_task_due_date)



