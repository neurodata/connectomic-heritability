---
marp: true
theme: slides
size: 16:9
paginate: false
---

<style scoped>
p {
    font-size: 24px;
}
</style>

# Heritability of Human Structural Connectomes

## Jaewon Chung

_(he/him)_ - [NeuroData lab](https://neurodata.io/)
_Johns Hopkins University - Biomedical Engineering_

![icon](../../images/mail.png) [_j1c@jhu.edu_](mailto:j1c@jhu.edu)
![icon](../../images/github.png) [_@j1c (Github)_](https://github.com/j1c)
![icon](../../images/twitter.png) [_@j1c (Twitter)_](https://twitter.com/j1c)

![bg right:45% w:500](./../../images/nd_logo_small.png)

---

# Outline

- Background
  - **What is heritability?**
  - Graphs, networks, connectomes
  - Where do connectomes come from?
- Problem
  - What are we trying to estimate?
  - Causal models
  - Dcorr
  - Distance functions
- Results
  - Dataset
  - Results 1
  - Results 2
  - Results 3

---

# What is heritability?

- Variations in phenotype caused by variations in genotype.
- Potentially discover relationships between diseases and genetics

Are the brain connectivity patterns heritable?

---

# Brains connectivity as connectomes

(aka networks or graphs)

- Vertex = a region of interest
- Edges = connectivity measure between a pair of vertices
- Diffusion MRI = # of estimated neuronal fibers
- Undirected = Edges have no direction

![center](./../../images/what_is_network.png)

<footer>
Image from Gu, Zijin, et al. "Heritability and interindividual variability of regional structure-function coupling." (2021)
</footer>

---

# Connectome Generation

![center](./../../images/m2g_pipeline.pdf)

---

# Overall DAG

![center](./../../images/dag.svg)

---

# Statistical problem

- Want an independence test!
- $H_0: F(Genome, Connectome) = F(Genome)F(Connectome)$
  $H_A: F(Genome, Connectome) \neq F(Genome)F(Connectome)$

- Test statistic: Distance correlation

---

# Statistical problem

- Want an independence test!
- $H_0: F(Genome, Connectome|Covariates) = F(Genome|Covariates)F(Connectome|Covariates)$
  $H_A: F(Genome, Connectome|Covariates) \neq F(Genome|Covariates)F(Connectome|Covariates)$

- Test statistic: Conditional distance correlation

---

# Distance Correlations

- Require distance functions

- Genetic distances
- Connectome distances $||X - YR||_F$

---

# Human Connectome Project

- Demographics:
  Van Essen, David C., et al., The WU-Minn human connectome project: an overview (2013)

---

# Monozygotic vs Dizygotic

- Assumptions:
  - Controls environment variable

Insert figure

---

# Why compare siblings and twins?

---

# All three groups

- Assumptions:
  - Add in environmental and genetic variance

Insert figure

---

# Neuroanatomy (effect mediator)

Test the existence of arrow

---

# Conditional Test as causal effect estimator

- Using conditional distance correlation

---

# The End

---

Additional slides

---

# Information on Distance Correlation

---

# Shortcomings

- Network models
- Problems with connectome estimation.
- dominant genetic effects and epistasis.
- No interaction between environment and genetics

---

# Environemtal effects

- Shared
  - Common experiences of siblings living in the same household.
    - household income, the family’s living situation, the dynamics between the parents, food consumed
- Non-shared
  - Everything else
  - Epigenetics
  - Luck
  - schools, peers

---
