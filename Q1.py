def isBal(s):
    st = []
    ob = ['{','[','(']
    for i in s:
        if i in ob:
            st.append(i)
        else:
            if not st:
                return False
            if (i == '}' and st[-1] == '{') or (i == ']' and st[-1] == '[') or (i == ')' and st[-1] == '('):
                st.pop()
            else:
                return False
            
    if len(st):
        return False
    else:
        return True
    

s = input("Enter Brackets:")
print("Bracket balanced?  ",isBal(s))