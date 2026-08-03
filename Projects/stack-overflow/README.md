# Curriculum Optimization for High-Yield Tech Stacks
### Stack Overflow Developer Survey - Exploratory Data Analysis
**Sara AlNajjar | General Assembly Data Science DSBFT2 | Project 2**

---

## Problem Statement

A coding bootcamp wants to know which programming languages and tools are associated with the highest compensation and the strongest year-over-year growth, so it can prioritize curriculum around the tech stacks that yield the best outcomes for graduates.

---

## Executive Summary

This project analyzes the 2024 and 2025 Stack Overflow Developer Survey datasets to identify which programming languages offer the strongest return on investment for a coding bootcamp's curriculum. The process is split across three notebooks: data collection and initial inspection, data cleaning (filtering to US respondents, reconciling schema differences between survey years, handling missing values and compensation outliers, and combining both years into a single cleaned file), and exploratory analysis on that cleaned file. The multi-select language field was split and restructured so compensation could be examined at the individual language level.

The analysis evaluated languages along three dimensions: median compensation, respondent sample size (as a proxy for market adoption), and year-over-year compensation growth from 2024 to 2025. The highest-paying languages overall, Scala, Erlang, Elixir, Solidity, and Clojure, were consistently backed by small, specialized respondent pools, suggesting their high pay reflects niche expertise rather than broad hiring demand. Go and Ruby were the only languages that combined top-tier compensation with a large respondent base, and Go was the sole language to show strength across all three measures simultaneously: high pay, wide adoption, and continued growth (+10.4% year-over-year).

Based on these findings, Go is recommended as the top priority for core curriculum investment, with Ruby as a strong secondary choice. Scala, Erlang, Elixir, Solidity, and Clojure are better suited to an advanced or elective track given their narrow respondent bases. HTML/CSS, while not top-tier on compensation, showed meaningful growth (+11.5%) and remains a valuable foundational module given its accessibility for beginner developers.

---

## File Directory

| File / Folder | Description |
| :--- | :--- |
| `README.md` | Project overview, problem statement, findings, and conclusions (this file) |
| `Code/01_Data_Collection.ipynb` | Loads the raw 2024 and 2025 survey data and documents schema differences between years |
| `Code/02_Data_Cleaning.ipynb` | Filters to US respondents, resolves missing data and compensation outliers, combines both years, and exports the cleaned CSV |
| `Code/03_EDA.ipynb` | Loads the cleaned data, parses the language field, and runs the compensation-by-language analysis, findings, and conclusions |
| `Data/Survey 2024/survey_results_2024.csv` | Original 2024 Stack Overflow Developer Survey data |
| `Data/Survey 2025/survey_results_2025.csv` | Original 2025 Stack Overflow Developer Survey data |
| `Data/Cleaned/stack_overflow_cleaned.csv` | Cleaned, combined dataset produced by `02_Data_Cleaning.ipynb` |
| `Data/StackOverflow_Data_Dictionary.pdf` | Field-level definitions for the 2024 and 2025 survey schemas, sourced from Stack Overflow |
| `Presentation/Curriculum_Optimization_Presentation.pdf` | Presentation slides summarizing findings for a non-technical audience |

---

## Data & Data Dictionary

**Source:** [Stack Overflow Developer Survey](https://survey.stackoverflow.co/), 2024 (114 fields) and 2025 (172 fields) results. Full field definitions are available via the survey's published schema files.

The following columns make up the final cleaned file (`Data/Cleaned/stack_overflow_cleaned.csv`):

| Column | Type | Description |
| :--- | :--- | :--- |
| `ResponseId` | integer | Unique identifier for each survey respondent |
| `Country` | string | Respondent's country of residence (filtered to United States only) |
| `EdLevel` | string | Highest level of formal education completed |
| `DevType` | string | Respondent's current job role |
| `OrgSize` | string | Size of the respondent's employer |
| `LanguageHaveWorkedWith` | string | Semicolon-delimited list of languages the respondent worked with in the past year |
| `ConvertedCompYearly` | float | Respondent's annual compensation, converted to USD, filtered to $15,000–$1,000,000 |
| `SurveyYear` | Tags each row as 2024 or 2025, added prior to combining the two survey years |
| `LanguageList` | `LanguageHaveWorkedWith` split into individual languages and exploded into one row per respondent-language pair (created in `03_EDA.ipynb` for analysis; not part of the saved cleaned CSV) |

---

## Conclusions & Recommendations

**Go** should be the top priority for curriculum investment. It is the only language in the dataset that pairs high compensation with wide market adoption (1,692 respondents) and continued year-over-year growth (+10.4%), making it the lowest-risk, highest-return addition to a bootcamp's core teaching stack.

**Ruby** is the second recommendation, offering the same combination of high pay ($170,000 median) and broad adoption (890 respondents), though without the same growth signal in this data.

**Scala, Erlang, Elixir, Solidity, and Clojure** should be considered for an advanced or elective track rather than the core curriculum. Their high pay is real, but their small respondent bases suggest a narrow, specialized job market rather than broad hiring demand, a riskier bet for a curriculum meant to serve a wide range of graduates.

**HTML/CSS** deserves a specific mention as a foundational skill: it is already a curriculum staple, and this data confirms it continues to grow in value (+11.5%), reinforcing that it should remain a core early-stage module rather than be deprioritized in favor of more advanced languages.

---

## Areas for Further Research

- This analysis used median compensation as the primary measure of value; incorporating job posting volume or `DevType` breakdowns would clarify whether high-paying languages also correspond to a high number of open roles, not just high individual salaries.
- The year-over-year comparison spans only two survey years (2024–2025); a longer time series would help confirm whether growth trends like Go's are sustained or one-off fluctuations.
- Segmenting compensation by `EdLevel` or years of experience would show whether a language's high pay is achievable early in a career (relevant to bootcamp graduates) or only after years of specialization.
- Expanding beyond `LanguageHaveWorkedWith` to include `LanguageWantToWorkWith` could reveal whether developer interest is shifting toward or away from these high-paying languages, which matters for long-term curriculum relevance.
- This analysis was scoped to US respondents only; comparing against other major tech markets could reveal whether these language trends are US-specific or globally consistent.

---

## Important Visualizations

- **Median Compensation by Language**, table ranking the top-paying languages among respondents with a reliable sample size (n ≥ 30)
- **Year-over-Year Compensation Growth by Language**, percentage change in median compensation from 2024 to 2025 by language
- **Language Popularity vs. Median Compensation**, scatter plot comparing respondent count against median compensation, highlighting Go and Ruby as outliers combining high pay with broad adoption

*(See `Code/03_EDA.ipynb`, Section 3, for the generated charts.)*

---

## Sources

- [Stack Overflow Developer Survey](https://survey.stackoverflow.co/)
