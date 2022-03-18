import core

MainSetka=core.OneCore(20)

MainSetka.AddPlayer([core.Player("Tom",True,"X",MainSetka.Step),core.Player("Jane",False,"Y",MainSetka.Step)])

MainSetka.initArr()
MainSetka.ToConsoleArray()
 
while True:
     activeplayer=MainSetka.GetActivePlayer()
     activeplayer.StepPlayer(activeplayer)

     MainSetka.ToConsoleArray()    
     if MainSetka.win():
        print('Win!')
        break