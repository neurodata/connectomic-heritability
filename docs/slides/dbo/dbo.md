---
marp: true
theme: slides
size: 16:9
paginate: true
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
- Potentially discover relationships between diseases and genetics.

 <br> <br> <br>

<style scoped>
h2 {
    justify-content: center;
    text-align: center;
}
</style>


## Are the brain connectivity patterns heritable?

---

# Brains connectivity as connectomes
<!-- (aka networks or graphs) -->

<div class="columns">
<div>

- Vertex: region of interest
- Edges: connectivity measure between a pair of vertices
- Diffusion MRI: # of estimated neuronal fibers
- Undirected: neurons have no direction

</div>
<div>

![center h:500](./../../images/what_is_network.png)

</div>

<footer>
Image from Gu, Zijin, et al. "Heritability and interindividual variability of regional structure-function coupling." (2021)
</footer>

---

# How do we get structural connectomes?

<br>

![center](./../../images/m2g_pipeline.png)

---

# Heritability as causal problem

![center h:500](./../../images/dag.svg)

---

# Do genomes affect connectomes?

- Hypothesis:
  $H_0: F($<span style="color: var(--connectome)">Connectome</span>|<span style="color: var(--genome)">Genome</span>$) = F($<span style="color: var(--connectome)">Connectome</span>$)$
  $H_A: F($<span style="color: var(--connectome)">Connectome</span>|<span style="color: var(--genome)">Genome</span>$) \neq F($<span style="color: var(--connectome)">Connectome</span>$)$

- Alternatively:
  $H_0: F($<span style="color: var(--connectome)">Connectome</span>, <span style="color: var(--genome)">Genome</span>$) = F($<span style="color: var(--connectome)">Connectome</span>$)F($<span style="color: var(--genome)">Genome</span>$)$
  $H_A: F($<span style="color: var(--connectome)">Connectome</span>, <span style="color: var(--genome)">Genome</span>$) \neq F($<span style="color: var(--connectome)">Connectome</span>$)F($<span style="color: var(--genome)">Genome</span>$)$

- Known as independence testing
- Test statistic: *distance correlation (dcorr)*

---

# What is distance correlation?

- Measures dependence between two multivariate quantities.
  - For example: connectomes, genomes.
- Can detect nonlinear associations.
- Measures correlation between pairwise distances.


![center w:800](./../../images/unconditional_test.png)

---

# How to compare genomes?
- Typical twin studies do not sequence genomes.
- Coefficient of kinship ($\phi_{ij}$)
  -  Probabilities of finding particular genes as identical among subjects.

- d(<span style="color: var(--genome)">Genome</span>$_i$, <span style="color: var(--genome)">Genome</span>$_j$) = 1 - 2\phi_{ij}$.

---

# How to compare connectomes?
- Statistical modelling of connectomes!
-

- d(<span style="color: var(--connectome)">Connectome</span>$_i$, <span style="color: var(--connectome)">Connectome</span>$_j$) = $||X^{(i)} - X^{(j)}R||_F$

Insert picture of rdpg embeddings

---

# Human Connectome Project

- Brain scans from identical (monozygotic), fraternal (dizygotic), non-twin siblings.

![center w:500](./../../images/hcp_demographics.svg)


<footer>
Van Essen, David C., et al., The WU-Minn human connectome project: an overview (2013)
</footer>

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

# Neuroanatomy (effect mediator)

- Literature show neuroanatomy (e.g. brain volume) is highly heritable.
- Want to test:
  $H_0: F($<span style="color: var(--neuroanatomy)">Neuroanatomy</span>, <span style="color: var(--genome)">Genome</span>$) = F($<span style="color: var(--neuroanatomy)">Neuroanatomy</span>$)F($<span style="color: var(--genome)">Genome</span>$)$
  $H_A: F($<span style="color: var(--neuroanatomy)">Neuroanatomy</span>, <span style="color: var(--genome)">Genome</span>$) \neq F($<span style="color: var(--neuroanatomy)">Neuroanatomy</span>$)F($<span style="color: var(--genome)">Genome</span>$)$

---

# New DAG

One with neuroanatomy

---

# Statistical problem

- Want a conditional independence test!
  $H_0: F($<span style="color: var(--connectome)">Conn.</span>, <span style="color: var(--genome)">Genome</span>|<span style="color: var(--neuroanatomy)">Neuro.</span>$) = F($<span style="color: var(--connectome)">Conn.</span>|<span style="color: var(--neuroanatomy)">Neuro.</span>$)F($<span style="color: var(--genome)">Genome</span>|<span style="color: var(--neuroanatomy)">Neuro.</span>$)$
  $H_A: F($<span style="color: var(--connectome)">Conn.</span>, <span style="color: var(--genome)">Genome</span>|<span style="color: var(--neuroanatomy)">Neuro.</span>$) \neq F($<span style="color: var(--connectome)">Conn.</span>|<span style="color: var(--neuroanatomy)">Neuro.</span>$)F($<span style="color: var(--genome)">Genome</span>|<span style="color: var(--neuroanatomy)">Neuro.</span>$)$

- Test statistic: Conditional distance correlation (cdcorr)

---

# What is conditional distance correlation?

- Augment distance correlation procedure with third distance matrix.
- d(<span style="color: var(--neuroanatomy)">Neuroanatomy</span>$_i$, <span style="color: var(--neuroanatomy)">Neuroanatomy</span>$_j$) = ||<span style="color: var(--neuroanatomy)">Neuroanatomy</span>$_i$ - <span style="color: var(--neuroanatomy)">Neuroanatomy</span>$_j$||$_F$

<br>

![center h:350](./../../images/conditional_test.png)

---

# Conditional Test as causal effect estimator

-

---

# Summary
![center h:250](./../../images/genome_to_connectome.png)

- Present a causal model for heritability of connectomes.
- Leveraged recent advances:
  1. Statistical models for networks, allowing meaningful comparison of connectomes.
  2. Distance and conditional distance correlation as test statistic for causal analysis$^1$.


<footer>

$^1$ Bridgeford, Eric W., et al. "Batch Effects are Causal Effects: Applications in Human Connectomics."  (2021).

</footer>

---
# Acknowledgements

#### Team

<style scoped>

p {
    font-size: 24px;
}
</style>


<div class='minipanels'>

<div>

![person](./../../images/people/mike-powell.jpg)
Mike Powell

</div>

<div>

![person](./../../images/people/bridgeford.jpg)
Eric Bridgeford

</div>

<div>

![person](./../../images/people/priebe_carey.jpg)
Carey Priebe

</div>

<div>

![person](./../../images/people/vogelstein_joshua.jpg)
Joshua Vogelstein

</div>
</div>

---


<style scoped>
h1 {
    justify-content: center;
    text-align: center;
}
</style>

<br> <br> <br> <br> <br>

# Additional slides

---

# Shortcomings - Network model
- Problems with connectome estimation.
  - Inability to determine the precise origin/termination of connections in the cortex.
    - -> false negatives
  - Crossing fibers
    - -> false positives
- RDPG can only represent subset of independent edge networks.

![center h:300](./../../images/network_models.png)

---

# Shortcomings - Model assumptions
- No interaction between genome and environment
- No epistatsis
  - Effect of one gene is dependent on another
  - Ex: black hair and baldness
- No dominance effects
- Strong assumptions in genetic distances

---

# What are environemtal effects?

- Shared
  - Common experiences of siblings living in the same household.
    - household income, the family’s living situation, the dynamics between the parents, food consumed
- Non-shared
  - Everything else
  - Epigenetics
  - Luck
  - schools, peers

---

# Random dot product graphs



---


---



---