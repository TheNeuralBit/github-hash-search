cat /usr/share/dict/american-english | grep -v "'" | xargs -I{} python git_urls.py {} | xargs -P10 -I {} ./get_hashes.sh {} > /var/hashes
