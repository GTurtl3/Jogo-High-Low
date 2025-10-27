
import time
import os
import msvcrt

def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()

def limpar():
    os.system('cls')
    
def listas_rank():
    try:
        ficheiro_backup = open("Ranking_Hi-Lo_Backup.csv", "r", encoding="utf-8")
        lista_rank.clear()
        for contador, linha in enumerate(ficheiro_backup.readlines()):
            if contador > 0:
                campos = linha.strip().split(",")
                if len(campos) == 3:
                    registo = [int(campos[0]), campos[1].strip(), int(campos[2].strip())]
                    lista_rank.append(registo)
        lista_rank.sort(key=lambda x: (int(x[2]), x[1]))
    except FileNotFoundError:
        print()
        print("Erro: O ficheiro 'Ranking_Hi-Lo.csv' não foi encontrado.")
    except Exception as e:
        print()
        print(f"Erro ao carregar o ranking: {e}")

def erros_input(prompt):
    while True:
        try:
            input_ = input(prompt)
            if input_ == '':
                return ''
            input_int = int(input_)
            return input_int
        except EOFError:
            return(prompt)
        except ValueError:
            return(prompt)

def temp(segundos):
    time.sleep(segundos)
    limpar()
    flush_input()

def cabecalho(texto):
    tamanho = len(texto) + 6
    limpar()
    print()
    print("="*tamanho)
    print("|| " + texto.center(tamanho - 6) + " ||")
    print("="*tamanho)
    print()

def sub_cabecalho(texto):
    limpar()
    print()
    print(f"#"*3 + " " + texto + " " + "#"*3)
    print()

def comeca_jogo():
    cabecalho("Vamos comecar o jogo!")
    print()
    temp(1)
    import random 
    numero_secreto = random.randint(1, 100)  
    contador = 1
    while True:
        try:
            sub_cabecalho("Foi escolhido um número Random entre 1 a 100!")
            print("Tens 10 tentativas!")
            print()
            numero = erros_input('"0" Para voltar ao Menu Incial\n\nEnter p/ continuar....')
            if numero == 0:
                cabecalho("A voltar ao Menu Inicial...")
                temp(1.5)
                return
            elif numero == '':
                break
            else:
                sub_cabecalho("Opção inválida")
                erros_input('Pressione Enter para tentar novamente...')
                continue
        except EOFError:
            sub_cabecalho("Número  inválido")
            erros_input("ENTER P/ continuar...")
            limpar()
        except ValueError:
            sub_cabecalho("Número  inválido")
            erros_input("ENTER P/ continuar...")
            limpar()
    
    while True:
        try:
            limpar()
            print()
            numero = int(input(f"{contador}ª tentativa: "))
            if numero == 0:
                cabecalho("A voltar ao Menu Inicial...")
                temp(1.5)
                break
            
            if numero > 100 or numero < 1:
                sub_cabecalho("O número escolhido é inválido.")
                print()
                erros_input("ENTER p/ continuar....")
                continue

            if numero == numero_secreto:
                cabecalho("### Parabéns! ###")
                print(f"Adivinhaste o número em {contador} vezes!")
                print("\n" * 2)
                erros_input("ENTER P/ continuar...")
                while True:
                    sub_cabecalho('Digite o seu nome (máx 10 chars)')
                    print('  ---------- ')
                    nome = input('=>').strip()
                    if 1 <= len(nome) <= 10:
                        break
                    else:
                        limpar()
                        print("O Nome deve conter entre 1 e 10 caracteres. Tente novamente.")
                        print()
                        erros_input("ENTER P/ continuar...")
                score = contador
                lista_rank.clear()
                ficheiro = open("Ranking_Hi-Lo.csv", "r", encoding="utf-8")
                for linha in ficheiro.readlines():
                    campos = linha.strip().split(",")
                    try:    
                        if len(campos) == 3:
                            rank = int(campos[0])
                            nome_rank = campos[1]
                            score_rank = int(campos[2].strip())
                            lista_rank.append([rank, nome_rank, score_rank]) 
                    except ValueError:
                        continue
                ficheiro.close()
                lista_rank.append([None, nome.strip(), score])
                lista_rank.sort(key=lambda x: (x[2], x[1].strip()))
                rank = 1
                lista_rank[0][0] = rank
                for i in range(1, len(lista_rank)):
                    if lista_rank[i][2] == lista_rank[i - 1][2]:
                        lista_rank[i][0] = lista_rank[i-1][0]
                    else:
                        rank += 1
                        lista_rank[i][0] = rank
                ficheiro = open("Ranking_Hi-Lo.csv", "r+", encoding="utf-8")
                ficheiro.write("Rank, Nome, Score\n")
                for rank, nome, score in lista_rank:
                    ficheiro.write(f"{rank}, {nome.strip()}, {score}\n")
                ficheiro.close()
                ranking_top10()                                 
                break
                            
            elif numero > numero_secreto:
                sub_cabecalho(f"O número escolhido é menor que o {numero}.")
                print()
                erros_input("ENTER p/ continuar....")
            else:
                sub_cabecalho(f"O número escolhido é maior que o {numero}.")
                print()
                erros_input("ENTER p/ continuar....")
            contador += 1
            
            if contador > 10:
                cabecalho("### GAME OVER ###")
                print()
                erros_input("ENTER P/ voltar ao Menu Inicial...")
                cabecalho("A voltar ao Menu Inicial...")
                temp(1.5)
                break

        except EOFError:
            sub_cabecalho("Número  inválido A")
            erros_input("ENTER P/ continuar...")
            limpar()
        except ValueError:
            sub_cabecalho("Número  inválido B")
            erros_input("ENTER P/ continuar...")
            limpar()

