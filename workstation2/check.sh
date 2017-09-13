#Python script to automate the checking task
#Starting point of the whole process
for run in {1..100}
do
python generator.py >input.txt
python naive.py <input.txt >naive_output.txt
python my.py <input.txt
python comparer.py
done
