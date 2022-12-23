print("Hello wellcome to simple multifungctional program", "This program include, Calculatr, conversion temprature")
print("Select Propgram To Use?")
print("To Use Calculator You can type 'cl' and if you want Use Conversion type 'cv' ")
query = ["1. Calculator", "2. Temprature Conversion"]
print (query)
operation =""
while operation != "quit" or operation != "exit" :
      operation = input("type your command : ")
      if operation == "quit" or operation == "exit" :
        print("Are You Sure For End This Program? ")
        q=input(" yes or no : ")
        if q  == "yes" :
            break
        if q  == "no" :
            continue
      if operation != "cl" and operation != "cv" :
          print("Command Undified")
          continue
#THIS IS FOR CONVERSION PROGRAM
      while operation == "cv" :
          print("Youa Chosing Conversion  Temprature ")
          print(("To Use Conversion You can type value of operation then you chose the operation."))
          print(" =================================    ")
          print("LIST OF Operation", "Celcius as c", "Kelvin As k", "Fahrenheit As f", "Reamur As r")
          if operation != "exit" or operation != "quit" :
              if operation =="exit" or operation == "quit" :
                  print("Are You Sure Want Exit This Program?")
                  q = input("yes or no :")
                  if q == "yes" or q =="y" :
                      exit()
                  elif q == "no" or q == "n" :
                       continue
              query = {"c" : "celcius",
                       "k" : "Kelvin",
                       "r" : "reamur",
                       "f" : "fahrenheit"
                       }
              if operation != "c" and operation != "k" and operation != "r" and operation != "f":
                  print("Operation Undified") 
                  x = float(input("Type Your Original Temprature "))
                  print("==================")
                  print("To Select Temprature You Can Type c,r,k,f")
                  operation = input("Input Original Temprature")
                  operation2 = input("Input Temprature Conversion")
                  if operation == "c" and operation2 == "k" :
                      output = x + 273.15
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "k" and operation2 == "c" :
                      output = x - 273.15
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "c" and operation2 == "r" :
                      output = 4/5 * x
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "r" and operation2 == "c":
                      output = 5/4 * x
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "c" and operation2 =="f" :
                      output = 9/5 * x + 32
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "k" and operation2 == "f" :
                      output= 9/5 *(x * 273 ) + 32
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "f" and operation2 == "k" :
                      output = 5/9 * (x - 32) + 273
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "k" and operation2 == "r" :
                      output = 4/5 * (x-273)
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "r" and operation2 == "k" :
                      output = (5/4) * x + 273
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "f" and operation2 == "r" :
                      output = 4/9*(x-32)
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif operation == "r" and operation == "f" :
                      output = (9/4)*x+32
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
                  elif   operation == "f" and operation2 == "c" :
                      output = 5/9 * (x-32)
                      print("Result Of Conversion From", x, operation, "To", operation2, "is", output)
#AND THIS IS FOR CALCILATOR PROGRAM                      
      if operation == "cl" :
          print("Youare Chosing Simple Calculator To Use")
          print(" To use Simple Calculator You Have To Type Command : +, x or *, -, /,")
          while operation != "quit" or operation != "exit" :
              operation = input("Type Your Operation : ")
              if operation == "exit" or operation == "quit" :
                  print("Are You Sure want", operation, " ? :")
                  operation = input("yes or no : ")
                  if operation == "yes" or operation == "y" :
                      exit()
                  elif operation  == "no" or operation == "n" :
                      continue
              elif operation != '+'and operation  != "-" and operation!= "x" and operation != "*" and operation != "/" :
                  print("Operation Undified")
                  continue
              a = float(input(" Type Your Number : "))
              b = float(input("Type Your Number : "))
              if operation == "+" :
                result = a + b
                print(a,"+",b,"=", result)
              elif operation == "-" :
                    result = a - b
                    print(a, "-", b, "=",result)
              elif operation == "*" or operation == "x":
                    result = a * b
                    print(a,"x", b, "=", result)
              elif operation == "/" :
                    result = a / b
                    print(a, "/", b, "=", result)

print("Thanks For Chosing My Program")
