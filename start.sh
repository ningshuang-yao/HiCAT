set -euo pipefail
function useage {
    echo "useage: ./start.sh input_fasta output_dir python_path stringdecomposer_path monomer_template (for StringDecomposer) thread"
    exit 1
}

if [ $# -lt 3 ]; then
    useage
    exit 1
fi


input_fasta=$1
output_dir=$2
python=$3
sd=$4
target_monomer=$5
t=$6

echo "input fasta is "$1
echo "output in "$2

min_similarity=0.94
step=0.005
max_hor_len=40


script_dir=$(cd $(dirname $0);pwd)
# HiCAT workflow

script=$script_dir'/HiCAT_HOR.py'
echo 'StringDecomposer'

$python $sd $input_fasta  $target_monomer -o  $output_dir

awk '/^>/&&NR>1{print "";}{printf "%s",/^>/?$0"\n":$0}' $input_fasta > $output_dir'/input_fasta.1.fa'
echo >> $output_dir'/input_fasta.1.fa'

echo 'HiCAR_HOR'
echo $script
$python $script -d $output_dir'/final_decomposition.tsv' -b $output_dir'/input_fasta.1.fa'  -o $output_dir -s $min_similarity -st $step -m $max_hor_len -t $t

