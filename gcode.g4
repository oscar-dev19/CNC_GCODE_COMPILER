grammar gcode;

start : expr | <EOF> ;

expr     : 'G00' 'X'x_cord=NUMBER 'Y'y_cord=NUMBER ('F' speed=NUMBER)? ('Z' color=COLORS)? #drawlineExpr
         | 'G01' x_cord=NUMBER y_cord=NUMBER #linInterpolateExpr
         | 'G02' degrees=NUMBER #circularInterpolateExpr
         | 'G03' radius=NUMBER degrees=NUMBER ('F' speed=NUMBER)? ('Z' color=COLORS)? #drawarcExpr
         | 'G04' time=NUMBER #dwellExpr
         ;
NUMBER : ('-')? ('0' .. '9') + ('.' ('0' .. '9') +)? ;
COLORS: 'blue' |'red' | 'green' | 'pink' | 'yellow' | 'purple' ;
WS : [ \r\n\t]+ -> skip;
