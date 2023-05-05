#Fernando Gentil Pinheiro Pacheco
#Basicamente, um DNA é constituido por nucleotideos. O que são nucleotideos?
# - Nucleotideos são estruturas químicas (moleculas) que basicamente formam a estrutura do ácido nucleico (DNA ou RNA).
# - Eles são moléculas que são presentes em células, formadas por bases nitrogenadas, fosfato e pentose.
# - Os seguintes compostos são nucleotideos: Adenina, Citosina, Guanina, Timina e Uracila.
#O que esse programa faz? 
# - Basicamente, ele irá fazer uma contagem de nucleotideos presentes no DNA. Um programa simples, que serve de introdução à bioinformática.

#definindo a sequencia de dna para ser analisada
sequencia_dna = 'ATCGATCG'

#dicionário que serve para analisar e armazenar a contagem de cada nucleotideo
cont_nucleotideo = {
        'A' : 0,
        'T' : 0,
        'C' : 0,
        'G' : 0
}

#percorrendo a sequencia de dna e contando cada nucleotideo
for nucleotideo in sequencia_dna:
    cont_nucleotideo[nucleotideo] += 1

#imprimindo a contagem de nucleotideos presentes na sequencia do dna
print(20 * '-')
print('Contagem de nucleotideos presentes na sequencia do dna:')
print(f"A: {cont_nucleotideo['A']}")
print(f"T: {cont_nucleotideo['T']}")
print(f"C: {cont_nucleotideo['C']}")
print(f"G: {cont_nucleotideo['G']}")
print(20 * '-')

