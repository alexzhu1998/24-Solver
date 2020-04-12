# This function permutes the list
def permutate(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    l = []
    for i in range(len(lst)):
        m = lst[i]
        ## prints remainder of the list
        remlst = lst[:i] + lst[i+1:]

        # recursive function to append to list
        for p in permutate(remlst):
            if type(p) == list:
                l.append([m]+p)
            else:
                l.append([m]+[p])
    return l

def cartProd(*args,repeat=1):
    # Creating list of lists
    pools = [pool for pool in args] * repeat
    result = [[]]
    for pool in pools:
        # for x in result: 
        #     print(x)
        #     for y in pool:
        #         result.append(x+[y])
        result = [x+[y] for x in result for y in pool]
    return result



def solver(lst,target):
    l = []
    
    for p in permutate(lst):
        # Listing all possible operations
        operations = [add,sub,mult,div,sub_from,div_from]
        for item in cartProd(operations,repeat = 3):
            # Manual code of possible operations
            x = item[2](item[1](item[0](p[0],p[1]),p[2]),p[3])
            if x == target:
                l.append([p[0],item[0].__name__,p[1],item[1].__name__,p[2],item[2].__name__,p[3]])
                print("Solution")
                print(p)
                print(p[0],item[0].__name__,p[1],item[1].__name__,p[2],item[2].__name__,p[3])
    
    return l


def div(dividend,divisor):
    if dividend == None or divisor == None:
        return None
    if divisor == 0 or dividend%divisor != 0 :
        return None
    else:
        return dividend//divisor
def mult(a,b):
    if a == None or b == None:
        return None
    return a*b

def sub(a,b):
    if a == None or b == None:
        return None
    if a>=b:
        return a-b
    else:
        return None

def add(a,b):
    if a == None or b == None:
        return None
    return a+b

def sub_from(a,b):
    if a == None or b == None:
        return None
    if a<=b:
        return b-a
    else:
        return None

def div_from(divisor,dividend):
    if dividend == None or divisor == None:
        return None
    if divisor == 0 or dividend%divisor != 0:
        return None
    else:
        return dividend//divisor


# result[0].append([6,4,3,2])
# permutate(result[0][0])
# for p in permutate(result[0][0]):
#     print(p)
# curset = 0
# curlvl = 0
# d = dict()

# operations = [add,sub,mult,div]
# for item in cartProd(operations, repeat=3):
#     print(item[1](item[0](2,4),3))
# print(range(2))
# for item in cartProd('ABCD', 'xy'):
#     print(item) 
# print(cartProd(['add','sub','mult',],repeat = 3))
# print([2,4,3])
# p = [1,2]
# print(p[2:].insert(0,0))
# p = [1,2]
# print(permutate([1,2]))
# operations = [add(p[0],p[1]),sub(p[0],p[1]),mult(p[0],p[1]),div(p[0],p[1])]
# print(operations)

# for curlvl in range(3):
#     for curset in range(len(result[curlvl])):
#         # print(result)
        
#         a = [result[curlvl][curset][0],result[curlvl][curset][1]]


#         operations = [add(a[0],a[1]),sub(a[0],a[1]),mult(a[0],a[1]),div(a[0],a[1])]
#         for item in operations:
#             if item != None:
#                 tmp = result[curlvl][curset][2:]
#                 tmp.insert(0,item)
#                 result[curlvl+1].append(tmp)

# print(result[3]) 


# print(operations[0])


# for index,item in enumerate(operations):
#     if item != None:
#         tmp = p[2:]
#         tmp.insert(0,item)
#         # op.append(index)
#         # p.insert(2,item)
#         # print(item)
#         # print(p)
#         # p = p[2:]
#         if index == 0:
#             oper = "add"
#         elif index == 1:
#             oper = "subtract"
#         elif index == 2:
#             oper = "multiply"
#         elif index == 3:
#             oper = "divide"
#         print(p)
#         tmp2 = p + oper
#         print(tmp2)
#         d[tuple(tmp2)] = tmp

#         if type(tmp) == list:
#             dfs(tmp,index,d)
#         else:
#             dfs(list(tmp),index,d)