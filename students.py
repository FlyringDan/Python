# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator_=','):
    ans = []
    fir = first_group.split(separator_)
    sec = second_group.split(separator_)
    for i in range(len(fir)):
        if fir[i] in sec:
            ans.append(fir[i])
    return ans


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
separator = '|'

print(find_common_participants(participants_first_group, participants_second_group, separator))

# TODO Провеьте работу функции с разделителем отличным от запятой
