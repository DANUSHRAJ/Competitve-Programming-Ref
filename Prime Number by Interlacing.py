def isPrime(n):
   # Checking for cases of 2 and 3
   if (n <= 1):
      return 0
   if (n <= 3):
      return 1
   # skip checking middle five numbers in the loop
   if (n % 2 == 0 or n % 3 == 0):
      return 0
   i = 5
   while (i * i <= n):
      if (n % i == 0 or n % (i + 2) == 0):
         return 0
      i = i + 6
   return 1

num1,num2=map(str,input().split())

# interlacing string
#By using zip_longest->string = "".join([ x + y for x, y in itertools.zip_longest(num1, num2, fillvalue="")])

string = list(num2)
for i,c in enumerate(num1):string.insert(i*2,c);#print(string)
string="".join(string)

if isPrime(int(string)):print("%s and %s Interlaced is %s is a Prime Number"%(num1,num2,string))
else:print("%s and %s Interlaced is %s is Not a Prime Number"%(num1,num2,string))
