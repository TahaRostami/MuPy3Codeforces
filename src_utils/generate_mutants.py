import json
from src.utils.timer import Timer
from multiprocessing import Pool
from mutpy import codegen,standard_operators,experimental_operators,controller,StatementDeletion,ArithmeticOperatorReplacement,ArithmeticOperatorDeletion
from astmonkey import transformers
import ast


def gen_mutants(source_code,percentage=100):
    operators = (standard_operators).union(experimental_operators)
    fom = controller.FirstOrderMutator(operators, percentage=percentage)
    mutants=[]
    for mutation, mutant in fom.mutate(transformers.ParentChildNodeTransformer().visit(ast.parse(source_code))):
        try:
            mutants.append({"mutation_operator": str(mutation[0].operator), "mutant": codegen.to_source(mutant)})
        except:pass
    return mutants




