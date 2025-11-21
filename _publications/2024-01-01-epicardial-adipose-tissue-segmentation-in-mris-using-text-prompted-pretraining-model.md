---
title: "Epicardial Adipose Tissue Segmentation in MRIs Using Text-Prompted Pretraining Model"
collection: publications
category: conferences
permalink: /publication/2024-01-01-epicardial-adipose-tissue-segmentation-in-mris-using-text-prompted-pretraining-model
date: 2024-12-02
venue: '2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)'
citation: 'Huping Ye, Yushan Deng, Yi Hong. "Epicardial Adipose Tissue Segmentation in MRIs Using Text-Prompted Pretraining Model." 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024.'
doi: 10.1109/bibm62325.2024.10822506
excerpt: 'Text-prompted SAM adaptation for epicardial adipose tissue segmentation on cardiac MRI with scarce labels.'
bibtex: |
  @inproceedings{ye2024epicardial,
      author = "Ye, Huping and Deng, Yushan and Hong, Yi",
      title = "Epicardial Adipose Tissue Segmentation in MRIs Using Text-Prompted Pretraining Model",
      booktitle = "2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)",
      pages = "7021--7028",
      year = "2024",
      organization = "IEEE"
  }
---

Abstract: This paper addresses the challenge of segmenting the epicardial adipose tissue (EAT) in MRI scans, a critical aspect in cardiac-related clinical diagnosis, treatment, and evaluation of cardiovascular diseases. Despite the abundance of research focusing on CT images, studies on MRI segmentation are relatively scarce and are hindered by limited datasets for EAT segmentation. Existing models, such as the Segment Anything Model (SAM) family, provide a way to leverage existing related datasets and have shown promising results in various segmentation tasks. However, there is a significant gap between the general SAM models and our domain-specific task, resulting in unsatisfied performance on segmenting EAT. To address this, we adopt the SAM design but adapt it to our task using text prompts, resulting in a vision-language pretraining model for cardiac segmentation, especially for segmenting EAT. We utilize multiple publicly available cardiac-related medical datasets for pretraining and then fine-tune our model on a small EAT dataset. Additionally, we propose a pseudo-mask augmentation strategy to further mitigate the issue of limited EAT segmentation masks. Extensive experimental results demonstrate the effectiveness of our proposed model, achieving the best performance on EAT segmentation compared to recent baseline methods. Our source code and pre-trained model will be publicly available later.
