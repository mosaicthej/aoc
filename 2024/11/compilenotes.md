if the system got flex and have libfl installed, great, just run make

otherwise, install `flex` locally from [githubrepo](https://github.com/westes/flex)

if using repo, first run ./autogen.sh
if downloaded release, untar it.

assuming $(LEXBUILD) is the path you want to install flex.

```bash
mkdir $(LEXBUILD) -p
./configure --prefix=$(LEXBUILD)
make
make install
```
then all flex stuff should be installed in $(LEXBUILD)

assuming $(LEX) is the `flex` binary (if built locally, it should be `$(LEXBUILD)/bin/flex`)
do following:

```bash
$(LEX) -t blink.lex > blink.c
$(CC) -o blink blink.c $(LDFLAGS) $(LDLIBS)
```

where if using locally-built flex:
`$(LDFLAGS)` is `-L$(LEXBUILD)/lib/`
`$(LDLIBS)` is `-lfl -Bstatic`
