import time
start_time=time.time()

for i in range(100):
    for j in range(1000):
        # After printing 0 give space as end="SPACE" .
        print(0,end =" ")
    print()

# round the time taken for completion of the code by decimal to 7 decimal places.
print(round((time.time() - start_time),7)," Seconds.")


def sum_of(*args):
    sum=0
    for x in args:
        sum+=x
    return sum
print(sum_of(5,6,7))


def kwargs_sum(**kwargs):
    sum0 =0
    for k,v in kwargs.items():
        sum0+=v
    return sum0
        
print(kwargs_sum(coffee=2.44, cake=4.55, millet=5.67))
