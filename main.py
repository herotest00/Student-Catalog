from validate.validatoare import ValidatorStudent, ValidatorDisciplina, ValidatorNota
from infrastructura.repos import Repo, RepoFile, RepoFileNew
from business.services import ServiceStudenti, ServiceDiscipline, ServiceNote
from prezentare.ui import Consola
from domain.domain import Student, Disciplina, Nota


validatorStudent = ValidatorStudent ()
validatorDisciplina = ValidatorDisciplina ()
validatorNota = ValidatorNota ()
#repoStudenti = Repo ()
#repoDiscipline = Repo ()
#repoNote = Repo ()
repoStudenti = RepoFile ("studenti.txt", Student.read_student, Student.write_student)
repoDiscipline = RepoFile ("discipline.txt", Disciplina.read_discipline, Disciplina.write_discipline)
repoNote = RepoFile ("note.txt", Nota.read_note, Nota.write_nota)
#repoStudenti = RepoFileNew ("studenti.txt", "studentiAux.txt", Student.read_student, Student.write_student)
#repoDiscipline = RepoFileNew ("discipline.txt", "disciplineAux.txt", Disciplina.read_discipline, Disciplina.write_discipline)
#repoNote = RepoFileNew ("note.txt", "noteAux.txt", Nota.read_note, Nota.write_nota)
serviceStudenti = ServiceStudenti (repoStudenti, validatorStudent, repoNote)
serviceDiscipline = ServiceDiscipline (repoDiscipline, validatorDisciplina, repoNote)
serviceNote = ServiceNote (repoNote, repoStudenti, repoDiscipline, validatorNota, validatorStudent, validatorDisciplina)
ui = Consola (serviceStudenti, serviceDiscipline, serviceNote)




#teste.run_all_tests ()
ui.run ()