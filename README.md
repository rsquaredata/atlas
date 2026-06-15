<div align="center">

# ATLAS

### *Agentic Text and Literature Analysis System*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Agentic AI](https://img.shields.io/badge/Agentic-AI-purple.svg)]()
[![Knowledge Graph](https://img.shields.io/badge/Knowledge-Graph-orange.svg)]()
[![LLM](https://img.shields.io/badge/LLM-Information%20Extraction-green.svg)]()
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)]()

*Personal Research Project*
*Agentic AI • Knowledge Graphs • Information Extraction*

---

</div>


## Overview

**ATLAS** is a research-oriented project investigating the use of multi-agent LLM systems for extracting, structuring, and validating knowledge from scientific literature.

Scientific publications contain large amounts of valuable information regarding methods, datasets, evaluation protocols, and experimental results. However, this information remains primarily embedded in unstructured text.

ATLAS explores whether an agentic workflow can assist in transforming scientific documents into structured knowledge representations suitable for downstream analysis.

The project focuses on literature related to machine learning, agentic AI, and automated data science systems.
---

## Research Question

Beyond simple document summarization, ATLAS investigates the following question:

> To what extent can multi-agent LLM systems reliably extract and organize scientific knowledge into structured graph representations while maintaining factual consistency?

The project aims to evaluate both extraction quality and structural coherence of generated knowledge graphs.

---

## Research Orientation

ATLAS integrates:

- Information extraction
- Knowledge representation
- Agentic workflows
- Human-in-the-loop validation
- Knowledge graph construction

The emphasis is placed on:

- Reproducibility
- Traceability
- Extraction transparency
- Structured evaluation

Rather than treating LLM outputs as final answers, ATLAS treats them as intermediate knowledge artifacts subject to validation and refinement.

## System Architecture

The system follows a multi-stage agentic pipeline::

```
Scientific Paper
↓
LLM Extraction
↓
Structured JSON
↓
Knowledge Graph Construction
↓
Graph Comparison
↓
Embedding-based Alignment
↓
Concept Graph
↓
Community Detection
↓
Knowledge Exploration
```

Each agent is responsible for a specific knowledge extraction task.

The workflow is intentionally designed as a semi-automated system where human review remains part of the decision process.

---

## Target Knowledge Representation

ATLAS focuses on extracting entities and relationships such as:

### Entities

| Type	| Examples |
|-|-|
| Papers | AIDE, AutoKaggle |
| Methods |	Tree Search, Multi-Agent Systems |
| Datasets |	MLE-Bench |
| Tasks	| Feature Engineering |
| Metrics	| Accuracy, F1-score |

### Relationships

| Relation	| Example |
|-|-|
| uses | AutoKaggle → Multi-Agent System |
| evaluated_on |	AutoKaggle → MLE-Bench |
| improves |	Method A → Baseline B |
| appplied_to	| Method → Task |

These elements are represented as a lightweight knowledge graph.

---

## Experimental Workflow

```
Literature Collection
↓
Document Processinf
↓
Agentic Extraction
↓
Graph Construction
↓
Consistency Validation
↓
Knowledge Exploration
```

---

## Evaluation Strategy

### Quantitative Evaluation

- Entity extraction accuracy
- Relationship extraction accuracy
- Graph completeness
- Consistency checks

### Qualitative Evaluation

- Hallucination analysis
- Missing relationship analysis
- Ambiguous entity resolution
- Human reviewer agreement

---

## Repository Structure

```
ATLAS/
├── data/
  ├── raw/
  └── processed/
├── notebooks/
├── outputs/
├── src/
  └── atlas/
├── tests/
├── docs/
└── README.md
```

---

## Current Development Status

ATLAS is currently under active development.

### Current Results

The current prototype has been evaluated on a growing corpus of scientific papers related to agentic AI systems, automated machine learning, and LLM-based software engineering agents.

#### Knowledge Graph Construction

ATLAS successfully extracts:

* Named systems and frameworks
* Scientific concepts
* Benchmarks and datasets
* Technical relationships

and converts them into lightweight knowledge graphs.

#### Cross-Paper Concept Alignment

Using sentence embeddings and semantic similarity analysis, ATLAS identifies related concepts across papers, even when different terminology is used.

Examples include:

* Large Language Models ↔ Frontier Large Language Models
* Multi-Agent System ↔ LLM-Based Multi-Agent Systems
* Kaggle Competitions ↔ Kaggle Evaluations

#### Emerging Research Communities

Experiments conducted on an initial corpus revealed the emergence of several thematic communities:

* Agent Systems and Multi-Agent Collaboration
* LLM-based Agents
* Prompting and Code Generation
* Benchmarking and Evaluation

This suggests that meaningful scientific structure can emerge from automatically extracted concepts without manually defined ontologies.

#### Observed Limitations

Semantic similarity successfully captures:

* synonymy
* near-synonymy
* concept variants

However, it struggles to capture higher-level knowledge relations such as:

* Agent → Reasoning
* Agent → Decision-Making
* Agent → Instruction Following

These findings motivate future work on ontology construction and relation discovery beyond embedding similarity alone.


---

## ## Future Work

Planned research directions include:

* Concept canonicalization
* Automatic ontology construction
* Cross-paper knowledge graph merging
* Community detection and graph analytics
* Relation discovery beyond semantic similarity
* Benchmark evolution tracking
* Agent-assisted literature mapping

A longer-term objective is to investigate whether agentic systems can automatically build and maintain dynamic scientific knowledge maps from continuously evolving research literature.

---

## License

This project is released under the MIT License.

See the LICENSE file for details.

---

## Disclaimer

This project is intended for research, educational, and portfolio purposes.
The extracted knowledge should not be considered authoritative without human verification.

<div align="center">

ATLAS - From Scientific Text to Structured Knowledge

</div>
