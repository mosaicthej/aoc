%{
    int n1, n2;
%}

MULL       mul\(
COMA      ,
DIGITS    [0-9]+
RPAREN    \)

%x MUL_0
%x MUL_1
%x MUL_C
%x MUL_2

%%

<INITIAL>{MULL}          { BEGIN(MUL_0); }

<MUL_0>{DIGITS}          { n1 = atoi(yytext);
                            BEGIN(MUL_1); }

<MUL_1>{COMA}            { BEGIN(MUL_C); }

<MUL_C>{DIGITS}          { n2=atoi(yytext);
                            BEGIN(MUL_2); }

<MUL_2>{RPAREN}          { printf("%d*%d+", n1, n2);
                            BEGIN(INITIAL); }

<MUL_0>.                 { BEGIN(INITIAL); } /* Ignore invalid input in states */
<MUL_1>.                 { BEGIN(INITIAL); }
<MUL_C>.                 { BEGIN(INITIAL); }
<MUL_2>.                 { BEGIN(INITIAL); }

<INITIAL>.               { BEGIN(INITIAL); } /* Ignore unexpected input in INITIAL state */

<INITIAL>\n              { BEGIN(INITIAL); } /* Handle newlines gracefully */

%%


int main() {
    yylex();
    return 0;
} 

