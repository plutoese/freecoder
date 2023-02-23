---
title: "ggplot2 demo"
author: "Norah Jones"
date: "5/22/2021"
format: docusaurus-md
---

## Air Quality {#air-quality}

``` r
library(ggplot2)

ggplot(airquality, aes(Temp, Ozone)) + 
  geom_point() + 
  geom_smooth(method = "loess"
)
```

![Temperature and ozone level.](quarto_demo.markdown_strict_files/figure-markdown_strict/fig-airquality-1.png)
