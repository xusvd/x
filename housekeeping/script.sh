#!/bin/bash
prev_count=0
fpath=var/log/apache/*.*
find $fpath -type f -mmin +1  -exec ls -ltrd {} \; > /tmp/file.out
find $fpath -type f -mmin +1  -exec rm -rf {} \;
count=$(cat /tmp/file.out | wc -l)
if [ "$prev_count" -lt "$count" ] ; then
MESSAGE="/tmp/file1.out"
TO="utpalkant.sahu@vodafone.com"
echo "Old raid server files are deleted as part of housekeeping"  >> $MESSAGE
echo "+--------------------------------------------- +" >> $MESSAGE
echo "" >> $MESSAGE
cat /tmp/file.out | awk '{print $6,$7,$9}' >> $MESSAGE
echo "" >> $MESSAGE
SUBJECT="Cleanup: Old raid server data dir cleanup $(date)"
mail -s "$SUBJECT" "$TO" < $MESSAGE
rm $MESSAGE /tmp/file.out
fi


# */5 * * * * /opt/scripts/clear-tmp.sh