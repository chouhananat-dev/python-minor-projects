# creating a to-do list in python

# first create an empty dictionary in python named as list
dict={}
while True:
    # print user options:
    user_input=None
    try:
        print('''Choose what you want to perform and type the serial no. below:
            1.View all the tasks
            2.Insert a new task
            3.Delete an existing task
            4.Mark done or not done an existing task
            5.Exit\n''')
        user_input=int(input())
    except ValueError as e:
        print(f"Error: {e}")

    # if user want to exit
    if user_input==5:
        break
    # display the whole to do list
    elif user_input==1:
        for key,value in dict.items():
            print(f"{key} : {value}")

    elif user_input==2:
        task=input("Type the new task below:\n")
        option=int(input("Mark it as: 1.Done 2.Not Done\n"))
        value=None
        if option==1:
            value="Done"
        elif option==2:
            value="Not Done"
        dict[task]=value
        print("Inserted Successfully!\n")
    elif user_input==3:
        while True:
            try:
                task=input("Enter the task you want to delete:\n")
                dict.pop(task)
                print("Deleted Successfully!\n")
                break
            except Exception as e:
                print("Enter a valid task please..\n")
        
    elif user_input==4:
        while True:
            task=input("Enter the task you want to update:\n")
            value=dict.get(task)
            if value!=None:
                option=int(input("Update it as 1.Done 2.Not Done\n"))
                if option==1:
                    dict[task]="Done"
                    print("Updated Successfully!\n")
                    break
                elif option==2:
                    dict[task]="Not Done"
                    print("Updated Successfully!\n")
                    break
            elif value==None:
                print("Enter valid task!\n")
            

