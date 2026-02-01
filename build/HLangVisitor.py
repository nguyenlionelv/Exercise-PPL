# Generated from HLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HLangParser import HLangParser
else:
    from HLangParser import HLangParser

# This class defines a complete generic visitor for a parse tree produced by HLangParser.

class HLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HLangParser#program.
    def visitProgram(self, ctx:HLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#vardecl.
    def visitVardecl(self, ctx:HLangParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#vard.
    def visitVard(self, ctx:HLangParser.VardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#funcdecl.
    def visitFuncdecl(self, ctx:HLangParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#func.
    def visitFunc(self, ctx:HLangParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#param.
    def visitParam(self, ctx:HLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#parameter.
    def visitParameter(self, ctx:HLangParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#var.
    def visitVar(self, ctx:HLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#body.
    def visitBody(self, ctx:HLangParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#stmtlist.
    def visitStmtlist(self, ctx:HLangParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#stmt.
    def visitStmt(self, ctx:HLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#assignstmt.
    def visitAssignstmt(self, ctx:HLangParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#callstmt.
    def visitCallstmt(self, ctx:HLangParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#paramcall.
    def visitParamcall(self, ctx:HLangParser.ParamcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#returnstmt.
    def visitReturnstmt(self, ctx:HLangParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#expr.
    def visitExpr(self, ctx:HLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#term.
    def visitTerm(self, ctx:HLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#fact.
    def visitFact(self, ctx:HLangParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#factor.
    def visitFactor(self, ctx:HLangParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#operand.
    def visitOperand(self, ctx:HLangParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HLangParser#type.
    def visitType(self, ctx:HLangParser.TypeContext):
        return self.visitChildren(ctx)



del HLangParser