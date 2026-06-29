class Father:
    def father_skill(self):
        print("Father teaches discipline.")


class Mother:
    def mother_skill(self):
        print("Mother teaches kindness.")


class Child(Father, Mother):
    def child_skill(self):
        print("Child learns from both parents.")


child = Child()
child.father_skill()
child.mother_skill()
child.child_skill()
