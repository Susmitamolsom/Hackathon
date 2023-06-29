# def list_sum(num_list):
#     if len(num_list)==1:
#         return num_list[0]
#     else:
#         return num_list[0]+list_sum(num_list[1:])
# print(list_sum([2,4,5,6,7]))
a=int(input(" "))
b=int(input("2nd "))
s=0
i=1
while a<0 or i<a:
    if i%b==0:
        s=i
    a=a+1
    i=i+1
print(s)