library(ggplot2)

netflix <- read.csv("netflix_data.csv", stringsAsFactors = FALSE)

# filling missing ratings
netflix$rating[is.na(netflix$rating)] <- "Unknown"


# plotting
ggplot(netflix, aes(x = rating)) +
  geom_bar(fill = "tomato") +
  coord_flip() +
  theme_minimal() +
  labs(title = "Netflix Ratings Distribution", x = "Rating", y = "Count")

