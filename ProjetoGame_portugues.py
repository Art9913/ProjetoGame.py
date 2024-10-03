import random  


defesa_tanque = 51
hp_tanque = 51
inteligencia_mago = 51
mana_mago = 51
dano_ninja = 51
agilidade_ninja = 51


defesa = 99
hp = 99
inteligencia = 99
mana = 99
dano = 99
agilidade = 99

# Programa para simular a primeira missão de um jogo RPG
print("???? - A sua aventura começa aqui!!!")
print("PERSIAN - Olá, meu nome é Persian. Sou um grande mago e serei também seu conselheiro durante sua aventura!")
nome = input("PERSIAN - Primeiro diga qual o nome do seu herói: ")
print("\n")


print(f"PERSIAN - Ótimo, é um prazer te conhecer {nome}!")
print("PERSIAN - Nesse mundo, os jovens aventureiros podem escolher entre três classes:")
print("PERSIAN - Tanque, Mago ou Ninja.")
print()
print("PERSIAN - A classe tanque tem a defesa e a vida aumentada, porém tem menos agilidade. Eles são quem aguentam porrada! ")
print()
print("PERSIAN - Os magos ganham aumento de inteligência e de mana, usados em feitiços durante a batalha, mas não possuem uma grande defesa.")
print()
print("PERSIAN - Já os ninjas ganham a grande vantagem no dano e na agilidade, no entanto, tem a mana inferior, que é importante para se curar. ")
print()
print("1) Tanque, 2) Mago, 3) Ninja") 
classe = int(input("PERSIAN - Agora é sua vez, qual classe deseja escolher?: "))


if classe == 1:
    print("PERSIAN - Você escolheu tanque, pelo visto você é forte!")
    defesa += defesa_tanque
    hp += hp_tanque
    agilidade -= 19  
    inteligencia += 1
    mana += 1
    dano += 1
elif classe == 2:
    print("PERSIAN - Você escolheu mago, pronto para fazer feitiços?")
    defesa -= 19  
    hp += 1
    inteligencia += inteligencia_mago
    mana += mana_mago
    agilidade += 1
    dano += 1 
elif classe == 3:
    print("PERSIAN - Você escolheu ninja, seja ágil e furtivo!")
    hp += 1
    inteligencia += 1
    mana -= 19
    dano += dano_ninja
    agilidade += agilidade_ninja
    defesa += 1
 


print(f"PERSIAN - Você possui: {defesa} pontos de defesa; {hp} pontos de vida; {inteligencia} pontos de inteligência; {mana} pontos de mana; {dano} pontos de dano; {agilidade} pontos de agilidade.")
print()

print("PERSIAN - Antes de sair para sua primeira missão, você pode escolher um item de cada categoria!")
print("PERSIAN - São elas [Arma Corpo-a-Corpo], [Armadura], [Poções] e [Passiva]")
lista_arma = [
    "Katana (+25 dano; -10 agilidade)",
    "Adaga Dupla (+15 dano; +15 agilidade)",
    "Maça (+35 dano; -15 agilidade)",
    "Lança (+20 dano; -2 agilidade)"
]
print("Arma Corpo-a-Corpo", lista_arma)
print()
print("1) Katana, 2) Adaga Dupla, 3) Maça, 4) Lança.")
arma = int(input("Escolha a Arma que deseja [1], [2], [3], [4]: "))


if arma == 1:  
    dano += 25  
    agilidade -= 10  
    print("Você escolheu Katana!")
elif arma == 2:  
    dano += 15  
    agilidade += 15 
    print("Você escolheu Adaga Dupla!")
elif arma == 3:  
    dano += 35  
    agilidade -= 15  
    print("Você escolheu Maça!")
elif arma == 4: 
    dano += 20  
    agilidade -= 2  
    print("Você escolheu Lança!")
print()



lista_armadura = [
    "Armadura do Cavaleiro (+30 defesa; - 15 agilidade)",
    "Capa da Agilidade (+25 de agilidade )",
    "Braçadeira Mágica (+ 20 de mana; +5 de agilidade)",
    "Armadura de Ataque (+10 de dano; - 10 de agilidade)"
]
print("Armadura", lista_armadura)
print()
print("1) Armadura do Cavaleiro, 2) Capa da Agilidade, 3) Braçadeira Mágica, 4) Armadura de Ataque.")
armadura = int(input("Escolha a Armadura que deseja [1], [2], [3], [4]: "))


