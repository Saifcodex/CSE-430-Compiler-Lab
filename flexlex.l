%{ 
   #include<stdio.h>
   extern int yylineno;
%}

%option noyywrap
%option yylineno

%%
[ \t\n]+   {}
"//".*     { printf("%d %s Singlelinecomment\n", yylineno, yytext); }
"/*"([^*]|\*+[^*/])*\*+"/"    { printf("%d %s Multilinecomment\n", yylineno, yytext); }
"void"|"int"|"float"|"char"|"double"|"if"|"else"|"for"|"while"|"do"|"switch"|"case"|"default"|"break"|"continue"|"return"|"goto"|"const"|"static"|"struct"|"union"|"typedef"|"enum"|"sizeof"|"volatile"|"register"|"extern"|"signed"|"unsigned"|"short"|"long"|"auto" { printf("%d %s keyword\n", yylineno, yytext); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("%d %s identifier\n", yylineno, yytext);}
[0-9]+(\.[0-9]+)?       { printf("%d %s constant\n", yylineno, yytext); }
\'([^\\']|\\.)\'   { printf("%d %s character-constant\n", yylineno, yytext); }
\"([^\\\"]|\\.)*\" { printf("%d %s string-constant\n", yylineno, yytext); }
"=="|"!="|"<="|">="|"<"|">"  { printf("%d %s relational-operator\n", yylineno, yytext);}
"&&"|"||"|"!"  { printf("%d %s logical-operator\n", yylineno, yytext);  }
"="|"+"|"-"|"*"|"/"|"%"|"++"|"--"  { printf("%d %s arithmetic-operator\n", yylineno, yytext); }
"&"|"|"|"^"|"~"|"<<"|">>"  { printf("%d %s bitwise-operator\n", yylineno, yytext);  }
","|";"|":"  { printf("%d %s punctuation\n", yylineno, yytext); }
"("|")"|"{"|"}"|"["|"]"  { printf("%d %s parenthesis\n", yylineno, yytext); }
. {}
%% 

int main(int argc, char** argv)
{
    if(argc>1)
    {
        FILE* f = fopen(argv[1],"r");
        if(!f) {
            printf("Could not open file %s\n", argv[1]);
            return 1;
        }
        yyin = f;
    }
    yylex();
    return 0;
}
