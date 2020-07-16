#1.)prime number program
def prime(num):
  if num>1:
     for i in range(2,num):
          if num%i==0:
              print(num,'is not a prime number')
              break           
     else:
         print(num, 'is prime')
  else:
    print('its is not') 
prime(num=int(input("pass input value to check whether number is prime or not")))


# 2.)Program for finding how many pairs count of a given list
def pair_count(num_list):
    m=dict()
    for i in x:
        m.update({i:x.count(i)})
    for key,val in m.items():
        if val>1:
            if val//2:
                print("these are the pairs ({},{}) {}".format(key,key,val//2))

x=[10,10,20,20,40,40,40,20,10,40]
pair_count(x)
"""
res: 
these are the pairs (10,10) 1
these are the pairs (20,20) 1
these are the pairs (40,40) 2
"""

#3.)program for sum of list numbers
def summ(num):
       sum=0
       for i in num:
              sum+=i
       print(sum )            
summ(num=[1,2,3,4])

#4.) Find the biggest word in a given list
def FyndBig(x):
        b=x.split(' ')
        c=''
        j=b[0]
        for i in range(len(b)-1):
            if len(b[i])>len(j):
               j=b[i]
        print(j)
            
FyndBig (input(''))#input format : textword text_word

#5.) Program
def func(num):
       for i in range(1,num+1):
              for j in range(1,num+1):
                    print(i,end=' ')
              print()
func(num=int(input()))#input :4
"""
res
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4 
"""
#6.)Program
def print_star(num):
       for i in range(1,num+1):
             print(i*'*')
print_star(num=int(input()))
"""
res
*
**
***
****
*****
"""
#7.)Program
def print_nums(a):
    for i in range(1,a+1):
        print(i*str(i))
        i=i+1
        if i==a+1:
            i=i-1
            for j in range(1,i+1):
                print((i-j)*str(i-j))
a=int(input())
print_nums(a)
"""
result:
1
22
333
4444
333
22
1
"""
#8.) Program for reverse string
def func(x):
    for i in range(1,len(x)+1):
        print(x[-i],end='')
func(x=input())

#9.)Program for printing charc "C" with '*'
def print_C(val):
    for i in range(1,val+1):
        if i==1:
            print(val*' *')
        if i==val:
            print(val*' *')
        else:
            print('*')
val=int(input())
print_C(val)

#10.)Program -- Missing elements from a list
def missing_elements(list_num):
    for i in range(min(array),max(array)+1):
        if i not in array:
            print(i, end = " ")
array=[1,2,3,4,6,7,8,19,30,24]
missing_elements(array)

#11.)Program for finding the pair of sum values from a list
def find_pair_sum_val(array,val):
    pair_list=[]
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==val:    
               pair_list.append((array[i],array[j]))
    print(pair_list)
array=[2,3,5,6,7,8]
val=11           
find_pair_sum_val(array,val)  

#12.)Program
def print_nums(val):
    a=''
    for i in range(1,val+1):
        a+=str(i)
        print (a,end=' ')
val=int(input())
print_nums(val)#val=5
# result:1 12 123 1234 12345 

#13.) Program
def print_pattern(chars):
    char_len=len(chars)                 # result of this check below @res
    for i in range(1,len(chars)+1):     #for i in range(1,len(chars)+1):                                                                               
        print(a[0:char_len])            #      print(a[0:i])
        char_len=char_len-1
a="abcdef"
print_pattern(a)
"""
result:       @res
abcdef        a
abcde         ab
abcd          abc  
abc           abcd
ab            abcde  
a             abcdef  
"""
#14.) Program to check odd sum of 1 and even sum of 2 from a list
def func(array,a):
    count =0
    for i in arr:
        if a==1:
            if i%2!=0:
                count+=i
        elif a==2:
            if i%2==0:
                count+=i
        else:
            return "chose 1 or 2"
    return count
    
arr=[4,2,3,6,8]
a=int(input())
obj=func(arr,a)

# 15.)Program
def print_rhombus(val):
    for i in range(1,a+1):
        print((a-i)*' '+i*'*'' ')
        if i==a:
            a1=1
            b=a-1
            for j in range(1,a+1):
                print ((a1+j)*' ',end='')
                print ((b*'*'' ')
                b=b-1
                a1=a1+1
a=int(input())
print_rhombus(a)

# 16.)Program
def pattern(val):
    c=''
    for i in range(1,val+1):
          if i%2==0:
             c+='*'
          else:
             c+=str(i)
             print(c)
pattern(val=5)
"""
result:
1
1*3
1*3*5
"""
# 17.)Program
def pattern_print(val):
    for m in range(1,val+1,2):
          print((val-m)*' ',end=' ')
          print((m)*'*'' ')
pattern_print(val=5)
"""
result:
     * 
   * * * 
 * * * * *
 """
# 18.)Program
#BOX or Square
def BOX(val):
    print(val*'*'' ')
    for i in range(0,val):
        print('*'+(val-2)*' '' '+' ''*')
    print (val*'*'' ')
BOX(val=3)
"""
Output
* * * 
*   *
*   *
*   *
* * *
"""

































