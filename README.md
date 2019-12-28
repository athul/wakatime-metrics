# Wakatime Language Metrics
## Wakatime's Language Metrics as Bar
Decorate your Wakatime Language metrics as bar graph showing your language and '%' of time you used it just by 16 lines of Python Code without any API calls and stuff.
**You'll need a wakatime account**
### How?
Before running you'll need to make a `.json` file with you wakatine metrics of languages. You can copy&paste it from your wakatime dashboard or by clicking [this](https://wakatime.com/share/embed) .
You can view this by running `python main.py <wakatime_metrics.json>`

After running you get an output like this 👇👇

```
Go          63.97% ████████████████████████████████
Markdown    17.38% ████████░░░░░░░░░░░░░░░░░
Bash        16.4 % ████████░░░░░░░░░░░░░░░░░
Other       1.48 % ░░░░░░░░░░░░░░░░░░░░░░░░░
Groff       0.33 % ░░░░░░░░░░░░░░░░░░░░░░░░░
Git         0.28 % ░░░░░░░░░░░░░░░░░░░░░░░░░
Text        0.17 % ░░░░░░░░░░░░░░░░░░░░░░░░░
```
You can refer the GitHub action result to see the o/p

------
I know most of this is a manual process(copying the json file) but You can automate the whole thing by running a simple shell script. For that you need
- An new Gist
- a text editor
**Clone** the gist to your local system ,you can find that from the dropdown list in "Embed" button of the gist.
The shell script is here
``` sh
cd <folder where the main.py and .json file exist>
python main.py <filename>.json > <path_of_gist file>
cd <folder_where_the_gist_is_present>
git commit -a -m "Timely Updates"
git push origin master
```
Save the script in `.sh` file and run `sh <filename.sh>` when you update the JSON file.

#### Show off this metrics in your gist
