"""
    创建学生信息存储模型
"""
class StudentModel:
    def __init__(self, name=None, sex=None, score=None, age=None, sid=None):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        self.sid = sid

    def __str__(self):
        """
            重写__str__方法根据需求输出对象
        :return:根据一定的格式输出的数据
        """
        return f"{self.name}的编号是{self.sid},年龄是{self.age},性别是{self.sex},成绩是{self.score}"

    def __eq__(self, other):
        """
            重写__eq__方法便于直接比较两个对象
        :param other: 待比较的外部对象
        :return: 比较结果
        """
        return self.sid == other.sid

#　测试
if __name__ == '__main__':
    model = StudentModel("engine", "man", 100, 21, 0)
    print(model)
