# TODO Напишите функцию для поиска индекса товара

def ind_of_arr(arr, thing):
    ans = ''
    for i in range(len(arr)):
        if thing == arr[i]:
            ans = i
            break
        else:
            ans = None
    return ans


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = ind_of_arr(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
