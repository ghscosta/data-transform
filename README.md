# Data transformations in variance analysis within agrarian sciences: a systematic review
This repository provide codes and supplementary tables for the article `Data transformations in variance analysis within agrarian sciences: a systematic review`.
The codes for downloading and separating the artcicles were written in Python 3.10 use the following open source libraries: [pyautogui], [openpyxl], [pandas] and [pypdf4]

The preprint is available at XXXXXXX. The following `BibTeX` code can be used to cite it:

```
@misc{jhennifer2023,
      title={Data transformations in variance analysis within agrarian sciences: a systematic review}, 
      author={J. S. Nascimento,  P. C. Emiliano and G. S. Costa},
      year={2023},
}
```
## Structure

### Tables

File `articles.csv` is a table that lists all articles selected after identification and screening stages of the systematic literature review of articles in agricultural sciences that employed data transformations to validate variance analysis. The table contains the following columns:

 - `reference_number`: 	This variable corresponds to the number for each article identification, where the tabulated articles that conducted more than one experiment in their work or used more than one transformation were treated as distinct observations and, therefore, have different identification numbers.
 - `title`: 	Title of each article.
 - `journal`: 	Journal of each article.
 - `year`: 	Year of publication of each article.
 - `authors`: 	Authors of each article.
 - `ANOVA_used`: 	Binary variable indicating whether variance analysis was used, where 'yes' indicates that it was used, and 'no' indicates that it was not.
 - `design_used`: 	The experimental design used in each article.
 - `assumptions_check` 	Binary variable indicating whether it was mentioned in the article that at least one variance analysis assumption was verified, 'yes' indicating verification, and 'no' indicating no verification
 - `which_assumptions_checked`: 	Checked variance analysis assumptions in each article.
 - `transformation_used`: 	Binary variable indicating whether the article mentioned performing a data transformation in the variance analysis. 'yes' indicates that a transformation was performed, while 'no' indicates that no transformation was mentioned."
 - `type_of_transformation`: 	Type of transformation used to meet variance analysis assumptions.
 - `motivation`: 	Variable indicating the motivation behind the author's choice to use a data transformation.
 - `reassessment_assumptions`: 	Verified variance analysis assumptions after data transformation.
 - `interpretation_scala`: 	Scale at which the variance analysis was interpreted, with 'transformed' indicating that the data was interpreted on the transformed scale, and 'original' indicating interpretation at the original scale.
 - `study_element`: 	Experimental subject.
 - `jcr_impact_factor`: 	Journal Citation Indicator, a metric indicating the citation performance of scientific journals, assigned by the Journal Citation Reports (JCR), which tracks citations journals indexed in the Web of Science database.
 - `status`: 	The binary variable indicating whether the article was selected or discarded at the eligibility and inclusion stages of the systematic review
 - `discard_reason`:	Reason for article discarding.
### Codes
Codes are available in the folder `codes` and were written in `Python 3.10` language.

 - File `download.py`is the code used to download the open access articles.
 - The `auxiliar` folder contains auxiliary files to facilitate the download of the articles and a list with all data exported from `Web of Science` and `Scopus`
 - File `search.py` is the code used to search for keywords within the downloaded articles.



