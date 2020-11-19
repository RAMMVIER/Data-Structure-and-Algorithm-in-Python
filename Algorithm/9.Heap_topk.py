# Top-k问题：取一串数中前k个最大的数
#   1.取列表前k个元素建立小根堆，堆顶是目前第k大的数
#   2.以此向后遍历列表，对于列表中的元素，如果小于堆顶，则忽略；如果大于堆顶，则将堆顶元素更换为该元素，并对堆进行一次调整
#   3.遍历列表所有元素后，倒序弹出堆顶


# 小根堆调整
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    else:
        li[i] = tmp


def topk(li, k):
    # 建堆
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 遍历
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 排序，逆序出数
    for i in range(k - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(heap, 0, i - 1)