def ranking_top10():
    while True:         
        try:
            cabecalho("Últimas 10 Pontuações")
            ficheiro = open("Ranking_Hi-Lo.csv", "r", encoding="utf-8")            
            contador = 0            
            print(f"{'Rank'.ljust(8)}{'Nome'.ljust(13)}{'Score'.ljust(6)}")
            print("="*27)
            for linha in ficheiro.readlines():
                if contador > 0:
                    campos = linha.strip().split(",")
                    if len(campos) == 3:
                        registo = [int(campos[0]), campos[1].strip(), int(campos[2].strip())]
                    print(f"{str(registo[0]).ljust(8)}{registo[1].ljust(13)}{str(registo[2]).ljust(6)}")
                contador += 1
                if contador > 10:                        
                        break
            ficheiro.close()
            print("\n"*2)
            erros_input("ENTER p/ continuar....")
            limpar()
            break
        except FileNotFoundError:
            print()
            print('Erro: O ficheiro "Ranking_Hi-Lo.csv" não foi encontrado.')
            erros_input("ENTER p/ continuar....")
            break
        except Exception as e:
            print()
            print(f"Erro ao abrir o ficheiro: {e}")
            print()
            erros_input("ENTER   P/ continuar...")
            break

def ranking():
    while True: 
        cabecalho("Todas as Pontuações")
        try:
            ficheiro = open("Ranking_Hi-Lo.csv", "r", encoding="utf-8")
            sub_cabecalho('Conteúdos do Ficheiro')
            contador = 0
            print("="*30)
            print(f"{'Rank':<8}{'Nome':<13}{'Score':<6}")
            print("="*30)
            for linha in ficheiro.readlines():
                if contador > 0:
                    campos = linha.strip().split(",")
                    if len(campos) == 3:
                        registo = [int(campos[0]), campos[1].strip(), int(campos[2].strip())]
                    print(f"{registo[0]:<8}{registo[1]:<13}{registo[2]:<6}")
                contador += 1
            ficheiro.close()
            print("\n" * 2)
            print("### Fim do Ficheiro ###")
            print()
            erros_input("ENTER p/ continuar....")
            limpar()
            break
        except FileNotFoundError:
            print()
            print('Erro: O ficheiro "Ranking_Hi-Lo.csv" não foi encontrado.')
            erros_input("ENTER p/ continuar....")
            break
        except Exception as e:
            print()
            print(f"Erro ao abrir o ficheiro: {e}")
            print()
            erros_input("ENTER   P/ continuar...")
            break

