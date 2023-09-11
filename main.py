import pandas as pd

def get_colums(bestand):
    info = []
    with open (bestand) as file:
        for line in file:
            l = line.replace('\n','').split('\t')

            info.append(l)
    # print(info[0])
    # print(info)
    return info[0]
    # print(info[1])


def read_file(bestand,header):
    file = pd.read_table(bestand)
    print(file.head(10))
    # print(header)
    # print(file['sample'].head(10))
    # print(file[['protein_group', 'sample']])


if __name__ == '__main__':
    bestand_tsv = 'HoPE_FA-mat-exp_Module-2_output_Cleaned-protein-'\
                  'abundances_tidy_20230911_131010.tsv'
    list = get_colums(bestand_tsv)
    print(list)
    read_file(bestand_tsv,list)