---
marp: false
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
_(he/him) - ![icon](../../images/email.png) [_j1c_@jhu.edu_](mailto:j1c@jhu.edu)
[NeuroData lab](https://neurodata.io/)_
_Johns Hopkins University - Biomedical Engineering_
![icon](../../images/email.png) [_j1c_@jhu.edu_](mailto:j1c@jhu.edu)
![icon](../../images/github.png) [_@j1c (Github)_](https://github.com/j1c)
![icon](../../images/twitter.png) [_@j1c (Twitter)_](https://twitter.com/j1c)


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
- Example:

---

# Brains as connectomes
(aka networks or graphs)

- Vertex = a region of interest
- Edges = connectivity measure between a pair of vertices
- Diffusion MRI = # of estimated neuronal fibers

---
# Connectome Generation

![center](./../../images/m2g-pipeline.pdf)

Source: https://www.biorxiv.org/content/biorxiv/early/2021/11/03/2021.11.01.466686.full.pdf


---
# Overall DAG

Insert dag

---
# Subject specifig DAGs

Insert 4 Dags

---
# Statistical problem
- Want an independence test!
- $H_0: F(Genome, Connectome) = F(Genome)F(Connectome)$
  $H_A: F(Genome, Connectome) \neq F(Genome)F(Connectome)$

- Distance correlation test statistics

---

# Human Connectome Project
-

---
# Assumptions
- Only 2 children per family
- Only identical twins, fraternal twins, non-twin siblings

---
# Monozygotic vs Dizygotic
- Assumptions:
  - Controls environment variable

Insert figure

---
# All three groups
- Assumptions:
  - Add in environmental and genetic variance

Insert figure

---
# Neuroanatomy Mediator

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