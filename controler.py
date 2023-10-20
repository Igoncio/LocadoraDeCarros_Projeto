from PyQt6 import uic, QtWidgets
import pymysql

banco = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="fabrica276"
)

app = QtWidgets.QApplication([])

# ============================== LIGAÇÕES COM AS TELAS ========================================


cadastro_cliente = uic.loadUi("cadastro_cliente.ui")
form_usuario = uic.loadUi("a.ui")
tela_login = uic.loadUi("tela_login.ui")
tela_opcao = uic.loadUi("tela_opcao.ui")
cadastro_carro = uic.loadUi("cadastro_carro.ui")
gerenciar_carro = uic.loadUi("gerenciar_car.ui")
loca_carro = uic.loadUi("locar_carro.ui")
loca_diaria = uic.loadUi("locar_diaria.ui")
loca_mensal = uic.loadUi("locar_mensal.ui")
compra_carro = uic.loadUi("comprar_carro.ui")
delet_carro = uic.loadUi("deletar_carro.ui")
edit_carro = uic.loadUi("editar_carro.ui")
comprar_carro2 = uic.loadUi("comprar_carro2.ui")
ger_cli = uic.loadUi("gerenciar_cli.ui")
delet_cli = uic.loadUi("deletar_cli.ui")
locar_car_d2 = uic.loadUi("loc_carro_d2.ui")
locar_car_m = uic.loadUi("loc_carro_m.ui")
edita_car = uic.loadUi("editar_dados_carro.ui")
reset_car = uic.loadUi("resetar_carro.ui")

# ============================== FUNÇÕES =======================================================


def tela_loginAdm():
    tela_login.show()
    tela_login.confirmarbtn.clicked.connect(verificar_credenciais)


def verificar_credenciais():
    cursor = banco.cursor()
    email = tela_login.email.text()
    senha = tela_login.senha.text()
    query = "SELECT * FROM administrador WHERE email = %s AND senha = %s"
    cursor.execute(query, (email, senha))
    resultado = cursor.fetchone()



    if resultado:
        print("Credenciais corretas")
        tela_opcao.show()
        tela_opcao.abtn.clicked.connect(tel_cad_cli)
        tela_opcao.cad_car.clicked.connect(tela_cad_car)
        tela_opcao.comprar_btn.clicked.connect(comprar_carro)

    else:
        print("Credenciais incorretas")


def cadastrar_cliente():
    nome = cadastro_cliente.nome.text()
    email2 = cadastro_cliente.email2.text()
    cpf = cadastro_cliente.cpf.text()
    telefone = cadastro_cliente.telefone.text()
    data_nasc = cadastro_cliente.data_nasc.text()

    cursor = banco.cursor()
    sql = "INSERT INTO usuario(nome, email_user, cpf, telefone, data_nasc) VALUES (%s, %s, %s, %s, %s)"
    dados = (str(nome), str(email2), str(cpf), str(telefone), data_nasc)
    cursor.execute(sql, dados)
    banco.commit()

    cadastro_cliente.nome.setText("")
    cadastro_cliente.email2.setText("")
    cadastro_cliente.cpf.setText("")
    cadastro_cliente.telefone.setText("")
    cadastro_cliente.data_nasc.setText("") 


def cadastrar_carro():
    marca = cadastro_carro.marca.text()
    modelo = cadastro_carro.modelo.text()
    ano = cadastro_carro.ano.text()
    cor = cadastro_carro.cor.text()
    placa = cadastro_carro.placa.text()
    preco = cadastro_carro.preco.text()
    preco_diaria = cadastro_carro.preco_diaria.text()
    preco_mensal = cadastro_carro.preco_mensal.text()

    cursor = banco.cursor()
    sql = "INSERT INTO carros(marca, modelo, ano, cor, placa, preco_total, preco_diaria, preco_mensal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (str(marca), str(modelo), str(ano), str(cor), str(placa), preco, preco_diaria, preco_mensal)
    cursor.execute(sql, dados)
    banco.commit()

    cadastro_carro.marca.setText("")
    cadastro_carro.modelo.setText("")
    cadastro_carro.ano.setText("")
    cadastro_carro.cor.setText("")
    cadastro_carro.placa.setText("")
    cadastro_carro.preco.setText("")
    cadastro_carro.preco_diaria.setText("")
    cadastro_carro.preco_mensal.setText("")
    

