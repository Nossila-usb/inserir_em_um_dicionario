# dicionario
usuario = {
    'nome': '',
    'CPF': '',
    'RG': '',
    'Data de Nascimento': '',
    'Sexo' : '',
    'Signo':'',
    'Mãe':'',
    'Pai':'',
    'E-Mail':'',
    'Senha':'',
    'CEP' :'',
    'Endereço':'',
    'Número':'',
    'Bairro':'',
    'Cidade' : '',
    'Estado':'',
    'Telefone':'',
    'Celular':'',
    'Altura':'',
    'Peso':'',
    'Tipo Sanguineo':'',
    'Cor Favorita':'',
}


# adicinador o valor de uma chave
usuario['nome'] = input('Informe o novo nome: ').capitalize()

# adicinador o valor de uma chave
usuario['CPF'] = input('Informe o novo CPF: ')

# adicinador o valor de uma chave
usuario['RG'] = input('Informe o novo RG: ')

# adicinador o valor de uma chave
usuario['Data de Nascimento'] = input('Informe o novo Data de Nascimento: ')

# adicinador o valor de uma chave
usuario['Sexo'] = input('Informe o novo Sexo: ').capitalize()

# adicinador o valor de uma chave
usuario['Signo'] = input('Informe o novo Signo: ').capitalize()

# adicinador o valor de uma chave
usuario['Mãe'] = input('Informe a nova Mãe: ').capitalize()

# adicinador o valor de uma chave
usuario['Pai'] = input('Informe o novo Pai: ').capitalize()

# adicinador o valor de uma chave
usuario['E-Mail'] = input('Informe o novo E-Mail: ')

# adicinador o valor de uma chave
usuario['Senha'] = input('Informe a nova Senha: ')

# adicinador o valor de uma chave
usuario['CEP'] = input('Informe o novo CEP: ')

# adicinador o valor de uma chave
usuario['Endereço'] = input('Informe o novo Endereço: ')

# adicinador o valor de uma chave
usuario['Número'] = input('Informe o novo Número: ')

# adicinador o valor de uma chave
usuario['Bairro'] = input('Informe o novo Bairro: ').capitalize()

# adicinador o valor de uma chave
usuario['Cidade'] = input('Informe a nova Cidade: ').capitalize()

# adicinador o valor de uma chave
usuario['Estado'] = input('Informe o novo Estado: ').capitalize()

# adicinador o valor de uma chave
usuario['Telefone'] = input('Informe o novo Telefone: ')

# adicinador o valor de uma chave
usuario['Celular'] = input('Informe o novo Celular: ')

# adicinador o valor de uma chave
usuario['Altura'] = input('Informe o novo Altura: ')

# adicinador o valor de uma chave
usuario['Peso'] = input('Informe o novo Peso: ')

# adicinador o valor de uma chave
usuario['Tipo Sanguineo'] = input('Informe o novo Tipo Sanguineo: ')

# adicinador o valor de uma chave
usuario['Cor Favorita'] = input('Informe a nova Cor Favorita: ').capitalize()



# exibindo valores do dicionario na tela
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')
