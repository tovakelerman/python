def print_args_kwargs(*args,**kwargs):
    print(args)
    for i, value in kwargs.items():
        print(i, value)

print_args_kwargs(1,2,3,4,i=5,p=4)

def find_student(name,studentDict):
   for key ,value in studentDict.items():
       if name == key:
           return value
   return "this student don't exist"

my_dict={"rut":"id=21548751 , age=20","tami":"id=21562652 , age=10","sara":"id=215465224 , age=15"}

print(find_student('rut',my_dict))
