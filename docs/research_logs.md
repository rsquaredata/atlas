# ATLAS Research Log

## Iteration 1 - (10 papers)

### Corpus

- [AutoKaggle](https://arxiv.org/abs/2410.20424)
- [AIDE](https://arxiv.org/abs/2502.13138)
- [Data Interpreter](https://arxiv.org/abs/2402.18679)
- [The AI Scientist](https://arxiv.org/abs/2408.06292)
- [SWE-Agent](https://arxiv.org/abs/2405.15793)
- [OpenHands](https://arxiv.org/abs/2407.16741)
- [MetaGPT](https://arxiv.org/abs/2308.00352)
- [AgentBench](https://arxiv.org/abs/2308.03688)
- [Voyager](https://arxiv.org/abs/2305.16291)
- [CAMEL](https://arxiv.org/abs/2408.06292)

### Observations

#### Concept Extraction

Mistral successfully extracts:
- Agents systems
- Frameworks
- Benchmarks
- Datasets
- Scientific Concepts
- Technical workflows

The extraction quality is sufficient for graph construction, although some concepts remain overly generic or paper-specific.

#### Concept Alignment

SentenceTransformers (all-MiniLM-L6-v2) successfully aligns:

- LLMs ↔ Large Language Models
- Multi-Agent System ↔ LLM-based Multi-Agent Systems
- Kaggle Competititions ↔ Kaggle Evaluations
- SWE-BENCH ↔ SWE-bench

Embedding-based alignment performs well for synonymy and terminology variants.

#### Normalization

Simple normalization significantly improves clustering.

Applied techniques:

- lowercasing
- acronym expansion
- duplicate removal
- canonical naming

Examples:

- LLMs → Large Language Models
- SWE-BENCH → SWE-bench

#### Community Detection

Using semantic similarity threshold threshold = 0.50:

##### Cluster 1 - Agents and LLM Systems

Contains concepts related to:

- AI Agents
- Multi-Agent Systems
- LLM-based Agents
- Workflow orchestrastion

##### Cluster 2 - Benchmarking

Contains:

- SWE-Bench
- OpenAI MLE-Bench
- METRs RE-Bench

##### Cluster 3 - Prompting and Code Tasks

Contains concepts related to:

- Prompting
- Instruction following
- Code execution
- Code optimization
- Code training

#### Cluster 4 - Kaggle Evaluation

Contains:

- Kaggle Competititons
- Kaggle Evaluations

#### Main Findings

1. Meaningful thematic communities emerge from concept extraction and semantic alignment alone.
2. Increasing corpus size produces denser communities rather than a single giant cluster.
3. Benchmark-related concepts naturally group together.
4. Agent-related concepts form the largest and most stable cluster.


#### Limitation

Embedding similarity captures:

- synonymy
- terminology variants
- near-synonymy

but does not reliably capture knowledge relations such as

- Agent → Reasoning
- Agent → Decision-Making
- Agent → Instruction Following

These relations appear to require ontology-level reasoning rather than pure semantic similarity.

### Future Work

- Add more agentic AI papers
- Concept canonicalization
- Ontology construction
- Knowledge relation discovery
- Multi-document graph merging
- Cluster evolution tracking
- Graph-based literature mapping

