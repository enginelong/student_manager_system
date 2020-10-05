from bll import StudentController
from model import StudentModel
"""
    学生界面视图（负责处理界面逻辑(输入/输出)）
"""

class StudentView:
    def __init__(self):
        """
            将控制器设置为属性
        """
        self.__controller = StudentController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加学生信息")
        print("2. 显示学生信息")
        print("3. 删除学生信息")
        print("4. 修改学生信息")

    def __select_menu(self):
        item = input("请输入执行选项序号: ")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__update_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生的名字: ")
        stu.sex = input("请输入学生的性别: ")
        stu.score = input("请输入学生的成绩: ")
        stu.age = input("请输入学生的年龄: ")
        self.__controller.add_student(stu)

    def __display_students(self):
        for stu in self.__controller.list_students:
            print(stu)

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号: "))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __update_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入需要修改的学生的编号: "))
        stu.name = input("请输入需要修改的学生的姓名: ")
        stu.sex = input("请输入需要修改的学生的性别: ")
        stu.score = int(input("请输入需要修改的学生的成绩: "))
        stu.age = int(input("请输入需要修改的学生的年龄: "))

        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")






