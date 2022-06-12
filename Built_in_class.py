# Write a Python class to implement pow(x, n)
# Explanation:
# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
# You must implement it using Class



# Sample_Input=x= 10,n= 2
# Sample_Output=100
class power:
    def pow(self,x,n):
        if x ==1 or x==0 :
            return x

        if x == -1:
            if x % 2==0:
                return 1
            else:
                return -1       

        if n == 0:
            return 1  
        if n<0:
            return 1/self.pow(x, -n) 

        value = self.pow(x, n//2)  
        if n%2==0:
            return value*value
        return value*value*x    


power_obj = power()
print(power_obj.pow(10, 2))


