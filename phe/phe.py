arquivos_pdb = ['1j4y.pdb', '1kka.pdb', '6b34.pdb','6b35.pdb', '6mw0.pdb', '6qxb.pdb', '7etp.pdb', '7k1m.pdb', '8ddg.pdb', '8hvs.pdb']

count_phe = 0
count_arq = 0
count_total = 0

for i in arquivos_pdb:
    with open(arquivos_pdb[count_arq], 'r') as arquivo:
        for linha in arquivo:
            if "PHE" in linha:
                count_phe+=1 #Contador de PHE
            if linha.startswith("ATOM") or linha.startswith("HETATM"): #Contador de dados relacionados a estrtura em geral
                count_total+=1
    count_arq+=1
print("\nA quantidade total de PHE em 10 estruturas do PDB é de", count_phe)

print("\nAo total existem ", count_total, "atomos em 10 estrturas de pdb")

count_media = count_phe/10
print("\nEm média, existem", count_media, "PHE para cada amostra de PDB")

count_perce = (count_phe/count_total)*100
print("\nO PHE representa", count_perce,"%"" de toda a estrtura do PDB")