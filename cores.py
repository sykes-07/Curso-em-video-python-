#cores no terminal 
#
#style(tipo)        text(fonte)        back(fundo)
#0 (nada)            30 (white)        40
#1 (negrito)         31 (red)          41  
#4 (sumblinh)        32 (green)        42
#7 (negativo)        33 (yellow)       43
#                    34 (blue)         44
#                    35 (purple)       45
#                    36 (cyan)         46
#                    37 (grey)         47
#
# 
# como criar?
# 
#print("\033[style ; text ;backm TEXTO ESCCRITO\033[m")
# 
# pode crar dicionario tambem
# 
# cores{"limpa" : "\033[m"
#       "azul" : "\033[34m"
#       "amarelo" : "\033[33m"
#       "pretobranco" :"\033[7;30m"}
# 
# 
# 
# 
# exemplo 

# print("\033[7;33;44mHello Word!\033[m") 