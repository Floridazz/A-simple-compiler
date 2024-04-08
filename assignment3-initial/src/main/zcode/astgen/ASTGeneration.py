# 2153148
from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_decl()))

    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.varis(): 
            return self.visit(ctx.varis())
        else:
            return self.visit(ctx.func())

    def visitList_decl(self, ctx:ZCodeParser.List_declContext):
        if ctx.list_decl():
            return [self.visit(ctx.decl())] + self.visit(ctx.list_decl())
        else:
            return [self.visit(ctx.decl())]

    def visitVaris(self, ctx:ZCodeParser.VarisContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        else:
            return self.visit(ctx.implicit_dynamic())

    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.ID().getText()), None, "var" , self.visit(ctx.exp()))

    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext): 
        rhs=None
        arr_type=None
        if ctx.exp():
            rhs=self.visit(ctx.exp())
        if ctx.BOOL():
            type=BoolType()
        elif ctx.NUMBER():
            type=NumberType()
        else:
            type=StringType()
        if ctx.list_NUMBER_LIT():
            arr_type=ArrayType(self.visit(ctx.list_NUMBER_LIT()), type)
            return VarDecl(Id(ctx.ID().getText()), arr_type, None, rhs)
        return VarDecl(Id(ctx.ID().getText()), type, None, rhs)


    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.exp():
            return VarDecl(Id(ctx.ID().getText()), None, "dynamic" , self.visit(ctx.exp()))
        else:
            return VarDecl(Id(ctx.ID().getText()), None, "dynamic" , None)



    # funcdecl: FUNC ID LB paralist RB  (ignore? return_stmt | ignore? block_stmt | ignore);
    # function: FUNC ID L_BRACKET params_list R_BRACKET  (ignore? return_stmt | ignore? block_stmt | ignore);
    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        if ctx.return_stmt(): 
            body=self.visit(ctx.return_stmt())
        elif ctx.block_stmt():
            body=self.visit(ctx.block_stmt())
        else:
            body=None
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.param_list()), body)


    # params_list: paraprime | ;
    # Visit a parse tree produced by ZCodeParser#params_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        if ctx.getChildCount() != 0: 
            return self.visit(ctx.paraprime())
        else:
            return []
        


    # Visit a parse tree produced by ZCodeParser#paraprime.
    # paraprime: param COMMA paraprime | param;
    def visitParaprime(self, ctx:ZCodeParser.ParaprimeContext):
        if ctx.getChildCount() == 1: 
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.paraprime())


    # para: (NUMBER|BOOL|STRING) ID (LSB num_lit_list RSB)?;
    # param: (NUMBER|BOOL|STRING) ID (LS_BRACKET list_NUMBER_LIT RS_BRACKET)?;
    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        if ctx.list_NUMBER_LIT():
            if ctx.NUMBER():
                return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.list_NUMBER_LIT()), NumberType()), None  )
            elif ctx.BOOL():
                return VarDecl(Id(ctx.ID().getText()),ArrayType(self.visit(ctx.list_NUMBER_LIT()), BoolType()), None )
            else:
                return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.list_NUMBER_LIT()), StringType()),  None)
        else:
            if ctx.NUMBER():
                return VarDecl(Id(ctx.ID().getText()), NumberType(), None, None )
            elif ctx.BOOL():
                return VarDecl(Id(ctx.ID().getText()), BoolType(), None, None)
            else:
                return VarDecl(Id(ctx.ID().getText()), StringType(), None, None)
    
    
    # exprlist: exp COMMA exprlist | exp; 
    # list_expr: exp list_expr_tail | exp;
    # Visit a parse tree produced by ZCodeParser#list_expr.
    def visitList_expr(self, ctx:ZCodeParser.List_exprContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.list_expr_tail())

    # list_expr_tail: COMMA exp list_expr_tail | ;
    # Visit a parse tree produced by ZCodeParser#list_expr_tail.
    def visitList_expr_tail(self, ctx:ZCodeParser.List_expr_tailContext):
        if ctx.getChildCount() == 0: 
            return []
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.list_expr_tail())
    
    # Visit a parse tree produced by ZCodeParser#exp.
    # exp: exp1 CONCAT exp1 | exp1;
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1()[0])
        else:
            return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.exp1()[0]),self.visit(ctx.exp1()[1]))

    # Visit a parse tree produced by ZCodeParser#exp1.
    # exp1: exp2 (CMP | NEQ | LOE | GOE | LT | GT | EQ) exp2 | exp2;
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2()[0])
        else:
            if ctx.CMP():
                return BinaryOp(ctx.CMP().getText(), self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))
            if ctx.NEQ():
                return BinaryOp(ctx.NEQ().getText(), self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))
            if ctx.LOE():
                return BinaryOp(ctx.LOE().getText(), self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))
            if ctx.GOE():
                return BinaryOp(ctx.GOE().getText(), self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))
            if ctx.LT():
                return BinaryOp(ctx.LT().getText(), self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))
            if ctx.GT():
                return BinaryOp(ctx.GT().getText(),self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))
            if ctx.EQ():
                return BinaryOp(ctx.EQ().getText(), self.visit(ctx.exp2()[0]), self.visit(ctx.exp2()[1]))

    # Visit a parse tree produced by ZCodeParser#exp2.
    # exp2: exp2 AND exp3 | exp2 OR exp3 | exp3;
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        op = ''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        return BinaryOp(op, self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    # Visit a parse tree produced by ZCodeParser#exp3.
    # exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4;

    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        op = ''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        return BinaryOp(op, self.visit(ctx.exp3()), self.visit(ctx.exp4()))


    # Visit a parse tree produced by ZCodeParser#exp4.
    # exp4: exp4 MUL exp5 | exp4 DIV exp5 | exp4 MOD exp5 | exp5;

    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        op = ''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        return BinaryOp(op, self.visit(ctx.exp4()), self.visit(ctx.exp5()))


    # Visit a parse tree produced by ZCodeParser#exp5.
    # exp5: NOT exp5 | exp6;
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))


    # Visit a parse tree produced by ZCodeParser#exp6.
    # exp6: SUB exp6 | exp7;
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp6()))


    # Visit a parse tree produced by ZCodeParser#exp7.
    # exp7: (ID | func_call) LS_BRACKET list_expr RS_BRACKET | exp8;
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        if ctx.func_call():
            return ArrayCell(self.visit(ctx.func_call()), self.visit(ctx.list_expr()))
        else:
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.list_expr()))
    

    # Visit a parse tree produced by ZCodeParser#exp8.
    # exp8: ID | literal | L_BRACKET exp R_BRACKET | func_call;

    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.lit():
            return self.visit(ctx.lit())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.func_call():
            return self.visit(ctx.func_call())


    # Visit a parse tree produced by ZCodeParser#func_call.
    # func_call: ID L_BRACKET nullable_list_expr R_BRACKET;

    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.nullable_list_expr()))

    # nulllistexpr: nulllistexprprime | ;
    # nullable_list_expr: exp Nullable_list_expr_tail | ;
    # Visit a parse tree produced by ZCodeParser#nullable_list_expr.
    def visitNullable_list_expr(self, ctx:ZCodeParser.Nullable_list_exprContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.nullable_list_expr_tail())


    # nulllistexprprime: exp COMMA nulllistexprprime | exp ;
    # Nullable_list_expr_tail: COMMA exp Nullable_list_expr_tail | ;
    # Visit a parse tree produced by ZCodeParser#Nullable_list_expr_tail.
    def visitNullable_list_expr_tail(self, ctx:ZCodeParser.Nullable_list_expr_tailContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.nullable_list_expr_tail())

    # Visit a parse tree produced by ZCodeParser#literal.
    # literal: NUM_LIT | STRING_LIT | TRUE | FALSE | arr_lit;

    def visitLit(self, ctx:ZCodeParser.LitContext):
        if ctx.NUM_LIT():
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.T():
            return BooleanLiteral(True)
        elif ctx.F():
            return BooleanLiteral(False)
        elif ctx.arr_lit():
            return self.visit(ctx.arr_lit())


    # Visit a parse tree produced by ZCodeParser#arr_lit.
    # arr_lit: LS_BRACKET list_expr RS_BRACKET;

    def visitArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        return ArrayLiteral(self.visit(ctx.list_expr()))


    # list_lit: literal COMMA list_lit | literal;
    # Visit a parse tree produced by ZCodeParser#list_lit.
    def visitList_lit(self, ctx:ZCodeParser.List_litContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.lit())]
        else:
            return [self.visit(ctx.lit())] + self.visit(ctx.list_lit())


    # Visit a parse tree produced by ZCodeParser#list_NUMBER_LIT.
    # list_NUMBER_LIT: NUM_LIT list_NUMBER_tail | NUM_LIT;
    def visitList_NUMBER_LIT(self, ctx:ZCodeParser.List_NUMBER_LITContext):
        if ctx.getChildCount()==1:
            return [float(ctx.NUM_LIT().getText())]
        else:
            return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.list_NUMBER_tail())


    # list_NUMBER_tail: COMMA NUM_LIT list_NUMBER_tail | ;
    # Visit a parse tree produced by ZCodeParser#list_NUMBER_tail.
    def visitList_NUMBER_tail(self, ctx:ZCodeParser.List_NUMBER_tailContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.list_NUMBER_tail())


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    # stmt_list: stmt stmt_list | ; 
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        if ctx.getChildCount() == 0: return []
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_list())


    # Visit a parse tree produced by ZCodeParser#stmt.
    # stmt: (decl_stmt | assign_stmt 
    #        | if_stmt | for_stmt 
    #       | break_stmt | cont_stmt 
    #        | return_stmt  | call_stmt | block_stmt);
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.decl_stmt(): 
            return self.visit(ctx.decl_stmt())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        elif ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt()) 
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.cont_stmt():
            return self.visit(ctx.cont_stmt())
        



    # Visit a parse tree produced by ZCodeParser#decl_stmt.
    # decl_stmt: variables ignore;
    def visitDecl_stmt(self, ctx:ZCodeParser.Decl_stmtContext):
        return self.visit(ctx.varis())


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    # assign_stmt : lhs ASSIGN_OP exp ignore;
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.exp()))

    #return_stmt: RETURN exp? ignore;
    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return()


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    # call_stmt: ID L_BRACKET nullable_list_expr R_BRACKET ignore;
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID()), self.visit(ctx.nullable_list_expr()))

    # block_stmt: BEGIN ignore stmt_list END ignore;
    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.stmt_list()))


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    # if_stmt: IF L_BRACKET exp R_BRACKET ignore? stmt elif_list (ELSE ignore? stmt )?;

    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.exp()), self.visit(ctx.stmt()[0]), self.visit(ctx.elif_list()),None)
        else:
            return If(self.visit(ctx.exp()),self.visit(ctx.stmt()[0]),self.visit(ctx.elif_list()),self.visit(ctx.stmt()[1]))


    # Visit a parse tree produced by ZCodeParser#elif_list.
    # elif_list:ELIF L_BRACKET exp R_BRACKET ignore? stmt elif_list | ;
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount() == 0: 
            return []
        else:
            return [(self.visit(ctx.exp()), self.visit(ctx.stmt()))] + self.visit(ctx.elif_list())

    # Visit a parse tree produced by ZCodeParser#for_stmt.
    # for_stmt: FOR ID UNTIL exp BY exp ignore? stmt ignore?;

    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return For(Id(ctx.ID()), self.visit(ctx.exp()[0]), self.visit(ctx.exp()[1]), self.visit(ctx.stmt()))

    # break_stmt: BREAK ignore;
    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by ZCodeParser#cont_stmt.
    # cont_stmt: CONTINUE ignore;
    def visitCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#lhs.
    # lhs: ID (LS_BRACKET list_expr RS_BRACKET)?;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.list_expr():
            return ArrayCell(Id(ctx.ID()), self.visit(ctx.list_expr()))
        else:
            return Id(ctx.ID().getText())


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None

