def hello_func():
    pass

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_info('math', 'art', name = 'John', age = 22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age' : 22}

student_info(*courses, **info)