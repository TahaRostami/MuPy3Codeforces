import json
from dpu_utils.codeutils.deduplication import DuplicateDetector
from dpu_utils.utils import RichPath
import tempfile
import ast
import tokenize

if __name__ == '__main__':

    detector = DuplicateDetector(min_num_tokens_per_document=10, set_similarity_threshold=0.90,multiset_similarity_threshold=0.70)

    with open("...../source.json","r",encoding="UTF_8") as f:sources=json.loads(f.read())

    for id, src in sources:
        with tempfile.TemporaryFile() as fp:
            try:
                fp.write(ast.unparse(ast.parse(src)).encode())
                fp.seek(0)
                detector.add_file(id=id, tokens=[token_obj.line for token_obj in tokenize.tokenize(fp.readline)])
            except:pass

    duplicates = detector.compute_duplicates()
    detector.print_clone_set_stats(duplicates)
    out_path = RichPath.create("....../output_filename.json.gz")
    out_path.save_as_compressed_file([list(l) for l in duplicates])


