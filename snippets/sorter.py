import logging

logging.basicConfig(level=logging.DEBUG)

def quicksort(A, lo, hi):
    logging.debug(f"quicksort({A}, {lo}, {hi})")
    
    if lo < hi:
        pivot_index = partition(A, lo, hi)
        quicksort(A, lo, pivot_index - 1)
        quicksort(A, pivot_index + 1, hi)
    

def partition(A, lo, hi):
    pivot = A[hi]
    logging.debug("Pivot", pivot)
    i = lo - 1
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            logging.debug(f"Swapping {A[i]} and {A[j]}, {A}")
            # Swap A[j] into the low partition and move the boundary
            A[i], A[j] = A[j], A[i]
            
    # Swap hi and i+1 to put the pivot in the right place
    A[i+1], A[hi] = A[hi], A[i+1]
    return i + 1            

mylist = [12, 29, 30, 45, -11, 11, 10, 0, 25]

quicksort(mylist, 0, len(mylist) - 1)
print(mylist)