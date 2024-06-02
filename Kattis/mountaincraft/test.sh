echo "start"
g++ mountaincraft.cpp
while [ $? -eq 0 ]; do
    echo "test:"
    pypy3 gen.py > in1
    pypy3 brute.py < in1 > brute.out
    ./a.out < in1 > my.out
    diff brute.out my.out
done
