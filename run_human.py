import datetime
import os

def main():
    # cu11
    python_path = '/home/shgao/.conda/envs/SCAT/bin/python'
    sd_path = '/home/shgao/home/soft/stringdecomposer-master/bin/stringdecomposer'
    workdir = '/home/shgao/home/PGTD/CHM13/testPGTD_0623/human'

    target_monomer = '/home/shgao/home/PGTD/CHM13/testPGTD_0623/AlphaSat.fa'

    time_file = '/home/shgao/home/PGTD/CHM13/testPGTD_0623/human_time.txt'

    file_list = ['1','2','3','4','5','6','7','8','9','10',
                 '11','12','13','14','15','16','17','18','19','20','21','22','X']

    thread = 28

    time_file = open(time_file,'w')
    for i in file_list:
        all_time_start = datetime.datetime.now()
        input_file = workdir + '/' + i + '/input.fa'
        output_path = workdir + '/' + i
        os.system('sh start.sh '+input_file+' '+output_path+
                  ' '+python_path+' '+sd_path+' '+target_monomer+' '+str(thread))
        all_time_end = datetime.datetime.now()
        print('human CEN'+str(i)+' Time: ' + str((all_time_end - all_time_start).seconds))
        time_file.write('human CEN'+str(i)+' Time: ' + str((all_time_end - all_time_start).seconds) +'\n')
        time_file.flush()
    time_file.close()


if __name__ == '__main__':
    main()