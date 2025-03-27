def heapify(A, n, i):
    largest = i  #Initialiserer largest som roten
    left = 2 * i + 1  #Venstre barn = 2*i + 1
    right = 2 * i + 2  #Høyre = 2*i + 2

    #Sjekker om venstre barn finnes og er større enn roten
    if left < n and A[left] > A[largest]:
        largest = left

    #Sjekker om høyre barn finnes og er større enn det største så langt
    if right < n and A[right] > A[largest]:
        largest = right

    #Bytter rot hvis nødvendig
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # swap

        #Bytter rot hvis nødvendig
        heapify(A, n, largest)

def heap_sort(A):
    n = len(A)

    #Bytter rot hvis nødvendig
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    #Ekstraherer elementer én etter én
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap-er plass
        heapify(A, i, 0)

    return A #Returnerer den sorterte listen

#Koden implementerer heapsort, som bygger et maksheap og sorterer listen
#ved å gjentatte ganger bytte roten med det siste elementet og gjenopprette heap-strukturen.