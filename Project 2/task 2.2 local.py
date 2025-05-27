import random
import heapq
import math
def search(dct):
    count = dct['count']
    size = dct['size']
    values = dct['values']
    target_sum = sum(values) / count

    def insertion_sort(lst):
        #print("sorting")
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key

    def isGoal(state):
        return len(completed) == count
    
    def random_initial_state():
        random.shuffle(values)
        state = []
        n = 0
        for i in range(count):
            state.append([])
            for j in range(size):
                state[i].append(values[n])
                n += 1
        return state
    
    def closest_pair(min_list, max_list, target):
        i = 0  # pointer for min_list
        j = 0  # pointer for max_list
        diff = float('inf')  # initialize diff as infinity
        res = ()  # initialize result pair

        # While both pointers do not exceed their list boundaries
        while(i < len(min_list) and j < len(max_list)):
            # If max_list[j] is greater than min_list[i]
            if max_list[j] > min_list[i]:
                # Calculate the absolute difference
                current_diff = abs(max_list[j] - min_list[i] - target)
                # If this pair provides a smaller difference
                if(current_diff < diff):
                    res = (i, j)
                    diff = current_diff
            # Move the pointers
            if max_list[j] - min_list[i] < target:
                j += 1
            else:
                i += 1

        return res

    def find_swaps(state):
        # looping through subsets
        change = ()
        best_deviation_change = 0
        for i in range(count):
            for j in range(i+1, count):
                # Only check sublists that are greater and smaller than the target_sum
                max_min_condition = (deviation[i] > 0 and deviation[j] < 0) or (deviation[i] < 0 and deviation[j] > 0)
                if max_min_condition:
                    deviation_before = abs(deviation[i]) + abs(deviation[j])
                    ideal_diff = deviation_before / 2
                    if deviation[i] < 0:
                        swap = closest_pair(state[i], state[j], ideal_diff)
                        if swap:
                            change = ((i, swap[0]), (j, swap[1]))
                    else:
                        swap = closest_pair(state[j], state[i], ideal_diff)
                        if swap:
                            change = ((i, swap[1]), (j, swap[0]))
                    i_value = state[i][change[0][1]]
                    j_value = state[j][change[1][1]]
                    deviation_after = abs(deviation[i] + j_value - i_value) + abs(deviation[j] + i_value - j_value)
                    if deviation_after < deviation_before:
                        return change
        return ()

    current = None
    while current is None or not isGoal(current):
        #print("restarting")
        current = random_initial_state()
        for sublist in current:
            sublist.sort()
        deviation = {}
        completed = []
        for i in range(count):
            deviation[i] = 0
            for j in range(size):
                value = current[i][j]
                deviation[i] += value
            deviation[i] -= target_sum
            if deviation[i] == 0:
                completed.append(i)

        while True:
            change = find_swaps(current)
            if not change:
                break
            else:
                sublist_1, sublist_2 = change
                i1, j1 = sublist_1
                i2, j2 = sublist_2
                x1, x2 = current[i1][j1], current[i2][j2]
                # update current lists
                current[i1][j1], current[i2][j2] = x2, x1
                insertion_sort(current[i1])
                insertion_sort(current[i2])
                # update deviation dictinoary and check for completed sublist
                deviation[i1] += x2 - x1
                if deviation[i1] == 0:
                    completed.append(i1)
                deviation[i2] += x1 - x2
                if deviation[i2] == 0:
                    completed.append(i2)
                #print(deviation)
                #print(completed)
    return current