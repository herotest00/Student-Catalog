from infrastructura.repos import Repo, RepoException, RepoFile
from business.services import ServiceStudenti, ServiceDiscipline, ServiceNote
from validate.validatoare import ValidatorStudent, ValidatorDisciplina, ValidatorNota, ValidationException
import unittest
from domain.domain import Student, Disciplina

class Teste (unittest.TestCase):
    
    def __init__ (self, p):
        
        unittest.TestCase.__init__ (self, p)
        self.__validStd = ValidatorStudent ()
        self.__validDiscpl = ValidatorDisciplina ()
        self.__validNota = ValidatorNota ()
        self.__repoTesteStd = Repo ()
        self.__repoTesteDiscpl = Repo ()
        self.__repoTesteNota = Repo ()
        self.__serviceStudenti = ServiceStudenti (self.__repoTesteStd, self.__validStd, self.__repoTesteNota)
        self.__serviceDiscipline = ServiceDiscipline (self.__repoTesteDiscpl, self.__validDiscpl, self.__repoTesteNota)
        self.__serviceNote = ServiceNote (self.__repoTesteNota, self.__repoTesteStd, self.__repoTesteDiscpl, self.__validNota, self.__validStd, self.__validDiscpl)
        self.__serviceStudenti.adauga_student (8, "Marius")
        self.__serviceStudenti.adauga_student (9, "Gica")
        self.__serviceStudenti.adauga_student (10, "Mihai")
        self.__serviceDiscipline.adauga_disciplina (73, "Mate", "Preda")
        self.__serviceDiscipline.adauga_disciplina (68, "Romana", "Lupu")
        self.__serviceDiscipline.adauga_disciplina (54, "Muzica", "Marinela")
        
        
    def setUp (self):
        self.__repoFile = RepoFile ("studentiFile.txt", Student.read_student, Student.write_student)
        
    def tests_rapoarte (self):
        self.__serviceStudenti.adauga_student (5, "Adi")
        self.__serviceStudenti.adauga_student (6, "Gabi")
        self.__serviceStudenti.adauga_student (7, "Marius")
        self.__serviceDiscipline.adauga_disciplina (10, "Fizica", "Preda")
        self.__serviceDiscipline.adauga_disciplina (11, "Romana", "Julieta")
        self.__serviceDiscipline.adauga_disciplina (12, "Muzica", "Preda")
        self.__serviceNote.adauga_nota (10, 5, 10)
        self.__serviceNote.adauga_nota (8, 6, 10)
        self.__serviceNote.adauga_nota (5, 7, 11)
        self.__serviceNote.adauga_nota (1, 8, 10)
        self.__serviceNote.adauga_nota (3, 9, 10)
        self.__serviceNote.adauga_nota (9, 10, 11)
        self.__serviceNote.adauga_nota (8, 5, 11)
        self.__serviceNote.adauga_nota (3, 5, 10)
        self.__serviceNote.adauga_nota (4, 6, 12)
        self.__serviceNote.adauga_nota (10, 9, 12)
        self.__serviceNote.adauga_nota (8, 7, 12)
        self.assertTrue (self.__serviceNote.statistica_1 (10) == [{'Nota': 3.0, 'Student': 5}, {'Nota': 10.0, 'Student': 5}, {'Nota': 8.0, 'Student': 6}, {'Nota': 1.0, 'Student': 8}, {'Nota': 3.0, 'Student': 9}])
        self.assertTrue (self.__serviceNote.statistica_2 () == [{'Medie': 9.0, 'Student': 10}])
        self.__serviceStudenti.sterge_student (5)
        self.__serviceStudenti.sterge_student (6)
        self.__serviceStudenti.sterge_student (7)
        self.__serviceDiscipline.sterge_disciplina (10)
        self.__serviceDiscipline.sterge_disciplina (11)
        self.__serviceDiscipline.sterge_disciplina (12)
                
        
    def tests_validare (self):
    
        self.assertRaises (ValidationException, self.__validDiscpl.valid_disciplina, Disciplina (-3, "Mate", "Preda"))
            
        self.assertRaises (ValidationException, self.__validDiscpl.valid_disciplina , Disciplina (5, "Mate@@@1", "Pr3d444"))
        
        self.assertTrue (self.__validDiscpl.valid_disciplina, Disciplina(6, "Mate", "Preda"))
            
        self.assertRaises (ValidationException, self.__validStd.valid_student, Student (-4, "Chirila"))
    
        self.assertRaises (ValidationException, self.__validStd.valid_student, Student (5, "Marius3l"))
        
        self.assertTrue (self.__validStd.valid_student (Student (4, "Adi")))
                         
        self.assertRaises (ValidationException, self.__validNota.valid_nota, 0)
            
        self.assertTrue (self.__validNota.valid_nota (10))

            
    def tests_adauga (self):
        
        self.__serviceStudenti.adauga_student (3, "Marcel")
        self.assertTrue (self.__repoTesteStd.getSizeElemente () == 4)

        self.assertRaises (RepoException, self.__serviceStudenti.adauga_student, 8, "Mircea")
            
        self.__serviceDiscipline.adauga_disciplina (94, "Fizica", "Bodas")
        self.assertTrue (self.__repoTesteDiscpl.getSizeElemente () == 4)
            
        self.assertRaises (ValidationException, self.__serviceDiscipline.adauga_disciplina, -93, "As@@", "asa!")
 
        self.__serviceNote.adauga_nota (5, 9, 73)
        self.assertTrue (self.__repoTesteNota.getSizeElemente () == 1)

        self.assertRaises (ValidationException, self.__serviceNote.adauga_nota, 0, 15, 19)

            
    def tests_modifica (self):
        
        self.__serviceStudenti.modifica_student (8, 19, "Cristi")
        self.assertTrue (self.__serviceStudenti.search_student (19))
        
        self.assertRaises (RepoException, self.__serviceDiscipline.modifica_disciplina, 84, 17, "Mate", "Preda")
            
    
    def tests_sterge (self):
        
        self.__serviceStudenti.sterge_student (8)
        self.assertTrue (self.__repoTesteStd.getSizeElemente () == 2)

        self.assertRaises (RepoException, self.__serviceDiscipline.sterge_disciplina, 99)            
        
            
    def tests_search (self):
        
        self.assertRaises (RepoException, self.__serviceStudenti.search_student, 120)
            
        self.assertTrue (self.__serviceDiscipline.search_disciplina (54))
        
    def tests_files (self):
        
        self.__repoFile.adauga_element (Student (9, "Marcel"))
        self.assertTrue (self.__repoFile.getSizeElemente () == 1)
        self.__repoFile.adauga_element (Student (5, "Adi"))
        self.assertTrue (self.__repoFile.getSizeElemente () == 2)
        self.__repoFile.delete_element (Student (9, ""))
        self.__repoFile.delete_element(Student (5, ""))
        self.assertTrue (self.__repoFile.getSizeElemente () == 0)
        