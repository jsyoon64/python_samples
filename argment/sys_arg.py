import sys

print (sys.argv)
argv1 = sys.argv[1:]
# argv1 = sys.argv

print(f'{len(argv1)=}')
for index,arg in enumerate(argv1):
    print(f'{index=},{arg=}')