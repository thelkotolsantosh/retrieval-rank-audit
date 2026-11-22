"""Evaluate ranked document identifiers against binary relevance judgments."""
import argparse
import json
from pathlib import Path


def identifiers(value):
    if not isinstance(value, list) or any(type(x) is not str or not x for x in value):
        raise ValueError("Expected a list of nonempty document identifiers")
    if len(set(value)) != len(value):
        raise ValueError("Duplicate document identifier")
    return value


def evaluate(rows, k):
    if type(k) is not int or k < 1 or not isinstance(rows, list) or not rows:
        raise ValueError("Supply at least one query and a positive cutoff")
    seen = set()
    recall = reciprocal = 0.0
    for row in rows:
        query = row["query"]
        if not isinstance(query, str) or not query.strip() or query in seen:
            raise ValueError("Query identifiers must be unique and nonempty")
        seen.add(query)
        relevant = set(identifiers(row["relevant"]))
        if not relevant:
            raise ValueError("Each query needs a relevance judgment")
        hits = [i for i, doc in enumerate(identifiers(row["ranked"])[:k], 1)
                if doc in relevant]
        recall += len(hits) / len(relevant)
        reciprocal += 1 / hits[0] if hits else 0
    return {"queries": len(rows), "k": k, "recall": recall / len(rows),
            "mrr": reciprocal / len(rows)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()
    try:
        print(json.dumps(evaluate(json.loads(args.file.read_text()), args.k)))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f"Invalid input: {error}\n")
