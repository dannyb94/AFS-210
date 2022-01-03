def mergeSort(nlist):
        print("Splitting ",nlist)
        # insert your code to complete the mergeSort functionz
        if len(nlist) <= 1:
            return nlist

        listLen = len(nlist) // 2
        pl1 = mergeSort(nlist[listLen:])
        pl2 = mergeSort(nlist[:listLen])
        
        print("Merging ",nlist)
        return merge(nlist, pl1, pl2)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist


l1 = [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]

# At each stage, print the status of the list as it is split and merged.
print(mergeSort(l1))