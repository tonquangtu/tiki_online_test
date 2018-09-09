import csv


def read_and_process(input_file_name):
    unique_phone = {}
    with open(input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            phone_number = row[0]
            act_date = row[1]
            deact_date = row[2]

            if not unique_phone.get(phone_number, False):
                unique_phone[phone_number] = [[act_date, deact_date]]
            else:
                items = unique_phone[phone_number]
                k = -1
                for i in range(len(items) - 1, -1, -1):
                    item = items[i]
                    if item:
                        if act_date == item[1]:
                            item[1] = deact_date
                            act_date = item[0]
                            if k != -1:
                                items[k] = False
                            k = i
                        elif deact_date == item[0]:
                            item[0] = act_date
                            deact_date = item[1]
                            if k != -1:
                                items[k] = False
                            k = i

                if k == -1:
                    items.append([act_date, deact_date])
    return unique_phone


def handle():
    input_file_name = 'input.csv'
    output_file_name = 'output1.csv'
    result = read_and_process(input_file_name)

    with open(output_file_name, mode='w') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',')
        csv_writer.writerow(['PHONE_NUMBER', 'REAL_ACTIVATION_DATE'])

        for key, value in result.items():
            real_act_date = ''
            for item in value:
                if item and item[0] > real_act_date:
                    real_act_date = item[0]
            csv_writer.writerow([key, real_act_date])


if __name__ == '__main__':
    handle()
