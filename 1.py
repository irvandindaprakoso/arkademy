class getbiodata(dict):
    def __init__(self): 
        self = dict() 
          
    def add(self, key, value): 
        self[key] = value 
    

dict_obj = getbiodata()

dict_obj.add('name',input('your name: '))
dict_obj.add('age',input('your age: '))
dict_obj.add('address',input('your address: '))
dict_obj.add('hobbies',input('your hobbies: ').split())
dict_obj.add('is_married',input('are you married ? True/False: '))
# array of object (list school)
dict_obj['list_school']= getbiodata()
dict_obj.nested_dict('list_school','name', input('school name : '))
dict_obj.nested_dict('list_school','year_in', int(input('year in : ')))
dict_obj.nested_dict('list_school','year_out', int(input('year out : ')))
dict_obj.nested_dict('list_school','major', input('major : '))
# array of object (skills)
dict_obj['skills']= getbiodata()
dict_obj.nested_dict('skills','skill_name', input('skill name : '))
dict_obj.nested_dict('skills','level', input('level : '))

dict_obj.add('interest_in_coding',input('are you interest in coding? True / False : '))
print(dict_obj)
