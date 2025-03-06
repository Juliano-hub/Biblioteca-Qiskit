from qiskit import QuantumCircuit
import numpy as np

from portas_quanticas.funcao_pertinencia import inicializa_circuito_com_probabilidades
from portas_quanticas.t_norma import toffoli_circuit_interactive
from portas_quanticas.t_conorma import apply_or_fuzzy_generic
from portas_quanticas.dif import diff_fuzzy
from portas_quanticas.grouping import add_grouping_function
from portas_quanticas.xor import add_xor_fuzzy
from portas_quanticas.overlap import add_overlap_function
from portas_quanticas.implicacaoSN import implication
from portas_quanticas.ql import ql_implication
from portas_quanticas.xor_fuzzy import xor_ominus
from portas_quanticas.xor_cross import xor_fuzzy_cross

def mostrar_menu():
    print("Selecione a porta quântica desejada:")
    print("1: T Norma do Produto (equivalente à porta Toffoli)")
    print("2: Aplicar operação OR fuzzy")
    print("3: Aplicar operação de Diferença Fuzzy")
    print("4: Aplicar função de Grouping")
    print("5: Aplicar XOR Fuzzy")
    print("6: Aplicar função de Overlap")  
    print("7: Aplicar função de Implicação (S, N)")  
    print("8: Aplicar XOR Fuzzy otimes")
    print("9: Aplicar XOR Fuzzy ominus")
    print("0: Sair")
    escolha = input("Digite o número da sua escolha e pressione Enter: ")
    return escolha


def get_qubit_indices():
    control_qubits = list(map(int, input("Digite os índices dos qubits de controle, separados por espaço (começando de 0): ").split()))
    target_qubits = list(map(int, input("Digite os índices dos qubits alvo, separados por espaço (começando de 0): ").split()))
    aux_qubits = list(map(int, input("Digite os índices dos qubits auxiliares, separados por espaço (começando de 0): ").split()))
    return control_qubits, target_qubits, aux_qubits

def main():
    num_qubits = int(input("Quantos qubits você quer no circuito? "))
    probabilidades = [float(x) for x in input("Digite as probabilidades para cada qubit, separadas por espaço: ").split()]

    my_circuit = inicializa_circuito_com_probabilidades(num_qubits, probabilidades)
    if my_circuit is None:
        return
    
    while True:
        escolha = mostrar_menu()
        if escolha == '1':
            toffoli_circuit_interactive(my_circuit)
            print("Desenhando o circuito:")
            print(my_circuit.draw('text'))
        elif escolha == '2':
            control_indices = list(map(int, input("Digite os índices dos qubits de controle, separados por espaço (começando de 0): ").split()))
            target_index = int(input("Digite o índice do qubit alvo para a operação OR fuzzy: "))
            apply_or_fuzzy_generic(my_circuit, control_indices, target_index)
            print("Circuito com operação OR fuzzy aplicada:")
            print(my_circuit.draw('text'))
        elif escolha == '3':
            qubit1 = int(input("Digite o índice do primeiro qubit para DIF: "))
            qubit2 = int(input("Digite o índice do segundo qubit para DIF: "))
            aux_qubit = int(input("Digite o índice do qubit auxiliar para DIF: "))
            diff_fuzzy(my_circuit, qubit1, qubit2, aux_qubit)
            print("Circuito com operação de Diferença Fuzzy aplicada:")
            print(my_circuit.draw('text'))
        elif escolha == '4':  # Adicionando a nova operação de Grouping
            qubit_indices = list(map(int, input("Digite os índices de todos os qubits para Grouping, separados por espaço: ").split()))
            add_grouping_function(my_circuit, qubit_indices)
            print("Circuito com função de Grouping aplicada:")
            print(my_circuit.draw('text'))
        elif escolha == '5':  # Chamada para a função XOR Fuzzy
            add_xor_fuzzy(my_circuit)
            print("Circuito com XOR Fuzzy aplicado:")
            print(my_circuit.draw('text'))
        elif escolha == '6':  # Chamada para a função Overlap
            qubit1 = int(input("Digite o índice do primeiro qubit para Overlap: "))
            qubit2 = int(input("Digite o índice do segundo qubit para Overlap: "))
            add_overlap_function(my_circuit, qubit1, qubit2)
            print("Circuito com função de Overlap aplicada:")
            print(my_circuit.draw('text'))
        elif escolha == '7':  # Implementação da chamada para a função de Implicação (S, N)
            control_qubit = int(input("Digite o índice do qubit de controle para IMP: "))
            target_qubit = int(input("Digite o índice do qubit alvo para IMP: "))
            aux_qubit = int(input("Digite o índice do qubit auxiliar para IMP: "))
            implication(my_circuit, control_qubit, target_qubit, aux_qubit)
            print("Circuito com função de Implicação (S, N) aplicada:")
            print(my_circuit.draw('text'))
        elif escolha == '7':  # Implementação da chamada para a função de Implicação QL
            control_qubit1 = int(input("Digite o índice do primeiro qubit de controle para IMP: "))
            control_qubit2 = int(input("Digite o índice do segundo qubit de controle para IMP: "))
            target_qubit = int(input("Digite o índice do qubit alvo para IMP: "))
            aux_qubit1 = int(input("Digite o índice do primeiro qubit auxiliar para IMP: "))
            aux_qubit2 = int(input("Digite o índice do segundo qubit auxiliar para IMP: "))
            ql_implication(my_circuit, control_qubit1, control_qubit2, target_qubit, aux_qubit1, aux_qubit2)
            print("Circuito com função de Implicação QL aplicada:")
            print(my_circuit.draw('text'))

        elif escolha == '8':  # Chamada para a função XOR Fuzzy ôminus
            print("Configuração para XOR ôminus")
            try:
                control_qubits = list(map(int, input("Digite os índices dos qubits de controle, separados por espaço (começando de 0): ").split()))
                target_qubits = list(map(int, input("Digite os índices dos qubits alvo, separados por espaço (começando de 0): ").split()))
                aux_qubits = list(map(int, input("Digite os índices dos qubits auxiliares, separados por espaço (começando de 0): ").split()))
                
                if len(control_qubits) < 2 or len(target_qubits) < 2 or len(aux_qubits) < 3:
                    print("Erro: Insira o número mínimo de qubits necessário para controle, alvo e auxiliares.")
                    continue

                xor_ominus(my_circuit, control_qubits, target_qubits, aux_qubits)
                print("Circuito com XOR Fuzzy ôminus aplicado:")
                print(my_circuit.draw('text'))
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Ocorreu um erro:", e)


        elif escolha == '9': 
            print("Configuração para XOR Fuzzy Cross")
            control_qubits = list(map(int, input("Digite os índices dos qubits de controle, separados por espaço (começando de 0): ").split()))
            if len(control_qubits) < 2:
                print("Erro: Insira pelo menos dois qubits de controle.")
                continue

            target_qubits = list(map(int, input("Digite os índices dos qubits alvo, separados por espaço (começando de 0): ").split()))
            if len(target_qubits) < 2:
                print("Erro: Insira pelo menos dois qubits alvo.")
                continue

            aux_qubits = list(map(int, input("Digite os índices dos qubits auxiliares, separados por espaço (começando de 0): ").split()))
            if len(aux_qubits) < 3:
                print("Erro: Insira pelo menos três qubits auxiliares.")
                continue

            xor_fuzzy_cross(my_circuit, control_qubits, target_qubits, aux_qubits)
            print("Circuito com XOR Fuzzy Cross aplicado:")
            print(my_circuit.draw('text'))

        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
