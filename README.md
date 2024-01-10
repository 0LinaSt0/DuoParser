<!-- PARS MAP:

1. INFORMATION

- UNIT NUMBER:
<section class="* KF0CX"> -> <header class="_3LsiE"> -> <div class="_2Z-Z4">
-> <h1 class="_3O98c _3Dmrr"> UNIT NUMBER </h1>


- COUNT OF WORDS:
<section class="* KF0CX"> -> <header class="_3LsiE"> -> <div class="_2Z-Z4">
-> <div class="_LXXG"> -> <div class="_2HCj4"> -> <div class="CAqAL">
-> <span class="_2ljv2">COUNT OF WORDS IN UNIT</span>

|
v
IF COUNT OF WORDS NOT 0
|
v

2. PRESS SHOW MORE BUTTON [OPTIONAL]
<div class="_2i_uN"> -> <div> -> <button class="_34v50 _275sd _1ZefG kRgiM">
-> <span class="_13HXc">

3. TAKE WORDS
<div class="_2i_uN"> -> <div> -> <div class="_3ewMG"> -> <div class="usJBg _1dAI3">
-> <div class="_3D4G0"> -> <p class="_2EAoP _2HH61">WORDS </p> -->


# DuoParser

> **Attention:**
Unfortunately, the Duolingo for School service doesn't support "Assign" page with course's words anymore.

## Description

For the best studying of new language it's important to understand your real lexicon (active and passive words). The parser can help with it. It parses Duolingo for School service and create json file with all learning words which are included to your language course.


It creates:
- json file with all words
- json file with words which are learned personally (by passed unit)
- json file with words by concrete language level


## Table of Contents

- [Dependencies](#dependencies)
- [Usage](#usage)
- [Features](#features)

## Dependencies

- You have to have an account in Duolingo for School service
- It uses Google Chrome browser for web scraping

## Usage

#### Preparation steps

1. Define path to the default chrome profile
    > Copy path to User Data directory from `chrome://version/` page. It looks like:
    `C:\Users\{username}\AppData\Local\Google\Chrome\User Data`
1. Log in to your ["Duolingo for school"](https://schools.duolingo.com/login) account in the Google Chrome browser (GCb)
1. Define number of your class
    > You can take it from start url:
    `https://schools.duolingo.com/classroom/{class_id}/students`
1. Define your Main Unit [optional]
    > If you want to see words which you already have learned, you should define your actual main unit. For that, you could plus count of all completed unit in every completed sections. Check it in your Duolingo account. For example:
    >> If I'm on Section 4 Unit 2, I should plus count of all Units in all three Sections before and plus one unit from Section 4
    > ```bash
    > Section 1 has 5 Units
    > Section 2 has 15 Units
    > Section 3 has 16 Units
    > Completed 1 extra Unit from Section 4
    > 5 + 15 + 16 + 1 => Number of my Main Unit is 37
    > ```
1. Close all GCb instances and make sure that all background instances of GCb have been closed
1. Create virtualenv and install all the packages from requirements.txt

> **Note:**
It works just with classes who have 'Language your students speak: English' in settings

#### Running
``` bash
$ python duoparser.py -d {path_to_User_Data_directory} -i {class_id} -n[optional] {custom_attach} -u[optional] {number_of_union} -l[optional] {name_of_level}
```

## Features

<table>
<tr>
    <th>Argument</th>
    <th>About</th>
    <th>Example</th>
    <th>Optional</th>
</tr>
<tr>
<td>

```bash
-d
--user_data_dir
```

</td>
<td>The path to default home profile</td>
<td style="max-width: 300px;">

```bash
C:/Users/{username}/AppData/Local/Google/Chrome/User\ Data
```

</td>
<td>No</td>
</tr>
<tr>
<td>

```bash
-i
--class_id
```

</td>
<td>Id number of class on Duolingo for school service</td>
<td>6731731</td>
<td>No</td>
</tr>
<tr>
<td>

```bash
-n
--attachment_name
```

</td>
<td>
Attachment for name of output files.<br>
If this argument is defined the name of the files will be
started with attachment else it will be started with class id.
</td>
<td>my_attachment</td>
<td>Yes</td>
</tr>
<tr>
<td>

```bash
-u
--main_union_number
```

</td>
<td>
Number of main interested unit.<br>
If this argument is defined the parser creates
"*_words_by_unit_{unit_number}.json" file with
list of all learned unique words before and
includes unit else the file isn't created.
</td>
<td>37</td>
<td>Yes</td>
</tr>
<tr>
<td>

```bash
-l
--level_name
```

</td>
<td>
Name of interested level.<br>
If this argument is defined the parser creates
"*_words_by_level_{level_name}.json" file with
list of all unique words before and includes level
else the file isn't created.
</td>
<td>A2</td>
<td>Yes</td>
</tr>
</table>
