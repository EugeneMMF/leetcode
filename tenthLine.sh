# Read from the file file.txt and output the tenth line to stdout.
c=0
while read line && [ $c -le 10 ]; do
  let c=c+1
  if [ $c -eq 10 ] ; then
    echo $line
  fi
done < file.txt