import datetime
import os

def main():
    # cu12
    python_path = '/home/shgao/.conda/envs/SCAT/bin/python'
    sd_path = '/home/shgao/home/soft/stringdecomposer-master/bin/stringdecomposer'
    workdir = '/home/shgao/home/PGTD/CHM13/testPGTD_0623/AT'

    target_monomer = '/home/shgao/home/PGTD/CHM13/testPGTD_0623/CEN180.fa'

    time_file = '/home/shgao/home/PGTD/CHM13/testPGTD_0623/AT_time.txt'

    file_list = ['1','2','3','4','5']

    thread = 28

    time_file = open(time_file,'w')
    for i in file_list:
        all_time_start = datetime.datetime.now()
        input_file = workdir + '/' + i + '/input.fa'
        output_path = workdir + '/' + i
        os.system('sh start.sh '+input_file+' '+output_path+
                  ' '+python_path+' '+sd_path+' '+target_monomer+' '+str(thread))
        all_time_end = datetime.datetime.now()
        print('AT CEN'+str(i)+' Time: ' + str((all_time_end - all_time_start).seconds))
        time_file.write('AT CEN'+str(i)+' Time: ' + str((all_time_end - all_time_start).seconds) +'\n')
        time_file.flush()
    time_file.close()


if __name__ == '__main__':
    main()
