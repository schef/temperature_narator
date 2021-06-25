#!/usb/bin/env python3

degree_list = [i for i in range(-15, 101)]
name_list = ["./%s.mp3" % (("%04d" % (i))) for i in range(1, 118)]

for i in range(len(name_list)):
    name = name_list[i]
    degree = degree_list[i]
    print(degree, name)