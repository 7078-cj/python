courses = ['History', 'Programming', 'Science'] #list

for index, course in enumerate(courses, start=1):
    print(index, course)
    
course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')

print(new_list)

#sets 
cs_course = {'History', 'Math', 'Physics', 'CompSci'}
art_course = {'History', 'Math','Art', 'Design'}

print(cs_course.intersection(art_course)) #it show where the two sets intersects
print(cs_course.difference(art_course)) #it show what the cs_course has that the art_course doesnt have
print(cs_course.union(art_course)) #it ads the 2 sets together