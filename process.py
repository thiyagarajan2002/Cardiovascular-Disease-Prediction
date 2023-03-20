from Database import Data


def sign_up(name,phone_number,email,password):
    db=Data('APH')
    data={"Name":name,"Phone_number":phone_number,"Email_id":email,"Password":password}
    db.Insert_data('User_details',data)
    return True

def login(email,password):
    db=Data('APH')
    tup=list(db.Read_data('User_details','*','Email_id=\''+email+"\'"))
    if tup:
        tup=tup[0]
        if tup[3]==email and tup[4]==password:
            return True
        else:
            return False
    else:
        return False


def store(user_id,result):
    db=Data('APH')
    data={"User_id":user_id,"Result":result}
    db.Insert_data('Disease_Datas',data)
    return True

def get_id(email):
    db=Data('APH')
    condition="Email_id=\'{}\'".format(email)
    id=db.Read_data('User_details',"User_id",condition)
    if len(id):
        return id[0][0]
    else:
        return "NA"
#Testing
#print(get_id("tr2002@gmail.com"))
#Sign up
#print(sign_up("trj","6369671812","trj@gmail.com","trj9543460192"))
#True

#login
#print(login("trj@gmail.com","trj9543460192"))

#store
#print(store(1,1))


"""
#insert
#dt=Data("user_details")
#data = {"name": "John Smith","salary":30000}
#dt.Insert_data("user_details", data)


#read
#s=dt.Read_data('user_details','*','id=3')
#print(s)
#[(3, 'John Smith', 30000.0)]
"""
