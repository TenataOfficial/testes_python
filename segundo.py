#criar uma consulta e cadastro de carros(cor, modelo, ano, placa) da consessionaria() das cidades()
def menu():
    while(True):
        try:
            x = int(input('=+=+=+=+=+ menu +=+=+=+=\n\n'+
                '1 - cadastrar carro\n'+
                '2 - consultar carro\n'
                )) 
            if x == 1:
                cadastrarCarro();
            if x == 2:
                if len(concessionaria) > 0:
                    while(True):
                        try:
                            y = int(input('1 - listar todos\n'+
                            '2 - consultar por estado\n'+
                            '3 - consultar por placa\n'+
                            '4 - consultar por cor\n'+
                            '5 - consultar por alugados\n'+
                            '6 - consultar no estoque\n'
                            ))
                            if y <= 6 and y>= 1:
                                consultarCarro(y)
                        except:
                            print('Entrada precisa ser um código válido!\n')
                else:
                    print('Não há cadastro')
        except:
            print('Entrada precisa ser um código válido!\n')

def consultarCarro(x):
    if int(x) == 1:
        printarCarros(0)
    elif int(x) == 2:
        printarCarros(1)
    elif int(x) == 3:
        printarCarros(2)
    elif int(x) == 4:
        printarCarros(3)
    elif int(x) == 5:
        printarCarros(4)
    elif int(x) == 6:
        printarCarros(5)
        
def printarCarros(x):
    if int(x) == 0:
        for i in concessionaria:
            est()
            print('Estado : '+ str(i['nome_estado']) +'\n')
            if len(i['carro']) > 0:
                y = i['carro']
                encap(y)
    elif int(x) == 1:
        x = str(input('Digite o nome do estado: \n'))
        for i in concessionaria:
            if str(i['nome_estado']) == str(x):
                est()
                print('Estado : '+ str(i['nome_estado']) +'\n')
                if len(i['carro']) > 0:
                    y = i['carro']
                    encap(y)
                menu()
        print('Estado não encontrado!')
        menu()
        
    elif int(x) == 2:
        ConsultAtributosCarro(str(input('Digite a placa\n')),1)
    elif int(x) == 3:
        ConsultAtributosCarro(str(input('Digite a cor do veículo\n')),2)
    elif int(x) == 4:
        ConsultAtributosCarro('Sim',3)
    elif int(x) == 5:
        ConsultAtributosCarro('Não',3)
def ConsultAtributosCarro(entrada,valor): 
    x2 = 0
    texto = ''
    if int(valor) == 1:
        texto = 'placa'
    elif int(valor) == 2:
        texto = 'cor'
    elif int(valor) == 3:
        texto = 'alugado'

    for i in concessionaria:
        for y in i['carro']:
            if str(y[str(texto)]) == str(entrada):
                est()
                if int(valor) == 3:
                    print('+-+-+- ALUGADOS -+-+-+')
                elif int(valor) == 4:
                    print('+-+-+- EM ESTOQUE -+-+-+')
                print('Estado : '+ str(i['nome_estado']) +'\n')
                if len(i['carro']) > 0:
                    encap(i['carro'])
                x2 += 1    
    if int(x2) == 0:
        if str(texto) == 'placa':
            print('Placa não encontrada\n')
        elif str(texto) == 'cor':
            print('Cor não encontrada\n')
    menu()
    
def encap(y):
    for z in y:
        print('Placa: ' + str(z['placa']) + '\tAno de fabricação:' + str(z['ano'])+
        '\tcor: ' + str(z['cor']) + '\tAlugado: ' + str(z['alugado'])) 
    print('\n')
    
def est():
    print('\n===============================================\n')

def cadastrarCarro():
    estado = estadoVer_Cad(str(input('Digite o estado\n')))
    while(True):
        placa = conferePlaca(str(input('Digite sua placa\n')),estado)
        if str(placa) != '######':
            break
    while(True):
        try:
            alugado = int(input('\nalugado?\n1 - para sim \ 2 - para não\n'))
            if int(alugado) == 1 or int(alugado) == 2:
                break
            else:
                print('Este valor não é válido\n')
        except:
            print('Este valor não é válido\n')
    while(True):
        try: 
            ano = int(input('digite o ano de fabricação do carro\n'))
            break
        except:
            print('ano precisa ser um número inteiro\n')
    cor = str(input('cor do carro\n'))
    sn = 'Não'
    if int(alugado) == 1:
        sn = 'Sim'
    carro = {
        'placa' : str(placa),
        'alugado' : str(sn),
        'ano' : int(ano),
        'cor' : str(cor)
    }
    try:
        pose = 0
        for i in concessionaria:
            
            if str(i['nome_estado']) == str(estado):
                ic = i['carro']
                ic.append(carro)
                estado = {**i,'nome_estado': str(estado), 'carro' : ic}
                concessionaria[pose] = estado
                print('adicionado com sucesso!\n')
                #print(concessionaria[pose])
            pose += 1
    except:
        print('Aconteceu algo :(\n')
    menu()


def conferePlaca(placa, estado):
    try:
        for i in concessionaria:
            if str(i['nome_estado']) == str(estado):
                if len(i['carro']) > 0:
                    for x in i['carro']:
                        if str(x['placa']) == str(placa):
                            print('Essa placa já existe\n')
                            return('######')
                return placa
        estadoVer_Cad(estado)
    except:
        print('algo deu errado ;-;\n')
        menu()

def estadoVer_Cad(estadoEnt):
    try:
        if len(concessionaria) > 0:
            for i in concessionaria:
                if str(i['nome_estado']) == str(estadoEnt):
                    return estadoEnt
        
        while(True):
            try:
                j = int(input('nenhum estado encontrado com esse nome\n'+
            'deseja adicionar ' + str(estadoEnt) + ' em estados?' +
            '\n1 - para sim \ 2 - para não\n'))
                if int(j) == 2:
                    menu()
                elif int(j) == 1:
                    break
            except:
                print('A opção deve ser válida\n')
        estado = {
            'nome_estado' : estadoEnt,
            'carro' : []
        }
        concessionaria.append(estado)
        print('Adicionado com sucesso!\n')
        return estadoEnt
    except:
        print('Houve um erro \n')
        menu()


carro = {} #carros vai conter(placa, modelo, ano, cor)
concessionaria = []#[{'nome_estado' : 'bahia', 'carro':[{'placa':'abc','alugado':'Sim','ano':'2000','cor':'branco'}]}, {'nome_estado':'acre','carro':[{'placa':'abc','alugado':'Não','ano':'1999','cor':'preto'}]}] #vai conter os estados
estado = {} #vai conter dentro os carros e o nome do estado
menu()