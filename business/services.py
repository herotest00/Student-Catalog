from domain.domain import Student, Disciplina, Nota

class ServiceStudenti:
    
    
    def __init__(self, repoStudenti, validatorStudent, repoNote):
        
        self.__repoStudenti = repoStudenti
        self.__validatorStudent = validatorStudent
        self.__repoNote = repoNote
    
    
    def adauga_student (self, ID, nume):
        
        ID = int (ID)
        student = Student (ID, nume)
        self.__validatorStudent.valid_student (student)
        self.__repoStudenti.adauga_element (student)
        
        
    def adauga_student2 (self, ID, nume):

        ID = int (ID)
        self.__repoStudenti.verif_student (ID)
        nume = self.__repoStudenti.verif_nume_student (nume)
        student = Student (ID, nume)
        self.__repoStudenti.adauga_student (student)


    def modifica_student (self, IDvechi, IDnou, nume):

        IDvechi = int (IDvechi)
        IDnou = int (IDnou)
        studentVechi = Student (IDvechi, "")
        self.__validatorStudent.valid_student (studentVechi)
        studentNou = Student (IDnou, nume)
        self.__validatorStudent.valid_student (studentNou)
        #self.__repoStudenti.modifica_element (studentVechi, studentNou)
        self.__repoStudenti.modifica_element_recursiv (0, studentVechi, studentNou)
        self.__repoNote.modifica_nota_student (studentVechi, studentNou)
        
        
    def sterge_student (self, ID):
        
        ID = int (ID)
        student = Student (ID, "")
        self.__validatorStudent.valid_student (student)
        self.__repoStudenti.delete_element (student)
            
    
    def search_student (self, ID):
        
        ID = int (ID)
        student = Student (ID, "")
        self.__validatorStudent.valid_student (student)
        #self.__repoStudenti.search_element (student)
        return self.__repoStudenti.search_element_recursiv (0, student)
    
    def get_studenti (self):
        
        return self.__repoStudenti.getElemente ()
    
    
class ServiceDiscipline ():
    
    def __init__ (self, repoDiscipline, validatorDisciplina, repoNote):
        self.__repoDiscipline = repoDiscipline
        self.__validatorDisciplina = validatorDisciplina
        self.__repoNote = repoNote

    def adauga_disciplina (self, ID, profesor, nume):
        
        ID = int (ID)
        disciplina = Disciplina (ID, profesor, nume)
        self.__validatorDisciplina.valid_disciplina (disciplina)
        self.__repoDiscipline.adauga_element (disciplina)
        
    def modifica_disciplina (self, IDvechi, IDnou, profesor, nume):
        
        IDvechi = int (IDvechi)
        IDnou = int (IDnou)
        disciplinaVeche = Disciplina (IDvechi, "", "")
        disciplinaNoua = Disciplina (IDnou, profesor, nume)
        self.__validatorDisciplina.valid_disciplina (disciplinaVeche)
        self.__validatorDisciplina.valid_disciplina (disciplinaNoua)
        self.__repoDiscipline.modifica_element (disciplinaVeche, disciplinaNoua)
        self.__repoNote.modifica_nota_disciplina (disciplinaVeche, disciplinaNoua)
        
    def search_disciplina (self, ID):
        
        ID = int (ID)
        disciplina = Disciplina (ID, "", "")
        self.__validatorDisciplina.valid_disciplina (disciplina)
        return self.__repoDiscipline.search_element (disciplina)
        
    def sterge_disciplina (self, ID):
        
        ID = int (ID)
        ID = int (ID)
        disciplina = Disciplina (ID, "", "")
        self.__validatorDisciplina.valid_disciplina (disciplina)
        self.__repoDiscipline.delete_element (disciplina)
        
    def get_discipline (self):
        
        return self.__repoDiscipline.getElemente ()


class ServiceNote ():
    
    def __init__ (self, repoNote, repoStudenti, repoDiscipline, validatorNota, validatorStudent, validatorDisciplina):
        self.__repoNote = repoNote
        self.__repoStudenti = repoStudenti
        self.__repoDiscipline = repoDiscipline
        self.__validatorNota = validatorNota
        self.__validatorStudent = validatorStudent
        self.__validatorDisciplina = validatorDisciplina
        self.__repoNote = repoNote
        
    def adauga_nota (self, nota, IDstd, IDdiscpl):
        
        nota = float (nota)
        IDstd = int (IDstd)
        IDdiscpl = int (IDdiscpl)
        student = Student (IDstd, "")
        disciplina = Disciplina (IDdiscpl, "", "")
        self.__validatorNota.valid_nota (nota)
        self.__validatorDisciplina.valid_disciplina (disciplina)
        self.__validatorStudent.valid_student (student)
        self.__repoStudenti.search_element (student)
        self.__repoDiscipline.search_element (disciplina)
        nota = Nota (nota, student, disciplina)
        self.__repoNote.adauga_element (nota)  
        
        
    def statistica_1 (self, id_disciplina):
    
        id_disciplina = int (id_disciplina)
        arr_aux = self.__repoNote.filtrare_1 (id_disciplina)
        return self.__repoNote.sortare (arr_aux)


    def statistica_2 (self):
        
        arr = self.__repoNote.filtrare_2 ()
        arr = self.__repoNote.sortare_2 (arr)
        arr = self.__repoNote.medie (arr)
        return self.__repoNote.sortare_2_ (arr)  
    
    
    def statistica_3 (self):
        
        arr_discipline = self.__repoDiscipline.getElemente ()
        arr = self.__repoNote.filtrare_3 (arr_discipline)
        arr = self.__repoNote.sortare_prof (arr)
        arr = self.__repoNote.medie_profesor (arr)
        return self.__repoNote.sortare_nota (arr)
        
        
    def get_note (self):

        return self.__repoNote.getElemente ()