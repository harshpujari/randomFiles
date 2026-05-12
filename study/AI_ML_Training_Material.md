**TRAINING PROGRAM**

**AI & ML Development**

A curriculum and learning framework for working professionals

**Audience** Engineers from 0 to senior, including non-AI backgrounds transitioning in.

**Structure** Part I - Mindset. Part II - Staying current framework. Part III - Tiered curriculum.

**Format** Self-paced or cohort. 12-week intensive or 6-month part-time.

**PART I**

**The Mindset**

AI/ML is the fastest-moving field in software. Specific tools, models, and techniques become obsolete in 12-24 months. Two years ago, key-value pair extraction from PDFs was a hot specialization with dedicated libraries and vendors. Today, a general-purpose LLM does it in a one-shot prompt and the entire sub-field has collapsed. This will happen again, repeatedly, in every adjacent space.

A curriculum that teaches only current tools will be partially obsolete before the cohort finishes. The only durable strategy is to teach a mindset that survives the churn, then layer concrete skills on top. Part I sets that mindset before any technical content is introduced.

## **1\. First principles over tools**

Tools are implementations of ideas. The idea "retrieve relevant context, then condition generation on it" is durable. The tool "LangChain v0.0.x with FAISS" is not. Learners must develop the instinct to ask, for any new technology: what problem does this solve, what is the underlying idea, and what would I build if this tool did not exist? Engineers who can answer those three questions stay employable across stack changes.

## **2\. Distinguish layers of permanence**

Not all knowledge decays at the same rate. The mental model below is the single most important framing in this entire program. Internalize it, and the rest of the framework follows.

| **Layer**       | **Half-life** | **Examples**                                                                                                                         |
| --------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Durable**     | 10+ years     | Linear algebra, probability, information theory, optimization, the bias-variance tradeoff, system design fundamentals.               |
| **Slow-moving** | 3-5 years     | Transformer architecture, gradient descent variants, evaluation methodology, MLOps practices, PyTorch as a framework.                |
| **Fast-moving** | 6-18 months   | Specific model releases, fine-tuning libraries, vector DB choices, agent frameworks, prompting techniques.                           |
| **Hype layer**  | 3-12 months   | "AutoGPT will replace developers," sub-niche applications like PDF KV extraction, one-off products built on a single capability gap. |

**Heuristic** Spend 60% of learning time on durable + slow-moving, 30% on fast-moving, 10% on hype. The temptation is the inverse.

## **3\. Comfort with obsolescence**

Your current stack will be partially dead in 18 months. That is normal and acceptable. The skill that does not die is the ability to evaluate, adopt, and discard tools quickly. Treat each tool as a hypothesis, not an identity. Engineers who tie their identity to a framework ("I am a Spark engineer") suffer more during transitions than engineers who tie it to a domain ("I build large-scale data systems").

## **4\. Ship to learn**

Reading about RAG does not teach you RAG. Building a retrieval system, watching it fail on edge cases, debugging the chunking strategy, and measuring the impact on answer quality teaches you RAG. The ratio should be roughly one hour of building per hour of consumption. Tutorial-only learning produces fluent talkers and poor builders.

## **5\. Build evaluation skill before building taste**

In a field where everything claims state-of-the-art, the rare skill is judging what is actually better. Learn evaluation methodology early: how to design a benchmark, what makes a metric trustworthy, why offline metrics drift from online behavior, and how to detect when a paper is overclaiming. Evaluation is the moat. Anyone can train a model; few can tell you if it is good.

## **6\. T-shaped depth**

Go deep in one area (say, retrieval systems, or training infrastructure, or evaluation, or alignment). Stay broadly aware of the rest. Pure breadth makes you a commodity who can speak about everything and ship nothing. Pure depth makes you fragile if your specialty commoditizes. The T-shape lets you ship in your area and converse credibly across the rest.

## **7\. Compound over sprint**

One paper per week for a year beats a 30-paper binge in March followed by nothing. The field is a marathon of marathons. Build a schedule you can sustain at week 50, not week 2.

**PART II**

**A Framework for Staying Current**

Mindset without a system collapses under information overload. Below is a concrete, repeatable framework. It has five components: a filter for incoming tech, an information diet, a weekly loop, a quarterly audit, and a list of anti-patterns.

## **Component 1 - The three-question filter**

Before investing time in any new tool, technique, or trend, ask three questions in order. If you cannot answer them, you are not ready to invest time.

