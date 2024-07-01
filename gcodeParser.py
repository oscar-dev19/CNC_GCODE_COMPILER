# Generated from gcode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,42,2,0,7,0,2,1,7,1,1,0,1,0,3,0,7,8,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,16,8,1,1,1,1,1,3,1,20,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,1,1,1,3,1,36,8,1,1,1,1,1,3,1,40,8,1,1,
        1,0,0,2,0,2,0,0,48,0,6,1,0,0,0,2,39,1,0,0,0,4,7,3,2,1,0,5,7,1,0,
        0,0,6,4,1,0,0,0,6,5,1,0,0,0,7,1,1,0,0,0,8,9,5,1,0,0,9,10,5,2,0,0,
        10,11,5,10,0,0,11,12,5,3,0,0,12,15,5,10,0,0,13,14,5,4,0,0,14,16,
        5,10,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,19,1,0,0,0,17,18,5,5,0,0,
        18,20,5,11,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,40,1,0,0,0,21,22,5,
        6,0,0,22,23,5,10,0,0,23,40,5,10,0,0,24,25,5,7,0,0,25,40,5,10,0,0,
        26,27,5,8,0,0,27,28,5,10,0,0,28,31,5,10,0,0,29,30,5,4,0,0,30,32,
        5,10,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,35,1,0,0,0,33,34,5,5,0,0,
        34,36,5,11,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,40,1,0,0,0,37,38,5,
        9,0,0,38,40,5,10,0,0,39,8,1,0,0,0,39,21,1,0,0,0,39,24,1,0,0,0,39,
        26,1,0,0,0,39,37,1,0,0,0,40,3,1,0,0,0,6,6,15,19,31,35,39
    ]

class gcodeParser ( Parser ):

    grammarFileName = "gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G00'", "'X'", "'Y'", "'F'", "'Z'", "'G01'", 
                     "'G02'", "'G03'", "'G04'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "COLORS", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMBER=10
    COLORS=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(gcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = gcodeParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CircularInterpolateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.degrees = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gcodeParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircularInterpolateExpr" ):
                listener.enterCircularInterpolateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircularInterpolateExpr" ):
                listener.exitCircularInterpolateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircularInterpolateExpr" ):
                return visitor.visitCircularInterpolateExpr(self)
            else:
                return visitor.visitChildren(self)


    class DwellExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.time = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gcodeParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDwellExpr" ):
                listener.enterDwellExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDwellExpr" ):
                listener.exitDwellExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDwellExpr" ):
                return visitor.visitDwellExpr(self)
            else:
                return visitor.visitChildren(self)


    class LinInterpolateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinInterpolateExpr" ):
                listener.enterLinInterpolateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinInterpolateExpr" ):
                listener.exitLinInterpolateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinInterpolateExpr" ):
                return visitor.visitLinInterpolateExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawarcExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.radius = None # Token
            self.degrees = None # Token
            self.speed = None # Token
            self.color = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)
        def COLORS(self):
            return self.getToken(gcodeParser.COLORS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawarcExpr" ):
                listener.enterDrawarcExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawarcExpr" ):
                listener.exitDrawarcExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawarcExpr" ):
                return visitor.visitDrawarcExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.speed = None # Token
            self.color = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)
        def COLORS(self):
            return self.getToken(gcodeParser.COLORS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawlineExpr" ):
                listener.enterDrawlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawlineExpr" ):
                listener.exitDrawlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawlineExpr" ):
                return visitor.visitDrawlineExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = gcodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = gcodeParser.DrawlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(gcodeParser.T__0)
                self.state = 9
                self.match(gcodeParser.T__1)
                self.state = 10
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 11
                self.match(gcodeParser.T__2)
                self.state = 12
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 13
                    self.match(gcodeParser.T__3)
                    self.state = 14
                    localctx.speed = self.match(gcodeParser.NUMBER)


                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 17
                    self.match(gcodeParser.T__4)
                    self.state = 18
                    localctx.color = self.match(gcodeParser.COLORS)


                pass
            elif token in [6]:
                localctx = gcodeParser.LinInterpolateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(gcodeParser.T__5)
                self.state = 22
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 23
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                pass
            elif token in [7]:
                localctx = gcodeParser.CircularInterpolateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(gcodeParser.T__6)
                self.state = 25
                localctx.degrees = self.match(gcodeParser.NUMBER)
                pass
            elif token in [8]:
                localctx = gcodeParser.DrawarcExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(gcodeParser.T__7)
                self.state = 27
                localctx.radius = self.match(gcodeParser.NUMBER)
                self.state = 28
                localctx.degrees = self.match(gcodeParser.NUMBER)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 29
                    self.match(gcodeParser.T__3)
                    self.state = 30
                    localctx.speed = self.match(gcodeParser.NUMBER)


                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 33
                    self.match(gcodeParser.T__4)
                    self.state = 34
                    localctx.color = self.match(gcodeParser.COLORS)


                pass
            elif token in [9]:
                localctx = gcodeParser.DwellExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.match(gcodeParser.T__8)
                self.state = 38
                localctx.time = self.match(gcodeParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





