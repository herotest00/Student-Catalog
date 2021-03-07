class RepoException (Exception):
    pass

class Repo ():
    
    def __init__ (self):
        self._arr = []
    
    def adauga_element (self, element):
        
        if element in self._arr:
            raise RepoException ("Element existent!")
        self._arr.append (element)
        
    def search_element (self, element):
        
        if element in self._arr:
            return True
        raise RepoException ("Element inexistent!")
    
        """
        !!!
        """
        
    def search_element_recursiv (self, index, element):
        
        if index == self.getSizeElemente ():
            raise RepoException ("Element inexistent!")
        if element == self._arr[index]:
            return True
        Repo.search_element_recursiv (self, index+1, element)
        
        """
        !!!
        """
    
    def modifica_element (self, element1, element2):
        
        self.search_element (element1)
        for index, obj in list (enumerate (self._arr)):
            if obj == element1:
                self._arr[index] = element2
           
    def modifica_nota_student (self, studentVechi, studentNou):
        
        for index in range (len (self._arr)):
            if self._arr[index].get_student () == studentVechi:
                self._arr[index].set_student (studentNou)
                
    def modifica_nota_disciplina (self, disciplinaVeche, disciplinaNoua):
        
        for index in range (len (self._arr)):
            if self._arr[index].get_disciplina () == disciplinaVeche:
                self._arr[index].set_disciplina (disciplinaNoua)          
                
                
        """
        !!!
        """
        
    def modifica_element_recursiv (self, index, element1, element2):
        
        if index == len (self._arr):
            raise RepoException ("Element inexistent!")
        if self._arr[index] == element1:
            self._arr[index] = element2
            return
        Repo.modifica_element_recursiv (self, index + 1, element1, element2)
        
        """
        !!!
        """
                
    def delete_element (self, element):
        
        for index, obj in list (enumerate (self._arr)):
            if obj == element:
                self._arr.pop (index)
                return
        raise RepoException ("Element inexistent!")
    
    
    def bubbleSort (self, aux, key = lambda x:x): 
    
        n = len (aux) 
        for i in range (n): 
            for j in range(0, n-i-1): 
                if key (aux[j]) > key (aux[j+1]): 
                    aux[j], aux[j+1] = aux[j+1], aux[j]   
        return aux
        
    
    def bubbleSort_lab12 (self, aux, cmp = lambda x,y: -1 if x<y else 0 if x==y else 1):
        
        n = len (aux)
        for i in range (n):
            for j in range (0, n-i-1):
                if cmp (aux[j], aux[j+1]) == 1:
                    aux[j], aux[j+1] = aux[j+1], aux[j]   
        return aux
                
    
    def bubbleSort_extra (self, aux, key = lambda x:x): 
    
        n = len (aux) 
        for i in range (n): 
            for j in range(0, n-i-1): 
                if key(aux[j])[0] > key(aux[j+1])[0] and key(aux[j])[1] == key(aux[j+1])[1]:
                    aux[j], aux[j+1] = aux[j+1], aux[j]   
        return aux
    
    
    def shellSort (self, aux, key = lambda x: x): 
 
        n = len (aux) 
        gap = n//2
        while gap > 0: 
            for i in range(gap,n):
                temp = key (aux[i])
                elem = aux[i]
                j = i 
                while  j >= gap and key (aux[j-gap]) > temp: 
                    aux[j] = aux[j-gap]
                    j -= gap 
                aux[j] = elem 
            gap //= 2
        return aux
    
    
    def filtrare_1 (self, id_disciplina):
        
        aux = []
        for index in range (len (self._arr)):
            if self._arr[index].getID_disciplina () == id_disciplina:
                aux.append ({"Nota": self._arr[index].getNota (), "Student": self._arr[index].getID_student ()})
        return aux 
    
    
    def sortare (self, aux):
        
        aux = self.bubbleSort_lab12 (aux, cmp = lambda x,y: 1 if x["Student"] < y["Student"] else 0 if x["Student"] == y["Student"] else -1)
        aux = self.bubbleSort_extra (aux, key = lambda aux: [aux["Nota"], aux["Student"]])
        return aux
    

    def filtrare_2 (self):
        
        aux = []
        for index in range (len (self._arr)):
            aux.append ({"Nota": self._arr[index].getNota (), "Disciplina": self._arr[index].getID_disciplina (), "Student": self._arr[index].getID_student ()})
        return aux    
    
    
    def sortare_2 (self, aux):
        
        aux.sort (key = lambda aux: [aux["Student"], aux["Disciplina"], aux["Nota"]])
        return aux
    
    
    def medie (self, aux):
        
        arr_aux = []
        aux_stud = aux[0]["Student"]
        aux_discpl = aux[0]["Disciplina"]
        i = 0
        counter = 0
        counterDiscpl = 0 
        suma = 0
        medie = 0
        while aux[i]["Student"] == aux_stud and aux[i]["Disciplina"] == aux_discpl and i < len (aux):
            suma += aux[i]["Nota"]
            counter += 1
            i += 1
            if i == len (aux):
                counterDiscpl += 1
                medie += suma/counter/counterDiscpl
                arr_aux.append ({"Medie": medie, "Student": aux[i-1]["Student"]})
                return arr_aux
            if aux[i]["Disciplina"] != aux_discpl:
                aux_discpl = aux[i]["Disciplina"]
                medie += suma/counter
                suma = 0
                counter = 0
                counterDiscpl += 1
            if aux[i]["Student"] != aux_stud:
                aux_stud = aux[i]["Student"]
                if counterDiscpl == 0:
                    counterDiscpl += 1
                if counter!= 0:
                    medie += suma/counter
                medie /= counterDiscpl
                arr_aux.append ({"Medie": medie, "Student": aux[i-1]["Student"]})
                medie = 0
                suma = 0
                counter = 0   
                counterDiscpl = 0 
        
    def sortare_2_ (self, arr_aux):

        arr_aux = self.shellSort (arr_aux, key = lambda arr_aux: arr_aux["Medie"])
        arr_aux = arr_aux[::-1] 
        return arr_aux[0:len (arr_aux)//5]
    
    
    def filtrare_3 (self, arr_discipline):
        
        arr_aux = []
        for index in range (len (self._arr)):
            arr_aux.append ({"Nota": self._arr[index].getNota (), "Profesor": self.search_filtrare_3 (arr_discipline, self._arr[index].getID_disciplina ())})
        return arr_aux
    
    def search_filtrare_3 (self, arr_discipline, id_disciplina):
        
        for index in range (len (arr_discipline)):
            if arr_discipline[index].getID_disciplina () == id_disciplina:
                return arr_discipline[index].getProfesor_disciplina ()
    
    
    def sortare_prof (self, arr):
        
        arr = self.shellSort (arr, key = lambda arr: arr["Profesor"])
        return arr
    
    
    def medie_profesor (self, arr):
        
        arr_aux = []
        index = 0
        counter = 0
        suma = 0
        prof = arr[index]["Profesor"]
        while index < len (arr):
            suma += arr[index]["Nota"]
            counter += 1
            index += 1
            if index == len (arr):
                medie = suma / counter
                arr_aux.append ({"Profesor": prof, "Medie": medie})
            elif arr[index]["Profesor"] != prof:
                medie = suma / counter
                arr_aux.append ({"Profesor": prof, "Medie": medie})
                prof = arr[index]["Profesor"]
                suma = 0
                counter = 0
        return arr_aux
                

    def sortare_nota (self, arr):
        
        arr = self.bubbleSort (arr, key = lambda arr: arr["Medie"])
        return arr
    
                
    def getElemente (self):
        
        return self._arr
    
    def getSizeElemente (self):
        
        return len (self._arr)
    
    
class RepoFile (Repo):
    
    def __init__ (self, filename, read_element, write_element):
        self.__filename = filename
        self.__read = read_element
        self.__write = write_element
        Repo.__init__ (self)
        
        
    def __read_all_from_file (self):
        self._arr = []
        with open(self.__filename,"r") as f:
            lines = f.readlines ()
            for line in lines:
                line = line.strip ()
                if line != "":
                    element = self.__read (line)
                    self._arr.append (element)
                
                
    def __write_all_to_file (self):
        with open(self.__filename, "w") as f:
            for element in self._arr:
                f.write (self.__write (element) + "\n") 
                
                
    def adauga_element (self, element):
        self.__read_all_from_file ()
        Repo.adauga_element (self, element)
        self.__write_all_to_file ()
        
    def modifica_element (self, element1, element2):
        self.__read_all_from_file ()
        Repo.modifica_element (self, element1, element2)
        self.__write_all_to_file ()
        
    def modifica_nota_student (self, studentVechi, studentNou):
        self.__read_all_from_file ()
        Repo.modifica_nota_student (self, studentVechi, studentNou)
        self.__write_all_to_file ()
        
    def modifica_nota_disciplina (self, disciplinaVeche, disciplinaNoua):
        self.__read_all_from_file ()
        Repo.modifica_nota_disciplina (self, disciplinaVeche, disciplinaNoua)
        self.__write_all_to_file ()
        
        """
        !!!
        """
        
    def modifica_element_recursiv (self, index, element1, element2):
        self.__read_all_from_file ()
        Repo.modifica_element_recursiv (self, index, element1, element2)
        self.__write_all_to_file ()
        
        """
        !!!
        """
        
    def search_element (self, element):
        self.__read_all_from_file ()
        return Repo.search_element (self, element)
    
        """
        !!!
        """
        
    def search_element_recursiv (self, index, element):
        self.__read_all_from_file ()
        Repo.search_element_recursiv (self, index, element)
    
        """
        !!!
        """
        
    def delete_element (self, element):
        self.__read_all_from_file ()
        Repo.delete_element (self, element)
        self.__write_all_to_file ()
        
    def filtrare_1 (self, id_disciplina):
        self.__read_all_from_file ()
        return Repo.filtrare_1 (self, id_disciplina)
    
    def filtrare_2 (self):
        self.__read_all_from_file ()
        return Repo.filtrare_2 (self)
        
    def filtrare_3 (self, arr_discipline):
        self.__read_all_from_file ()
        return Repo.filtrare_3 (self, arr_discipline)
        
    def getElemente (self):
        self.__read_all_from_file ()
        return Repo.getElemente (self)
    
    def getSizeElemente (self):
        self.__read_all_from_file ()
        return Repo.getSizeElemente (self)
    
    
class RepoFileNew (Repo):
    
    def __init__ (self, filename, filenameAux, read_element, write_element):
        self.__filename = filename
        self.__filenameAux = filenameAux
        self.__read = read_element
        self.__write = write_element 
        
    def adauga_element (self, element):
        with open (self.__filename, "a") as f:
            f.write (self.__write (element) + "\n")
        
    def search_element (self, element):
        index = 0
        with open (self.__filename, "r") as f:
            line = f.readline ()
            line = line.strip ()
            while line != "":
                readLine = self.__read (line)
                if readLine == element:
                    return True
                index += 1
                line = f.readline ()
                line = line.strip ()
            raise RepoException ("Element inextistent!")
    
    def modifica_element (self, elementVechi, elementNou):
        index = 0
        with open (self.__filename, "r") as f:
            with open (self.__filenameAux, "w") as f_aux:
                line = f.readline ()
                line = line.strip ()
                while line != "":
                    element = self.__read (line)
                    if element == elementVechi:
                        index_gasit = index
                    else:
                        element = self.__read (line)
                        f_aux.write (self.__write (element) + "\n")
                    index += 1  
                    line = f.readline ()
                    line = line.strip ()
                
        index = 0
        with open (self.__filenameAux, "r") as f_aux:
            with open (self.__filename, "w") as f:
                line = f_aux.readline ()
                line = line.strip ()
                while line != "" or index <= index_gasit:
                    if index == index_gasit:
                        f.write (self.__write (elementNou) + "\n")
                    element = self.__read (line)
                    f.write (self.__write (element) + "\n")
                    index += 1
                    line = f_aux.readline ()
                    line = line.strip ()
                
    def delete_student (self, index2):
        index1 = 0
        with open (self.__filename_stud, "r") as f:
            with open (self.__filename_stud_aux, "w") as f_aux:
                line = f.readline ()
                line = line.strip ()
                while line != "":
                    if index1 != index2:
                        student = self.__read_stud (line)
                        f_aux.write (self.__write_stud (student) + "\n")
                    index1 += 1
                    line = f.readline ()
                    line = line.strip ()
        
        with open (self.__filename_stud_aux, "r") as f_aux:
            with open (self.__filename_stud, "w") as f:
                line = f_aux.readline ()
                line = line.strip ()
                while line!= "":
                    student = self.__read_stud (line)
                    f.write (self.__write_stud (student) + "\n")
                    line = f_aux.readline ()
                    line = line.strip ()