class SchoolMember:
    def show_school(self):
        print("Belongs to the school.")


class Teacher(SchoolMember):
    def teach(self):
        print("Teacher teaches students.")


class SportsCoach(SchoolMember):
    def train(self):
        print("Sports coach trains students.")


class PhysicalEducationTeacher(Teacher, SportsCoach):
    def manage_activity(self):
        print("Physical education teacher manages sports activities.")


pe_teacher = PhysicalEducationTeacher()
pe_teacher.show_school()
pe_teacher.teach()
pe_teacher.train()
pe_teacher.manage_activity()
