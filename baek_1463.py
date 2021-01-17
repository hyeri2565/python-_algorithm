N=int(input())

def make_one(n):
    math_count=0
    while n!=1:
        if n%3!=0 and n%2!=0:
            n-=1
            math_count+=1
            print('n-1 performed')
        elif n%3==0:
            while n%3==0:
                n=n/3
                math_count+=1
                print('n/3 performed')
        elif n%2==0:
            while n%2==0:
                n=n/2
                math_count+=1
                print('n/2 performed')
    return math_count
print(make_one(N))