#Bubble Sorting 
# Mutates 1st so that it is sorted via swapping adjacent elements until the entire 1st sorted.

class Problem4434(object):
    def bubble_sort(self, lst):
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(lst)-1):
                if lst[i]>lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    has_swapped = True
        return lst
    
if __name__ == "__main__":
    solution = Problem4434()
    lst = [7,3,2,1,5,6,10, 9,8]
    print(solution.bubble_sort(lst))