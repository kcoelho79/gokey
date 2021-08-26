# gokey
Controle de acesso dos dispositivos da LINEAR e NICE, utilizando comunicação IP SOCKET.
compativeis com os controladores MG3000, GuaritaIP e ControladoraII

## app_server
daemon que receber conexões das controladoras,
usando SOCKET, com o Selector que registra os 
eventos (read, write) das conexões.
[select] (https://pymotw.com/2/select/)

fluxo request =>accept => read => process_event

## Modulo Controler
possui as configuracoes das controladoras para lidar com os eventos
