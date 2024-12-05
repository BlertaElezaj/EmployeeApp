from model import Employee ,Task

class EmployeeManagerController:

    def add_employee(self,department,employee_data):
      #Step 1:Retrieve the list of the employees from the dapartment
      employees = department.employee_list
      #Step 2 :Create a new Employee object with the provided data
      new_employee =Employee(employee_data[0],employee_data[1],employee_data[2],employee_data[3],[])
      employees.append(new_employee)
      department.employees_list = employees

    def delete_Employee(self,department ,employee_data):
        #Retreive the employee list from the department
        employee_list = department.employee_list
        #Iterate over the employee list to find the employee to be deleted
        for employee in employee_list :
            if employee.name == employee_data[0]:
               #Remove the employee from the employee list
               employee_list.remove(employee)

    def update_row(self, old_employee_data ,new_employee_data ,department):
       employee_list = department.employee_list

       for employee in employee_list:
           if employee.name == old_employee_data[0]:
            #Update the employee 's data 
            employee.name = new_employee_data[0]
            employee.address = new_employee_data[1]
            employee.email = new_employee_data[2]
            employee.phone_nr = new_employee_data[3]

            break
           
               


class TaskManagerController:

   def add_task(self,employee,task_data):
      tasks = employee.task_list

      new_task = Task(task_data[0],task_data[1],task_data[2])
      tasks.append(new_task)
     

   def delete_task(self,employee,task_name):
      task_list = employee.task_list

      for task in task_list :
         if task.name == task_name:
            task_list.remove(task)
            employee.task_list = task_list
            break
         
   def update_task(self,old_task_name,new_task_data,employee):
      task_list = employee.task_list
      for task in task_list:
         if task.name == old_task_name:
            task.name=new_task_data[0]
            task.description =new_task_data[1]
            task.priority = new_task_data[2]
            

      
      

