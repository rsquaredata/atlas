# ATLAS Research Log

## Iteration 1 - Initial corpus (8 papers)

### Corpus

- AutoKaggle
- AIDE
- Data Interpreter
- The AI Scientist
- SWE-Agent
- OpenHands
- MetaGPT
- AgentBench

### Observations

#### Concept Extraction

Mistral successfully extracts:
- Agents
- Frameworks
- Benchmarks
- Scientific Concepts

The extraction quality is acceptable for graph construction.

#### Concept Alignment

SentenceTransformers (all-MiniLM-L6-v2) successfully aligns:

- LLMs ↔ Large Language Models
- Multi-Agent System ↔ LLM-based Multi-Agent Systems
- Code Execution ↔ Code Optimization

#### Normalization

Simple normalization significantly improves clustering.

Examples:

- LLMs → Large Language Models
- SWE-BENCH → SWE-bench
- Lowercasing concepts reduces duplicates.

#### Clustering

At threshold = 0.50:

Main cluster:

- AI Agents
- Multi-Agent Systems
- Language Model Agents
- LLM-based Agents
- Workflow concepts

Benchmark cluster:

- SWE-Bench
- OpenAI MLE-Bench
- METRs RE-Bench

#### Limitation

Embedding similarity captures:

- synonymy
- near-synonymy

but fails to capture:

Agent → Reasoning
Agent → Decision-Making
Agent → Instruction Following

These are knowledge relations rather than semantic similarity relations.

### Future Work

- Add more papers
- Concept canonicalization
- Automatic ontology construction
- Relation discovery beyond similarity