import json

jsonuser = """

{
    "name" : "abhinav",
    "age" : 20,
    "islanguage" : false,
    "skills" : ["java,py,linux"],
    "address" : {
        "email" : "abhiavai" ,
        "street" : 1
    }
} 
"""

userdict = json.loads(jsonuser)
print(type(userdict)) #dictionary


todo = {
    "name" : 212
}

convert_pyobj_jsonstr = json.dumps(todo)
print(type(convert_pyobj_jsonstr)) #string