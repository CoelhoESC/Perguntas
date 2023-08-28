print(F'{"Jogo de PERGUNTAS & REPOSTAS".center(50)}')

Perguntas = {'Pergunta 1°': {
    'pergunta': 'Quanto é 2+2?',
    'resposta': {'A': '1', 'B': '4', 'C': '5'},
    'resposta_certa': 'B'
}, 'Pergunta 2°': {
    'pergunta': 'Qual a capital do Brasil?',
    'resposta': {'A': 'Bahia', 'B': 'São Paulo', 'C': 'Brasilia'},
    'resposta_certa': 'C'
}, 'Pergunta 3°': {
    'pergunta': 'Quanto é 9 X 6?',
    'resposta': {'A': '54', 'B': '60', 'C': '52'},
    'resposta_certa': 'A'
}, 'Pergunta 4°': {
    'pergunta': 'Quanto é aumento de 15% em um salario R$1,100?',
    'resposta': {'A': '1,115', 'B': '1,265', 'C': '1,295'},
    'resposta_certa': 'B'
}, }

Acerto = 0
Erros = 0
for pk, pv in Perguntas.items():   # Verificando chaves e valores do 1 dicionario (Perguntas)
    print(f'{pk} - {pv["pergunta"]}')  # Mostrando na tela chave e valor(pergunta)
    for rk, rv in pv['resposta'].items():  # Verificando Chave e valore do dicionario(reposta) dentro do 1 dicio(pc)
        print(f'[{rk}]: {rv}')
    Usuario_respota = input('Responda: ').upper()
    if Usuario_respota == pv['resposta_certa']:
        print('Você acertou!')
        Acerto += 1
    else:
        print('Você errou!')
        Erros += 1
    print()

if '__main__' in __name__:
    Quantidade_pergunta = len(Perguntas)
    Porcentagem_acertos = Acerto / Quantidade_pergunta * 100
    Porcentagem_erros = Erros / Quantidade_pergunta * 100
    print(f'Você acertou {Acerto} resposta(s)!')
    print(f'Você tem {Porcentagem_acertos}% de acerto e {Porcentagem_erros}% erros!')