def resumo_geral():
    while True:
        cabecalho("Resumo Geral")
        if lista_rank == 0:
            print("Não há dados no ranking para calcular estatísticas.")
            print()
            erros_input("Enter p/ voltar ao Menu anterior....")
            break

        soma_tentativas = 0
        n = int(len(lista_rank))

        for jogador in lista_rank:
            try:
                soma_tentativas += jogador[2]
            except IndexError:
                print(f"Erro ao processar jogador: {jogador[1]}. Formato inválido.")
                continue
        if n > 0:
            media_tentativas = soma_tentativas / n
        else: 
            media_tentativas = 0

        if n > 0:
            print(f"Total de jogadores registados: {n}")
            print(f"Total de partidas jogadas: {n}")
        else:
            print("Não há dados para calcular Total de jogadores registados.")
            print("Não há dados para calcular Total de partidas jogadas.")
        if media_tentativas > 0:
            print(f"Média de tentativas por jogador: {media_tentativas:.0f}")
        else:
            print("Não há dados para calcular a media.")
        print()
        erros_input('Enter p/ voltar ao Menu anterior....')
        break

def melhores_piores():
    while True:
        cabecalho("Melhores e Piores Jogadores")
        if lista_rank == 0:
            sub_cabecalho("Não há dados no ranking para mostrar estatísticas.")
            erros_input('Enter p/ voltar ao Menu Anterior....')
            break
        if len(lista_rank) > 0:
            print(f"                {'Rank'.ljust(8)}{'Nome'.ljust(11)}{'Tentativas'.ljust(6)}")
            print("=" * 46)
            print(f"Melhor Jogador: 1".ljust(24) + f"{lista_rank[0][1].ljust(11)}{str(lista_rank[0][2])}")
            print(f"Pior Jogador:   {str(lista_rank[-1][0]).ljust(8)}{lista_rank[-1][1].ljust(11)}{str(lista_rank[-1][2])}")
            print("=" * 46)
            print()
        erros_input('Enter p/ voltar ao Menu Anterior....')
        break

def menu_estat():
    while True:
        cabecalho("Menu de Estatísticas")
        print("1. Resumo Geral")
        print("2. Melhores e Piores Jogadores")
        print("3. Ranking Total")
        print("0. Voltar ao Menu Anterior")
        print()
        try:
            opcao = erros_input("Escolha uma opção: ")
        except ValueError:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')
            continue

        if opcao == 1:
            resumo_geral()
        elif opcao == 2:
            melhores_piores()
        elif opcao == 3:
            ranking()
        elif opcao == 0:
            break
        else:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')

def ver_numero():
    cabecalho("Vamos comecar o jogo!")
    print()
    temp(1)
    import random 
    numero_secreto = random.randint(1, 100)  
    contador = 1
    while True:
        try:
            sub_cabecalho("Foi escolhido um número Random entre 1 a 100!")
            print("Tens 10 tentativas!")
            print()
            numero = erros_input('"0" Para voltar ao Menu Anterior\n\nEnter p/ continuar....')
            if numero == 0:
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)
                return
            elif numero == '':
                break
            else:
                sub_cabecalho("Opção inválida")
                erros_input('Pressione Enter para tentar novamente...')
                continue
        except EOFError:
            sub_cabecalho("Número  inválido")
            erros_input("ENTER P/ continuar...")
            limpar()
        except ValueError:
            sub_cabecalho("Número  inválido")
            erros_input("ENTER P/ continuar...")
            limpar()
    
    while True:
        try:
            limpar()
            print()
            print(f"O número sercreto é {numero_secreto}.")
            print()
            numero = int(input(f"{contador}ª tentativa: "))
            if numero == 0:
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)
                break
                            
            if numero == numero_secreto:
                cabecalho("### Parabéns! ###")
                print(f"Adivinhaste o número em {contador} vezes!")
                print("\n" * 2)
                erros_input("ENTER P/ continuar...")                
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)                    
                break
                
            elif numero > numero_secreto:
                sub_cabecalho(f"O número escolhido é menor que o {numero}.")
                print()
                erros_input("ENTER p/ continuar....")
            else:
                sub_cabecalho(f"O número escolhido é maior que o {numero}.")
                print()
                erros_input("ENTER p/ continuar....")
            contador += 1

            if contador > 10:
                cabecalho("### GAME OVER ###")
                print()
                erros_input("ENTER P/ voltar ao Menu Anterior...")
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)
                break

        except EOFError:
            sub_cabecalho("Número  inválido A")
            erros_input("ENTER P/ continuar...")
            limpar()
        except ValueError:
            sub_cabecalho("Número  inválido B")
            erros_input("ENTER P/ continuar...")
            limpar()

