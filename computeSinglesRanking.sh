if [ -z "$1" ]
  then
    echo Please provide a csv file with singles matches as first argument
fi

if command -v python3 >/dev/null; then
    python3 ./singles/main.py $1
else
    echo Please install Python 3
fi