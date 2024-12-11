CC=clang
LDLIBS=-lfl
LEX=flex

all: blink

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


blink: blink.c
	$(CC) -o $@ $< $(CFLAGS) $(LDLIBS) -Ofast

%.c: %.lex
	$(LEX) -t $< > $@

clean:
	rm -f a.out *.c blink
