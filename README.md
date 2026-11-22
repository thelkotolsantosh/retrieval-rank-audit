# retrieval-rank-audit

Score a ranked retrieval run using macro recall and mean reciprocal rank at a chosen cutoff.

RAG developers comparing retrievers need to know whether relevant documents appear early enough to reach the generation model.

Compare two runs with the same query judgments and cutoff before choosing a retrieval configuration.

It rejects repeated query IDs, repeated document IDs and empty relevance judgments.

## Setup and usage

Use Python 3.10 or later and a readable JSON file.

Clone the repository and open its directory. The evaluator uses the standard library.

Set --k to a positive integer. Its default is 5.

```sh
python src/report.py examples/demo.json --k 5
```

Supply a JSON list. Each object needs query, ranked and relevant. Both document fields are lists of string IDs.

The demo returns recall 1 and MRR 0.5 because the sole relevant document ranks second.

## Architecture

argparse parses the cutoff, json reads the run and unittest covers scoring behavior.

src/report.py contains evaluate and the command-line entry point. tests/ holds regression cases.

For each query, divide retrieved relevant documents by all judged relevant documents. Average over queries. MRR averages the reciprocal rank of the first hit, counting misses as zero.

## Tests

```sh
python -m unittest discover -s tests -v
```

## Operational scope

Binary judgments cannot express degrees of relevance. This measures retrieval quality only.

This is an offline evaluator for trusted, memory-sized files. Benchmark throughput before integrating a large corpus.

Use synthetic IDs when sharing examples. The program reads locally and makes no network requests.

Per-query output and graded nDCG would help diagnose individual misses.

See [FAQ](faq.md), [contribution instructions](CONTRIBUTING.md) and the [MIT license](LICENSE).
