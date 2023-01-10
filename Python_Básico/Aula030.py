# CONSTANTE = "Variáveis" que não vão mudar
# Muitas condições no mesmo if (ruim)
# <- Contagem de complexidade (ruim)


velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada
RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega


ultrapassou_velocidade = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and ultrapassou_velocidade


if ultrapassou_velocidade:
    print('Carro utrapassou velocidade máxima!')
    
if carro_multado_radar_1:
    print('Carro multado no primeiro radar!')