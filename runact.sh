
#prerequists
# git clone https://github.com/nektos/act  -> https://github.com/meta-introspector/actx
#  make build


# git clone https://github.com/moovweb/gvm
# cd gvm/ &&./autogen.sh && make install
# use .secrets PAT And DOCKER
act    -P ubuntu-latest=localhost/my_local_act \
       --verbose \
    --job python-package-build

#    --pull=false \