def listar_dados():

    gerenciar_carro.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    gerenciar_carro.tableWidget.setRowCount(len(dados_recebidos))
    gerenciar_carro.tableWidget.setColumnCount(13)

    nomes_colunas = ["Número", "Marca", "Modelo","Ano","Cor","Placa","Preco_Total","Preco_Diaria","Preco_Mensal", "Tempo Loc.Dia", "Tempo Loc.Mes", "Status", "Dono"]
    gerenciar_carro.tableWidget.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 13):
            gerenciar_carro.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))

    gerenciar_carro.delet_btn.clicked.connect(delet_car)
    gerenciar_carro.edit_btn.clicked.connect(edit_car)
    gerenciar_carro.reset_btn.clicked.connect(resetar_car)


def locar_carro():
    loca_carro.show()

    loca_carro.dbtn.clicked.connect(locar_diaria)
    loca_carro.mbtn.clicked.connect(locar_mensal)


def locar_diaria():
    loca_diaria.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    loca_diaria.tabela_diaria.setRowCount(len(dados_recebidos))
    loca_diaria.tabela_diaria.setColumnCount(8)

    nomes_colunas = ["Número", "Marca", "Modelo","Ano","Cor","Placa","Preco_Total","Preco_Diaria"]
    loca_diaria.tabela_diaria.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 9):
            loca_diaria.tabela_diaria.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))


def locar_d2():
    locar_car_d2.show()
    

    cursor = banco.cursor()
    sql3 = "SELECT * FROM usuario"
    cursor.execute(sql3)
    dados_recebidos = cursor.fetchall()

    locar_car_d2.table_cli.setRowCount(len(dados_recebidos))
    locar_car_d2.table_cli.setColumnCount(7)

    nomes_colunas = ["Número", "Nome", "Email","Cpf","Telefone","Data_nascimento","Numero do carro"]
    locar_car_d2.table_cli.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 7):
            locar_car_d2.table_cli.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))


def locar_d3():

    status = "Locado Diaria"
    carro_locado = loca_diaria.id_carro.text()
    loca_diaria.id_carro.setText("")

    
    cliente_comprou = locar_car_d2.id_cli.text()
    locar_car_d2.id_cli.setText("")


    dias_locados = locar_car_d2.id_cli_3.text()
    locar_car_d2.id_cli_3.setText("")

    cursor = banco.cursor()


    sql_teste2 = "SELECT modelo FROM carros WHERE id = {}".format(carro_locado)
    cursor.execute(sql_teste2)
    result2 = cursor.fetchone()

    sql = "UPDATE carros SET status = '{}' WHERE id = {}".format(status, carro_locado)
    cursor.execute(sql)
    banco.commit()

    sql_teste = "SELECT nome FROM usuario WHERE id = {}".format(carro_locado)
    cursor.execute(sql_teste)
    result = cursor.fetchone()

    sql2 = "UPDATE usuario SET id_carro = '{}' WHERE id = {}".format(result2[0], cliente_comprou)
    cursor.execute(sql2)
    banco.commit()

    sql4 = "UPDATE carros SET tempo_locacao_dia = '{}', dono = '{}' WHERE id = {}".format(dias_locados, result[0], carro_locado)
    cursor.execute(sql4)
    banco.commit()

    tela_opcao.show()


def locar_mensal():
    loca_mensal.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    loca_mensal.table_mensal.setRowCount(len(dados_recebidos))
    loca_mensal.table_mensal.setColumnCount(9)

    nomes_colunas = ["Número", "Marca", "Modelo","Ano","Cor","Placa","Preco_Total","Preco_Diaria","Preco_Mensal"]
    loca_mensal.table_mensal.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 9):
            loca_mensal.table_mensal.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))


