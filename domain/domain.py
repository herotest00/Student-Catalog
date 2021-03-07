class Student:
    
    def __init__ (self, ID, nume):
        
        self.__ID = ID
        self.__nume = nume
    
    
    def __repr__ (self):
        
        return "ID: " + str (self.__ID) + " Nume: " + self.__nume
    
    
    def __eq__ (self, other):
        
        return self.getID_student () == other.getID_student ()
    
        
    def getID_student (self):
        
        return self.__ID
    
    
    def getNume_student (self):
        
        return self.__nume
    
    
    def setID_student (self, ID):
        
        self.__ID = ID
    
        
    def setNume_student (self, Nume):
        
        self.__nume = Nume
        
    
    @staticmethod
    def read_student (line):
        parts = line.split (",")
        return Student (int(parts[0].strip ()), parts[1].strip ())
    
    @staticmethod
    def write_student (student):
        return str (student.getID_student ()) + "," + student.getNume_student ()
        

class Disciplina:
    
    def __init__ (self, ID, nume, profesor):
        
        self.__ID = ID
        self.__nume = nume
        self.__profesor = profesor
    
    
    def __repr__ (self):
        
        return "ID: " + str (self.__ID) + " Nume: " + self.__nume + " Profesor: " + self.__profesor  
    
    def __eq__ (self, other):
        
        return self.getID_disciplina () == other.getID_disciplina () or ((self.getNume_disciplina () == other.getNume_disciplina () and self.getProfesor_disciplina () == other.getProfesor_disciplina ()) and (self.getNume_disciplina () != "" and self.getProfesor_disciplina () != ""))  
        
    def getID_disciplina (self):
        
        return self.__ID
    
    
    def getNume_disciplina (self):
        
        return self.__nume
    
    
    def getProfesor_disciplina (self):
        
        return self.__profesor
    
    
    def setID_disciplina (self, ID):
        
        self.__ID = ID
    
        
    def setNume_disciplina (self, Nume):
        
        self.__nume = Nume
        
        
    def setProfesor_disciplina (self, Profesor):
        
        self.__profesor = Profesor    
        

    @staticmethod
    def read_discipline (line):
        parts = line.split (",")
        return Disciplina (int(parts[0].strip ()), parts[1].strip (), parts[2].strip ())
    
    
    @staticmethod
    def write_discipline (disciplina):
        return str (disciplina.getID_disciplina ()) + "," + disciplina.getNume_disciplina () + "," + disciplina.getProfesor_disciplina ()       

        
class Nota ():
    
    def __init__ (self, nota, student, disciplina):
        
        self.__nota = nota
        self.__student = student
        self.__disciplina = disciplina
    
    
    def __repr__ (self):
        
        return "Nota: "+ str (self.__nota) + " Student: " + str (self.__student.getID_student ()) + " Disciplina: " + str (self.__disciplina.getID_disciplina ())

    def get_student (self):
        
        return self.__student
    
    def get_disciplina (self):
        
        return self.__disciplina
    
    def set_student (self, student):
        
        self.__student = student
        
    def set_disciplina (self, disciplina):
        
        self.__disciplina = disciplina
    
    
    def getID_student (self):
        
        return self.__student.getID_student ()
    
    
    def getID_disciplina (self):
        
        return self.__disciplina.getID_disciplina ()
    
    def getProfesor_disciplina (self):
        
        return self.__disciplina.getProfesor_disciplina ()
    
    
    def getNota (self):
        
        return self.__nota
    
    
    def setID_student (self, ID):
        
        self.__IDstd = ID
        
    
    def setID_disciplina (self, ID):
        
        self.__IDdiscpl = ID
        
        
    @staticmethod
    def read_note (line):
        parts = line.split (",")
        return Nota (float(parts[0].strip ()), Student (int (parts[1].strip ()), ""), Disciplina (int (parts[2].strip ()), "", ""))
    
    
    @staticmethod
    def write_nota (nota):
        return str (nota.getNota ()) + "," + str (nota.getID_student ()) + "," + str (nota.getID_disciplina ())  
    