def definir_numero():
    cabecalho("Vamos comecar o jogo!")
    print()
    temp(1)
    while True:
        try:
            sub_cabecalho("Define um número entre 1 a 100!")
            numero_secreto = int(input("Número: "))
            if 1 < numero_secreto > 100:
                sub_cabecalho("Número  inválido")
                erros_input("ENTER P/ continuar...")
                limpar()
                continue  
            limpar()
            sub_cabecalho("Foi escolhido um número Random entre 1 a 100!")         
            print("Tens 10 tentativas!")
            print()
            numero = erros_input('"0" Para voltar ao Menu Anterior\n\nEnter p/ continuar....')
            if numero == 0:
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)
                return
            elif numero == '':
                break
            else:
                sub_cabecalho("Opção inválida")
                erros_input('Pressione Enter para tentar novamente...')
                continue
        except EOFError:
            sub_cabecalho("Número  inválido")
            erros_input("ENTER P/ continuar...")
            limpar()
        except ValueError:
            sub_cabecalho("Número  inválido")
            erros_input("ENTER P/ continuar...")
            limpar()
    contador = 1
    while True:
        try:
            limpar()
            print()
            numero = int(input(f"{contador}ª tentativa: "))
            if numero == 0:
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)
                break
                            
            if numero == numero_secreto:
                cabecalho("### Parabéns! ###")
                print(f"Adivinhaste o número em {contador} vezes!")
                print("\n" * 2)
                erros_input("ENTER P/ continuar...")                
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)                    
                break
                
            elif numero > numero_secreto:
                sub_cabecalho(f"O número escolhido é menor que o {numero}.")
                print()
                erros_input("ENTER p/ continuar....")
            else:
                sub_cabecalho(f"O número escolhido é maior que o {numero}.")
                print()
                erros_input("ENTER p/ continuar....")
            contador += 1

            if contador > 10:
                cabecalho("### GAME OVER ###")
                print()
                erros_input("ENTER P/ voltar ao Menu Anterior...")
                cabecalho("A voltar ao Menu Anterior...")
                temp(1.5)
                break

        except EOFError:
            sub_cabecalho("Número  inválido A")
            erros_input("ENTER P/ continuar...")
            limpar()
        except ValueError:
            sub_cabecalho("Número  inválido B")
            erros_input("ENTER P/ continuar...")
            limpar()

def menu_teste():
    
    while True:
        cabecalho('Ferramentas de Teste')
        print(" 1. Ver o número secreto")
        print(" 2. Definir manualmente o número secreto")
        print(" 0. Voltar ao Menu Anterior")
        print()
        try:
            opcao = erros_input("Escolha uma opção: ")
        except ValueError:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')
            continue
        if opcao == 1:
            ver_numero()
        elif opcao == 2:
            definir_numero()
        elif opcao == 0:
            break
        else:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')

