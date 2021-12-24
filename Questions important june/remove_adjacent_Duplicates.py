def remove_adjacent_duplicates(s):
    st=[]
    for i in s:
        if len(st)==0:
            st.append(i)
        elif st[-1]==i:
            st.pop()
        else:
            st.append(i)
    return st



def recursive_remove_adjacent_duplicates(s):
    pass

print(remove_adjacent_duplicates('mississippi'))