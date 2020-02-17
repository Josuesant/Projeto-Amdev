class BaseNotificacao:
    def __init__(self):
        arquivo = open(r'C:\Users\900172\Documents\JosueHBSIS\GitHub\notificacao\notificacao.txt', 'r')
        self.lista = []
        for linha in arquivo:
            linha = linha.strip()
            lista_linha = linha.split(';')
            dicionario_linhas = {'id':lista_linha[0], 'pessoa_id': lista_linha[1], 'data_evento': lista_linha[2], 'comentario': lista_linha[3], 'tipo_evento': lista_linha[4]}
            self.lista.append(dicionario_linhas)
        arquivo.close()
        return self.lista

