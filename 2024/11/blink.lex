%{
    long long n0, n1, n2;
    char h0[1024], h1[1024];
    int len;
%}

DIGITS  [0-9]+

%%
{DIGITS}      { 
            n0 = atoll(yytext);
            if (!n0) printf("%d",1);
            else {
                len = strlen(yytext);
                if (!(len%2)){
                    strncpy(h0, yytext, len/2);
                    strcpy(h1, yytext+(len/2));

                    n0 = atoll(h0); n1 = atoll(h1);
                    memset(h0,0,1024);memset(h1,0,1024);

                    printf("%llu %llu", n0, n1);}
                else
                    printf("%llu", n0*2024);
            }}
.           ECHO;
%%

int main(){
    yylex();
    return 0;}
