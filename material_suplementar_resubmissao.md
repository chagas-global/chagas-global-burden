---
dcterms.date: 2025-10-26
generator: quarto-1.7.32
lang: en
title: Age-Related Distribution of Chagas Disease Clinical Forms
viewport: width=device-width, initial-scale=1.0, user-scalable=yes
---

::: {#quarto-content .page-columns .page-rows-contents .page-layout-article}
::: {#quarto-margin-sidebar .sidebar .margin-sidebar}
## Table of contents {#toc-title}

-   [Introduction](#introduction){#toc-introduction .nav-link .active
    scroll-target="#introduction"}
    -   [Load Packages](#load-packages){#toc-load-packages .nav-link
        scroll-target="#load-packages"}
    -   [Data Preparation](#data-preparation){#toc-data-preparation
        .nav-link scroll-target="#data-preparation"}
    -   [Multinomial Regression
        Model](#multinomial-regression-model){#toc-multinomial-regression-model
        .nav-link scroll-target="#multinomial-regression-model"}
    -   [Model Summary
        Table](#model-summary-table){#toc-model-summary-table .nav-link
        scroll-target="#model-summary-table"}
:::

::: {#quarto-document-content .content role="main"}
::: {#title-block-header .quarto-title-block .default}
::: quarto-title
# Age-Related Distribution of Chagas Disease Clinical Forms {#age-related-distribution-of-chagas-disease-clinical-forms .title}
:::

<div>

::: quarto-title-meta-heading
Published
:::

::: quarto-title-meta-contents
October 26, 2025
:::

</div>
:::
:::

::: {#introduction .section .level1}
# Introduction

This document analyzes the influence of age on the distribution of
clinical forms of Chagas disease. It is supplementary material to our
main article.

This analysis was performed using Quarto, RStudio (v2024.04.1), and R
(v4.2.2). Packages used include `VGAM`, `tidyr`, `ggplot2`, `openxlsx`,
`dplyr`, `readxl`, `gt`, and `broom`.

::: {#load-packages .section .level2}
## Load Packages {#load-packages .anchored anchor-id="load-packages"}

::: cell
Code

::: {#cb1 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
library(VGAM)
library(tidyr)
library(ggplot2)
library(openxlsx)
library(dplyr)
library(readxl)
library(gt)
library(broom)
library(forcats)
library(tidyverse)
library(readr)
library(DT)
```
:::
:::
:::

::: {#data-preparation .section .level2}
## Data Preparation {#data-preparation .anchored anchor-id="data-preparation"}

::: cell
Code

::: {#cb2 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
df <- read_excel("df_samitrop.xlsx")
```
:::
:::

::: cell
Code

::: {#cb3 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
datatable(df, options = list(scrollX = TRUE, scrollY = "300px"))
```
:::

::: cell-output-display
::: {#htmlwidget-9ae8306d277dd44c9b2e .datatables .html-widget .html-fill-item style="width:100%;height:auto;"}
:::
:::
:::
:::

::: {#multinomial-regression-model .section .level2}
## Multinomial Regression Model {#multinomial-regression-model .anchored anchor-id="multinomial-regression-model"}

::: cell
Code

::: {#cb4 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
multi_model <- vglm(
  cbind(
    sample_cardiac, 
    sample_digestive, 
    sample_mixed, 
    sample_indeterminate
  ) ~ Age_mean,
  family = multinomial(refLevel = 4),
  data = df
)
```
:::
:::
:::

::: {#model-summary-table .section .level2}
## Model Summary Table {#model-summary-table .anchored anchor-id="model-summary-table"}

::: cell
::: cell-output-display
::: {#frpcahhkvw style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;"}
  Multinomial Logistic Regression Results                                                                    
  ----------------------------------------- ------------- -------------- ------------ ------------ --------- -------
  Predicting Chagas Disease Form by Age                                                                      
  Disease Form                              Predictor     Log-Odds (β)   Odds Ratio   Std. Error   z         P
  Cardiac                                   Age_mean      0.057          1.059        0.004        16.093    0.000
  Cardiac                                   (Intercept)   −3.113         0.044        0.199        −15.651   0.000
  Digestive                                 Age_mean      0.035          1.036        0.006        5.707     0.000
  Digestive                                 (Intercept)   −3.584         0.028        0.344        −10.412   0.000
  Mixed                                     Age_mean      0.070          1.072        0.006        12.289    0.000
  Mixed                                     (Intercept)   −5.049         0.006        0.332        −15.220   0.000
  Reference category: Indeterminate                                                                          
:::
:::
:::

::: cell
Code

::: {#cb5 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
summary(multi_model)
```
:::

::: {.cell-output .cell-output-stdout}
    Call:
    vglm(formula = cbind(sample_cardiac, sample_digestive, sample_mixed, 
        sample_indeterminate) ~ Age_mean, family = multinomial(refLevel = 4), 
        data = df)

    Coefficients: 
                   Estimate Std. Error z value Pr(>|z|)    
    (Intercept):1 -3.113214   0.198909 -15.651  < 2e-16 ***
    (Intercept):2 -3.583539   0.344183 -10.412  < 2e-16 ***
    (Intercept):3 -5.049107   0.331732 -15.220  < 2e-16 ***
    Age_mean:1     0.056986   0.003541  16.093  < 2e-16 ***
    Age_mean:2     0.034992   0.006131   5.707 1.15e-08 ***
    Age_mean:3     0.069514   0.005657  12.289  < 2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Names of linear predictors: log(mu[,1]/mu[,4]), log(mu[,2]/mu[,4]), 
    log(mu[,3]/mu[,4])

    Residual deviance: 459.7913 on 51 degrees of freedom

    Log-likelihood: -352.0242 on 51 degrees of freedom

    Number of Fisher scoring iterations: 5 

    Warning: Hauck-Donner effect detected in the following estimate(s):
    '(Intercept):2', '(Intercept):3'


    Reference group is level  4  of the response
:::
:::

::: cell
Code

::: {#cb7 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
n_boot <- 1000

age_range <- seq(15, 80, length.out = 100)
novos_dados <- data.frame(Age_mean = age_range)

pred_probs <- predict(multi_model, type = "response")

row_totals <- rowSums(df[, c("sample_cardiac", "sample_digestive", "sample_mixed", "sample_indeterminate")])

boot_results <- array(NA, dim = c(length(age_range), 4, n_boot),
                      dimnames = list(NULL, c("Cardiac", "Digestive", "Mixed", "Indetermined"), NULL))

for (b in 1:n_boot) {
  
  sim_counts <- t(apply(pred_probs, 1, function(p) {
    rmultinom(1, size = row_totals[1], prob = p) 
  }))
  
  sim_counts <- matrix(NA, nrow = nrow(df), ncol = 4)
  for (i in seq_len(nrow(df))) {
    sim_counts[i, ] <- rmultinom(1, size = row_totals[i], prob = pred_probs[i, ])
  }
  
  colnames(sim_counts) <- c("sample_cardiac", "sample_digestive", "sample_mixed", "sample_indeterminate")
  
  df_sim <- df
  df_sim[, c("sample_cardiac", "sample_digestive", "sample_mixed", "sample_indeterminate")] <- sim_counts
  
  modelo_boot <- vglm(
    cbind(sample_cardiac, sample_digestive, sample_mixed, sample_indeterminate) ~ Age_mean,
    family = multinomial(refLevel = 4),
    data = df_sim
  )
  
  pred_boot <- predict(modelo_boot, newdata = novos_dados, type = "response")
  
  boot_results[,,b] <- pred_boot
}

mean_probs <- apply(boot_results, c(1,2), mean)
low_probs  <- apply(boot_results, c(1,2), quantile, probs = 0.025)
high_probs <- apply(boot_results, c(1,2), quantile, probs = 0.975)

df_pred <- data.frame(Age_mean = age_range, mean_probs)
df_low  <- data.frame(Age_mean = age_range, low_probs)
df_high <- data.frame(Age_mean = age_range, high_probs)

df_long <- df_pred %>%
  pivot_longer(-Age_mean, names_to = "Forma", values_to = "Probabilidade")
df_low_long <- df_low %>%
  pivot_longer(-Age_mean, names_to = "Forma", values_to = "Low")
df_high_long <- df_high %>%
  pivot_longer(-Age_mean, names_to = "Forma", values_to = "High")

df_plot <- df_long %>%
  left_join(df_low_long, by = c("Age_mean", "Forma")) %>%
  left_join(df_high_long, by = c("Age_mean", "Forma"))

ggplot(df_plot, aes(x = Age_mean, y = Probabilidade, color = Forma, fill = Forma)) +
  geom_line(linewidth = 1.2) +
  geom_ribbon(aes(ymin = Low, ymax = High), alpha = 0.2, linetype = "dotted", color = NA) +
  labs(
    x = "Mean Age",
    y = "Predicted Probability",
    color = "Clinical Form",
    fill = "Clinical Form"
  ) +
  # --- Y-AXIS MODIFICATION ---
  # Sets the Y-axis breaks from 0 to 1 (0% to 100%) in steps of 0.1 (10%)
  scale_y_continuous(
    breaks = seq(0, 1, by = 0.1), 
    labels = scales::percent_format(accuracy = 1)
  ) +  theme_bw() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    legend.position = "bottom",
    legend.title = element_text(size = 12, face = "bold"),
    legend.text = element_text(size = 12)
  )
```
:::

::: cell-output-display
<div>

![](data:image/png;base64,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){.img-fluid
.figure-img role="img" width="672"}

</div>
:::
:::

::: cell
Code

::: {#cb8 .sourceCode .cell-code}
``` {.sourceCode .r .code-with-copy}
# Age bands and means
age_bands <- c(
  "15-19", "20-24", "25-29", "30-34", "35-39",
  "40-44", "45-49", "50-54", "55-59",
  "60-64", "65-69", "70-74", "75-79",
  "80-84", "85-89", "90-94", "95+"
)

age_means <- c(
  17, 22, 27, 32, 37,
  42, 47, 52, 57,
  62, 67, 72, 77,
  82, 87, 92, 97
)

df_pred <- data.frame(
  age_name = age_bands,
  Age_mean = age_means
)

# Predict class probabilities from the fitted VGAM multinomial model
# Note: type = "response" returns probabilities per outcome
probs_mat <- predict(multi_model, newdata = df_pred, type = "response")

# Bind predictions to the predictor grid
df_prob <- cbind(df_pred, probs_mat)

# Ensure the prediction column names match your response names in the fit:
# Expected: sample_cardiac, sample_digestive, sample_mixed, sample_indeterminate
# If they differ, rename here accordingly before pivot_longer.

# Long format for plotting if needed
df_prob_long <- df_prob %>%
  tidyr::pivot_longer(
    cols = c("sample_cardiac", "sample_digestive", "sample_mixed", "sample_indeterminate"),
    names_to = "clinical_form",
    values_to = "probability"
  ) %>%
  dplyr::mutate(
    age_name = factor(age_name, levels = age_bands),
    clinical_form = forcats::fct_relevel(
      clinical_form,
      c("sample_indeterminate", "sample_cardiac", "sample_digestive", "sample_mixed")
    )
  )

# Wide table for presentation
df_prob_wide <- df_prob_long %>%
  dplyr::select(age_name, clinical_form, probability) %>%
  tidyr::pivot_wider(
    names_from = clinical_form,
    values_from = probability
  ) %>%
  dplyr::rename(
    `Age Range` = age_name,
    `Indeterminate` = sample_indeterminate,
    `Cardiac` = sample_cardiac,
    `Digestive` = sample_digestive,
    `Mixed` = sample_mixed
  ) %>%
  dplyr::mutate(
    dplyr::across(c(Indeterminate, Cardiac, Digestive, Mixed), ~ round(.x, 3))
  )

DT::datatable(
  df_prob_wide,
  options = list(
    scrollX = TRUE,
    scrollY = "400px",
    pageLength = 10,
    lengthMenu = c(5, 10, 15, 20, 50, 100)
  ),
  class = "display compact",
  rownames = FALSE
)
```
:::

::: cell-output-display
::: {#htmlwidget-daab2e240ba142b5a809 .datatables .html-widget .html-fill-item style="width:100%;height:auto;"}
:::
:::
:::
:::
:::
:::
:::