def loc_mensal2():
    locar_car_m.show()


    cursor = banco.cursor()
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    locar_car_m.table_cli.setRowCount(len(dados_recebidos))
    locar_car_m.table_cli.setColumnCount(7)

    nomes_colunas = ["Número", "Nome", "Email","Cpf","Telefone","Data_nascimento","Carro"]
    locar_car_m.table_cli.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 7):
            locar_car_m.table_cli.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))

def loc_mensal3(): 
    
    status = "Locado Mensal"
    carro_locado = loca_mensal.id_carro.text()
    loca_mensal.id_carro.setText("")

    
    cliente_comprou = locar_car_m.id_cli.text()
    locar_car_m.id_cli.setText("")


    dias_locados = locar_car_m.id_cli_3.text()
    locar_car_m.id_cli_3.setText("")

    cursor = banco.cursor()

    sql_teste = "SELECT nome FROM usuario WHERE id = {}".format(carro_locado)
    cursor.execute(sql_teste)
    result = cursor.fetchone()

    sql_teste2 = "SELECT modelo FROM carros WHERE id = {}".format(carro_locado)
    cursor.execute(sql_teste2)
    result2 = cursor.fetchone()

    sql = "UPDATE carros SET status = '{}' WHERE id = {}".format(status, carro_locado)
    cursor.execute(sql)
    banco.commit()

    sql2 = "UPDATE usuario SET id_carro = '{}' WHERE id = {}".format(result2[0], cliente_comprou)
    cursor.execute(sql2)
    banco.commit()

    sql4 = "UPDATE carros SET tempo_locacao_mes = '{}', dono = '{}' WHERE id = {}".format(dias_locados, result[0], carro_locado)
    cursor.execute(sql4)
    banco.commit()


def comprar_carro():
    compra_carro.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    compra_carro.tabela_compra.setRowCount(len(dados_recebidos))
    compra_carro.tabela_compra.setColumnCount(7)

    nomes_colunas = ["Número", "Marca", "Modelo", "Ano", "Cor", "Placa", "Preço Total"]
    compra_carro.tabela_compra.setHorizontalHeaderLabels(nomes_colunas)

    for linha, carro in enumerate(dados_recebidos):
        for coluna, valor in enumerate(carro):
            compra_carro.tabela_compra.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(valor)))

    sql3 = "SELECT id, nome, telefone, id_carro FROM usuario"
    cursor.execute(sql3)
    dados_recebidos = cursor.fetchall()

    comprar_carro2.table_cli.setRowCount(len(dados_recebidos))
    comprar_carro2.table_cli.setColumnCount(4)

    nomes_colunas = ["Número", "Nome", "Telefone", "Carro de Posse"]
    comprar_carro2.table_cli.setHorizontalHeaderLabels(nomes_colunas)

    for linha, carro in enumerate(dados_recebidos):
        for coluna, valor in enumerate(carro):
            comprar_carro2.table_cli.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(valor)))


def compra_carro2():
    
    status = "COMPRADO"
    carro_comprado = compra_carro.id_compra.text()
    compra_carro.id_compra.setText("")

    
    cliente_comprou = comprar_carro2.id_cli.text()
    comprar_carro2.id_cli.setText("")
    
    cursor = banco.cursor()

    sql_teste = "SELECT nome FROM usuario WHERE id = {}".format(cliente_comprou)
    cursor.execute(sql_teste)
    result = cursor.fetchone()

    sql_teste2 = "SELECT modelo FROM carros WHERE id = {}".format(carro_comprado)
    cursor.execute(sql_teste2)
    result2 = cursor.fetchone()

    sql = "UPDATE carros SET status = '{}', dono = '{}' WHERE id = {}".format(status, result[0], carro_comprado)
    cursor.execute(sql)
    banco.commit()


    sql2 = "UPDATE usuario SET id_carro = '{}' WHERE id = {}".format(result2[0], cliente_comprou)
    cursor.execute(sql2)
    banco.commit()