- Is this a new capability or a better implementation of an existing one? New capabilities are rare and worth chasing (e.g., transformers in 2017, in-context learning in 2020, function calling in 2023). Better implementations matter less and can be picked up reactively when you need them.
- What is this commoditizing, and what layer above it is now more valuable? When LLMs commoditized text generation, the layer above (evaluation, retrieval, agent design, product UX) became more valuable. When KV extraction got commoditized by LLMs, the layer above (document understanding workflows, structured output, hallucination control) became more valuable. Always ask: where did the value migrate to?
- Will the underlying problem still exist in three years? If yes, invest. If no, ignore. Problems persist; solutions rotate.

**Worked example** "Should I learn LangChain deeply?" Q1: not a new capability, just an orchestration layer. Q2: commoditizing glue code, value migrates to evaluation + retrieval + system design. Q3: problem (composing LLM calls) will exist, but the specific tool likely won't. Verdict: know it well enough to ship, don't build identity around it.

## **Component 2 - Information diet**

Curate sources by signal-to-noise ratio. Re-evaluate quarterly.

### **High signal (read regularly)**

- arXiv listings: cs.CL, cs.LG, cs.AI - scan abstracts daily, read 1-2 papers per week.
- Hugging Face Daily Papers - community-curated, surfaces what practitioners actually care about.
- Anthropic, OpenAI, DeepMind, Google Research, Meta AI engineering blogs - slow, but each post is high-signal.
- Sebastian Raschka's Ahead of AI, Andrew Ng's The Batch, Jack Clark's Import AI, Latent Space - newsletters worth your inbox.
- Conference proceedings: NeurIPS, ICML, ICLR, ACL, EMNLP. Skim accepted lists; deep-read 2-3 papers per conference.

### **Moderate signal (sample selectively)**

- Twitter/X - curate a list of researchers, not influencers. Practitioners over thought-leaders.
- Podcasts: Latent Space, Dwarkesh, MLST, The Gradient. Best for long-form context on ideas.
- YouTube: Andrej Karpathy's lectures, 3Blue1Brown for math, Yannic Kilcher for paper walkthroughs.

### **Low signal (treat with caution)**

- LinkedIn posts, product demo threads, "X is dead" hot takes, VC commentary on technical merit.
- Tool-vendor benchmarks where the vendor's own tool wins.
- Anything that goes viral on day one - wait six weeks and re-evaluate.

## **Component 3 - The weekly learning loop**

A fixed weekly rhythm beats motivation-driven learning. The minimum effective dose:

| **Day**        | **Time** | **Activity**                                                                                                                     |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Monday**     | 45 min   | Scan. Skim arXiv listings, newsletters, paper titles. Bookmark 2-3 items for the week. Don't read deeply yet.                    |
| **Wed/Thu**    | 90 min   | Deep dive. Read one paper or technical blog properly. Take notes in your own words. If you can't explain it after, re-read.      |
| **Weekend**    | 2-3 hrs  | Build. Implement something from the week's learning. A notebook, a tiny replication, a tool, an experiment. Ship it (commit it). |
| **Continuous** | -        | Teach. Write a short note, a tweet, a Slack post, a Loom - explaining what you learned. Teaching exposes gaps.                   |

**Rule of three** Scan, dive, build. If you do all three on one topic in a week, you actually learned it. If you only scanned, you didn't.

## **Component 4 - The quarterly obsolescence audit**

Every 90 days, sit down for one hour and answer:

- What did I invest learning time in this quarter?
- For each item, is it: still useful / partially useful / dead?
- Which sources gave me signal? Which gave me noise? Drop the noisy ones.
- What problem in the field did I underestimate? What did I overestimate?
- Where did value migrate to that I missed?

The audit is uncomfortable on purpose. It forces honesty about wasted effort and recalibrates the next quarter. Engineers who do this audit consistently look prescient five years in; engineers who don't accumulate dead skills.

## **Component 5 - Anti-patterns to avoid**

- Tool-hopping: switching frameworks every quarter without shipping anything in any of them.
- Tutorial hell: completing courses and notebooks without ever building from a blank file.
- FOMO learning: chasing every new model release; you cannot keep up and you don't need to.
- Reading without building: papers without code are mythology.
- Building without measuring: shipping a RAG system without an eval set is a vibe, not engineering.
- Identity capture: "I am a \[framework\] developer." You are an engineer who solves problems, frameworks rotate.
- Demo-driven learning: judging tech by polished demos rather than your own boring experiments.

## **Building moats that don't go obsolete**

As specific skills churn, certain capabilities compound and protect you across cycles. Invest disproportionately in these:

