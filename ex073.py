tabela_brasileirao = ('Ceará SC', 'Botafogo', 'Goiás', 'São Paulo', 'Sport Recife', 'Grêmio', 'Coritiba', 'Flamengo', 'Atlético MG', 'Fluminense', 'Corinthians', 'Fortaleza', 'Atlético GO', 'Santos', 'Vasco da Gama', 'Palmeiras', 'Internacional', 'Athletico PR', 'Bahia', 'Bragantino SP')
print(f'Os Cincos primeiros times colocados da tabela do Brasileirão foram :{tabela_brasileirao[:4]}')
print(f'Os últimos quatro times colocados foram:{tabela_brasileirao[-4:]}')
print(f'Todos os times em ordem alfabética:{sorted(tabela_brasileirao)}')
print(f'O Fluminense está em {tabela_brasileirao.index("Fluminense") + 1}° na colocação da tabela do brasileirão.')
