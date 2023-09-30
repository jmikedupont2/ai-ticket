
#prerequists
# git clone https://github.com/nektos/act  -> https://github.com/meta-introspector/actx
#  make build


# git clone https://github.com/moovweb/gvm
# cd gvm/ &&./autogen.sh && make install

act \
    -s GITHUB_TOKEN=`cat github_pat.txt` \
    -s GITHUB_PAT=`cat github_pat.txt` \
    -s DOCKER=`cat dckr_pat_.txt` \
    -P ubuntu-latest=localhost/my_local_act \
    --verbose \
    --job python-package-build

#    --pull=false \
