use py3codeforces


SELECT source.id, raw_mutation_score, test_suite_size FROM source,problems WHERE problems.id = source.problems_id


SELECT COUNT(*) FROM mutants WHERE src_id_original In (SELECT DISTINCT mutants.src_id_original FROM mutants WHERE mutants.src_id_original IN (SELECT source.id FROM source,problems WHERE
problems.id = source.problems_id
AND percent_passed_tests>=0.75 AND percent_passed_tests<1
AND test_suite_size>=14
AND raw_mutation_score>0.50 
AND test_suite_diversity>=0.04) 
AND mutants.strongly_killed_frequency>0 AND mutants.strongly_killed_frequency<0.95
 AND mutants.real_fault_revelation_frequency=1)

SELECT COUNT(DISTINCT mutants.src_id_original) FROM mutants WHERE mutants.src_id_original IN (SELECT source.id FROM source,problems WHERE
problems.id = source.problems_id
AND percent_passed_tests>=0.75 AND percent_passed_tests<1
AND test_suite_size>=14
AND raw_mutation_score>0.50 
AND test_suite_diversity>=0.04) 
AND mutants.strongly_killed_frequency>0 AND mutants.strongly_killed_frequency<0.9
 AND mutants.real_fault_revelation_frequency=1


SELECT COUNT(*) FROM mutants WHERE mutants.src_id_original IN (SELECT source.id FROM source,problems WHERE
problems.id = source.problems_id
AND percent_passed_tests>=0.75 AND percent_passed_tests<1
AND test_suite_size>=14
AND raw_mutation_score>0.50 
AND test_suite_diversity>=0.04)


SELECT COUNT(*) FROM source,problems WHERE
problems.id = source.problems_id
AND percent_passed_tests>=0.75 AND percent_passed_tests<1
AND test_suite_size>=14
AND raw_mutation_score>0.57 
AND test_suite_diversity>=0.04

SELECT COUNT(*) FROM source WHERE 

SELECT src_id_original,AVG(strongly_killed_frequency) FROM mutants
GROUP BY src_id_original

SELECT mutants.src_id_original,AVG(mutant_execution.killed) FROM mutant_execution,mutants WHERE mutant_execution.mutant_id = mutants.id
GROUP BY mutants.src_id_original

SELECT problems_id,COUNT(*) FROM testcases 
GROUP BY problems_id

SELECT COUNT(*) FROM source WHERE raw_mutation_score >= 0.85



SELECT source_id,AVG(passed)
FROM source_execution  
GROUP BY source_id

SELECT mutant_id,SUM(killed),Count(*)
FROM mutant_execution  
GROUP BY mutant_id

SELECT mutant_id,AVG(killed)
FROM mutant_execution  
GROUP BY mutant_id

SELECT mutant_id,AVG(real_fault_revealed)
FROM mutant_execution WHERE killed=1
GROUP BY mutant_id