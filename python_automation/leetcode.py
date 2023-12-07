def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for idx, num in enumerate(nums):
        if idx == 0:
            result.append(num)
        else:

            result.append(sum(nums[:idx], num))
    return result


# result = runningSum([1, 2, 3, 4])
# print(result)

def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0
    while True:
        if num % 2 != 0:
            num = num - 1
            steps += 1
            if num == 0:
                return steps
            num = num / 2
            steps += 1
            if num == 0:
                return steps
        else:
            num = num / 2

            if num == 0:
                return steps
            steps += 1


# steps = numberOfSteps(14)
# print(steps)
def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    length = len(list(head))
    list_node_len = 0
    for link in head:
        list_node_len += 1
    print(list_node_len)

    if length % 2 == 0:
        return head[int(length/2)]
    else:
        num = int(length / 2)
        return head[num]


# middle = middleNode([1, 2, 3, 4, 5, 6])
# print(middle)

def chek_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    list_1 = list(s1)
    list_2 = list(s2)
    freq_1 = {}
    for char in list_1:
        if char in list_2:
            freq_1[char] = 1
        else:
            return False
    return freq_1


print(chek_anagram('angered', 'enraged'))
