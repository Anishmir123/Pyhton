course = {
    'php':{'duration':'2 month','fees':'15000'},
    'python':{'duration':'3 month','fees':'10000'},
    'java':{'duration':'4 month','fees':'15000'}

}
#print(course)
#print(course['java']['fees'])

for k,v in course.items():
    print(k,v['duration'],v['fees'])
