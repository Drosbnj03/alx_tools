def validate_password(password):
    u,l,d,s=0,0,0,0
    if len(password) < 8:
        return False
    for letter in password:
        if letter.isupper():
            u+=1
        if letter.islower():
            l+=1
        if letter.isdigit():
            d+=1
        if letter.isspace():
            s+=1
    if u == 0 or l== 0 or d== 0 or s!=0:
        return False
    return True    
    
    
    

