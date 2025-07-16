SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for i in $(ls -1 $1); do
    filename=$(basename -- "$i")
    extension="${filename##*.}"
    filename="${filename%.*}"
    mv -v $i $(date +%Y%m%d_%H%M%S -r $i).${extension}
done

IFS=$SAVEIFS
