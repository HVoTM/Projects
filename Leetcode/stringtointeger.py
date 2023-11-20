if __name__ == '__main__':
    s = ' 1234  '
    
    if s == '':
        print(0)

    int_return = ''

    for ch in s:
    
        while ch != '+' and ch != '-' and not ch.isdigit() :
            continue

        # Check if 
        if ch == '-' or ch == '+':
            int_return += ch
            continue
        while ch.isdigit():
            int_return += ch
                    
    print(int_return)
       
