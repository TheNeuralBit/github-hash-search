echo "parallel grep"
echo "============="
time cat hashes_to_find.txt | xargs -P4 -I{} grep ^{} $1

echo "egrep"
echo "====="
time grep -E `cat hashes_to_find.txt | python -c "import sys; print('|'.join('^' + line.strip() for line in sys.stdin))"` $1

echo "fgrep"
echo "====="
time grep -F "`cat hashes_to_find.txt`" $1 | grep -E `cat hashes_to_find.txt | python -c "import sys; print('|'.join('^' + line.strip() for line in sys.stdin))"`
