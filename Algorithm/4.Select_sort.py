# 选择排序，每次遍历中选择最小的元素，与列表第一个元素交换位置，实现原地排序


# 简单版选择排序，需要两个list，且需要对原list进行min、append、remove操作，效率过低
def select_sort_simple(li):                # 时间复杂度：O(n^2)
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    


# test
test_list = [3, 4, 6, 7, 8, 1, 9, 2, 5]
print(select_sort_simple(test_list))