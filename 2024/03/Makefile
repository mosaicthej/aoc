CC=clang
LDLIBS=-lfl
LEX=flex

all: remover mul

.PHONY: all clean run

STR1 = $(shell cat input | ./mul | head -c -1)
STR2 = $(shell cat input | ./remover | ./mul | head -c -1)

RES1 = $(shell echo $(( $$STR1 )) 1>&2)
RES2 = $(shell echo $(( $$STR2 )) 1>&2)

solve: remover mul
	@STR1=$(shell cat input | ./mul | head -c -1); \
	STR2=$(shell cat input | ./remover | ./mul | head -c -1); \
	RES1=$$(echo $$(( $$STR1 ))); \
	RES2=$$(echo $$(( $$STR2 ))); \
	echo "part01: $$RES1"; \
	echo "part02: $$RES2"

strings:
	@cat input | ./mul | head -c -1

remover.c: remover.lex
	$(LEX) -t $< > $@

mul.c: mul.lex
	$(LEX) -t $< > $@

remover: remover.c
	$(CC) -o $@ $< $(CFLAGS) $(LDLIBS)

mul: mul.c
	$(CC) -o $@ $< $(CFLAGS) $(LDLIBS)

clean:
	rm -f a.out *.c mul remover
