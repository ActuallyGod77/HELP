with open('day 1.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

def split(string):
    return [char for char in string]

num_list = []
x = 0
while x < len(content):
    selection = split(content[x])
    y = 0
    while y < len(selection):
        if selection[y].isnumeric() is True:
            first = selection[y]
            y = len(selection)
        else:
            space = len(selection) - y
            if space > 3:
                c3 = selection[y] + selection[y+1] + selection[y+2]
            if space > 4:
                c4 = selection[y] + selection[y+1] + selection[y+2] + selection[y+3]
            if space > 5:
                c5 = selection[y] + selection[y+1] + selection[y+2] + selection[y+3] + selection[y+4]        
            if c3 == 'one':
                first = '1'
                y = len(selection)
            elif c3 == 'two':
                first = '2'
                y = len(selection)
            elif c5 == 'three':
                first = '3'
                y = len(selection)
            elif c4 == 'four':
                first = '4'
                y = len(selection)
            elif c4 == 'five':
                first = '5'
                y = len(selection)
            elif c3 == 'six':
                first = '6'
                y = len(selection)
            elif c5 == 'seven':
                first = '7'
                y = len(selection)
            elif c5 == 'eight':
                first = '8'
                y = len(selection)
            elif c4 == 'nine':
                first = '9'
                y = len(selection)
        y = y + 1
    y = 0
    while y < len(selection):
        if selection[-(y+1)].isnumeric() is True:
            last = selection[-(y+1)]
            y = len(selection)
        else:
            space = len(selection) - y
            if space > 3:
                c3 = selection[-(y+1)] + selection[-(y+2)] + selection[-(y+3)]
            if space > 4:
                c4 = selection[-(y+1)] + selection[-(y+2)] + selection[-(y+3)] + selection[-(y+4)]
            if space > 5:
                c5 = selection[-(y+1)] + selection[-(y+2)] + selection[-(y+3)] + selection[-(y+4)] + selection[-(y+5)]
            if c3 == 'eno':
                last = '1'
                y = len(selection)
            elif c3 == 'owt':
                last = '2'
                y = len(selection)
            elif c5 == 'eerht':
                last = '3'
                y = len(selection)
            elif c4 == 'ruof':
                last = '4'
                y = len(selection)
            elif c4 == 'evif':
                last = '5'
                y = len(selection)
            elif c3 == 'xis':
                last = '6'
                y = len(selection)
            elif c5 == 'neves':
                last = '7'
                y = len(selection)
            elif c5 == 'thgie':
                last = '8'
                y = len(selection)
            elif c4 == 'enin':
                last = '9'
                y = len(selection)
        y = y + 1
    number = first + last
    num_list.append(number)
    x = x + 1

num_list = [ int(x) for x in num_list ]
print(num_list)
print(sum(num_list))