if armadura == 1:
    defesa += 30
    agilidade -= 15
    print("Você escolheu Armadura do Cavaleiro!")
elif armadura == 2:
    agilidade += 25
    print("Você escolheu Capa da Agilidade!")
elif armadura == 3:
    mana += 20
    agilidade += 5
    print("Você escolheu Braçadeira Mágica!")
elif armadura == 4:
    dano += 10 
    agilidade -= 10 
    print("Você escolheu Armadura de Ataque!")
print()



lista_pocoes = [
    "Poção de Cura (+20 vida)",
    "Poção da Velocidade (+20 agilidade)",
    "Poção da Fúria (+20 dano)",
    "Poção do Mago (+20 de mana)"
]
print("Poção", lista_pocoes)
print()
print("1) Poção de Cura, 2) Poção da Velocidade, 3) Poção de Fúria, 4) Poção do Mago.")
pocao = int(input("Escolha a Poção que deseja [1], [2], [3], [4]: "))


if pocao == 1:
    hp += 20
    print("Você escolheu Poção de Cura!")
elif pocao == 2:
    agilidade += 20
    print("Você escolheu Poção da Velocidade!")
elif pocao == 3:
    dano += 20 
    print("Você escolheu Poção da Fúria!")
elif pocao == 4:
    mana += 20
    print("Você escolheu Poção do Mago!")
print()



lista_passiva = [
    "A Vontade do Brigão (+10 dano; +10 defesa)",
    "A Sabedoria do Mago (+10 inteligência; +10 mana )"
    "O veloz (+20 agilidade)"
    "Fortificado (+20 de defesa)"
]
print("Passiva", lista_passiva)
print()
print("1) Vontade do Brigão, 2) A Sabedoria do Mago, 3) O Veloz, 4) Fortificado.")
passiva = int(input("Escolha a Passiva que deseja [1], [2], [3], [4]: "))


if passiva == 1:
    dano += 10
    defesa += 10
    print("Você escolheu A Vontade do Brigão!")
elif passiva == 2:
    inteligencia += 10
    mana += 10
    print("Você escolheu A Sabedoria do Mago!")
elif passiva == 3:
    agilidade += 20
    print("Você escolheu O Veloz!")
elif passiva == 4:
    defesa += 20
    print("Você escolheu Fortificado!")
print()


print(f"PERSIAN - Seu status final é:")
print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
print()



print(f"PERSIAN - Pronto, agora {nome} você está pronto para sua primeira missão.")
print("PERSIAN - Vá falar com meu amigo TYR na taverna, ele irá te instruir melhor. Até mais.")
print()
print(f"???? - Ao chegar na taverna, {nome} se depara com um homem imenso e bêbado.")
print()
print(f"TYR - Olá, você deve ser o {nome}, PERSIAN me falou que você iria aparecer.")
print("TYR - Eu sou um cientista e pesquiso sobre monstros e dna, visando domesticar os monstros para nos ajudar em batalha.")
print()
print("TYR - Preciso de uma ajuda com um dos nossos filhotes de dragão.")
print("TYR - Ele foi roubado por goblins que ficam no bosque maléfico, o dragãozinho é manso e medroso, então ajude-o.")
print()
print("MISSÃO 1 - Procure e resgate o Filhote de Dragão.")
print("\n")


vida_goblins = 220
dano_total = 0
ataque_magico = mana + inteligencia 
print(f"???? - Ao chegar no bosque maléfico, {nome} se deparou com 3 goblins pequenos, porém, ardilosos... ")
print("Goblins (220 de vida juntos.)")
print()


