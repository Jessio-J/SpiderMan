import json

json_list = ['result_BiLSTM.json', 'result_ContextAware.json', 'result_GCN.json']

correct_list = []
incorrect_list = []


def main():
    pass


def read_file():
    f1 = open('dev.json', encoding='utf-8')
    standard_list = json.loads(f1.read())
    dict_list = []
    for file_name in json_list:
        f = open(file_name, encoding='utf-8')
        dict_list.append(list_to_dict(json.loads(f.read())))
        f.close()
    return standard_list, dict_list


def list_to_dict(list):
    dict_rt = {}
    for i in range(len(list)):
        title = list[i]['title']
        if title in dict_rt.keys():
            rlist = dict_rt[title]
            rlist.append({'ht': str(list[i]['h_idx']) + ',' + str(list[i]['t_idx']), 'r': list[i]['r'], 'i': i})
        else:
            dict_rt[title] = [{'ht': str(list[i]['h_idx']) + ',' + str(list[i]['t_idx']), 'r': list[i]['r'], 'i': i}]
    return dict_rt


def count(s_list, dicts):
    standard_list = s_list
    for i in range(len(standard_list)):
        title = standard_list[i]['title']
        label_list = standard_list[i]['labels']
        for label in label_list:
            ht = str(label['h']) + ',' + str(label['t'])
            r = label['r']
            evidence_count = len(label['evidence'])
            for i in range(len(dicts)):
                get_result_from_dict(title, ht, r, dicts[i], i, evidence_count)


def get_result_from_dict(title, ht, r, dict_to_search, i, evidence_count):
    if title in dict_to_search.keys():
        ht_list = dict_to_search[title]
        for ht_d in ht_list:
            if ht == ht_d['ht']:
                if r == ht_d['r']:
                    while len(correct_list) < i + 1:
                        model_correct_list = []
                        correct_list.append(model_correct_list)
                    model_correct_list = correct_list[i]
                    while len(model_correct_list) < evidence_count + 1:
                        model_correct_list.append(0)
                    model_correct_list[evidence_count] = model_correct_list[evidence_count] + 1
                else:
                    while len(incorrect_list) < i + 1:
                        model_correct_list = []
                        incorrect_list.append(model_correct_list)
                    model_correct_list = incorrect_list[i]
                    while len(model_correct_list) < evidence_count + 1:
                        model_correct_list.append(0)
                    model_correct_list[evidence_count] = model_correct_list[evidence_count] + 1


def write_file():
    with open('count.json', 'r+', encoding='utf-8') as f:
        f.truncate()
        f.write('correct_list:  '+str(correct_list) + '\n')
        f.write('incorrect_list:  '+str(incorrect_list) + '\n')
        f.close()


if __name__ == '__main__':
    # main()
    standard_list, dict_list = read_file()
    count(standard_list, dict_list)
    write_file()
