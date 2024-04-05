canditatos = [
    ['canditato 1' , 'e5_t10_p8_s8'],
    ['canditato 2' , 'e10_t7_p7_s8'],
    ['canditato 3' , 'e8_t5_p4_s9'],
    ['canditato 4' , 'e2_t2_p2_s1'],
    ['canditato 5' , 'e10_t10_p8_s9'],
]


nomeCandidato = input(f'''
==========================================
       infome o nome do candidadoto:
=>''')

ava_entrevista = input(f'''
============================================
       informe a avaliação da entrevista(e):
=>''')

ava_testeTeorico = input(f'''
============================================
       infome a avaliação teste teorico(t):
=>''')

ava_testePratico = input(f'''
============================================
       infome a avaliação teste pratico(p):
=>''')

ava_softSkills = input(f'''
============================================
       infome a avaliação soft skills(s):
=>''')



def buscaCandidato(canditatos,entrevista,teorico,pratico,soft):
    canditatosAprovados = []
    for candidato, resultado in canditatos:
        notas = resultado.split('_')
        e = int(notas[0][1:])
        t = int(notas[1][1:])
        p = int(notas[2][1:])
        s = int(notas[3][1:])
        if e >= entrevista and t >= teorico and p >= pratico and s >= soft:
            canditatosAprovados.append(candidato)
    return canditatosAprovados

entrevista = int(input("Qual a nota mínima necessaria da entrevista [e]?"))
teorico = int(input("Qual a nota mínima necessaria para o teste teorico [t]?"))
pratico = int(input("Qual a nota mínima necessaria para o teste pratico [p]?"))
soft = int(input("Qual a nota mínima necessaria para o soft skills [s]?"))

canditatosAprovados = buscaCandidato(canditatos,entrevista,teorico,pratico,soft)

if canditatosAprovados:
    print("canditatos Aprovados: ")
    for canditato in canditatosAprovados:
        print(canditato)
else:
    print("Não existem canditatos aptos para a vaga!")