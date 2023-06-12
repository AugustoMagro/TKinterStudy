import pyodbc

class ConectarDB:
    """Classe."""

    def __init__(self):
        """Construtor.
        O construtor é executado sempre que a classe é instanciada.
        """
        self.con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                  # Deve ser utilizado o path/caminho absoluto até o arquivo.
                                  r'DBQ=C:\Users\augus\OneDrive\Documentos\TelaPY\telaBase1.accdb;')

        # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
        self.cur = self.con.cursor()

    def exibir_tabelas(self):
        return self.cur.tables(tableType='TABLE')

    def exibir_colunas(self, table):
        return self.cur.columns(table)

    # CRUD.
    def inserir_registro(self, Nome, Sobrenome, CPF, Email):
        """Adiciona uma nova linha na tabela.
        :param dados: (tuple) Tupla contendo os dados.
        """
        try:
            self.cur.execute('''INSERT INTO base_geral (nome, sobrenome, cpf, email) VALUES (?,?,?,?)''', Nome, Sobrenome, CPF, Email)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            # rollback reverte/desfaz a operação.
            self.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def inserir_varios_registros(self, dados):
        """Adiciona varias linhas na tabela.
        Desta forma não se faz necessário um laço de
        repetição com vários ``inserts``.
        :param dados: (list) lista contendo tuplas
        (tuple) com os dados que serão inseridos.
        """
        try:
            self.cur.executemany(
                '''INSERT INTO NomeDaTabela (nome, idade, sexo) VALUES (?, ?, ?)''', dados)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registro_pela_id(self, CPF):
        """Consulta registro pela id.
        :param rowid: (int) id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        return self.cur.execute("""SELECT nome FROM base_geral WHERE cpf=? """, CPF).fetchone()

    def consultar_registros(self, nome):
        """Consulta todos os registros da tabela.
        Utilizando ``limit`` para evitar consultas longas de mais.
        :param limit: (int) Parâmetro que limita a
        quantidade de registros que serão exibidos.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia [``[]``].
        """
        return self.cur.execute(f'''SELECT TOP {10} * FROM base_geral WHERE nome=?''', nome).fetchall()

    def alterar_registro(self, rowid, nome, sexo):
        """Alterar uma linha da tabela com base na id.
        A query está configurada para alterar apenas o nome e sexo.
        :param rowid: (int) id da linha que se deseja alterar.
        :param nome: (str) String com o novo valor.
        :param sexo: (str) String com o novo valor.
        """
        try:
            self.cur.execute(
                '''UPDATE NomeDaTabela SET nome=?, sexo=? WHERE rowid=?''', (nome, sexo, rowid))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def remover_registro(self, rowid):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid: (int) id da linha que se deseja remover.
        """
        try:
            self.cur.execute(
                '''DELETE FROM NomeDaTabela WHERE rowid=?''', rowid)
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')


if __name__ == '__main__':
    # Verificar se o driver está instalado.
    # Se for retornada uma lista varia o driver precisa ser instalado.
    print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])

    # Criando a conexão com o banco.
    banco = ConectarDB()

    # Exibindo as tabelas que estão no banco.
    print('Tabelas do banco:')
    for tabela in banco.exibir_tabelas():
        print(tabela.table_name)

    # Exibindo as colunas de uma tabela;
    # print('\nColunas da tabela:')
    # for coluna in banco.exibir_colunas(table='NomeDaTabela'):
    #     print(coluna.column_name)

    # Dados
    # usuario = ('Felipe', 35, 'Masculino')
    # usuarios = [('Maria', 20, 'Feminino'), ('Pedro', 50, 'Masculino')]

    # Inserindo um registro tabela.
    # banco.inserir_registro(dados=usuario)

    # Inserindo vários registros na tabela.
    # banco.inserir_varios_registros(dados=usuarios)

    # Consultando com filtro.
    # print(banco.consultar_registro_pela_id(rowid=4))

    # Consultando todos (limit=10).
    # print(banco.consultar_registros())

    # Alterando registro da tabela.
    # Antes da alteração.
    # print(banco.consultar_registro_pela_id(rowid=1))
    # Realizando a alteração.
    # banco.alterar_registro(rowid=1, nome='Rafaela', sexo='Feminino')
    # Depois da alteração.
    # print(banco.consultar_registro_pela_id(rowid=1))

    # Removendo registro da tabela.
    # Antes da remoção.
    # print(banco.consultar_registros())
    # Realizando a remoção.
    # banco.remover_registro(rowid=1)
    # Depois da remoção.
    # print(banco.consultar_registros())