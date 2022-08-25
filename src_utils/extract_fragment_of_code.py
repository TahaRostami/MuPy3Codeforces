import ast
import json
from astmonkey import transformers

def find_line_mutation_started(source_lines,mutant_lines):
    tbl=[[source_lines[k] if k<len(source_lines) else "",mutant_lines[k] if k<len(mutant_lines) else ""] for k in range(max(len(mutant_lines),len(source_lines)))]
    i=0
    while tbl[i][0]==tbl[i][1]:
       i+=1
    return i+1

def find_node(node,line_number):
    for child in node.children:
        if hasattr(child, 'lineno') and child.lineno==line_number:
            return child
        x=find_node(child,line_number)
        if x is not None:
            return x
    return None

def find_parent(node):
    if isinstance(node, ast.Module):
        return node
    if isinstance(node, ast.FunctionDef):
        return node
    return find_parent(node.parent)

def unparse(node):
    if isinstance(node, ast.FunctionDef):
        return ast.unparse(node)
    if isinstance(node, ast.Module):
        code=""
        for child in node.children:
            if isinstance(child,ast.FunctionDef)==False and\
               isinstance(child,ast.AsyncFunctionDef)==False and\
               isinstance(child,ast.ClassDef)==False and \
               isinstance(child, ast.Return) == False and \
               isinstance(child, ast.Import) == False and \
               isinstance(child, ast.ImportFrom) == False:
                 code+=ast.unparse(child) + "\n"
        return code

    return None

def extract_code_fragment(dict_sources,dict_mutants,mutant_id):
    m0,m=None,None
    mutant = dict_mutants[mutant_id]
    source = dict_sources[mutant["src_id_original"]]
    mutant_code = mutant["sourceCode"].split("\n")
    source_code = source["modifiedSourceCode"].split("\n")
    line_number_change_started = find_line_mutation_started(source_code, mutant_code)
    try:
        node = ast.parse(mutant["sourceCode"])# or source["modifiedSourceCode"]
        node = transformers.ParentChildNodeTransformer().visit(node)
        node = find_node(node, line_number_change_started)
        node=find_parent(node)
        if isinstance(node, ast.FunctionDef):
            for x in ast.walk(ast.parse(source["modifiedSourceCode"])):
                if isinstance(x, ast.FunctionDef) == True and x.name == node.name:
                    m0 = unparse(x)
                    break
        elif isinstance(node, ast.Module):
            m0 = unparse(transformers.ParentChildNodeTransformer().visit(ast.parse(source["modifiedSourceCode"])))
        m = unparse(node)
    except Exception as e:
        raise Exception("identified as stillborn mutant")
    return {"code fragment before mutation":m0,"code fragment after mutation":m}


"""
example:
        with open("....../source.json","r",encoding="UTF_8") as f:
           dict_sources={item['id']:item for item in json.loads(f.read())}
   
        with open("....../mutants.json","r",encoding="UTF_8") as f:
           dict_mutants = {item['id']: item for item in json.loads(f.read())}
           
        for muid in dict_mutants:
            try:          
               print(extract_code_fragment(dict_sources,dict_mutants,muid))                         
            except Exception as e:
               print(e)                           
"""