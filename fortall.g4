grammar fortall;

programa: 'programa' ID ';' declaracao* funcaoPrincipal funcao* EOF;

funcaoPrincipal: 'retorna' 'nada' 'funcao' 'principal' '(' ')' bloco;

declaracao: declaracaoVariavel | declaracaoFuncao;

declaracaoVariavel: tipo ID ('=' expressao)? ';';

declaracaoFuncao: 'retorna' (tipo | 'nada') 'funcao' ID '(' parametros? ')' bloco;

funcao: declaracaoFuncao;

parametros: tipo ID (',' tipo ID)*;

tipo: 'int' | 'bool';

// Comandos
bloco: '{' comando* '}';

comando: 
    declaracaoVariavel |
    atribuicao |
    chamadaFuncao ';' |
    comandoSe |
    comandoEnquanto |
    comandoEscreva |
    comandoLeia |
    comandoRetorna |
    bloco;

atribuicao: ID '=' expressao ';';

comandoSe: 'se' '(' expressao ')' comando ('senao' comando)?;

comandoEnquanto: 'enquanto' '(' expressao ')' comando;

comandoEscreva: 'escreva' '(' listaExpressoes ')' ';';

comandoLeia: 'leia' '(' ID ')' ';';

comandoRetorna: 'retorna' expressao? ';';

listaExpressoes: expressao (',' expressao)*;

// Expressões com precedência
expressao: expressaoOu;

expressaoOu: expressaoE ('||' expressaoE)*;

expressaoE: expressaoIgualdade ('&&' expressaoIgualdade)*;

expressaoIgualdade: expressaoRelacional (('==' | '!=') expressaoRelacional)*;

expressaoRelacional: expressaoAditiva (('<' | '>' | '<=' | '>=') expressaoAditiva)*;

expressaoAditiva: expressaoMultiplicativa (('+' | '-') expressaoMultiplicativa)*;

expressaoMultiplicativa: expressaoUnaria (('*' | '/' | '%') expressaoUnaria)*;

expressaoUnaria: ('!' | '-' | '+')? expressaoPrimaria;

expressaoPrimaria: 
    NUMERO |
    BOOLEAN |
    STRING |
    ID |
    chamadaFuncao |
    '(' expressao ')';

chamadaFuncao: ID '(' argumentos? ')';

argumentos: expressao (',' expressao)*;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+;
BOOLEAN: 'true' | 'false';
STRING: '"' (~["\\\r\n] | '\\n' | '\\t' | '\\\\' | '\\"')* '"';

COMENTARIO: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;