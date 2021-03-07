class ValidationException (Exception):

    pass


class ValidatorDisciplina:
    
    def valid_disciplina (self, disciplina):
        
        errors = ""
        illegal = (",./;'[]\=-0987654321`~!@#$%^&*()_+{}|:'?><")
        errors = self.valid_ID (disciplina.getID_disciplina (), errors)
        errors = self.valid_nume (disciplina.getNume_disciplina (), errors, illegal)
        errors = self.valid_profesor (disciplina.getProfesor_disciplina (), errors, illegal)
        if errors != "":
            raise ValidationException (errors)
        return True

    
    def valid_ID (self, ID, errors):
        
        if ID < 0:
            errors += "ID-ul trebuie sa fie un numar pozitiv!\n"
        return errors
    
    
    def valid_nume (self, nume, errors, illegal):
        
        for i in range (len (illegal)):
            if illegal[i] in nume:
                errors += "Caractere interzise in numele disciplinei!\n"
        return errors
    
    
    def valid_profesor (self, profesor, errors, illegal):
        
        for i in range (len (illegal)):
            if illegal[i] in profesor:
                errors += "Caractere interzise in numele profesorului!"
        return errors
    
    
    
class ValidatorNota:
    
    def valid_nota (self, nota):
        
        errors = ""
        errors = self.valid_valoare (nota, errors)
        if errors != "":
            raise ValidationException (errors)
        return True
    
    
    def valid_valoare (self, nota, errors):
        
        if nota < 1 or nota > 10:
            errors += "Nota nu poate sa fie mai mica decat 1 sau mai mare decat 10!"
        return errors

        

class ValidatorStudent:
    
    def valid_student (self, student):
        
        errors = ""
        illegal = (",./;'[]\=-0987654321`~!@#$%^&*()_+{}|:'?><")
        errors = self.valid_ID (student.getID_student (), errors)
        errors = self.valid_nume (student.getNume_student (), errors, illegal)
        if errors != "":
            raise ValidationException (errors)
        return True
    
        
    def valid_ID (self, ID, errors):
        
        if ID < 0:
            errors += "ID-ul trebuie sa fie un numar pozitiv!\n"
        return errors
    
    
    def valid_nume (self, nume, errors, illegal):
        
        for i in range (len (illegal)):
            if illegal[i] in nume:
                errors += "Caractere interzise in numele studentului!"
                break 
        return errors