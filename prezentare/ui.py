from validate.validatoare import ValidationException
from infrastructura.repos import RepoException

class Consola:
    
    
    def __init__(self, serviceStudenti, serviceDiscipline, serviceNote):
        self.__serviceStudenti = serviceStudenti
        self.__serviceDiscipline = serviceDiscipline
        self.__serviceNote = serviceNote
        self.__comenzi = {"adauga_student": self.__serviceStudenti.adauga_student,
                          "adauga_student2": self.__serviceStudenti.adauga_student2,
                          "adauga_disciplina": self.__serviceDiscipline.adauga_disciplina,
                          "adauga_nota": self.__serviceNote.adauga_nota,
                          "modifica_student": self.__serviceStudenti.modifica_student,
                          "modifica_disciplina": self.__serviceDiscipline.modifica_disciplina,
                          "search_student": self.__serviceStudenti.search_student,
                          "search_disciplina": self.__serviceDiscipline.search_disciplina,
                          "sterge_student": self.__serviceStudenti.sterge_student,
                          "sterge_disciplina": self.__serviceDiscipline.sterge_disciplina,
                          "statistica_1": self.statistica_1,
                          "statistica_2": self.statistica_2,
                          "statistica_3": self.statistica_3,
                          "get_studenti": self.afisare_student,
                          "get_discipline": self.afisare_disciplina,
                          "get_note": self.afisare_nota,
                          "tema13": self.tema13_citire,
                          "lab14": self.lab14_citire}

        

    def run (self):
        while True:
            self.afisare_run ()
            try:
                cmd = input (">>>")
                if cmd == "exit":
                    return
                cmd = cmd.strip ()
                parts = cmd.split ()
                nume_cmd = parts[0]
                params = parts [1:]
                if nume_cmd in self.__comenzi:
                    try:
                        self.__comenzi[nume_cmd] (*params)
                    except ValueError as ve:
                        print ("UI Error:\n" + str(ve))
                    except ValidationException as error:
                        print ("Validator Error:\n" + str (error))
                    except RepoException as error:
                        print ("Repository Error:\n" + str (error))
                else:
                    print ("Comanda invalida!")
            except TypeError as error:
                print (error)
            
        
    def statistica_1 (self, id_discpl):
        
        print (self.__serviceNote.statistica_1 (id_discpl))
        
        
        
    def statistica_2 (self):
        
        print (self.__serviceNote.statistica_2 ())
        
    
    def statistica_3 (self):
        
        print (self.__serviceNote.statistica_3 ())    
    
    
    def tema13_citire (self):
        
        nr = input ("Nr meciuri: ")
        arr = []
        print ("Recursiv:")
        self.tema13 (int (nr), arr, ("1", "X", "2"))
        arr = []
        print ("Iterativ 3 meciuri:")
        self.tema13_iterativ3 (arr, ("1", "X", "2"))
        
        
    """
        solutie candidat: arr = [x1, x2, ..., xk]  x1,x2, ..., xn apartin ("1", "X", "2")
        conditie consistent: arr = [x1, x2, ..., xk] daca nu exista mai mult de 2 elemente = "1"
        conditie solutie: arr = [x1, x2, ... ,xk] daca este consistent si k = n si xn != "X"
    """
    
    def tema13 (self, nr, arr, symb):
        
        if len (arr) == nr:
            print (arr)
            return
        for i in range (len (symb)):
            arr += symb[i]
            if self.verif_1 (arr) and self.verif_X (arr, nr):
                self.tema13 (nr, arr, symb)
            arr.pop ()
        return
            
            
    def verif_1 (self, arr):
        
        counter = 0
        for i in range (len (arr)):
            if arr[i] == "1":
                counter += 1
                if counter > 2:
                    return False
        return True
    
    
    def verif_X (self, arr, nr):
        if len (arr) == nr and arr[-1] == "X":
            return False
        return True
    
    
    def tema13_iterativ3 (self, arr, symb):
        
        for i in range (len (symb)):
            arr += symb[i]
            for j in range (len (symb)):
                arr += symb[j]
                for k in range (len (symb)):
                    arr += symb[k]
                    if self.verif_1 (arr) and self.verif_X (arr, 3):
                        print (arr)
                    arr.pop ()
                arr.pop ()
            arr.pop ()
            
            
    def lab14_citire (self):
        
        nr = input ("n:")
        nr = int (nr)
        arr = []
        for index in range (nr):
            x = input (">>")
            arr.append (int (x))
        for index in range (nr):
            aux = []
            suma = 0
            self.lab14 (nr, arr, aux, suma, index)
    
    """
        solutie candidat: aux = [x0, x1, ..., xk]   k <= nr  xi apartine arr
        conditie consistent: aux = [x0, x1, ..., xk] daca elementele listei respecta ordinea din lista initiala
        conditie solutie: aux = [x0, x1, ..., xk] daca este consistenta si k <= nr si daca suma elementor este divizibila cu nr
    """
    
    
    def lab14 (self, nr, arr, aux, suma, index):
        
        if index == nr:
            return
        aux.append (arr[index])
        suma += arr[index]
        if suma % nr == 0:
            print (aux)
        self.lab14 (nr, arr, aux, suma, index+1)
        return
            

    def afisare_student (self):
        
        arr = self.__serviceStudenti.get_studenti ()
        for i, obj in list (enumerate (arr)):
            print (str (i+1) + ". " + str (obj))
     
     
    def afisare_disciplina (self):
        
        arr = self.__serviceDiscipline.get_discipline ()
        for i, obj in list (enumerate (arr)):
            print (str (i+1) + ". " + str (obj))
        
        
    def afisare_nota (self):
        
        arr = self.__serviceNote.get_note ()
        for i, obj in list (enumerate (arr)):
            print (str (i+1) + ". " + str (obj))
                    

    def afisare_run (self):
        
        print (" ")
        print ("Adauga: adauga_student (ID, nume), adauga_disciplina (ID, nume, profesor), adauga_nota (nota, ID student, ID disciplina)")
        print ("Modifica: modifica_student (ID vechi, ID nou, nume), modifica_disciplina (ID vechi, ID nou, nume, profesor)")
        print ("Sterge: sterge_student (ID), sterge_disciplina (ID)")
        print ("Search: search_student (ID), search_disciplina (ID)")
        print ("Statistica: statistica_1 (ID disciplina), statistica_2 ()")
        print ("Get: get_studenti, get_discipline, get_note")