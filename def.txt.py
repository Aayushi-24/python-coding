class employee:
    def hello_emp(self,ename=None):
        if ename is not None:
            print("hello" + ename)
        else:
            print("hello")
emp1=employee()
emp1.hello_emp()
emp1.hello_emp("aayushi")