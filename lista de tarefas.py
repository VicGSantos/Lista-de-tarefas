import json
import os
import sys


#ENTRADA:
# titulo da tarefa
# tarefa
# descrição da tarefa

#PROCESSOS:
# menu: acessar tarefas, adicionar tarefa, remover tarefa
# adicionar tarefas
# nomear tarefa
# adicionar descrição a tarefa (opicional)
# listar titulo das tarefas
# trazer a tarefa e a descrição ao selecionar o titulo correspondente

#menu principal
def menu():
    print("____________________________________")
    print()
    print()
    print("1- Tarefas")
    print("2- adicionar tarefa")
    print("3- remover tarefa")
    print()
    print()
    print("____________________________________")

#menu tarefa
def lista_tarefaVazio():    #caso nao tenha nenhuma tarefa listada
    print("____________________________________")
    print()
    print()
    print("Sem tarefas para hoje.")
    print("1- adicionar tarefa")
    print("2- remover tarefa")
    print()
    print("____________________________________") 


def lista_tarefa():
    print("____________________________________")
    print()
    print()
    print("victor, coloca a lista de tarefas aqui")
    print()
    print("X- menu")    #volta ao menu
    print("____________________________________") 

#layout de add tarefa
def add_tarefa1():  #titulo da tarefa
    print("____________________________________")
    print()
    print()
    print("Qual o titulo da sua tarefa?")
    print()
    print()
    print("____________________________________") 

def add_tarefa2():  #qual é a tarefa
    print("____________________________________")
    print("victor, coloca o titulo aqui")   #titulo
    print()
    print("Tarefa: ")   #usario escreve a tarefa
    print()
    print()
    print("____________________________________")

def add_tarefa3():  #descrição da tarefa (opcional)
    print("____________________________________")
    print("victor, coloca o titulo aqui")   #titulo
    print()
    print("Resumo da sua tarefa: ")   #usario escreve a tarefa
    print()
    print("X- pular")   #nao quer por descrição
    print("____________________________________")



def tarefas():
    print()





#inicio da execução
while True:
    
    print()







    break

