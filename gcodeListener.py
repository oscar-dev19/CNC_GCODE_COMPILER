# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete listener for a parse tree produced by gcodeParser.
class gcodeListener(ParseTreeListener):

    # Enter a parse tree produced by gcodeParser#start.
    def enterStart(self, ctx:gcodeParser.StartContext):
        pass

    # Exit a parse tree produced by gcodeParser#start.
    def exitStart(self, ctx:gcodeParser.StartContext):
        pass


    # Enter a parse tree produced by gcodeParser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#linInterpolateExpr.
    def enterLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#linInterpolateExpr.
    def exitLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#circularInterpolateExpr.
    def enterCircularInterpolateExpr(self, ctx:gcodeParser.CircularInterpolateExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#circularInterpolateExpr.
    def exitCircularInterpolateExpr(self, ctx:gcodeParser.CircularInterpolateExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#drawarcExpr.
    def enterDrawarcExpr(self, ctx:gcodeParser.DrawarcExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#drawarcExpr.
    def exitDrawarcExpr(self, ctx:gcodeParser.DrawarcExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#dwellExpr.
    def enterDwellExpr(self, ctx:gcodeParser.DwellExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#dwellExpr.
    def exitDwellExpr(self, ctx:gcodeParser.DwellExprContext):
        pass



del gcodeParser