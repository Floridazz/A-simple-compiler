# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0194\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\5&\u0116\n&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\7,\u0124\n,\f,\16,")
        buf.write("\u0127\13,\3-\3-\5-\u012b\n-\3-\5-\u012e\n-\3.\3.\5.\u0132")
        buf.write("\n.\3/\3/\3\60\6\60\u0137\n\60\r\60\16\60\u0138\3\61\3")
        buf.write("\61\7\61\u013d\n\61\f\61\16\61\u0140\13\61\3\62\3\62\5")
        buf.write("\62\u0144\n\62\3\62\6\62\u0147\n\62\r\62\16\62\u0148\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\7\63\u0151\n\63\f\63\16\63")
        buf.write("\u0154\13\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3")
        buf.write("\65\7\65\u015f\n\65\f\65\16\65\u0162\13\65\3\65\3\65\3")
        buf.write("\66\6\66\u0167\n\66\r\66\16\66\u0168\3\66\3\66\3\67\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u0172\n\67\38\38\38\58\u0177\n")
        buf.write("8\39\39\79\u017b\n9\f9\169\u017e\139\39\39\39\39\59\u0184")
        buf.write("\n9\39\39\3:\3:\7:\u018a\n:\f:\16:\u018d\13:\3:\3:\3:")
        buf.write("\3;\3;\3;\2\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\60g\61i\62k\63")
        buf.write("m\2o\2q\64s\65u\66\3\2\17\5\2C\\aac|\6\2\62;C\\aac|\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhp")
        buf.write("pttvv\3\2))\3\2$$\3\2\f\f\4\2\f\f\17\17\5\2\n\13\16\17")
        buf.write("\"\"\3\2\17\17\2\u01a7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5")
        buf.write("|\3\2\2\2\7\u0082\3\2\2\2\t\u0089\3\2\2\2\13\u008e\3\2")
        buf.write("\2\2\r\u0095\3\2\2\2\17\u009c\3\2\2\2\21\u00a0\3\2\2\2")
        buf.write("\23\u00a8\3\2\2\2\25\u00ad\3\2\2\2\27\u00b1\3\2\2\2\31")
        buf.write("\u00b4\3\2\2\2\33\u00ba\3\2\2\2\35\u00c0\3\2\2\2\37\u00c9")
        buf.write("\3\2\2\2!\u00cc\3\2\2\2#\u00d1\3\2\2\2%\u00d6\3\2\2\2")
        buf.write("\'\u00dc\3\2\2\2)\u00e0\3\2\2\2+\u00e4\3\2\2\2-\u00e8")
        buf.write("\3\2\2\2/\u00eb\3\2\2\2\61\u00ed\3\2\2\2\63\u00ef\3\2")
        buf.write("\2\2\65\u00f1\3\2\2\2\67\u00f3\3\2\2\29\u00f5\3\2\2\2")
        buf.write(";\u00f8\3\2\2\2=\u00fb\3\2\2\2?\u00fe\3\2\2\2A\u0101\3")
        buf.write("\2\2\2C\u0103\3\2\2\2E\u0105\3\2\2\2G\u0109\3\2\2\2I\u010c")
        buf.write("\3\2\2\2K\u0115\3\2\2\2M\u0117\3\2\2\2O\u0119\3\2\2\2")
        buf.write("Q\u011b\3\2\2\2S\u011d\3\2\2\2U\u011f\3\2\2\2W\u0121\3")
        buf.write("\2\2\2Y\u0128\3\2\2\2[\u0131\3\2\2\2]\u0133\3\2\2\2_\u0136")
        buf.write("\3\2\2\2a\u013a\3\2\2\2c\u0141\3\2\2\2e\u014a\3\2\2\2")
        buf.write("g\u0158\3\2\2\2i\u015a\3\2\2\2k\u0166\3\2\2\2m\u0171\3")
        buf.write("\2\2\2o\u0176\3\2\2\2q\u0178\3\2\2\2s\u0187\3\2\2\2u\u0191")
        buf.write("\3\2\2\2wx\7v\2\2xy\7t\2\2yz\7w\2\2z{\7g\2\2{\4\3\2\2")
        buf.write("\2|}\7h\2\2}~\7c\2\2~\177\7n\2\2\177\u0080\7u\2\2\u0080")
        buf.write("\u0081\7g\2\2\u0081\6\3\2\2\2\u0082\u0083\7p\2\2\u0083")
        buf.write("\u0084\7w\2\2\u0084\u0085\7o\2\2\u0085\u0086\7d\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7t\2\2\u0088\b\3\2\2\2\u0089")
        buf.write("\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7n\2\2\u008d\n\3\2\2\2\u008e\u008f\7u\2\2\u008f")
        buf.write("\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092\7k\2\2\u0092")
        buf.write("\u0093\7p\2\2\u0093\u0094\7i\2\2\u0094\f\3\2\2\2\u0095")
        buf.write("\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write("\u0099\7w\2\2\u0099\u009a\7t\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\16\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e\7c\2\2\u009e")
        buf.write("\u009f\7t\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7f\2\2\u00a1")
        buf.write("\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7e\2\2\u00a7")
        buf.write("\22\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7w\2\2\u00aa")
        buf.write("\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\24\3\2\2\2\u00ad")
        buf.write("\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7t\2\2\u00b0")
        buf.write("\26\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2\u00b3\7{\2\2\u00b3")
        buf.write("\30\3\2\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6\7p\2\2\u00b6")
        buf.write("\u00b7\7v\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7n\2\2\u00b9")
        buf.write("\32\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7t\2\2\u00bc")
        buf.write("\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7m\2\2\u00bf")
        buf.write("\34\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7q\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7k\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\36\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb")
        buf.write(" \3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce")
        buf.write("\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\"\3\2\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5$\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db&\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df(\3\2\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7v\2\2\u00e3")
        buf.write("*\3\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7f\2\2\u00e7,\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea.\3\2\2\2\u00eb\u00ec\7-\2\2\u00ec")
        buf.write("\60\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee\62\3\2\2\2\u00ef")
        buf.write("\u00f0\7,\2\2\u00f0\64\3\2\2\2\u00f1\u00f2\7\61\2\2\u00f2")
        buf.write("\66\3\2\2\2\u00f3\u00f4\7\'\2\2\u00f48\3\2\2\2\u00f5\u00f6")
        buf.write("\7@\2\2\u00f6\u00f7\7?\2\2\u00f7:\3\2\2\2\u00f8\u00f9")
        buf.write("\7>\2\2\u00f9\u00fa\7?\2\2\u00fa<\3\2\2\2\u00fb\u00fc")
        buf.write("\7>\2\2\u00fc\u00fd\7/\2\2\u00fd>\3\2\2\2\u00fe\u00ff")
        buf.write("\7#\2\2\u00ff\u0100\7?\2\2\u0100@\3\2\2\2\u0101\u0102")
        buf.write("\7>\2\2\u0102B\3\2\2\2\u0103\u0104\7@\2\2\u0104D\3\2\2")
        buf.write("\2\u0105\u0106\7\60\2\2\u0106\u0107\7\60\2\2\u0107\u0108")
        buf.write("\7\60\2\2\u0108F\3\2\2\2\u0109\u010a\7?\2\2\u010a\u010b")
        buf.write("\7?\2\2\u010bH\3\2\2\2\u010c\u010d\7?\2\2\u010dJ\3\2\2")
        buf.write("\2\u010e\u0116\5G$\2\u010f\u0116\5? \2\u0110\u0116\5;")
        buf.write("\36\2\u0111\u0116\59\35\2\u0112\u0116\5A!\2\u0113\u0116")
        buf.write("\5C\"\2\u0114\u0116\5I%\2\u0115\u010e\3\2\2\2\u0115\u010f")
        buf.write("\3\2\2\2\u0115\u0110\3\2\2\2\u0115\u0111\3\2\2\2\u0115")
        buf.write("\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2")
        buf.write("\u0116L\3\2\2\2\u0117\u0118\7*\2\2\u0118N\3\2\2\2\u0119")
        buf.write("\u011a\7+\2\2\u011aP\3\2\2\2\u011b\u011c\7]\2\2\u011c")
        buf.write("R\3\2\2\2\u011d\u011e\7_\2\2\u011eT\3\2\2\2\u011f\u0120")
        buf.write("\7.\2\2\u0120V\3\2\2\2\u0121\u0125\t\2\2\2\u0122\u0124")
        buf.write("\t\3\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126X\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u012a\5_\60\2\u0129\u012b\5a\61\2")
        buf.write("\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3")
        buf.write("\2\2\2\u012c\u012e\5c\62\2\u012d\u012c\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012eZ\3\2\2\2\u012f\u0132\5\3\2\2\u0130\u0132")
        buf.write("\5\5\3\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132")
        buf.write("\\\3\2\2\2\u0133\u0134\t\4\2\2\u0134^\3\2\2\2\u0135\u0137")
        buf.write("\5]/\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139`\3\2\2\2\u013a\u013e")
        buf.write("\7\60\2\2\u013b\u013d\5]/\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013fb\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0143\t\5\2")
        buf.write("\2\u0142\u0144\t\6\2\2\u0143\u0142\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0147\5]/\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149d\3\2\2\2\u014a\u0152\7$\2\2\u014b")
        buf.write("\u0151\n\7\2\2\u014c\u014d\7^\2\2\u014d\u0151\t\b\2\2")
        buf.write("\u014e\u014f\t\t\2\2\u014f\u0151\t\n\2\2\u0150\u014b\3")
        buf.write("\2\2\2\u0150\u014c\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0154")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0155\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\7$\2\2")
        buf.write("\u0156\u0157\b\63\2\2\u0157f\3\2\2\2\u0158\u0159\t\13")
        buf.write("\2\2\u0159h\3\2\2\2\u015a\u015b\7%\2\2\u015b\u015c\7%")
        buf.write("\2\2\u015c\u0160\3\2\2\2\u015d\u015f\n\f\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0163\u0164\b\65\3\2\u0164j\3\2\2\2\u0165\u0167\t\r\2")
        buf.write("\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\b\66\3\2\u016bl\3\2\2\2\u016c\u0172\n\7\2\2\u016d")
        buf.write("\u016e\7^\2\2\u016e\u0172\t\b\2\2\u016f\u0170\7)\2\2\u0170")
        buf.write("\u0172\7$\2\2\u0171\u016c\3\2\2\2\u0171\u016d\3\2\2\2")
        buf.write("\u0171\u016f\3\2\2\2\u0172n\3\2\2\2\u0173\u0177\t\16\2")
        buf.write("\2\u0174\u0175\7^\2\2\u0175\u0177\n\b\2\2\u0176\u0173")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0177p\3\2\2\2\u0178\u017c")
        buf.write("\7$\2\2\u0179\u017b\5m\67\2\u017a\u0179\3\2\2\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u0183\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0184\7")
        buf.write("\2\2\3\u0180\u0181\7\17\2\2\u0181\u0184\7\f\2\2\u0182")
        buf.write("\u0184\7\f\2\2\u0183\u017f\3\2\2\2\u0183\u0180\3\2\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\b")
        buf.write("9\4\2\u0186r\3\2\2\2\u0187\u018b\7$\2\2\u0188\u018a\5")
        buf.write("m\67\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\5o8\2\u018f\u0190\b:\5\2\u0190")
        buf.write("t\3\2\2\2\u0191\u0192\13\2\2\2\u0192\u0193\b;\6\2\u0193")
        buf.write("v\3\2\2\2\25\2\u0115\u0125\u012a\u012d\u0131\u0138\u013e")
        buf.write("\u0143\u0148\u0150\u0152\u0160\u0168\u0171\u0176\u017c")
        buf.write("\u0183\u018b\7\3\63\2\b\2\2\39\3\3:\4\3;\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T = 1
    F = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    BY = 11
    UNTIL = 12
    BR = 13
    CONT = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    GOE = 28
    LOE = 29
    ASSIGN = 30
    NEQ = 31
    LT = 32
    GT = 33
    CONCAT = 34
    CMP = 35
    EQ = 36
    REL_OP = 37
    LB = 38
    RB = 39
    SLB = 40
    SRB = 41
    CM = 42
    ID = 43
    NUM_LIT = 44
    BOOL_LIT = 45
    STRING_LIT = 46
    NEWL = 47
    CMT = 48
    WS = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'by'", "'until'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'>='", "'<='", "'<-'", "'!='", "'<'", "'>'", "'...'", 
            "'=='", "'='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "T", "F", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
            "FUNC", "FOR", "BY", "UNTIL", "BR", "CONT", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "GOE", "LOE", "ASSIGN", "NEQ", "LT", "GT", "CONCAT", 
            "CMP", "EQ", "REL_OP", "LB", "RB", "SLB", "SRB", "CM", "ID", 
            "NUM_LIT", "BOOL_LIT", "STRING_LIT", "NEWL", "CMT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T", "F", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                  "DYNAMIC", "FUNC", "FOR", "BY", "UNTIL", "BR", "CONT", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "GOE", "LOE", "ASSIGN", 
                  "NEQ", "LT", "GT", "CONCAT", "CMP", "EQ", "REL_OP", "LB", 
                  "RB", "SLB", "SRB", "CM", "ID", "NUM_LIT", "BOOL_LIT", 
                  "Digit", "Int", "Dec", "Expo", "STRING_LIT", "NEWL", "CMT", 
                  "WS", "YES", "NO", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.STRING_LIT_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            		raise UncloseString(self.text[1:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


