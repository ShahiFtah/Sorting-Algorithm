def sort(A):
    n = len(A)
    for i in range(1, n):
        j = i
        #Flytter det nåværende elementet til venstre så lenge det er mindre enn det forrige elementet,
        #noe som plasserer det på riktig posisjon i den delvis sorterte listen.
        while j > 0 and A[j - 1] > A[j]:
            A.swap(j, j - 1) #Bytter plasser
            j = j - 1

    return A # Returnerer listen A (den er sortert)
#Det er egentlig nesten det samme som bubble sort bare at vi flytter hvert element til sin riktige posisjon,
#mens bubble sort flytter det største elementet til slutten