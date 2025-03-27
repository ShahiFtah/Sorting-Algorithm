def bubble_sort(A):
    # Sorterer listen A ved å gjentatte ganger bytte plasser på naboelementer
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j] # Sorterer listen A ved å gjentatte ganger bytte plasser på naboelementer
    return A # Returnerer den sorterte listen