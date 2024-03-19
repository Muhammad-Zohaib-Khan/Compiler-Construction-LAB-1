import re
import pandas as pd
from matplotlib import pyplot as plt

class Lexical_Analysis(object):
    def __init__(self,code):
        self.input_code=code
        self.count={}
        self.tokens=[]
        self.class_part=[]
        self.language_specifications = {
            "operators": r'\+\+|--|!=|<=|>=|==|[-+*/%=<>🤝👐💢]',
            "special_keyword": r'✍|🖨|🤔|😅|➰|➿|✅|❌|💔|🧡',
            "special_characters": r'[\(\)\[\]\{\};,:]',
            "integer": r'\b[1-9][0-9]*\b',
            "string": r'"(?:\\.|[^"\\])*"',
            "ID": r'[🔤🔢]\s*[a-zA-Z_]+[a-zA-Z0-9_]*'
        }
        
        self.class_part_values={
            "✍": "INPUT",
            "🖨": "PRINT",
            "🤔": "IF",
            "😅":"ELSE",
            "➰": "FOR",
            "➿": "WHILE",
            "✅": "TRUE",
            "❌": "FALSE",
            "💔": "BREAK",
            "🧡": "CONTINUE",
            "🤝":"AND",
            "👐":"OR",
            "💢":"NOT",
            "<": "LT",
            ">": "GT",
            "<=":"LE",
            ">=":"GE",
            "=": "EQ",
            "+": "ADD",
            "-": "SUB",
            "*": "MUL",
            "/": "DIV",
            "%":"MOD",
            "+=":"INC",
            "-=":"DEC",
            "!=":"NE",
            "==":"EQT",
            "[": "OSB",
            "]": "CSB",
            "{": "OCB",
            "}": "CCB",
            "(": "ORB",
            ")": "CRB",
            ":": "COLON",
            ";": "SEMI COLON",
            ",": "COMMA",
            "?":"QM",
            }
    def get_tokens(self):
        position=0
        while position<len(self.input_code):
            for pattern in self.language_specifications.values():
                match=re.match(pattern,self.input_code[position::])
                if match:
                    token=match.group()
                    self.tokens.append(token)
                    position+=len(token)
                    break
            else:
                position+=1

    def get_class_part(self):
          for token in self.tokens:
            for cls,pattern in self.language_specifications.items():
                if re.match(pattern,token):
                    if token in self.class_part_values:
                        self.class_part.append((token,self.class_part_values[token],cls))
                    elif re.match(self.language_specifications["integer"],token):
                        self.class_part.append((token,cls,"Datatype"))
                    elif re.match(self.language_specifications["string"],token):
                        self.class_part.append((token,cls,"Datatype"))
                    elif re.match(self.language_specifications["ID"],token):
                        self.class_part.append((token,"ID",cls))
    def get_count(self):
        for cls,pattern in self.language_specifications.items():
            pattern=re.findall(pattern,self.input_code)
            self.count.update({cls:len(pattern)})

    def show_result(self):
        print("Lexical Analysis".center(60))
        result=pd.DataFrame(self.class_part,columns=["Token","Class Part","Value Part"])
        print(result.to_string(index=False))
        Name=[]
        Count=[]
        print("Count is:")
        for name,count in self.count.items():
            print(f"{name}:{count}\n")
            Name.append(name)
            Count.append(count)
        print("The Total Tokens are: ",sum(Count))
        
        fig = plt.figure(figsize=(10, 5)) 

        plt.bar(Name,Count,color="g",width=0.4)

        plt.xlabel("Class Part") 
        plt.ylabel("Count") 
        plt.title("Compiler Construction") 
        plt.show()

code='''
🔢 num=✍("Enter a number: ")
🤔(num % 2)== 0:
   🖨("num is Even")
😅:
   🖨("num is Odd")'''

Lexemes=Lexical_Analysis(code)
Lexemes.get_tokens()
Lexemes.get_class_part()
Lexemes.get_count()
Lexemes.show_result()
