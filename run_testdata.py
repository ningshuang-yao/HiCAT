import datetime
import os

def main():
    # Python environment
    python_path = '/home/shgao/.conda/envs/SCAT/bin/python'
    # StringDecomposer install path
    sd_path = '/home/shgao/home/soft/stringdecomposer-master/bin/stringdecomposer'
    # input cen DNA sequence
    input_file = './testdata/cen21.fa'
    # Monomer template for StringDecomposer
    monomer_template = './testdata/AlphaSat.fa'
    # Output
    output_path = './testdata'

    thread = 1

    # Other parameters are set in start.sh
    os.system('sh start.sh ' + input_file + ' ' + output_path + ' ' + python_path +
              ' ' + sd_path + ' ' + monomer_template + ' ' + str(thread))



if __name__ == '__main__':
    main()