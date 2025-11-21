---
title: "DiffLGE: Diffusion-Based Image Generation for Synthesizing Late Gadolinium Enhancement Scans"
collection: publications
category: conferences
permalink: /publication/2024-01-01-difflge-diffusion-based-image-generation-for-synthesizing-late-gadolinium-enhancement-scans
date: 2024-12-01
venue: '2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)'
citation: 'Yushan Deng, Yuqiu Jiang, Yi Hong. "DiffLGE: Diffusion-Based Image Generation for Synthesizing Late Gadolinium Enhancement Scans." 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024.'
doi: 10.1109/bibm62325.2024.10821814
excerpt: 'Diffusion model to synthesize high-quality LGE CMR without gadolinium by conditioning on CINE and T1 mapping.'
bibtex: |
  @inproceedings{deng2024difflge,
      author = "Deng, Yushan and Jiang, Yuqiu and Hong, Yi",
      title = "DiffLGE: Diffusion-Based Image Generation for Synthesizing Late Gadolinium Enhancement Scans",
      booktitle = "2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)",
      pages = "6990--6997",
      year = "2024",
      organization = "IEEE"
  }
---

Abstract: In recent years, late gadolinium enhancement (LGE) cardiac magnetic resonance (CMR) imaging synthesis using deep learning has gained attention for generating high-quality LGE images without relying on gadolinium-based contrast agents (GBCA). However, traditional methods like GANs struggle with issues such as unstable training and mode collapse, making them less reliable for clinical applications. Diffusion models have emerged as a promising alternative, offering more stable training and the capability to generate high-resolution, realistic images. In this study, we address the challenge of effectively integrating multiple noninvasive imaging modalities for LGE synthesis by proposing DiffLGE, a novel method based on diffusion models that leverages both CINE and T1 mapping data. Utilizing the stable diffusion framework, we condition the generative network on CINE and T1 mapping inputs to achieve controlled and stable synthesis. Furthermore, we integrate a VideoMAE encoder to extract and enhance CINE features, which are often challenging to incorporate due to their dynamic nature. Trained on a private dataset of 240 samples from 83 subjects, our approach outperforms existing image generation methods, producing high-quality LGE images and offering a more reliable and accurate solution for LGE image synthesis.
