# SMS Spam Detection — Testing Report

## Dataset
- Records after cleaning: 5,572
- Training records: 4,457
- Testing records: 1,115
- Split: 80/20, stratified, random_state=42

## Model
- TF-IDF vectorization (English stop words, unigrams and bigrams)
- Multinomial Naive Bayes
- Vectorizer and classifier saved together as `model.pkl`

## Test-set results
- Accuracy: 96.23%
- Ham precision: 95.83%
- Ham recall: 100.00%
- Ham F1: 97.87%
- Spam precision: 100.00%
- Spam recall: 71.81%
- Spam F1: 83.59%

The model's spam recall is notably lower than its overall accuracy. It misses some spam messages, so accuracy alone should not be used to judge this classifier.

## Smoke tests
- Spam example classified as `spam`: passed
- Legitimate example classified as `ham`: passed
- Saved pipeline loaded and inferred on raw strings: passed

Metrics are from the held-out split in this run and may vary if the dataset or training settings change.