- Evaluation skill. Can you tell good from bad systematically? This is the rarest skill in AI engineering.
- System design intuition. Latency, cost, failure modes, scaling - these transfer across every model generation.
- Domain depth × AI. Healthcare + AI, legal + AI, finance + AI, manufacturing + AI. The domain anchor outlasts model versions.
- Speed of shipping. Building a working v1 in a week beats a perfect v1 in three months, every time.
- A network of practicing engineers. Most real signal travels through people, not blogs.
- Writing. People who write get pulled into the rooms where decisions happen.

**PART III**

**The Tiered Curriculum**

The curriculum is organized as seven tiers. Each tier produces a tangible capability. A placement test at intake lets experienced engineers skip tiers they have already mastered. Each tier ends with a mini-project; the program ends with a capstone.

Time estimates assume 6-8 hours per week. Compress or expand based on cohort needs.

**TIER 0**

**Prerequisites**

_2-3 weeks · Skippable for experienced developers_

| **Python for data**  | NumPy, Pandas, Matplotlib, virtualenv / uv, Jupyter, basic profiling.                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Math essentials**  | Linear algebra (vectors, matrices, eigenvectors), calculus (gradients, chain rule), probability and statistics (distributions, Bayes, hypothesis testing), information theory (entropy, KL divergence). |
| **Software hygiene** | Git, type hints, testing, logging, reproducibility - seeds, lockfiles, deterministic data splits.                                                                                                       |
| **Mini-project**     | A reproducible notebook that loads a public dataset, computes descriptive statistics, and produces three publication-quality plots.                                                                     |

**TIER 1**

**Classical Machine Learning Foundations**

_3-4 weeks_

| **The ML workflow**       | Problem framing, train/val/test splits, leakage, cross-validation, baselines.                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Supervised learning**   | Linear & logistic regression, SVMs, decision trees, random forests, gradient boosting (XGBoost / LightGBM).        |
| **Unsupervised learning** | k-means, hierarchical clustering, PCA, t-SNE, UMAP.                                                                |
| **Feature engineering**   | Encoding, scaling, target leakage, handling imbalanced data, missingness.                                          |
| **Evaluation**            | Precision, recall, F1, ROC-AUC, PR curves, calibration, RMSE/MAE, confusion matrices.                              |
| **Theory**                | Bias-variance tradeoff, regularization (L1/L2), hyperparameter tuning, the curse of dimensionality.                |
| **Mini-project**          | A tabular ML project end-to-end on a real dataset - including a written analysis of why a chosen baseline matters. |

**TIER 2**

**Deep Learning**

_4-5 weeks_

| **Neural network mechanics** | Forward pass, backpropagation, autograd, gradient flow problems.                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Framework fluency**        | PyTorch deeply; TensorFlow at survey level.                                                             |
| **Optimization**             | SGD, Adam, AdamW, learning rate schedulers, gradient clipping, mixed precision training.                |
| **Regularization**           | Dropout, batch / layer norm, data augmentation, early stopping, label smoothing.                        |
| **Architectures**            | MLPs, CNNs (ResNet), RNN/LSTM/GRU, attention, Transformers - implemented from scratch.                  |
| **Training at scale**        | Distributed training, DDP, FSDP, gradient checkpointing, profiling, fault recovery.                     |
| **Mini-project**             | Train an image classifier and a small transformer from scratch. Reproduce a published number within 5%. |

**TIER 3**

**Modern AI & Large Language Models**

_5-6 weeks · The current center of gravity_

| **Transformer internals**                | Attention mechanics, KV cache, positional encodings (RoPE, ALiBi), tokenization (BPE, SentencePiece).                                         |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pretraining concepts**                 | Scaling laws, data curation, compute economics, mixture-of-experts.                                                                           |
| **Fine-tuning**                          | Full SFT, LoRA, QLoRA, PEFT, instruction tuning. When each makes sense.                                                                       |
| **Alignment**                            | RLHF, DPO, constitutional AI, reward modeling, the failure modes of each.                                                                     |
| **Prompt engineering**                   | Few-shot, chain-of-thought, structured outputs (JSON, schemas), function/tool calling.                                                        |
| **Retrieval-augmented generation (RAG)** | Chunking strategies, embeddings, vector DBs (FAISS, Qdrant, pgvector), hybrid retrieval, reranking, multi-segment retrieval, query rewriting. |
| **Agents**                               | Tool use, planning loops, ReAct, multi-agent patterns, memory architectures.                                                                  |
| **Evaluation**                           | LLM-as-judge, eval harnesses, hallucination detection, RAG-specific metrics (faithfulness, context precision, answer relevance).              |
| **Inference optimization**               | Quantization (GGUF, AWQ, GPTQ), speculative decoding, vLLM, continuous batching, KV cache management.                                         |
| **Mini-project**                         | Build a production-grade RAG system on a real corpus with a documented eval set and a measured baseline-to-final improvement.                 |

