# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.
import turtle
machinePointer = turtle.Turtle()

class gcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcodeParser#start.
    def visitStart(self, ctx:gcodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        
        x_cord = int(ctx.x_cord.text)
        y_cord = int(ctx.y_cord.text)
        
        #G00 goes at max speed.
        machinePointer.speed(10)

        if ctx.color:
            color = ctx.color.text

            machinePointer.color(color)

        #actual "machine movement"
        
        #assure pointer is set on canvas
        machinePointer.pendown()

        #move machine pointer
        machinePointer.goto(x_cord,y_cord)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#linInterpolateExpr.
    def visitLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):
        x_cord = int(ctx.x_cord.text)
        y_cord = int(ctx.y_cord.text)

        #determine feed rate.
        if ctx.speed:
            speed = int(ctx.speed.text)
            machinePointer.speed(speed)

        #assure machine is off canvas.
        machinePointer.penup()
        #machine movement.
        machinePointer.goto(x_cord,y_cord)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#circularInterpolateExpr.
    def visitCircularInterpolateExpr(self, ctx:gcodeParser.CircularInterpolateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawarcExpr.
    def visitDrawarcExpr(self, ctx:gcodeParser.DrawarcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#dwellExpr.
    def visitDwellExpr(self, ctx:gcodeParser.DwellExprContext):
        return self.visitChildren(ctx)



del gcodeParser
