---
marp: true
theme: poster
paginate: false
size: a0
math: katex
---

<!-- Start header -->
<div class="header">

<!-- Image in the upper left -->
<div>

![headerlogo](./images/hopkins-logo.png)

</div>

<!-- Title and author information -->
<div>

# Statistical Modeling of Structural Connectomes Reveal High Genetic Influence on Connectivity

## Jaewon Chung<span class=super>1\*</span>, Eric Bridgeford<span class=super>1</span>, Michael Powell<span class=super>1</span>, Joshua T. Vogelstein<span class=super>1</span>

##### 1 - Johns Hopkins University, $\ast$ - correspondence: ![icon](./images/email.png) [_j1c@jhu.edu_](mailto:j1c@jhu.edu) ![icon](./images/github.png) [_@j1c(Github)_](https://github.com/j1c) ![icon](./images/twitter.png) [_@j1chung(Twitter)_](https://twitter.com/j1chung)

</div>

<!-- Image on the upper right -->
<div>

![headerlogo](./images/nd_logo.png)

</div>

<!-- End header -->
</div>

<!-- Summary box title -->

<span class='h3-noline'> Summary </span>

<!-- Summary box using 5 columns-->
<div class='box'>
<div class="columns-box">

<!-- Box col1 -->
<div>

- Aimed to define heritability for populations of connectomes using statistical modelling.

</div>
<div>

- Structural connectomes are heritable without controlling for neuroanatomy.
- Neuroanatomy is also highly heritable

</div>
<div>

- Connectomes remain heritable after controlling for effects of neuroanatomy on connectomes.

</div>
<div>

- Provide tools for future analysis on populations of connectomes.

</div>

<!-- End columns-box -->
</div>
<!-- End box -->
</div>

<!-- Start main 2 column split for poster -->
<div class="columns-main">

<!-- Start main column 1 -->
<div>

### Motivation

- Understanding how brain connectivity is influenced by genetics can improve our understanding of brain function and diseases.
- Current methods of analyzing connectomes or hertability exhibit limitations:
  - Selection Graph theoretic features
  - Multivariate normality assumptions

### Overview of Analysis

<!-- Big question for this work -->

![](./ohbm22/overview.png)
**Fig 1:** Overview of the framework for measuring heritability of connectomes.

<br>

## Do changes in <span style="color:var(--genome)"> genome </span> cause changes in <span style="color:var(--connectome)">connectomes</span>?

<br>

### Causal Analysis of Effect of Genome on Connectomes

<!-- ![w:1100px center](./ohbm22/dag.png) -->

- Genome directly affects the structural connectome.
- Neuroanatomym (e.g. brain volume) indirectly affects the connectome.
- Participant history, such as the shared and non-shared environmental influences, and traits are potential confounders.
- The shared and non-shared environment is controlled by comparing between the same sex individuals.

![center](./ohbm22/dag.png)
**Fig 2:** Directed acyclic graph (DAG) illustrating potential relationships between the genome and connectome.

### Human Connectome Project 1200

- Structural connectomes are estimated using structural (sMRI) and diffusion magnetic resonance imaging (dMRI).
- Processed with _m2g_ pipeline, which uses Constrained Spherical Deconvolution (CSD) model and deterministic tractography.

|            | Monozygotic  |  Dizygotic  | Non-twin siblings |
| :--------: | :----------: | :---------: | :---------------: |
|     N      |     322      |     212     |        490        |
|    Sex     | 196 F, 126 M | 125 F, 87 M |   237 F, 253 M    |
| Age (mean) |  29.6 (3.3)  | 28.9 (3.4)  |    28.3 (3.9)     |

<div align="center">

**Table 1:** Participants and their demographics of HCP1200 Dataset.

</div>
<!-- End main column 1 -->
</div>

<!-- Start main column 2 -->
<div>

### Three Models of Connectomes

- **Exact:** Are the generative models of connectomes the same?
- **Global scale:** Are the generative models same after considering global scaling?
- **Vertex scale:** Are the generative models same after considering vertex wise scaling?

![](./ohbm22/Illustrative_example.png)
**Fig 3:** Examples of the three different models (exact, global scale, and vertex scale) of connectome heritability visualized as adjacency matrices.

<br>

### Connectome Validation and Heritability of Neuroanatomy

![](./ohbm22/results_ohbm_1.png)
**Fig 4:** Validating connectomes by comparing monozygotic and dizygotic twins using Kolmogrov-Smirnov test. Heritability of neuroanamy is tested using unconditional test framework. Red squares indicate significant tests; blue indicate non-significant tests.

### Tests for Heritability of Connectomes

![](./ohbm22/results_ohbm.png)
**Fig 5:** Testing for unconditional and conditional heritability of connectomes. Red squares indicate significant tests; blue indicate non-significant tests.

### Limitations and extensions

- Other staitsical models to consider (e.g. COSIE [3])
- Repeated analysis on functional MRI or in other twin study datasets.

<!-- Code/Refs/Thanks/Funding - small section -->

###

<div class="columns2">
<div>

#### Code

<div class="columns3-np">
<div>

<!-- Logo for a package -->

![left h:1in](./ohbm22/graspologic-logo.svg)

</div>
<div>

<!-- Badges for a package -->

[![h:.4in](https://pepy.tech/badge/graspologic)](https://pepy.tech/project/graspologic)
[![h:.4in](https://img.shields.io/github/stars/microsoft/graspologic?style=social)](https://github.com/microsoft/graspologic)

</div>
<div>

<!-- QR code to a package -->

![center h:1in](./ohbm22/graspologic-qr.svg)

</div>
</div>

<div class="columns3-np">
<div>

<!-- Logo for a package -->

<p style="text-align: center;">

**hyppo**

</p>

</div>
<div>

<!-- Badges for a package -->

[![h:.4in](https://pepy.tech/badge/hyppo)](https://pepy.tech/project/hyppo)
[![h:.4in](https://img.shields.io/github/stars/neurodata/hyppo?style=social)](https://github.com/neurodata/hyppo)

</div>
<div>

<!-- QR code to a package -->

![center h:1in](./ohbm22/hyppo-qr.svg)

</div>
</div>

<br>

#### Acknowledgements

<footer>
NeuroData lab for many ideas and feedback. Many at Microsoft Research for w/ graspologic.
</footer>

</div>
<div>

#### References

<!-- Need these breaks <br> between refs otherwise formatting breaks for some reason -->
<footer>
[1] Chung et al. "Connectomic Heritability," In preparation (2022)
<br>
[2] Chung et al. "Statistical connectomics," Ann. Rev. Statistics and its Application (2021)
<br>
[3] Arroyo et al. "Inference for multiple heterogeneous networks with a common invariant subspace," JMLR (2021)
</footer>

#### Funding

<footer>
J.C. supported by the BRAIN Initiative (1RF1MH123233). J.T.V. supported by NSF CAREER Award (1942963). Findings and conclusions expressed are  those of the authors and not necessarily those of the funders.
</footer>

</div>
</div>

<!-- End main column 2 -->
</div>

<!-- End main columns -->
</div>
