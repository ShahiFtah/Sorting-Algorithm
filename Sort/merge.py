def merge(A1, A2, A):
    i = 0
    j = 0
    #Her slår vi sammen A1 og A2
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            A[i + j] = A1[i] #Kopier elementer fra A1 til A
            i += 1
        else:
            A[i + j] = A2[j] #Kopier elementer fra A2 til A
            j += 1

    #Her koperer vi de gjenstående elementene fra A1 til A
    while i < len(A1):
        A[i + j] = A1[i]
        i += 1 

    #Her gjør vi det samme som while-løkken over men med A2
    while j < len(A2):
        A[i + j] = A2[j]
        j += 1 
    return A

def sort(A):
    if len(A) <= 1:
        return A
    i = len(A) // 2
    A1 = sort(A[:i])
    A2 = sort(A[i:])

    #Slå sammen og returner den sorterte listen:
    return merge(A1, A2, A)

#Denne merge funksjonen slår sammen to sorterte lister til en ved å sammenligne
#elementene ved bruk at sort funksjonen som deler listen rekursivt før den slår de sammen
