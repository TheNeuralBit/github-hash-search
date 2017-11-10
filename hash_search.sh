cat hashes_to_find.txt | xargs -P4 -I{} grep ^{} /var/hashes