def edit_car():
    edit_carro.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    edit_carro.tabela_edit.setRowCount(len(dados_recebidos))
    edit_carro.tabela_edit.setColumnCount(9)

    nomes_colunas = ["Número", "Marca", "Modelo","Ano","Cor","Placa","Preco_Total","Preco_Diaria","Preco_Mensal"]
    edit_carro.tabela_edit.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 9):
            edit_carro.tabela_edit.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))

    edit_carro.submitbtn_3.clicked.connect(edit_car1)


def edit_car1():
    edita_car.show()


def edit_car3():

    carro_edit = edit_carro.id_carro.text()
    edit_carro.id_carro.setText("")


    preco_total = edita_car.preco.text()
    edita_car.preco.setText("")

    
    preco_d = edita_car.preco_diaria.text()
    edita_car.preco_diaria.setText("")


    preco_m = edita_car.preco_mensal.text()
    edita_car.preco_mensal.setText("")

    cursor = banco.cursor()
    sql = "UPDATE carros SET preco_total = '{}',  preco_diaria = '{}', preco_mensal = '{}' WHERE id = {}".format(preco_total, preco_d, preco_m, carro_edit)
    cursor.execute(sql)
    banco.commit()


def delet_car():
    delet_carro.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    delet_carro.tabela_delet.setRowCount(len(dados_recebidos))
    delet_carro.tabela_delet.setColumnCount(9)

    nomes_colunas = ["Número", "Marca", "Modelo","Ano","Cor","Placa","Preco_Total","Preco_Diaria","Preco_Mensal"]
    delet_carro.tabela_delet.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 9):
            delet_carro.tabela_delet.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))


def delet_carro2():

    carro_deletado = delet_carro.id_delet.text()
    delet_carro.id_delet.setText("")

    cursor = banco.cursor()
    sql = "DELETE FROM carros WHERE id = {}".format(carro_deletado)
    cursor.execute(sql)
    banco.commit()


def resetar_car():
    reset_car.show()

    reset_car.submitbtn_4.clicked.connect(resetar_car2)


def resetar_car2():
    try:
        carro_reset = reset_car.reset_id.text()
        reset_car.reset_id.setText("")

        cursor = banco.cursor()
        sql = "UPDATE carros SET tempo_locacao_dia = 'disponivel',  tempo_locacao_mes = 'disponivel', status = 'Disponivel' WHERE id = {}".format(carro_reset)
        sql2 = "UPDATE carros SET dono = 'Disponivel' WHERE id = {}".format(carro_reset)
        cursor.execute(sql)
        cursor.execute(sql2)
        banco.commit()
    except:
        print("aaaaaaa")



def delet_client():
    delet_cli.show()

    delet_cli.voltar_delet.clicked.connect(voltar_opc)

 
def delet_cli2():

    cli_deletado = delet_cli.id_delet.text()
    delet_cli.id_delet.setText("")

    cursor = banco.cursor()
    sql = "DELETE FROM usuario WHERE id = {}".format(cli_deletado)
    cursor.execute(sql)
    banco.commit()


def gerenciar_cli():
    ger_cli.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    ger_cli.tableWidget.setRowCount(len(dados_recebidos))
    ger_cli.tableWidget.setColumnCount(7)

    nomes_colunas = ["Número", "Nome", "Email","Cpf","Telefone","Data_nascimento","Carro"]
    ger_cli.tableWidget.setHorizontalHeaderLabels(nomes_colunas)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0, 7):
            ger_cli.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))

    ger_cli.delet_btn.clicked.connect(delet_client)


def tel_cad_cli():
    cadastro_cliente.show()


def voltar_opc():
    cadastro_cliente.hide()
    cadastro_carro.hide()
    gerenciar_carro.hide()
    compra_carro.hide()
    loca_carro.hide()
    ger_cli.hide()
    tela_opcao.show()


def voltar_ger():
    edit_carro.hide()
    delet_carro.hide()
    gerenciar_carro.show()


def voltar_loc():
    loca_diaria.hide()
    loca_mensal.hide()
    loca_carro.show()


def ir_compra2():
    comprar_carro2.show()


def ir_cad_cli():
    cadastro_cliente.show()


