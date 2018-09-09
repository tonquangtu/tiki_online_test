import csv


def get_sorted_key(item):
    return item[0]


def read_csv_file(input_file_name):
    phone_dict = {}
    with open(input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            phone_number = row[0]
            date_row = [row[1], row[2]]
            if not phone_dict.get(phone_number, False):
                phone_dict[phone_number] = [date_row]
            else:
                phone_dict[phone_number].append(date_row)

    return phone_dict


def get_real_act_date(date_values):
    len_values = len(date_values)
    act_date = date_values[len_values - 1][0]
    deact_date = date_values[len_values - 1][1]

    for i in range(len_values - 2, -1, -1):
        item = date_values[i]
        if act_date > item[1]:
            break
        elif act_date == item[1]:
            act_date = item[0]
        elif deact_date == item[0]:
            deact_date = item[1]

    return act_date


def handle():
    input_file_name = 'input.csv'
    output_file_name = 'output2.csv'
    phone_dict = read_csv_file(input_file_name)

    with open(output_file_name, mode='w') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',')
        csv_writer.writerow(['PHONE_NUMBER', 'REAL_ACTIVATION_DATE'])

        for key, value in phone_dict.items():
            if len(value) > 1:
                value.sort(key=get_sorted_key)

            real_act_date = get_real_act_date(value)
            csv_writer.writerow([key, real_act_date])


if __name__ == '__main__':
    handle()
