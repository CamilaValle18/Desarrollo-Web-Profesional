class Student:
    # Variable de clase para contar estudiantes
    count = 0

    def __init__(self, name, age, language, city):
        self.name = name
        self.age = age
        self.language = language
        self.city = city
        # Incrementar el contador al crear una nueva instancia
        Student.count += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Language: {self.language}, City: {self.city}"

    @staticmethod
    def get_total_students():
        return Student.count

    @classmethod
    def get_total_students_class(cls):
        return cls.count


if __name__ == '__main__':
    estudiante = Student(name='Juan', age=21, language='Python', city='Math')
    print(estudiante)  # Esto llama implícitamente al método __str__
    print(f"Total de estudiantes: {Student.get_total_students()}")

    estudiante_2 = Student(name='Ana', age=22, language='Python', city='Physics')
    print(estudiante_2)
    print(f"Total de estudiantes: {Student.get_total_students()}")