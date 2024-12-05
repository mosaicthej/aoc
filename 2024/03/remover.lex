%x REMOVE
%%

"don't()"        { BEGIN(REMOVE); }  /* Enter REMOVE state when encountering don't() */
<REMOVE>"do()"   { BEGIN(INITIAL); } /* Exit REMOVE state upon the first do() */
<REMOVE>.|\n     { /* Ignore everything in REMOVE state */ }
.                { putchar(yytext[0]); } /* Print any other characters */

%%

int main() {
    yylex();
    return 0;
}