def guarda_backup():    
    while True:
        cabecalho("Guardar Dados em Back Up")
        print()
        numero = erros_input('"0" Para cancelar e voltar atrás.\n\nEnter p/ continuar....')
        if numero == 0:
            return
        elif numero == '':
            break
        else:
            print()
            sub_cabecalho("Opção inválida")
            temp(2) 
            return 
    try:
        lista_rank.clear()
        ficheiro = open("Ranking_Hi-Lo.csv", "r", encoding="utf-8")
        sub_cabecalho('Ranking')
        contador = 0
        print("="*30)
        print(f"{'Rank':<8}{'Nome':<13}{'Score':<6}")
        print("="*30)
        for linha in ficheiro.readlines():
            campos = linha.strip().split(",")
            if len(campos) == 3:
                try:
                    rank = int(campos[0])
                    nome = campos[1].strip()
                    score = int(campos[2].strip())
                    lista_rank.append([rank, nome, score])  
                except ValueError:
                    continue         
        ficheiro_backup = open('Ranking_Hi-Lo_Backup.csv', 'w', encoding='utf-8')
        ficheiro_backup.write("Rank, Nome, Score\n")
        for rank, nome, score in lista_rank:
            ficheiro_backup.write(f"{rank}, {nome.strip()}, {score}\n")    
        sub_cabecalho("Os Dados foram guardados em Backup com sucesso!")    
        print()
        erros_input("ENTER p/ continuar....")
    except FileNotFoundError:
        print()
        print('Erro: O ficheiro "Ranking_Hi-Lo.csv" não foi encontrado.')
        erros_input("ENTER p/ continuar....")
    except Exception as e:
        print()
        print(f"Erro ao abrir o ficheiro: {e}")
        print()
        erros_input("ENTER   P/ continuar...")
    
def limpa_dados():
    while True: 
        cabecalho("Limpar Dados")
        print()
        try:
            ficheiro = open("Ranking_Hi-Lo.csv", "r", encoding="utf-8")
            sub_cabecalho('Conteúdos do Ficheiro')
            contador = 0
            print("="*30)
            print(f"{'Rank':<8}{'Nome':<13}{'Score':<6}")
            print("="*30)
            for linha in ficheiro.readlines():
                if contador > 0:
                    campos = linha.strip().split(",")
                    if len(campos) == 3:
                        registo = [int(campos[0]), campos[1].strip(), int(campos[2].strip())]
                    print(f"{registo[0]:<8}{registo[1]:<13}{registo[2]:<6}")
                contador += 1
            print("\n" * 2)
            print("### Fim do Ficheiro ###")
            print()
            print("Tem a certeza de que deseja apagar o conteúdo do ficheiro?")
            print()
            confirma = erros_input('"0" Para cancelar e voltar atrás.\n\nEnter p/ continuar....')
            if confirma == '':
                ficheiro = open('Ranking_Hi-Lo.csv', 'w', encoding='utf-8')
                ficheiro.write("Rank, Nome, Score\n")                
            elif confirma == 0:
                cabecalho('Operação cancelada. Os Dados não foram limpos.')
                print()
                erros_input("ENTER p/ continuar....")
                break
            else:
                sub_cabecalho("Operação inválida.")
                temp(1.5)
                continue
            limpar()
            cabecalho("Os Dados foram limpos com sucesso!")
            print()
            erros_input("ENTER p/ continuar....")
            break
        except FileNotFoundError:
            print()
            print('Erro: O ficheiro "Ranking_Hi-Lo.csv" não foi encontrado.')
            erros_input("ENTER p/ continuar....")
            break
        except Exception as e:
            print()
            print(f"Erro ao abrir o ficheiro: {e}")
            print()
            erros_input("ENTER   P/ continuar...")
            break

