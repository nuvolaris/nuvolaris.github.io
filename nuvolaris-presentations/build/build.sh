CUR=${1:?target file}
if ! test -f "$CUR"
then echo "$CUR does not exist" ; exit 1
fi
DIR=$(dirname "$CUR")
rm -Rvf $DIR/pres
rm -f $DIR/pres.pdf
if ! test -e ~/.local/bin/ipython
then python3 -m pip install ipython
fi
if ! test -e ~/node_modules/bin/marp
then cd ~ ; npm install @marp-team/marp-cli ; cd -
fi
export PATH=~/.local/bin:~/node_modules/.bin:$PATH
ipython convert.ipy $CUR
