info_student = [
    "João", "Wagner", "Andre", "Victor", "Odilon", "Maycon", "Marlon", "Alan", "Patrick", "Guilherme Reis", "Brecailo", "Eduarda", "Eduardo", "Erick", "Fabricio", "Giselle", "Gui Felicio", "Júlio", "Kauany", "Kazulle", "Lucas", "Rafael", "Rhuan", "Sasah"
]

user_logat = input("Digite Seu Usuario: ")
user_person = ""

user_person = user_logat 

for i in info_student:
    if user_logat == i: 
        user_person = "Seja bem vindo aluno da FAP: " + user_logat


print(user_person)