**TIER 4**

**MLOps & Production**

_3-4 weeks_

| **Experiment tracking** | MLflow, Weights & Biases. Why naming experiments matters more than people think.                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Versioning**          | Data and model versioning (DVC), model registries.                                                                 |
| **Serving**             | FastAPI, TorchServe, Triton, ONNX, BentoML, vLLM for LLM serving.                                                  |
| **Deployment patterns** | Shadow deployments, canary, A/B testing, blue-green, feature flags for models.                                     |
| **Monitoring**          | Data drift, concept drift, prediction drift, latency, cost, LLM-specific observability (Langfuse, Arize, Phoenix). |
| **Data pipelines**      | Feature stores, orchestration (Airflow, Prefect, Dagster), batch vs streaming.                                     |
| **Infrastructure**      | Docker, Kubernetes, GPU scheduling, autoscaling, spot-instance economics.                                          |
| **Cost engineering**    | Token budgets, semantic caching, prompt compression, model routing, distillation.                                  |
| **Mini-project**        | Deploy the Tier 3 RAG system with monitoring, drift detection, and a documented rollback procedure.                |

**TIER 5**

**System Design for AI Products**

_2-3 weeks_

| **End-to-end system design**    | Designing chatbots, search systems, recommendation engines, document-understanding pipelines.                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tradeoffs**                   | Latency vs accuracy vs cost. When to use a small model, when to use a frontier model, when to use both.                                             |
| **Multi-modal pipelines**       | Vision + language, audio + language, structured data + language.                                                                                    |
| **Caching**                     | Exact-match, semantic, prompt caching, result caching with TTLs.                                                                                    |
| **Privacy-preserving patterns** | On-device, federated learning, air-gapped deployments, data residency.                                                                              |
| **Reliability**                 | Guardrails, fallback chains, circuit breakers, graceful degradation, retry policies for LLM calls.                                                  |
| **Mini-project**                | Write a design doc for a real AI product - covering architecture, evaluation, cost, failure modes, and an honest list of what you would skip in v1. |

**TIER 6**

**Responsible AI**

_2 weeks · Threaded through every tier in practice_

| **Fairness & bias** | Auditing methodology, dataset documentation (datasheets, model cards), known failure modes.                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Privacy**         | Differential privacy basics, PII handling, GDPR, data minimization, right to deletion.                               |
| **Security**        | Prompt injection, jailbreaks, data exfiltration via output channels, model theft, supply chain.                      |
| **Explainability**  | SHAP, LIME, attention analysis, counterfactual explanations, when each is meaningful and when it's theater.          |
| **Red-teaming**     | Adversarial testing methodology, internal red teams, structured probing of model behaviors.                          |
| **Mini-project**    | Red-team your Tier 3 system. Find five distinct failure modes. Mitigate two. Document the rest as known limitations. |

**CAPSTONE**

**Production AI Product**

_4 weeks_

Build one production-quality AI system end-to-end. The system must include: a defensible problem statement, an evaluation set built before any modeling, a baseline, a final system with measured improvement over baseline, monitoring, a rollback plan, a written design doc, and a red-team report. Present to peers and external reviewers.

## **Cross-cutting tracks (run continuously)**

- Paper reading club: one paper per week, summarized in your own words. The summary is the artifact, not the read.
- Code review: every project gets reviewed by a peer. ML-specific debugging (shape mismatches, silent NaNs, training instability, data leakage) requires its own muscle.
- Writing: every learner publishes at least one technical post per tier. Internal blog, Medium, personal site - the venue matters less than the act.
- Portfolio: GitHub hygiene, README quality, a personal site with three flagship projects.

## **Suggested cadences**

| **Cadence**               | **Hours/week** | **Duration** |
| ------------------------- | -------------- | ------------ |
| **Intensive (full-time)** | 30-40          | 12 weeks     |
| **Standard (part-time)**  | 6-10           | 6 months     |
| **Sustainable**           | 3-5            | 12 months    |

## **Closing note**

A training program is only as good as what learners can build on their own afterwards. The mindset and framework in Parts I and II are the actual deliverable. The curriculum in Part III is scaffolding. By month 18, half of Part III will be partially outdated; by month 36, more. Parts I and II will still be working.

That is by design. Teach learners to renew their own curriculum, and the program never goes stale.