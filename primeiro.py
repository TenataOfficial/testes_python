def menu():
    
    try:
        x = int(input('=+=+=+=+=+ MENU +=+=+=+=+=\n\n'+
            '1 - cadastrar aluno\n' +
            '2 - consultar aluno\n' +
            '3 - Deletar aluno\n'
            ))
                
        if x == 1:
            alunoCad()

        if x == 2:
            if int(contarId(0)) != 0:
                alunoCon()
            else:
                print('Sem alunos cadastrados ;-;\n')
                menu()

        if x == 3:
            if int(contarId(0)) != 0:
                alunoRem()
            else:
                print('Sem alunos cadastrados ;-;\n')
    except:
        print('Comando não válido!\n')
    menu()

def alunoRem():
    id = verificaId(input('Digite o id do aluno: '),2)
    x = 0
    for i in escola:
        if int(i["id"]) == int(id):
            if int(input('\nDeseja mesmo remove-lo? \n1- sim / 2-não\n')) == 1:
                escola.pop(x)
                print('\n Aluno id '+ str(id) +' foi removido\n')
            else:
                print('\n Não foi removido\n')
        x += 1
    menu()

def alunoCon():
    print('\n1 - Listar todos \n'+
    '2 - Consultar por id \n'+
    '3 - Consultar por nome\n'+
    '4 - consultar por idade\n'
    )
    try:
        x = int(input())
        if x == 1:
            for i in escola:
                    printAluno(i)
            print('\n')
        elif x == 2:                        #consulta por id
            id = int(verificaId(input('\nDigite o id:'),2))
            for i in escola:
                if int(i["id"]) == int(id):
                    printAluno(i)
                    menu()
            print('Id não encontrado\n')
        elif x == 3:                        #consulta por nome
            achou = 0 
            nome = str(input('Digite o nome:'))
            for i in escola:
                    if str(i["nome"]) == str(nome):
                        printAluno(i)
                        achou += 1
            if achou == 0:
                print('Nome não encontrado\n')
        elif x == 4:                        #consulta por idade
            achou = 0
            try:
                idade = int(input('Digite a idade :'))
                for i in escola:
                        if int(i["idade"]) == int(idade):
                            printAluno(i)
                            achou += 1
                if achou == 0:
                    print('Idade não encontrada\n')
            except:
                print('Idade não é válida\n')
    except:
        print('Comando não válido!\n')
    menu()

def printAluno(i): #imprime no terminal os dados dos alunos
    print('Id: ' + str(i["id"]) + '\t' + 'Nome: ' + str(i["nome"]) + "\t" + 'Idade: ' + str(i["idade"]))

def alunoCad(): #recebe dados e monta um dicionario depois insere o dicionario criado em uma array
    x = contarId(1)
    print('id sugerido = ' + str(x) + '\n')
    id =  verificaId(input('Digite um id: '),1)
    nome = str(input('\nagora digite um nome: '))
    while(True):
        try:
            idade = int(input('\nidade: '))
            break
        except:
            print('A idade precisa ser um numero inteiro\n')
    aluno = {
        "id": id,
        "nome" : nome,
        "idade": idade
    }
    escola.insert(int(id),aluno)
    print('\naluno ' + nome + ' cadastrado com sucesso\n')
    menu()

def contarId(y): #verifica se contem alguma informação em escola, se tive ele conta os itens até achar um id não preenchido, caso não ele retorna 0 
    id = 0
    if len(escola) >= 0:
        for i in escola:
            x = i
            if int(id) != int(x["id"]):
                if int(y) == 1:
                    return id
            id += 1
    return id
    

def verificaId(id,ver): #verifica se existe itens dentro da array escola[] 
    try: #try verificando se o id que foi digitado é um int
        for i in escola:
            x = i

            if int(id) == int(x["id"]):

                if int(ver) ==  2: #retorna id caso exista
                    return int(id) 

                elif int(ver) == 1: #não retorna pois só quer uma validação se existe ou não
                    print('Este id já existe')
                    alunoCad()

        return int(id)
    except: #aqui ele retorna ao menu ou ao cadastro após a verificação que o id não é válido
        print('\nO valor não é válido\n')
        if int(ver) ==  2:
            menu() 
        elif int(ver) == 1:    
            alunoCad()

escola = [] #servirá para guardar os dicionarios alunos.
aluno = {} #dicionario aluno vai conter id: , nome: e idade:
menu()