select
    *
from
    status;

select
    *
from
    tipo;

select
    *
from
    mamada_status;

select
    *
from
    Mamadas;

select
    mamadas.mamadaID,
    tipo.Tipo,
    status.status,
    mamada_status.mamada_status,
    Mamadas.Data_Hora_inicio,
    Mamadas.Data_Hora_fim,
    Mamadas.Quantidade
from
    Mamadas
    inner join status on Mamadas.statusID = status.statusID
    inner join mamada_status on Mamadas.mamada_statusID = mamada_status.mamada_statusID
    inner join tipo on Mamadas.tipoID = tipo.tipoID;
