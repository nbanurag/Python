students = [
    {
        "name": "Anurag",
        "marks": [85, 78, 90],
        "total": 253,
        "percentage": 84.33,
        "grade": "A"
    }
]

def getValidatedValue(inputText, minVal, maxValue):
    value = int(input(inputText))
    if(minVal <= value <= maxValue):
        return value
    else:
        print('Please enter valid value')
        return getValidatedValue(inputText, minVal, maxValue)
    
def getGrade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'Fail'

while True:
    print("\n1. Add student\n2. View all students\n3. Search student\n4. Update marks\n5. Delete student\n6. Exit\n")
    option = input("Please choose option number: ")

    match option:
        case '1':
            name = input("Student Name: ")
            number_of_subjects = getValidatedValue("Number of subjects: ", 1,5)
            marks=[]
            for i in range(number_of_subjects):
                mark=  getValidatedValue("Student Marks: ", 0, 100)
                marks.append(mark)
            percentage = sum(marks)/number_of_subjects

            students.append({
                "name":name,
                "marks": marks,
                "total": sum(marks),
                "percentage": percentage,
                "grade": getGrade(percentage)
            })    
            print("Student record added sucessfully")
        case '2':
            print('No. Name   Marks  Total  Percentage  Grade')
            for i, item in enumerate(students):
                print(f'{i+1}. {item.get("name")}  {item.get("marks")}  {item.get("total")}  {item.get("percentage")}%  {item.get("grade")}')
        case '3':
            seachName = input('Student name to search: ').strip().lower()
            searchedStudent=None
            for item in students:
                if item.get("name").lower()==seachName:
                    searchedStudent=item
                    break
            if searchedStudent:
                print('Searched Student: ', searchedStudent)
            else:
                print('Student record not found')    
        case '4':
            seachName = input('Student name to search: ').strip().lower()
            index= None
            for i,item in enumerate(students):
                if item.get("name").lower()==seachName:
                    index=i
                    searchedStudent=item
                    break
            if searchedStudent:
                print('Searched Student marks: ', searchedStudent['marks'])
                print("Input new Marks")
                number_of_subjects = getValidatedValue("Number of subjects: ", 1,5)
                marks=[]
                for i in range(number_of_subjects):
                    mark=  getValidatedValue("Student Marks: ", 0, 100)
                    marks.append(mark)
                percentage = sum(marks)/number_of_subjects

                students[index]={
                    **searchedStudent, 
                    "marks": marks,
                    "total": sum(marks),
                    "percentage": percentage,
                    "grade": getGrade(percentage)
                    }
                print('Student record updated')    
            else:
                print('Student record not found')    
        case '5':
            deleteName = input('Student name to delete: ').strip().lower()
            updatedStudentRecord = [item for item in students if item['name'].lower() != deleteName ]
            students=updatedStudentRecord
            print('Student record deleted')    
            print(updatedStudentRecord)
        case '6':
            break    
                    


    
