
#Lista de Tarefas (sem banco de dados)


#menu
def menu():
    print("____________________________________")
    print("\n1- Tarefas")
    print("2- adicionar tarefa")
    print("3- remover tarefa")
    print("\n4- exit")
    print("____________________________________")

#tarefas
def lista_tarefa():
    if not all_tarefas:
        print("⚠️ Sem tarefas registradas!⚠️")  
        return 
    print("____________________________________\n")
    for chave, elemento in all_tarefas.items():
        print(f"📌{chave}- {elemento}")        
    print("\n____________________________________") 
    input("Aperte Enter para voltar ao menu: ")

#adicionar tarefa
def add_tarefa():
    print("____________________________________")
    chave = input("\nQual o titulo da sua tarefa? ").upper()
    elemento = input(f"\nDescreva a tarefa\n📌{chave}- ").lower()
    all_tarefas[chave] = elemento
    print("____________________________________") 
    print(f"✔️ Tarefa '{chave}' adicionada com sucesso!✔️")

#apagar tarefa
def apagar_tarefa():
    if not all_tarefas:
        print("⚠️ Sem tarefas registradas!⚠️")  
        return 
    print("____________________________________\n")
    for chave in all_tarefas:
        print(f"❌{chave}")       
    chave = input("\nEscreva o nome da tarefa para apagar: ").upper()
    if chave in all_tarefas:
        del all_tarefas[chave]
        print(f"✔️ Tarefa '{chave}' apagada com sucesso!✔️")
        return    
    print("____________________________________")  
    print("⚠️ ERRO: Tarefa nao encontrada!⚠️")

#opçoes 1 a 4
def opçoes():
    try:
        opçao = int(input())
    except ValueError:
        opçao = input("⚠️ Escolha uma numero: ")
    if opçao not in [1, 2, 3, 4]:
        opçao = input("⚠️ Escolha uma numero válido: ")
    return opçao
    

all_tarefas = {}

#começo da execuçao
while True:
    menu()
    opçao = opçoes()
    
    if opçao == 1:
        lista_tarefa()
    
    elif opçao == 2:
        add_tarefa()
    
    elif opçao == 3:
        apagar_tarefa()
    
    else:
        print("Adeus......")
        break
