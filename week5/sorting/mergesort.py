def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    print("Merging ",nlist)

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

# Output
#Splitting  [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]

#Splitting  [55, 31, 26, 20, 63]

#Splitting  [55, 31]

#Splitting  [55]

#Merging  [55]

#Splitting  [31]

#Merging  [31]

#Merging  [31, 55]

#…….

#Merging  [40]

#Merging  [40, 81]

#Merging  [40, 74, 81]

#Merging  [7, 40, 51, 74, 81]

#Merging  [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

#Sorted: [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]