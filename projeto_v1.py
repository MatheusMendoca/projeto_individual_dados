pergunta = -1

while (pergunta != 0):
    pergunta = int(input(f'''
================== E X A M E ===================
           [1]QUAL E A MAIOR NOTA
           [2]QUAL E A MENOR NOTA
           [3] SAIR
================================================
'''))
    
    if (pergunta == 1):
           print(f'''
================================================
          Caditato 3 e9_t7_p8_s7
          Caditato 1 e8_t9_p3_s7
          Caditato 4 e10_t6_p6_s3
          Caditato 6 e5_t3_p9_s6
          Caditato 2 e7_t5_p5_s4
          Caditato 5 e4_t2_p8_s6
================================================
''')
    
    elif (pergunta == 2):
        print(f'''
================================================
         Caditato 5 e4_t2_p8_s6
         Caditato 2 e7_t5_p5_s4
         Caditato 6 e5_t3_p9_s6
         Caditato 4 e10_t6_p6_s3
         Caditato 1 e8_t9_p3_s7
         Caditato 3 e9_t7_p8_s7
==================================================
''')    
    elif (pergunta == 3):
        print(f'''
===============================================
  O B R I G A D O  V O L T E  S E M P R E
===============================================
''')
        break
    else:
         print("!!! ESSA OPÇÃO NÃO EXISTE POR FAVOR ESCOLHA OUTRA OPÇÃO !!!")