while hp > 0 and vida_goblins > 0:
    print("\nEscolha seu ataque: ")
    print("1) Ataque Normal (Necessário 100 de dano)")
    print("2) Ataque Mágico (Necessário 110 de mana e 110 de inteligência)")
    print("3) Ataque Rápido (Necessário 115 de agilidade )")      
    ataque_1 = int(input("Qual ataque deseja escolher? "))


    if ataque_1 == 1:
        dano_total = dano 
        print(f"{nome} escolheu Ataque Normal!")


    elif ataque_1 == 2 and mana >= 110 and inteligencia >= 110:
        dano_total = ataque_magico
        print(f"{nome} escolheu Ataque Mágico!")

    
    elif ataque_1 == 3 and agilidade >= 115:
        dano_total = agilidade 
        print(f"{nome} escolheu Ataque Mágico!")


    vida_goblins = max(vida_goblins - dano_total, 0)

    if dano_total > 0:
        print(f"Os goblins perderam {dano_total} de vida!")
        print(f"Vida restante dos goblins: {vida_goblins}")

    if vida_goblins > 0:
        dano_jogador = 10
        hp -= dano_jogador
        print(f"Os goblins contra-atacaram! {nome} perdeu {dano_jogador} de vida.")
        print(f"Vida restante do jogador: {hp}")
    

    elif vida_goblins == 0:
        print(f"{nome} venceu os goblins, parabéns!")
        print(f"Vida restante do jogador: {hp}")
        break

    
    if hp <= 0:
        print(f"{nome} foi derrotado pelos goblins...")
        break 



