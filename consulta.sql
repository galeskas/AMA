
--select * from status;

--select * from tipo;

select
mamadas.mamadaID,
tipo.Tipo, status.status, Mamadas.Data_Hora, Mamadas.Quantidade
from Mamadas
inner join status on Mamadas.statusID = status.statusID
inner join tipo on Mamadas.tipoID = tipo.tipoID;

select
*
from Mamadas;
