if [ -z "$1" ]
  then
    echo Please provide a csv file with singles matches as first argument
fi

if [ -z "$2" ]
  then
    echo Please provide a file to redirect the output to
fi

if command -v python3 >/dev/null; then
    python3 ./main_doubles.py $1 $2
else
    echo Please install Python 3
fi