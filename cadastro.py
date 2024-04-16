class Aluno:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.notas = []

class SistemaNotas:
    def __init__(self):
        self.alunos = []
        self.notas_fila = []

    def cadastrar_aluno(self, nome):
        numero = len(self.alunos) + 1
        aluno = Aluno(numero, nome)
        self.alunos.append(aluno)
        print(f"Aluno {aluno.numero} ({aluno.nome}) cadastrado com sucesso!")

    def cadastrar_nota(self, numero_aluno, nota):
        aluno = self._buscar_aluno(numero_aluno)
        if aluno:
            if 0 <= nota <= 10:
                aluno.notas.append(nota)
                self.notas_fila.append((numero_aluno, nota))
                print(f"Nota {nota} cadastrada para o aluno {aluno.nome}.")
            else:
                print("A nota deve estar no intervalo entre 0 e 10.")
        else:
            print(f"Aluno com número {numero_aluno} não encontrado.")

    def calcular_media(self, numero_aluno):
        aluno = self._buscar_aluno(numero_aluno)
        if aluno:
            if aluno.notas:
                media = sum(aluno.notas) / len(aluno.notas)
                print(f"Média do aluno {aluno.nome}: {media:.2f}")
            else:
                print(f"O aluno {aluno.nome} não possui notas cadastradas.")
        else:
            print(f"Aluno com número {numero_aluno} não encontrado.")

    def listar_alunos_sem_notas(self):
        for aluno in self.alunos:
            if not aluno.notas:
                print(f"Aluno {aluno.numero} ({aluno.nome}) não possui notas cadastradas.")

    def excluir_aluno(self, numero_aluno):
        aluno = self._buscar_aluno(numero_aluno)
        if aluno:
            if not aluno.notas:
                self.alunos.remove(aluno)
                print(f"Aluno {aluno.numero} ({aluno.nome}) excluído com sucesso!")
            else:
                print(f"O aluno {aluno.nome} possui notas cadastradas e não pode ser excluído.")
        else:
            print(f"Aluno com número {numero_aluno} não encontrado.")

    def excluir_nota(self, numero_aluno):
        aluno = self._buscar_aluno(numero_aluno)
        if aluno:
            if aluno.notas:
                nota_removida = aluno.notas.pop(0)
                print(f"Nota {nota_removida} excluída para o aluno {aluno.nome}.")
            else:
                print(f"O aluno {aluno.nome} não possui notas cadastradas.")
        else:
            print(f"Aluno com número {numero_aluno} não encontrado.")

    def _buscar_aluno(self, numero_aluno):
        for aluno in self.alunos:
            if aluno.numero == numero_aluno:
                return aluno
        return None

if __name__ == "__main__":
    sistema = SistemaNotas()
    while True:
        print("\nMENU:")
        print("1 – Cadastrar aluno")
        print("2 – Cadastrar nota")
        print("3 – Calcular média de um aluno")
        print("4 – Listar nomes dos alunos sem notas")
        print("5 – Excluir aluno")
        print("6 – Excluir nota")
        print("7 – Sair")

        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            sistema.cadastrar_aluno(nome)
        elif opcao == 2:
            numero_aluno = int(input("Digite o número do aluno: "))
            nota = float(input("Digite a nota: "))
            sistema.cadastrar_nota(numero_aluno, nota)
        elif opcao == 3:
            numero_aluno = int(input("Digite o número do aluno: "))
            sistema.calcular_media(numero_aluno)
        elif opcao == 4:
            sistema.listar_alunos_sem_notas()
        elif opcao == 5:
            numero_aluno = int(input("Digite o número do aluno: "))
            sistema.excluir_aluno(numero_aluno)
        elif opcao == 6:
            numero_aluno = int(input("Digite o número do aluno: "))
            sistema.excluir_nota(numero_aluno)
        elif opcao == 7:
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida. Tente Novamente")
