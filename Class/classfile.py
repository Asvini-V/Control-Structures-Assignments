class MultiFunction():
    def Subfields():
        list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Subfields in AI are:")
        for i in list:
            print(i)
            
    def OddEven():
        num=int(input("Enter a number:"))  
        if num%2==0:
            print(num, "is Even number")
        else:
            print(num, "is Odd number")  
            
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if Gender=="Male":

            if Age>21:
#                 print("ELIGIBLE")
                Elg="ELIGIBLE"
            else:
#                 print("NOT ELIGIBLE")
                Elg="NOT ELIGIBLE"

        elif Gender=="Female":  
            if Age>18:
#                 print("ELIGIBLE")
                Elg="ELIGIBLE"
            else:
#                 print("NOT ELIGIBLE")
                Elg="NOT ELIGIBLE"
        return Elg
    
    def percentage():
        Subject1=int(input("Subject1:"))
        Subject2=int(input("Subject2:"))
        Subject3=int(input("Subject3:"))
        Subject4=int(input("Subject4:"))
        Subject5=int(input("Subject5:"))
        Total= Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",Total)
        Percentage=(Total/500)*100
        print("Percentage:",Percentage)
        
        
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area=(Height*Breadth)/2
        print("Area of Triangle:",Area)

        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1 + Height2 + Breadth
        print("Perimeter of Triangle:", Perimeter)
        return Area,Perimeter
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        