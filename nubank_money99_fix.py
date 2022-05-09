import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('É necessário fornecer o arquivo a ser corrigido.\nExemplo: >.\\nubank_money99_fix .\\nome_do_arquivo.ofx')
    else:
        try:
            f = open(sys.argv[1], "r")
            Lines = f.readlines()
            flag = False
            f.close()
            f = open(sys.argv[1], "w")

            for line in Lines:
                if line.__contains__('ENCODING:UTF-8'):
                    line = 'ENCODING:USASCII\n'
                if line.__contains__('CHARSET:NONE'):
                    line = 'CHARSET:1252\n'
                if line.__contains__('<BALLIST>'):
                    flag = True
                    line = ''
                if line.__contains__('</BALLIST>'):
                    flag = False
                    line = ''
                if flag == True:
                    line = ''
                f.write(line)

            f.close()

        except FileNotFoundError as error:
            print(error)
            print('Arquivo não encontrado')
