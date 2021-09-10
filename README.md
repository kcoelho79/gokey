# gokey
Controle de acesso dos dispositivos da marca LINEAR e NICE, utilizando a comunicação via IP por SOCKET.
compativeis com os controladores MG3000, GuaritaIP e ControladoraII

## app_server
daemon que estabele conexões e recebe os eventos(frames) das controladoras,usando SOCKET, com o Selector que registra os eventos (read, write) das conexões.
[select] (https://pymotw.com/2/select/)

### fluxo funções
=>request  
=>accept (aceita conexões) 
=>read 	 (recebe o frame)
=>run_command (que identifica qual e a controladora,
deserializa o frame, identifica o tipo de evento, valida se é autorizado e executa)

## Modulo Controler
possui as configuracoes das controladoras para lidar com os eventos, cada modulo é um controlador

controlers (biblioteca)
	"nome_contoler.py" 		Classe que trata os eventos, e executa comandos
	"nome_controlerconf.py" Tabelas com as configurações

## Modulo frames
frame_evt.py = parse no evento, pegandos informaçoes como:
	data, 
	tipo evento = Dispositivo Acionado, Passagem, etc.
	dispositivos = tipo de dispositivo (cartão, RF,biometria, etc)
	serial = numero de identificaçao do cartao de acesso
	info_evento = informações diversas, tipo fora de horário, passagem_autorizada, etc.
	entre outras

essas informações: são usadas para tomada de decisões de negócio

## objeto controler
Ao criar(init) o objeto, no arquivo __init__.py identifica o tipo da controladora, MG3000, GuaritaIP, ControladoraII, pega o 7Byte, contem informação do tipo do PC_Comando, ver tabela de protocolo, e então chama a funcão que executará o comando

## libevents, libbit, libserver
Sao handler funções auxiliadores

## Gokey
### backend
Essa versão OpenSource, é StateFull,o evento é lido e respondido no mesmo objeto em um único fluxo, isso é feito para trabalhar com links dinamicos, e as limitações de não conseguir identificar controladora usando TCP e link dinamicp em um ambiente cloud computing.

### frontend

## Diferenças e pecularidades Controladores

### Controladora II
Quando trata de catraca, tem que tratar o evento de acionamento e passage, pois a catraca tem um x tempo para passar (girar a catraca), se não ela é novamente bloqueada. para efeito de log de contagem de entrada com sucesso, deve ser feito pelo LOG de passagem e não de acionamento.
na MG3000 uma vez o acionamento feito, a porta é liberada e considerado o acesso. 

Controladora tem uma informação a mais, numero do dispositivo 0-64 ou o numero de controladoras. na MG3000 essa info não tem. ambas controladoras tem informações da Porta CAN e da Saida de Rele.

Modo REMOTO = que todos os eventos são enviados para o servidor remoto no caso o Gokey, que envia de volta os comando para controladora acionar os dispositivos

Modo LOCAL = a controladora valida os acesso e faz o acionamento

### MG3000, GuaritaIP
Por padrão não vem configurado informação de evento de passagem, que deve ser configurado no software windows que vem da nice,

Envia no seu cabeçalho uma palavra de identficação
contem @MASaddress@palavra@
com isso é possível identificar MG3000 atraves do MACAddress ou de uma palavra como por exemplo o nome do cliente, o metodo self.token é uma tupla que contem token[0] MAM e o token[1] palavra

o Modo Cliente que é o mesmo que o modo Remoto, só funciona por 90 segundas.

Gokey operando com a mG3000, ao receber um serial autorizado pela regra de negócio, porem nao esta cadastrado na MG3000, o Gokey enviar um comando para abrir porta e depois para cadastrar na MG3000