def recupera_dados():
    while True:
        cabecalho("Recuperar Dados")
        ficheiro_backup = open("Ranking_Hi-Lo_Backup.csv", "r", encoding="utf-8")
        print("="*30)
        print(f"{'Rank':<8}{'Nome':<13}{'Score':<6}")
        print("="*30)
        lista_rank.clear()
        for contador, linha in enumerate(ficheiro_backup.readlines()):
            if contador > 0:
                campos = linha.strip().split(",")
                if len(campos) == 3:
                    registo = [int(campos[0]), campos[1].strip(), int(campos[2].strip())]
                    lista_rank.append(registo)
                    print(f"{registo[0]:<8}{registo[1]:<13}{registo[2]:<6}")
        lista_rank.sort(key=lambda x: (int(x[2]), x[1]))
        print()
        print("### Fim do Ficheiro ###")        
        print()
        numero = erros_input('"0" Para cancelar e voltar atrás.\n\nEnter p/ continuar....')      
        if numero == 0:
            return
        elif numero == '':
            break
        else:
            print()
            sub_cabecalho("Opção inválida")
            temp(2) 
            return 
    try:        
        ficheiro_principal = open("Ranking_Hi-Lo.csv", "w", encoding="utf-8")
        ficheiro_principal.write("Rank, Nome, Score\n")
        for i, (_, nome, score) in enumerate(lista_rank, start=1):
                ficheiro_principal.write(f"{i}, {nome}, {score}\n")
        limpar()
        print()
        cabecalho("Dados recuperados e guardados no ficheiro principal")
        print()
        erros_input("ENTER p/ continuar....")
        limpar()
        return lista_rank
    except FileNotFoundError:
        print()
        print('Erro: O ficheiro "Ranking_Hi-Lo.csv" não foi encontrado.')
        erros_input("ENTER p/ continuar....")
    except Exception as e:
        print()
        print(f"Erro ao abrir o ficheiro: {e}")
        print()
        erros_input("ENTER   P/ continuar...")

def menu_ajuda():
    cabecalho(" MENU AJUDA ")
    print("""
    === COMO JOGAR ===
    1. O objetivo do jogo é adivinhar o número secreto gerado pelo sistema.
    2. O número secreto está entre 1 e 100.
    3. Tens 10 tentativas para adivinhar o número.
    4. Após cada tentativa, o sistema indicará se o número secreto é maior ou menor que o número escolhido.

    === FUNÇÕES DO MENU ===
    1. Iniciar Jogo: Começa uma nova partida.
    2. Ranking: Consulta as 10 melhores pontuações.
    3. Recuperar Dados: Recupera o backup das pontuações salvas anteriormente.
    4. Limpar Dados: Apaga o conteúdo atual do ranking.
    5. Guardar Backup: Salva os dados do ranking em um ficheiro de backup.

    === OUTRAS INFORMAÇÕES ===
    1. Para voltar ao menu principal, digita "0".
    2. Se desejares sair do programa, seleciona a opção "0" no menu principal.

    === SOBRE O SISTEMA ===
    Este jogo foi desenvolvido como um exercício de programação para treinar lógica e manipulação de ficheiros.
    """)
    print()
    erros_input("Pressiona ENTER para voltar ao menu principal...")

def menu_manutencao():
    
    while True:
        cabecalho('Menu de Manutenção')
        print(" 1. Ferramentas de Teste")
        print(" 2. Ver estatísticas internas")
        print(" 3. Guardar dados em Backup")
        print(" 4. Recuperar dados em Backup")
        print(" 5. Limpar dados")
        print(" 0. Sair")
        print()

        try:
            opcao = erros_input("Escolha uma opção: ")
        except ValueError:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')
            continue
        if opcao == 1:
            menu_teste()
        elif opcao == 2:
            menu_estat()
        elif opcao == 3:
            guarda_backup()
        elif opcao == 4:
            recupera_dados()
        elif opcao == 5:
            limpa_dados()
        elif opcao == 0:
            break
        else:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')

def main(): 
    listas_rank()
    while True:
        cabecalho("Jogo Hi-Lo")
        print(" 1. Começar Jogo")
        print(" 2. Top 10 Ranking")
        print(" 3. Ajuda")
        print(" 0. Sair")
        print()
        try:
            opcao = erros_input("Escolha uma opção: ")
        except ValueError:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')
            continue

        if opcao == 1:
            comeca_jogo()
        elif opcao == 2:
            ranking_top10()
        elif opcao == 3:
            menu_ajuda()
        elif opcao == 1234:
            menu_manutencao()
        elif opcao == 0:
            limpar()
            cabecalho("Obrigado por jogares! Até a próxima!")
            temp(2)
            limpar()
            break
        else:
            cabecalho("Opção inválida")
            erros_input('Enter p/ voltar ao Menu....')

lista_rank = []

main()