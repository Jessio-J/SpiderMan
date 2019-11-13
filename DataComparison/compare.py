import json

json_list = ['result_BiLSTM.json', 'result_ContextAware.json', 'result_GCN.json']


def main():
    pass


# f = open('result_ContextAware.json', encoding='utf-8')
# res = f.read()
# dict = json.loads(res)
# print(dict[0].keys())
# print(dict[0])
# f = open('dev.json', encoding='utf-8')
# res = f.read()
# standard_list = json.loads(res)
# print(standard_list[0].keys())
# print(standard_list[0]['vertexSet'][0])
# print(standard_list[0]['vertexSet'])
# print(standard_list[0]['title'])
# print(standard_list[0]['labels'])
# print(standard_list[0]['sents'])


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


def comparison(s_list, dicts):
    standard_list = s_list
    for i in range(len(standard_list)):
        title = standard_list[i]['title']
        label_list = standard_list[i]['labels']
        for label in label_list:
            ht = str(label['h']) + ',' + str(label['t'])
            r = label['r']
            rlist = []
            for dict in dicts:
                ri = get_result_from_dict(title, ht, r, dict)
                rlist.append(ri)
            write_file(i, rlist)


def get_result_from_dict(title, ht, r, dict_to_search):
    r1 = 'F'
    r2 = ''
    r3 = '-1'
    if title in dict_to_search.keys():
        ht_list = dict_to_search[title]
        for ht_d in ht_list:
            if ht == ht_d['ht']:
                if r == ht_d['r']:
                    r1 = 'T'
                else:
                    r1 = 'F'
                r2 = ht_d['r']
                r3 = ht_d['i']
                break
    return r1, r2, r3


def write_file(i, rlist):
    with open('result.json', 'a', encoding='utf-8') as f:
        r1 = ''
        r2 = ''
        r3 = ''
        for r in rlist:
            r1 = r1 + r[0] + ','
            r2 = r2 + r[1] + ','
            r3 = r3 + str(r[2]) + ','
        result = str(i)+',' + r1 + r2 + r3
        f.write(result + '\n')
        f.close()


if __name__ == '__main__':
    # main()
    standard_list, dict_list = read_file()
    comparison(standard_list, dict_list)
