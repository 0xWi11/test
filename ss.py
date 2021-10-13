# coding=utf-8
a= "[1,0,1,1]"
#print(a[1:-1].split(','))
#print(type(a[1:-1].split(',')))


def check(input, rule_cnt, rules):
    hack = input[1:-1].split(',')
    print(type(hack))
    #hack = hack.split("")
    rule = rules[1:-1].split(',')
    #rule = rule.split("")
    print("rule",rule)
    mi = 1
    flag = 0
    ban =0
    start = 0
    for i in range(len(hack)):
        mi+=1
        #print(i)
        if int(hack[i]) == 1:
            start = 1
        if int(hack[i]) == 1:
            flag+=1
        if int(rule[1]) == flag and mi <= int(rule[0]):
            ban+=1
            i+=int(rule[2])
            if i > len(hack):
                break
    return ban
    # Write Code Here

print(check("[1,0,1,1,0,0,0,1]",1,"[2,2,8]"))










