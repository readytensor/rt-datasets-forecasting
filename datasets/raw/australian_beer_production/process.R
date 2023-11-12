

# Load the RDA file
# Replace 'your_data_file.rda' with the path to your RDA file
load("ausbeer.rda")


# Convert the time series to a data frame
ausbeer_df <- data.frame(Date = time(ausbeer), Beer = as.numeric(ausbeer))

# Export to CSV
write.csv(ausbeer_df, "ausbeer.csv", row.names = FALSE)
