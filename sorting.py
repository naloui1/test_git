# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place de deux éléments dans un tableau"""
    """Échange la place des éléments aux indices i et j du tableau"""
    tab[j], tab[i] = tab[i], tab[j]
    return tab   

# ---------------
# Tris classiques
# ---------------
def bubble_sort(tab):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    tab_sorted=tab.copy()
    n = len(tab_sorted)
    for i in range(n,1,-1):
        for j in range (0, i- 1):
            if tab_sorted[j+1] < tab_sorted[j]:
                swap(tab_sorted,j,j+1)
                #A_sorted[j], A_sorted[j+1] = A_sorted[j+1], A_sorted[j]
    return tab_sorted


def insertion_sort(tab):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    tab_sorted=tab.copy()
    n=len(tab_sorted)
    
    for i in range(1,n):
        x=tab_sorted[i]
        j=i
        while j>0 and x<tab_sorted[j-1]:
            tab_sorted[j]=tab_sorted[j-1]
            j=j-1
        tab_sorted[j]=x
        
    return tab_sorted


def selection_sort(tab):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    tab_sorted=tab.copy()
    n=len(tab_sorted)
    for k in range(n):
        mini=tab_sorted[k]
        index_mini=k
        for i in range(k+1,n):
            if tab_sorted[i]<mini:
                mini=tab_sorted[i]
                index_mini=i
        swap(tab_sorted,  index_mini,k)     
    return(tab_sorted)


# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    merge_sort_r(tab, 0, len(tab))    

def merge_sort_r(tab, start, end):
    if start<end-1:
        m=(start+end)//2                #<=> m=int((start+end)/2) 
        merge_sort_r(tab, start, m)
        merge_sort_r(tab, m, end)       # ATTENTIOn erreur dans le pseudo-code: faut mettre m et non pas m+1
        merge(tab,start,m,end)        
    
def merge(tab, start, middle, end):
    i=start
    j=middle
    temp=[]
    #tab_new=tab.copy()
    for k in range(start,end):
        if i<middle and j<end:
            if tab[i] <= tab[j]:
                temp.append(tab[i])
                i=i+1
            else:
                temp.append(tab[j])
                j=j+1
        else:
            if i<middle:
                temp.append(tab[i])
                i=i+1
            else:
                temp.append(tab[j])
                j=j+1
    for k in range(start,end):
        tab[k]=temp[k-start] 
        
    

def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    if len(tab) <=1:
        return tab
    pivot=tab.pop()
    
    petit=[]
    grand=[]
    
    for nombre in tab:
        if nombre < pivot:
            petit.append(nombre)
        else:
            grand.append(nombre)
    return quick_sort(petit)+[pivot]+quick_sort(grand)
