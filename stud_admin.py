"""   my_captain_Assignment - 6   """

# Write a Python Program to implement a School Administration system that creates and excel sheet of  Student's information

import  csv

def write_int_csv(info_list):
   with open('student_info.csv','a',newline='') as csv_file:
      writer = csv.writer(csv_file)
      if csv_file.tell() == 0:
         writer.writerow(["Name" , "Age" , "Contact_Number","Email-ID"]) 
      writer.writerow(info_list) 

if __name__ == '__main__':
   Condition = 1
   student_id = 1 

   while(Condition):

      student_info = input("Enter the student #{} information in this order \n ( Name Age Contact_Number Email-ID )\n".format(student_id))

      student_info_list = student_info.split(" ")

      print("Entered Student's Information \n Name: {}\n Age: {} \n Contact_Number: {}\n Email-ID: {} \n" 
      .format(student_info_list[0] , student_info_list[1] ,student_info_list[2] , student_info_list[3] ) )

      cc = choice_Check = input(" Is the entered information correct  [ Y / N ] : ")

      if cc == 'Y' or cc =='y':
         write_int_csv(student_info_list)

         cC = codition_Check =  input("Enter [ Y / N ] if you want to enter information for another student : ")
         if cC == 'Y' or cC =='y':
            Condition = 1
            student_id = student_id + 1
         elif cC == 'N' or cC =='n':
            Condition = 0
      elif cc == 'N' or cc =='n':
         print("Please re-enter Correct inforamtion !!")
      else:
         print("Enter [ Y / N ] if you want to enter information for another student : ")




