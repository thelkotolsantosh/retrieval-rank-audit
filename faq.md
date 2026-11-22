# Frequently asked questions

## 1. What does the tool do?

Score a ranked retrieval run using macro recall and mean reciprocal rank at a chosen cutoff.

## 2. Who encounters this problem?

RAG developers comparing retrievers need to know whether relevant documents appear early enough to reach the generation model.

## 3. What decision does the report support?

Compare two runs with the same query judgments and cutoff before choosing a retrieval configuration.

## 4. What does it check?

It rejects repeated query IDs, repeated document IDs and empty relevance judgments.

## 5. Which language runs the report?

Python implements both the evaluator and its command-line interface.

## 6. Which libraries does it use?

argparse parses the cutoff, json reads the run and unittest covers scoring behavior.

## 7. What do I need locally?

Use Python 3.10 or later and a readable JSON file.

## 8. How do I install it?

Clone the repository and open its directory. The evaluator uses the standard library.

## 9. Which settings can I change?

Set --k to a positive integer. Its default is 5.

## 10. How do I run the demonstration?

python src/report.py examples/demo.json --k 5

## 11. Where does the implementation live?

src/report.py contains evaluate and the command-line entry point. tests/ holds regression cases.

## 12. How is the result calculated?

For each query, divide retrieved relevant documents by all judged relevant documents. Average over queries. MRR averages the reciprocal rank of the first hit, counting misses as zero.

## 13. What input should I prepare?

Supply a JSON list. Each object needs query, ranked and relevant. Both document fields are lists of string IDs.

## 14. What do the output numbers mean?

The demo returns recall 1 and MRR 0.5 because the sole relevant document ranks second.

## 15. How can I extend it?

Add a metric inside evaluate and document its denominator for queries with no hits.

## 16. How are invalid records handled?

Malformed input exits with status 2 and an error on standard error.

## 17. What input mistake is easy to miss?

Numeric IDs must be converted to strings consistently in both document lists.

## 18. How can I investigate an unexpected result?

Run one query at a time and inspect the first k document IDs against its judgments.

## 19. How do I run the tests?

python -m unittest discover -s tests -v

## 20. How can I contribute a change?

Add a hand-calculated ranked list that demonstrates the scoring change and submit the test with the implementation.

## 21. What does the report leave out?

Binary judgments cannot express degrees of relevance. This measures retrieval quality only.

## 22. Can I deploy it for production?

This is an offline evaluator for trusted, memory-sized files. Benchmark throughput before integrating a large corpus.

## 23. What could a future version add?

Per-query output and graded nDCG would help diagnose individual misses.

## 24. How should I handle sensitive data?

Use synthetic IDs when sharing examples. The program reads locally and makes no network requests.

## 25. Where can I see a worked example?

examples/demo.json contains the two ranked documents used in the README.

