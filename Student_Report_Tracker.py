std_data ={}

while True:
    print("\n======= Student Report Card =======")
    print("1. Add Students (name & marks)")
    print("2. View All")
    print("3. View Result")
    print("4. Save Result")
    print("5. Quit")

    try:
      choice = int(input("Enter Choice:"))

      if choice == 1:
         
         name = input("Enter student name:").title()
         std_data[name] = []
         for i in range(6):

            marks = int(input(f"Enter marks for subject {i + 1}: "))

            if marks < 0 or marks > 100:
               print("Marks should be between 0 and 100.")
               break

            std_data[name].append(marks)
         else:
            print("Student added succesfully!")

            with open("students_report.txt","w") as file:
               for name, marks in std_data.items():
                  file.write(f"name: {name}\ntotal marks: {marks}")

      elif choice == 2:
         
         with open("students_report.txt","r") as file:
            for line in file:
               print(line.strip())

      elif choice == 3:
       
       name = input("Enter student name: ").title()

       if name in std_data:
          total = sum(std_data[name])
          perc = (total / 600) * 100  # 6 subjects x 100 = 600
          if perc >= 60:
            grade = "A"
          elif perc >= 50:
            grade = "B"
          elif perc >= 40:
            grade = "C"
          elif perc >= 34:
            grade = "D"
          else:
            grade = "Fail"
        
          print("\n======= Student Report =======")
          print(f"Name       : {name}")
          print(f"Marks      : {std_data[name]}")
          print(f"Total      : {total}/600")
          print(f"Percentage : {perc:.2f}%")
          print(f"Grade      : {grade}")
       else:
        print("Student not found!")

      elif choice == 4:
         
         print("Saving report.....")
         with open("students_report.txt", "w") as file:
          for name, marks in std_data.items():
           
           total = sum(marks)
           percentage = total / 6

           if percentage >= 60:
                grade = "A"
                result = "PASS"

           elif percentage >= 50:
                grade = "B"
                result = "PASS"

           elif percentage >= 40:
                grade = "C"
                result = "PASS"

           elif percentage >= 34:
                grade = "D"
                result = "PASS"

           else:
                grade = "F"
                result = "FAIL"
          
           file.write(f"Name       : {name}\n")
           file.write(f"Marks      : {marks}\n")
           file.write(f"Total      : {total}/600\n")
           file.write(f"Percentage : {percentage:.2f}%\n")
           file.write(f"Grade      : {grade}\n")
           file.write(f"Result     : {result}\n")
           file.write("----------\n")
           print("Report saved!")
         
      elif choice == 5:

        print("Quiting......\nThank you for using Student Report Card!") 
        break

      else:
         print("Please enter a valid option(1-5).") 

    except ValueError:
       print("Please enter the approprite information!!")