if hp > 0:
    print(f"???? - Após vencer os goblins {nome} continuou a explorar o bosque maléfico.")
    print(f"Você encontrou um baú contendo um item aleátorio!")
    itens = {
        1: "Poção da Vida", #Aumentar 30 de vida 
        2: "Espada Mágica", #Aumentar 30 de mana e 30 de dano
        3: "Escudo", #Aumentar 30 de defesa 
        4: "Livro de Mágias", #Aumentar 30 de mana e 30 de inteligencia
        5: "Caneleiras da Correria", #Aumentar 30 de agilidade 
        6: "Luvas do Caos" #Aumentar 30 de dano
        }
    numero_sorteado = random.randint(1,6)
    item_encontrado = itens.get(numero_sorteado)
    print(f"{nome} abriu o baú e encontrou: {item_encontrado}!")
    print()
    if numero_sorteado == 1:
        hp += 1
        print(f"Agora você possui {hp} pontos de vida!")
        print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
    elif numero_sorteado == 2:
        mana += 30
        dano += 30
        print(f"Agora você possui {mana} pontos de mana e {dano} pontos de dano!")
        print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
    elif numero_sorteado == 3:
        defesa += 30
        print(f"Agora você possui {defesa} pontos de defesa!")
        print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
    elif numero_sorteado == 4:
        mana += 30 
        inteligencia += 30
        print(f"Agora você possui {mana} pontos de mana e {inteligencia} de inteligência!") 
        print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
    elif numero_sorteado == 5:
        agilidade += 30
        print(f"Agora você possui {agilidade} pontos de agilidade!")
        print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
    elif numero_sorteado == 6: 
        dano += 30 
        print(f"Agora você possui {dano} pontos de dano!")
        print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")
        

    print()
    print(f"???? - Após muita exploração, {nome} encontrou uma caverna totalmente escura e aterrorizante")
    print(f"???? - Encontrando vários goblins no caminho, aquela caverna não era normal como as outras, {nome} tinha um pressentimento ruim")
    print(f"???? - Até que deu de cara com um monstro enorme, um ORC, porém o mais estranho, era que o monstro falou.")
    print("\n")
    print("ORC DAS TREVAS - Então enfim chegou o humano no qual me falaram, disseram que iriam vir atrás desse dragão filhote")
    print("ORC DAS TREVAS - Quer recuperalo, então me enfrente, só um de nós sairá vivo dessa caverna HAHAHAHAHAHAHA!")
    print()
    print("MISSÂO 2 - Derrote o ORC DAS TREVAS e leve o filhote de dragão para casa!")
    print("ORC DAS TREVAS (500 de vida e 250 de defesa)")
    print("\n")




    vida_orc = 500
    defesa_orc = 250
    dano_total_1 = 0 
    ataque_magico_fortificado = mana + inteligencia 
    ataque_supremo = dano + mana + inteligencia + agilidade 


    while hp > 0 and vida_orc > 0:
        print("\nEscolha seu ataque: ")
        print("1) Ataque Normal (Necessário 120 de dano)")
        print("2) Ataque Mágico Fortificado (Necessário 170 de mana e 150 de inteligência)")
        print("3) Ataque Ultra Rápido (Necessário 150 de agilidade )")      
        print("4) Ataque Supremo (Necessário 130 de dano, 130 de mana, 130 de inteligência e 130 de agilidade)")
        print("OBS: O Ataque Supremo tira 65 pontos de vida do jogador, use com sabedoria!")
        ataque_1 = int(input("Qual ataque deseja escolher? "))


        if ataque_1 == 1:
            dano_total_1 = dano 
            print(f"{nome} escolheu Ataque Normal!")

        
        elif ataque_1 == 2 and mana >= 170 and inteligencia >= 150:
            dano_total_1 = ataque_magico_fortificado
            print(f"{nome} escolheu Ataque Mágico Fortificado!")


        elif ataque_1 == 3 and agilidade >= 150:
            dano_total_1 = agilidade
            print(f"{nome} escolheu Ataque Ultra Rápido!")


        elif ataque_1 == 4 and dano >= 130 and mana >= 130 and inteligencia >= 130 and agilidade >= 130:
            dano_total_1 = ataque_supremo
            hp -= 65
            print(f"{nome} escolheu Ataque Supremo!")
            print(f"{nome} perdeu 65 pontos de hp!")
            print(f"{hp} pontos de vida restante para o jogador!")
        


        if defesa_orc > 0:
                defesa_orc = max(defesa_orc - dano_total_1, 0)
                
                
                if dano_total_1 > 0:
                    print(f"O ORC DAS TREVAS perdeu {dano_total_1} de defesa!")
                    print(f"Defesa restante do ORC DAS TREVAS: {defesa_orc}")

                if defesa_orc == 0:
                    print(f"{nome} destruiu a defesa do ORC DAS TREVAS. Agora derrote ele de uma vez por todas!")
                    print(f"Vida restante do jogador: {hp}")

    
        else:
            vida_orc = max(vida_orc - dano_total_1, 0)
            if dano_total_1 > 0:
                print(f"O ORC DAS TREVAS perdeu {dano_total_1} de vida!")
                print(f"Vida restante do ORC DAS TREVAS: {vida_orc}")

            if vida_orc == 0:
                print(f"{nome} derrotou o ORC DAS TREVAS, parabéns!")
                break
             

    
        if vida_orc > 0:
            dano_base_orc = 20

            dano_jogador_2 = max(dano_base_orc - (defesa // 40), 1)  
            
            hp -= dano_jogador_2
            print(f"O ORC DAS TREVAS contra-atacou! {nome} perdeu {dano_jogador_2} de vida!")
            print(f"Vida restante do jogador: {hp}")  

        if hp <= 0:
            print(f"{nome} foi derrotado pelo ORC DAS TREVAS...")
            break
    
    
    print("\n")
    if hp > 0:
        print(f"???? - {nome} recuperou o filhote de dragão e voltou para vila ao encontro de TYR.")
        print("TYR - Parabéns, você concluiu sua primeira missão, pensei que não conseguiria!")
        print("TYR - Pode ficar com esse filhote de dragão, ele gostou de você, cuide bem dele.")
        print(f"TYR - Além disso {nome}, como recompensa, você tem direito de escolher uma das bençãos a seguir!")
        print()
        print("1) A Coragem do fraco: Concede ao jogador mais 75 pontos em cada atributo!")
        print("2) O Mago Superior: Concede ao jogador mais 150 em mana e inteligência!")
        print("3) A Velocidade Sobre-Humana: Concede ao jogador mais 200 pontos em agilidade!")
        print("4) A Barreira Impenetrável: Concede ao jogador mais 150 pontos em defesa e vida!")
        escolha_bencao = int(input("Escolha sua Benção [1], [2], [3], [4]: "))
        


        if escolha_bencao == 1:
            defesa += 75
            hp += 75
            inteligencia += 75
            mana += 75
            dano += 75
            agilidade += 75
            print(f"{nome} escolheu A Coragem do Fraco!")
            print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")


        elif escolha_bencao == 2:
            mana += 150 
            inteligencia += 150
            print(f"{nome} escolheu O Mago Superior!")
            print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")


        elif escolha_bencao == 3:
            agilidade += 200
            print(f"{nome} escolheu A Velocidade Sobre-Humana!")
            print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")


        elif escolha_bencao == 4:
            defesa += 150
            hp += 150
            print(f"{nome} escolheu A Barreira Inpenetrável!")
            print(f"Defesa: {defesa}, Vida: {hp}, Inteligência: {inteligencia}, Mana: {mana}, Dano: {dano}, Agilidade: {agilidade}")



    print("TYR - Você se provou ser muito forte, espere por novas ordens para sua próxima missão!")
    print("\n")
    print("???? - Próxima missão em breve!")
