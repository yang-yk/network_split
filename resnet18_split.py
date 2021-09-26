from STtable.adapter import testcase
import collections
import json

if __name__=='__main__':

    src_all_st_matrix, dst_all_st_matrix, all_used_core_num, core_group = testcase()

    groups = collections.OrderedDict()
    groups[0] = [0]
    groups[1] = [1,2,3]
    groups[2] = [4,5,6]
    groups[3] = [7,8,9,10]
    groups[4] = [11,12,13]
    groups[5] = [14,15,16,17]
    groups[6] = [18,19,20]
    groups[7] = [21,22,23,24]
    groups[8] = [25,26,27]

    groups_core_num = collections.OrderedDict()
    for i in range(len(groups)):
        num = 0
        for core_id, group_id in core_group.items():
            if (group_id-1) in groups[i]:
                num = num + 1
            if i==0 and (group_id-1)==-1:
                num = num + 1
        groups_core_num[i] = num



    new_src_all_st_matrix = []
    new_dst_all_st_matrix = []

    for key,group in groups.items():
        if len(group)==1:
            new_src_all_st_matrix.append(src_all_st_matrix[group[0]])
        elif len(group)==3:
            group_st = collections.OrderedDict()
            layer_0_st = src_all_st_matrix[group[0]]
            layer_1_st = src_all_st_matrix[group[1]]
            layer_2_st = src_all_st_matrix[group[2]]
            group_st.update(layer_0_st)
            group_st.update(layer_1_st)
            group_st.update(layer_2_st)
            new_src_all_st_matrix.append(group_st)
        #残差块层串联方式
        elif len(group)==4:
            group_st = collections.OrderedDict()
            group_st = collections.OrderedDict()
            layer_0_st = src_all_st_matrix[group[0]]
            layer_1_st = src_all_st_matrix[group[1]]
            layer_2_st = src_all_st_matrix[group[2]]
            layer_3_st = src_all_st_matrix[group[3]]
            group_st.update(layer_0_st)
            group_st.update(layer_1_st)
            group_st.update(layer_2_st)
            group_st.update(layer_3_st)
            new_src_all_st_matrix.append(group_st)


    for key,group in groups.items():
        if len(group)==1:
            new_dst_all_st_matrix.append(dst_all_st_matrix[group[0]])
        elif len(group)==3:
            group_st = collections.OrderedDict()
            layer_0_st = dst_all_st_matrix[group[0]]
            layer_1_st = dst_all_st_matrix[group[1]]
            layer_2_st = dst_all_st_matrix[group[2]]
            group_st.update(layer_0_st)
            group_st.update(layer_1_st)
            group_st.update(layer_2_st)
            new_dst_all_st_matrix.append(group_st)
        #残差块层串联方式
        elif len(group)==4:
            group_st = collections.OrderedDict()
            group_st = collections.OrderedDict()
            layer_0_st = dst_all_st_matrix[group[0]]
            layer_1_st = dst_all_st_matrix[group[1]]
            layer_2_st = dst_all_st_matrix[group[2]]
            layer_3_st = dst_all_st_matrix[group[3]]
            group_st.update(layer_0_st)
            group_st.update(layer_1_st)
            group_st.update(layer_2_st)
            group_st.update(layer_3_st)
            new_dst_all_st_matrix.append(group_st)

    final_src_all_st_matrix = []
    final_dst_all_st_matrix = []

    for src_group_st in new_src_all_st_matrix:
        f_src_group = collections.OrderedDict()
        num = 0
        for key,val in src_group_st.items():
            f_src_group[str(num)+key] = val
            num = num + 1
        final_src_all_st_matrix.append(f_src_group)

    for dst_group_st in new_dst_all_st_matrix:
        f_dst_group = collections.OrderedDict()
        num = 0
        for key,val in dst_group_st.items():
            f_dst_group[str(num)+key] = val
            num = num + 1
        final_dst_all_st_matrix.append(f_dst_group)

    # with open('./st_table_json/src_all_st_matrix.json', 'w') as f:
    #      json.dump(final_src_all_st_matrix, f)
    #
    # with open('./st_table_json/dst_all_st_matrix.json', 'w') as f:
    #      json.dump(final_dst_all_st_matrix, f)
    #
    # import numpy as np
    # with open('./st_table_json/all_used_core_num.json', 'w') as f:
    #      json.dump(str(all_used_core_num), f)
    #
    # with open('./st_table_json/group_core_num.json', 'w') as f:
    #      json.dump(groups_core_num, f)


    st_info = collections.OrderedDict()
    st_info['src'] = final_src_all_st_matrix
    st_info['dst'] = final_dst_all_st_matrix
    st_info['core_num'] = float(all_used_core_num)
    st_info['groups_core_num'] = groups_core_num

    with open('./st_table_json/st_info.json', 'w') as f:
         json.dump(st_info, f)




    print('pause')