def tela_cad_car():
    cadastro_carro.show()
    

# ============================== BOTÕES DE LIGAÇÕES ========================================


cadastro_cliente.submitbtn.clicked.connect(cadastrar_cliente)
cadastro_carro.submitbtn_3.clicked.connect(cadastrar_carro)
tela_opcao.pushButton_5.clicked.connect(listar_dados)
tela_opcao.pushButton_3.clicked.connect(locar_carro)
compra_carro.confirmar_compra.clicked.connect(ir_compra2)
comprar_carro2.comprar_btn_2.clicked.connect(compra_carro2)
delet_carro.delet_btn.clicked.connect(delet_carro2)
tela_opcao.ger_cli.clicked.connect(gerenciar_cli)
delet_cli.delet_btn.clicked.connect(delet_cli2)
loca_diaria.btn_continuar.clicked.connect(locar_d2)
locar_car_d2.comprar_btn_2.clicked.connect(locar_d3)
loca_mensal.submitbtn_3.clicked.connect(loc_mensal2)
locar_car_m.comprar_btn_2.clicked.connect(loc_mensal3)
edita_car.submitbtn_4.clicked.connect(edit_car3)


# ============================== BOTÕES DE VOLTAR ========================================


form_usuario.logarbtn.clicked.connect(tela_loginAdm)
compra_carro.voltar_cbtn.clicked.connect(voltar_opc)
comprar_carro2.voltar_cbtn.clicked.connect(voltar_opc)
edit_carro.voltar_edit.clicked.connect(voltar_ger)
delet_carro.voltar_delet.clicked.connect(voltar_ger)
loca_diaria.voltar_dbtn.clicked.connect(voltar_loc)
loca_mensal.voltar_mbtn.clicked.connect(voltar_loc)

cadastro_carro.cad_btn.clicked.connect(ir_cad_cli)
cadastro_carro.comprar_car.clicked.connect(comprar_carro)
cadastro_carro.loc_car.clicked.connect(locar_carro)
cadastro_carro.ger_car.clicked.connect(listar_dados)
cadastro_carro.ger_cli.clicked.connect(gerenciar_cli)

cadastro_carro.voltar.clicked.connect(voltar_opc)

cadastro_cliente.cadcar_btn.clicked.connect(tela_cad_car)
cadastro_cliente.comprar_car.clicked.connect(comprar_carro)
cadastro_cliente.loc_car.clicked.connect(locar_carro)
cadastro_cliente.ger_car.clicked.connect(listar_dados) 
cadastro_cliente.ger_cli.clicked.connect(gerenciar_cli)

cadastro_cliente.submitbtn_2.clicked.connect(voltar_opc)

loca_carro.cadcar_btn.clicked.connect(tela_cad_car)
loca_carro.comprar_car.clicked.connect(comprar_carro)
loca_carro.cad_btn.clicked.connect(ir_cad_cli)
loca_carro.ger_car.clicked.connect(listar_dados) 
loca_carro.ger_cli.clicked.connect(gerenciar_cli)

loca_carro.voltar_loc.clicked.connect(voltar_opc)

gerenciar_carro.cadcar_btn.clicked.connect(tela_cad_car)
gerenciar_carro.comprar_car.clicked.connect(comprar_carro)
gerenciar_carro.cad_btn.clicked.connect(ir_cad_cli)
gerenciar_carro.loc_car.clicked.connect(locar_carro) 
gerenciar_carro.ger_cli.clicked.connect(gerenciar_cli)
 
gerenciar_carro.voltar_gerenciar.clicked.connect(voltar_opc)

ger_cli.cadcar_btn.clicked.connect(tela_cad_car)
ger_cli.comprar_car.clicked.connect(comprar_carro)
ger_cli.cad_btn.clicked.connect(ir_cad_cli)
ger_cli.loc_car.clicked.connect(locar_carro) 
ger_cli.pushButton_5.clicked.connect(listar_dados) 

ger_cli.voltar_gerenciar.clicked.connect(voltar_opc) 


form_usuario.show()
app.exec()